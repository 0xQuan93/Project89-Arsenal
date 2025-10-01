# Reality Glitch Logger

A utilitarian synchronicity tracking system for logging, analyzing, and exporting reality anomalies.

## Features

✅ **Category-based logging** - Number Sync, Déjà Vu, Temporal, Pattern, Prophetic, Entity, Other  
✅ **Local storage persistence** - All data stored in browser IndexedDB  
✅ **Search & filter** - Find entries by description, category, or date  
✅ **Statistics dashboard** - Total glitches, today's count, weekly trends, top categories  
✅ **Export functionality** - JSON and formatted text export  
✅ **Mobile responsive** - Log glitches on any device  

## How to Use

### Logging a Glitch
1. Select category using the category tags
2. Enter description of the anomaly/synchronicity
3. Add optional tags (comma-separated)
4. Click "Log Glitch"

### Viewing & Filtering
- **Search**: Type keywords to filter descriptions
- **Category filter**: Show only specific types of glitches
- **Sort order**: View newest or oldest first

### Exporting Data
- **Export JSON**: Machine-readable format for data analysis
- **Export Text**: Human-readable format for sharing/archiving
- **Clear All**: Permanently delete all logged data (with confirmation)

## Squarespace Integration

### Method 1: Code Block (Recommended)
1. Add a **Code** block to your page
2. Copy entire contents of `index.html`
3. Paste into code block
4. Save and publish

### Method 2: Embed Block
1. Add an **Embed** block
2. Paste the HTML
3. Adjust height if needed (recommended: 900px)

## Data Storage

All data is stored **locally in your browser** using `localStorage`:
- No external servers
- No data transmission
- Persists across browser sessions
- Cleared only when you clear browser data or use "Clear All"

## Statistics Tracked

- **Total Glitches**: Lifetime count of logged events
- **Today**: Events logged since midnight
- **This Week**: Events from last 7 days
- **Top Category**: Most frequently logged type

## Technical Details

- **Framework**: Vanilla JavaScript (no dependencies)
- **Storage**: localStorage (approximately 5-10MB limit)
- **Compatibility**: Modern browsers (Chrome 90+, Firefox 88+, Safari 14+, Edge 90+)
- **File size**: ~15KB (self-contained)

## Privacy

This tool:
- ✅ Runs entirely in your browser
- ✅ Never sends data to external servers
- ✅ Never uses cookies or tracking
- ✅ Stores data only on your device

## Troubleshooting

**Data not persisting?**
- Check if browser is in private/incognito mode
- Verify localStorage is enabled in browser settings
- Check available storage space

**Export not working?**
- Ensure pop-ups are not blocked
- Try a different browser
- Check browser's download settings

---

*Part of Project 89 Arsenal - Reality Hacking Technology*


