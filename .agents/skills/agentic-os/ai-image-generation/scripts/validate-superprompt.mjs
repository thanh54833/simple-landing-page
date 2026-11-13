#!/usr/bin/env node
// Dependency-free validator for superprompt JSON (see references/superprompt.md).
// Usage: node scripts/validate-superprompt.mjs --input prompt.json [--strict]
// Exit 0 = valid, 1 = invalid (or warnings under --strict), 2 = usage/parse error.

import { readFileSync } from 'node:fs';

const WRAPPER_KEYS = [
  'superprompt', 'name', 'description', 'input_prompt', 'target_model',
  'model_adaptations', 'flattened_prompt', 'negative_prompt_flat',
  'playbook_principles_applied', 'template_type', 'template_instructions',
  'replacement_guide',
];
const REQUIRED = {
  portrait: ['prompt_type', 'meta', 'subject', 'wardrobe', 'pose_action', 'environment', 'lighting', 'camera_technical', 'realism_anchors', 'negative_prompt'],
  product: ['prompt_type', 'meta', 'subject', 'environment', 'lighting', 'camera_technical', 'realism_anchors', 'negative_prompt'],
  collage: ['prompt_type', 'meta', 'composition', 'subject', 'environment', 'lighting'],
};
const META_KEYS = ['quality_tier', 'aspect_ratio', 'style', 'target_model'];
const QUALITY_TIERS = ['masterpiece', 'professional', 'standard', 'draft'];
const ASPECT_RATIOS = ['1:1', '4:5', '5:4', '3:4', '4:3', '16:9', '9:16', '21:9', '3:2', '2:3'];
const STYLES = ['photorealistic', 'cinematic', 'editorial', 'artistic', 'illustration', 'vector', 'anime', '3d-render', 'sketch', 'painterly'];
const LIGHTING_TYPES = ['natural', 'studio', 'dramatic', 'soft', 'hard', 'golden-hour', 'blue-hour', 'overcast', 'backlit', 'rim-light', 'volumetric'];

function parseArgs(argv) {
  const out = { strict: false };
  for (let i = 0; i < argv.length; i++) {
    if (argv[i] === '--input') out.input = argv[++i];
    else if (argv[i] === '--strict') out.strict = true;
  }
  return out;
}

const isStr = (v) => typeof v === 'string' && v.trim().length > 0;
const isArr = (v) => Array.isArray(v);

export function validate(p) {
  const errors = [];
  const warnings = [];
  if (p === null || typeof p !== 'object' || isArr(p)) {
    return { errors: ['Root must be a JSON object'], warnings };
  }

  for (const k of WRAPPER_KEYS) {
    if (k in p) errors.push(`Remove wrapper/metadata key "${k}": superprompt fields belong at the top level`);
  }

  const type = p.prompt_type;
  if (!REQUIRED[type]) {
    errors.push(`prompt_type must be one of ${Object.keys(REQUIRED).join(', ')} (got ${JSON.stringify(type)})`);
    return { errors, warnings };
  }
  for (const k of REQUIRED[type]) {
    if (!(k in p)) errors.push(`Missing required field "${k}" for prompt_type "${type}"`);
  }

  const meta = p.meta ?? {};
  for (const k of META_KEYS) {
    if (!isStr(meta[k])) errors.push(`meta.${k} is required`);
  }
  if (isStr(meta.quality_tier) && !QUALITY_TIERS.includes(meta.quality_tier)) warnings.push(`meta.quality_tier "${meta.quality_tier}" not in ${QUALITY_TIERS.join('|')}`);
  if (isStr(meta.aspect_ratio) && !ASPECT_RATIOS.includes(meta.aspect_ratio)) warnings.push(`meta.aspect_ratio "${meta.aspect_ratio}" not in ${ASPECT_RATIOS.join('|')}`);
  if (isStr(meta.style) && !STYLES.includes(meta.style)) warnings.push(`meta.style "${meta.style}" not in ${STYLES.join('|')}`);

  const minDesc = type === 'portrait' ? 10 : 5;
  if (p.subject && (!isStr(p.subject.description) || p.subject.description.length < minDesc)) {
    errors.push(`subject.description must be a string of at least ${minDesc} characters`);
  }

  const env = p.environment;
  if (env) {
    if (!isStr(env.location)) errors.push('environment.location is required');
    if (!isArr(env.background) || env.background.length === 0) errors.push('environment.background must be a non-empty array of strings');
    if (!isStr(env.atmosphere)) errors.push('environment.atmosphere is required');
  }

  const light = p.lighting;
  if (light && type !== 'collage') {
    if (!isStr(light.type)) errors.push('lighting.type is required');
    else if (!LIGHTING_TYPES.includes(light.type)) warnings.push(`lighting.type "${light.type}" not in ${LIGHTING_TYPES.join('|')}`);
    if (!isStr(light.quality)) errors.push('lighting.quality is required');
    if (!isArr(light.effects)) errors.push('lighting.effects must be an array');
  }

  if ('negative_prompt' in p) {
    if (!isArr(p.negative_prompt) || p.negative_prompt.length < 3) errors.push('negative_prompt must be an array of at least 3 strings');
  }
  if ('realism_anchors' in p) {
    const min = meta.style === 'photorealistic' ? 3 : 1;
    if (!isArr(p.realism_anchors) || p.realism_anchors.length < min) errors.push(`realism_anchors must be an array of at least ${min} strings for style "${meta.style}"`);
  }

  if (type === 'portrait' && p.subject) {
    for (const k of ['identity', 'physical_details', 'expression_mood']) {
      if (!(k in p.subject)) errors.push(`subject.${k} is required for portrait`);
    }
    if (p.wardrobe && !isArr(p.wardrobe.clothing)) errors.push('wardrobe.clothing must be an array');
  }
  if (type === 'product' && p.subject && !p.subject.physical_details) {
    errors.push('subject.physical_details is required for product');
  }
  if (type === 'collage' && p.composition && !isArr(p.composition.panels)) {
    errors.push('composition.panels must be an array');
  }

  return { errors, warnings };
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const args = parseArgs(process.argv.slice(2));
  if (!args.input) {
    console.error('Usage: node scripts/validate-superprompt.mjs --input prompt.json [--strict]');
    process.exit(2);
  }
  let data;
  try {
    data = JSON.parse(readFileSync(args.input, 'utf8'));
  } catch (e) {
    console.error(`✗ Cannot read/parse ${args.input}: ${e.message}`);
    process.exit(2);
  }
  const { errors, warnings } = validate(data);
  for (const e of errors) console.log(`  error:   ${e}`);
  for (const w of warnings) console.log(`  warning: ${w}`);
  const bad = errors.length > 0 || (args.strict && warnings.length > 0);
  console.log(bad ? `✗ INVALID (${errors.length} errors, ${warnings.length} warnings)` : `✓ VALID (${warnings.length} warnings)`);
  process.exit(bad ? 1 : 0);
}
