# Reference images

Add a reference image when the output must match something that already exists: a logo, a face, a product, a previous cover, a layout. The superprompt stays complete; a `reference` block and the `images` input are added on top of it ([superprompt.md](superprompt.md)).

## What a reference does

| Goal | Reference | Instruction in the prompt |
|---|---|---|
| Keep a face or character | photo of the subject | `identity_lock`; same facial structure, skin texture, expression |
| Use a real logo or icon | the logo file | name where it goes; say `reproduce the attached mark exactly` |
| Keep a brand shape | existing mark or style frame | say what to preserve (silhouette, palette) and what may change |
| Revise a previous result | the last output | `change only X; keep everything else the same` |
| Match a layout | screenshot or sketch | describe the layout in words too; the image alone is ambiguous |

## Steps

1. **Collect** — one file or URL per reference, each with a one-line role. Done when every reference has a role (`logo`, `identity`, `previous cover`, `layout`).
2. **Pick the app** — `openai/gpt-image-2-5-flare` by default, `openai/gpt-image-2-5-sunburst` when an existing image is edited and its composition must survive. Both take `images` (array); a `mask` applies to the first image. Confirm with `belt app get <app-id>`.
3. **Add the `reference` block** to the superprompt, top level (the validator accepts it as an extra key):
   ```json
   "reference": {
     "images": [
       {"role": "logo", "use": "reproduce exactly, bottom-right, small"},
       {"role": "previous cover", "use": "keep layout and palette, change only the organism density"}
     ],
     "preserve": ["silhouette", "palette", "tile layout"]
   }
   ```
   Add `"identity_lock": true` only when a reference is a person's face or a recurring character. For a logo or shape, `preserve` and each image's `use` carry the instruction: `reproduce exactly` when the mark appears in the output, `shape reference only` when the model redraws it.
4. **Reflect it in the text** — in `subject` and `negative_prompt`, state the preserved facts (`face_accuracy`, `same silhouette`) and the drift to avoid (`no face change`, `no identity drift`, `no redrawn logo`).
5. **Flatten** with the first sentence naming the images: `Using the attached images: image 1 is the logo, image 2 is the previous cover.` Order in the sentence matches the order in `images`.
6. **Price and run** — `belt app estimate` first. Each reference adds about $0.008 on the GPT-Image-2.5 apps. Pass local paths or URLs in `images`; use files the user owns, since they are sent to inference.sh.

```json
{
  "prompt": "Using the attached images: image 1 is the project logo, image 2 is the previous cover. ...",
  "images": ["/path/to/logo.png", "/path/to/previous-cover.png"],
  "width": 1536,
  "height": 864,
  "quality": "high"
}
```

## Limits

- The model treats references as guidance, not a pixel copy; small marks and text may still drift. Check the result against the reference before reporting it done.
- Real third-party logos may be refused or redrawn. Place the real logos in a compositing step (HTML/SVG or image editor) when exactness matters, and let the model draw only the surrounding art.
- Faces: use a reference only for a person who has agreed to it.
