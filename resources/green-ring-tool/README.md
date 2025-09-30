# Agent Halo Forge Embed

This folder contains a self-contained HTML/CSS/JS bundle that can be dropped into a Squarespace Code Injection block or custom code section to provide the “Agent Halo Forge” avatar tooling experience.

## Files

- `index.html` – Markup scaffold for the tool. Reference this inside a Squarespace code block.
- `styles.css` – Cyberpunk-styled presentation layer.
- `script.js` – Client-side logic for canvas compositing and exports.
- `squarespace-inline.html` – One-file snippet with inline CSS/JS for platforms that do not allow separate uploads.
- `green-ring.png` – **Place your transparent halo asset here.** The script assumes a square PNG. 1024×1024 is ideal.

## Usage (Squarespace)

1. Upload `styles.css`, `script.js`, and `green-ring.png` to **Website > Design > Custom CSS > Manage Custom Files** (Squarespace 7.1) or your preferred asset host and copy the URLs.
2. In a page section, add a **Code** block and paste the contents of `index.html`.
3. Update the `<link rel="stylesheet" href="styles.css" />` and `<script src="script.js"></script>` paths in the code block to the Squarespace-hosted URLs from step 1.
4. Ensure `green-ring.png` path in the markup points to the hosted halo asset (replace the relative `green-ring.png` path if needed).
5. Save the page. The app runs entirely client-side; no further configuration is required.

### Squarespace all-in-one snippet

If your Squarespace plan does **not** let you host individual CSS/JS files, open `squarespace-inline.html`, copy everything, and paste it directly into a single Code block. Only edit the `src="green-ring.png"` attribute so it references the halo asset you uploaded via **Manage Custom Files** (or another public host). Everything else is already inlined so no additional uploads are required.

## Notes

- The tool accepts PNG/JPG files up to 5 MB, with a minimum edge of 512 px.
- Drag the canvas to reposition your portrait; use the zoom slider for scaling.
- PNG exports preserve transparency outside the halo. JPG exports render on a dark backdrop.
- All image processing happens locally in the browser; no uploads are sent to a server.
