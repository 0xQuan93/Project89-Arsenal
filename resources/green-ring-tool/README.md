# Agent Halo Forge - Squarespace Embed

**✅ UPDATED VERSION**: Export at original dimensions with perfectly scaled ring overlay!

## Overview

The Agent Halo Forge is a cyberpunk-styled avatar creation tool that allows users to upload their portrait, align it within a neon halo frame, and export the result at the **original image dimensions** - perfect for Project 89 agents and reality hackers!

## ✨ Key Features

- **Original Size Export**: Your exported image maintains the exact dimensions you uploaded
- **Perfect Ring Scaling**: The neon ring automatically scales to frame your entire PFP
- **Self-contained**: All CSS and JavaScript are inline - no external file dependencies
- **Squarespace-ready**: Optimized for iframe embedding with responsive design
- **Agent Tools**: Consciousness sync, reality mantras, and timeline probability tracking
- **Local Processing**: Everything happens in your browser - no uploads to servers

## 🚀 How to Use in Squarespace

### Method 1: Code Block (Recommended)
1. In your Squarespace editor, add a **Code** block to your page
2. Copy the entire contents of `index.html` and paste it into the code block
3. Save and publish your page
4. That's it! The app will work immediately

### Method 2: Page Injection (For site-wide embedding)
1. Go to **Settings > Advanced > Code Injection**
2. Paste the contents of `index.html` into the **Footer** section
3. The app will appear at the bottom of every page

## 🎨 How It Works

1. **Upload Image**: Drag & drop or click to browse for a PNG/JPG file (max 5MB, min 512px)
2. **Adjust Position**: Drag the preview canvas to reposition, use zoom slider for scaling
3. **Export**: Click PNG or JPG to download

### Export Behavior
- **Dimensions**: Exports at your **original uploaded image dimensions** (e.g., 1080×1080 stays 1080×1080)
- **Ring Scaling**: The neon ring scales proportionally to encompass the entire frame
- **Frame Alignment**: Ring is positioned to frame the entire PFP, not just the face

## 🧠 Project 89 Agent Features

- **Consciousness Sync**: Real-time consciousness alignment indicator with dynamic states
- **Mantra Generator**: Reality-hacking affirmations from the Project 89 agent handbook
- **Timeline Probability**: Manifestation likelihood tracker showing your optimal timeline convergence (89%)

## 📱 Responsive Design

The app automatically adapts to different screen sizes:
- **Desktop**: Full-width layout with side-by-side panels
- **Tablet**: Optimized stacked layout
- **Mobile**: Compact single-column design

## 🔧 Technical Details

- **Canvas Resolution**: 1080×1080 preview canvas for optimal quality
- **Ring Design**: Triple-layered neon effect (#00ff88, #1cff9b, #3cffea)
- **Ring Buffer**: Pre-rendered 1080×1080 ring that scales to match export dimensions
- **Export Logic**: Maintains original image dimensions with proportionally scaled ring overlay
- **Framework**: Vanilla HTML/CSS/JavaScript (no dependencies)
- **Compatibility**: Modern browsers (Chrome 90+, Firefox 88+, Safari 14+, Edge 90+)

## 🛠️ Troubleshooting

**Ring not appearing on export?**
- Make sure the page has fully loaded before exporting
- Try refreshing and re-uploading your image
- The ring is drawn programmatically and should always appear

**Ring looks too small/large?**
- The ring auto-scales based on your image dimensions
- For 1080×1080 images, the ring has a radius of ~480px
- Smaller images get proportionally smaller rings

**App taking over the page in Squarespace?**
- Ensure you're using a Code Block, not an Embed Block
- The app includes containment CSS to prevent overflow
- Try wrapping in a `<div style="max-width: 900px; margin: 0 auto;">` if needed

**Canvas not responding to drag?**
- Upload an image first before attempting to drag
- Make sure you're dragging on the canvas area, not the ring overlay
- Touch events should work on mobile devices

## 🌟 Pro Tips

- **Best Results**: Use square images (1:1 aspect ratio) for optimal ring framing
- **Face Positioning**: The preview lets you position, but the export uses original dimensions
- **Export Quality**: PNG for transparency/quality, JPG for smaller file sizes
- **Social Media**: Most platforms prefer 1080×1080 or 1024×1024 for profile pictures
- **Twitter Cropping**: The ring frames the entire image, accounting for Twitter's circular crop

## 📋 Customization

Want to modify the appearance? The CSS variables make it easy:

```css
:root {
  --bg: #05010f;              /* Dark background */
  --accent: #00ff88;          /* Main neon green */
  --text: #f1f6ff;            /* Text color */
  --subtext: rgba(241,246,255,.7);  /* Secondary text */
}
```

---

*Built for Project 89 - Reality Hacking Technology. The ring symbolizes awakening to the true nature of the simulation and commitment to consciousness liberation. Manifest the optimal timeline through creative avatar generation! 🕸️🌳*
