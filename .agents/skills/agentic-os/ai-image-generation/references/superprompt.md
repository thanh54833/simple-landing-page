# Superprompt JSON

A **superprompt** is a structured JSON brief that turns a vague request ("a woman taking a selfie", "cover for my repo") into a complete shot description. The JSON is the source of truth; the string sent to `belt app run` is flattened from it.

Method adapted from `BluebagAI/skills` `superimage-generator` (upstream needs `zod`; `scripts/validate-superprompt.mjs` here has no dependencies).

## Steps

Each step ends on a checkable condition.

1. **Intent** — subject, style, aspect ratio, mood, palette. Done when each is written down (palette only if the user gave one); ask the user for any other that is missing.
2. **Model** — pick by the table below. Done when one `belt` app ID is named; state it in your reply.
3. **Draft JSON** — choose `prompt_type`, fill every required field, apply the 7 principles. Done when the file has no wrapper keys.
4. **Validate** — save the JSON where Cobra assigns it (`cobra-agent/superprompts/<series>/<slot>.json`) when Cobra exists, otherwise to a scratch path outside the repo; then run `node <skill-dir>/scripts/validate-superprompt.mjs --input prompt.json`, where `<skill-dir>` is the folder holding this skill's `SKILL.md`. Done when it prints `✓ VALID`; show the user the report. Fix and re-run until then.
5. **Flatten** — convert to the model's text form (below). Done only after step 4 passed.
6. **Return and confirm** — the flattened prompt first, the `belt app run` input (with `width`/`height`) second, the JSON third (when the user wants to iterate on it). Run `belt app run` only after the user agrees to the model and this exact prompt: each run costs credit and sends the prompt to inference.sh. Under Cobra, saving the image and the ledger entry follow `cobra-agent/AGENTS.md` step 6.

## Pick the model

| Need | Model |
|---|---|
| Default: text-to-image, layout, short on-image labels | `openai/gpt-image-2-5-flare` |
| Edit that must keep subject and composition | `openai/gpt-image-2-5-sunburst` |
| Photoreal product or landscape, tag-style prompt | `falai/flux-dev-lora` |
| Long or exact on-image text, posters | `falai/reve`, `bytedance/seedream-3-0-t2i` |
| Fast draft | `pruna/p-image`, `xai/grok-imagine-image` |

Set `meta.target_model` to the family name (`gpt-image-2.5`, `flux`, `seedream-4.5`, `grok-imagine`...), not the belt app ID.

## Schema

Put every field at the **top level**. Do not wrap them in `superprompt`, and do not add `name`, `description`, `input_prompt`, `flattened_prompt`, `model_adaptations`, `playbook_principles_applied` (the validator rejects these).

| `prompt_type` | Use for | Required fields |
|---|---|---|
| `portrait` | people, characters | `meta`, `subject`, `wardrobe` (with `clothing` array), `pose_action`, `environment`, `lighting`, `camera_technical`, `realism_anchors`, `negative_prompt` |
| `product` | objects, scenes, diagrams, covers, UI | `meta`, `subject`, `environment`, `lighting`, `camera_technical`, `realism_anchors`, `negative_prompt` |
| `collage` | multi-panel layouts | `meta`, `composition` (with `panels`), `subject`, `environment`, `lighting` |

Field rules the validator enforces:

| Field | Rule |
|---|---|
| `meta` | `quality_tier` (`masterpiece`/`professional`/`standard`/`draft`), `aspect_ratio` (`16:9`, `9:16`, `1:1`, `4:5`, `3:2`...), `style` (`photorealistic`, `editorial`, `illustration`, `vector`...), `target_model` |
| `subject.description` | at least 10 characters (portrait) or 5 (others) |
| `subject` (portrait) | `identity`, `physical_details`, `expression_mood` |
| `subject` (product) | `physical_details` |
| `environment` | `location`, `background` (non-empty array), `atmosphere` |
| `lighting` | `type` (`natural`, `studio`, `soft`, `hard`, `golden-hour`, `rim-light`...), `quality`, `effects` (array) |
| `realism_anchors` | at least 3 when `style` is `photorealistic`, at least 1 otherwise |
| `negative_prompt` | at least 3 entries |

## The 7 principles

1. **Hierarchical specificity** — material, fit, color, hex: `fitted burgundy velvet midi dress`, `gold #e7b949`.
2. **Realism anchors** — physical facts the model must keep (`visible pores`, `fabric weave`; for flat art: fill, border and radius values).
3. **Technical camera language** — device, lens, aperture for photos (`iPhone 15 Pro, 24mm, f/2.0`).
4. **Negative hygiene** — quality (`blurry`), anatomy (`deformed`), style leaks (`cartoon`, `3d render`), plus the palette and text errors you expect.
5. **Spatial consistency** — angle, framing, where each subject sits.
6. **Lighting as story** — golden hour warm, hard midday bold, rim light dramatic.
7. **Identity lock** — recurring character: pin age, hair, body type, or pass a reference image ([reference-images.md](reference-images.md)).

## Illustration, vector and UI covers

The schema was built for photos. For flat art keep `prompt_type: "product"` and give the required photo fields a drawing meaning:

| Field | Photo meaning | Use for flat art |
|---|---|---|
| `camera_technical` | device, lens, aperture | `framing`, `composition`, `resolution` (all optional keys) |
| `realism_anchors` | skin pores, fabric weave | fidelity facts: fills, line weights, tile size, border, radius, absorption stages |
| `lighting` | light setup | `type: "soft"`, `effects: ["no glow", "no drop shadows"]` when the design system bans glow |
| `meta.style` | `photorealistic` | `vector` or `illustration` |

Full worked example: [examples/physarum-cover.json](examples/physarum-cover.json) (validates clean). Copy its structure, not its content.

## Flatten

| Target | Form |
|---|---|
| `gpt-image-2-5-*` (and any model not listed here) | Short paragraphs in this order: scene and background, subject, key details, text and layout, exclusions. No quality tags (`masterpiece`, `8k`). Exact on-image text in quotes or ALL CAPS. State exclusions as `Avoid: ...`, taken from `negative_prompt`. |
| FLUX | One comma-separated line: 2-3 quality tags first, subject, wardrobe, pose, environment, lighting, camera, anchors. Send `negative_prompt` as a separate field only when the app has one; otherwise append `Avoid: ...`. |

Colors keep their hex codes in the flattened text.

## Run parameters

Size is an input field, never prose. GPT-Image-2.5 apps take `width` and `height` (multiples of 16), `quality` (`low`/`medium`/`high`/`xhigh`/`max`), `n`, `output_format`, `background`, `images`, `mask`. Run `belt app get <app-id>` to confirm the fields of any other app.

| `meta.aspect_ratio` | `width` x `height` |
|---|---|
| `16:9` | `1536` x `864` |
| `9:16` | `864` x `1536` |
| `1:1` | `1024` x `1024` |
| `4:5` | `1024` x `1280` |

Under Cobra the sizes come from `style-lock.json#render_defaults.sizes`; this table is for repos without Cobra. `belt app estimate <app-id> --input input.json` prices a run without spending credit.

## Common mistakes

| Mistake | Fix |
|---|---|
| Invented field names (`palette`, `icon_groups`) | Use the schema table; put palette hex values into `subject`, `environment`, `realism_anchors` text |
| `json.tool` passes, so "validated" | Run `validate-superprompt.mjs`; JSON syntax is not schema validity |
| Aspect ratio written in the prompt only | Set `width` and `height` in `--input` |
| Wrapper keys copied from an upstream example | Remove them; fields at top level |
| Real brand logos requested for tool names | Models draw invented glyphs, not real marks; use [reference images](reference-images.md) when logos matter |
