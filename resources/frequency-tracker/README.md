# 89 Frequency Tracker

Statistical analysis tool for detecting synchronicity patterns in random number generation with cryptographic-grade randomness.

## Features

✅ **Cryptographic randomness** - Uses `crypto.getRandomValues()` for true randomness  
✅ **Statistical analysis** - Chi-square testing, deviation calculation, significance testing  
✅ **Configurable ranges** - Custom min/max values and target numbers  
✅ **Batch generation** - Generate 1, 10, 100, or 1000 numbers at once  
✅ **Real-time tracking** - Live frequency analysis and deviation monitoring  
✅ **CSV export** - Export data for external statistical analysis  
✅ **Visual indicators** - Deviation bars, significance warnings, hit highlighting  

## How to Use

### Basic Operation
1. Set your range (default: 1-100)
2. Set target number (default: 89)
3. Click "Generate" to produce random numbers
4. Watch statistics update in real-time

### Batch Testing
1. Select batch size from dropdown:
   - Single (1) - Generate one number at a time
   - Small (10) - Quick batch testing
   - Medium (100) - Statistical significance starts here
   - Large (1000) - Comprehensive analysis
2. Click "Generate"
3. View batch summary in alert

### Understanding the Stats

**Total Generated**: Total number count across all sessions  
**89 Occurrences**: How many times target number appeared  
**Actual Frequency**: (Hits / Total) × 100  
**Deviation**: Difference from expected statistical frequency  

### Statistical Significance

The tool uses z-score analysis to determine if results are statistically significant:

- **< 100 samples**: Not enough data for meaningful analysis
- **p < 0.05**: Significant deviation (z-score > 1.96) - Pattern emerging
- **p < 0.01**: Highly significant (z-score > 2.576) - Reality glitch detected

## Squarespace Integration

### Method 1: Code Block (Recommended)
1. Add a **Code** block to your page
2. Copy entire contents of `index.html`
3. Paste into code block
4. Save and publish

### Method 2: Full Page
1. Create a new blank page
2. Add Code Injection in page settings
3. Paste the HTML in the header
4. Set page width to full

## Data Export

Click "Export CSV" to download data in spreadsheet format:
```csv
Timestamp,Number,Is_Target_Hit
2025-10-01T12:34:56.789Z,89,true
2025-10-01T12:35:01.234Z,42,false
```

Import into Excel, Google Sheets, or R/Python for further analysis.

## Testing Different Numbers

The tracker works for **any number**, not just 89:

- **23**: Discordian synchronicity
- **93**: Thelemic significance  
- **111/222/333**: Angel numbers
- **137**: Fine structure constant
- **420/666/777**: Cultural significance

## Technical Details

### Randomness Quality
Uses `crypto.getRandomValues()` which:
- Sources from operating system entropy
- Cryptographically secure
- Passes NIST randomness tests
- Suitable for statistical analysis

### Statistical Methods
- **Expected frequency**: 1 / (max - min + 1)
- **Chi-square test**: Compares observed vs expected distribution
- **Z-score**: Measures standard deviations from expected
- **P-value**: Probability results occurred by chance

### Browser Compatibility
- Chrome 90+ ✅
- Firefox 88+ ✅
- Safari 14+ ✅
- Edge 90+ ✅

## Privacy & Storage

- All data stored locally using `localStorage`
- No external API calls
- No tracking or analytics
- Reset clears all data permanently

## Interpretation Guide

### Normal Results (p > 0.05)
Your results fall within expected statistical variance. This is the most common outcome with true randomness.

### Significant Results (p < 0.05)
Your results deviate from expected frequency more than would occur by chance 95% of the time. Could indicate:
- Genuine synchronicity pattern
- Sample size still too small
- Random clustering (happens ~5% of the time)

### Highly Significant Results (p < 0.01)
Extremely unlikely to occur by chance. Could indicate:
- Strong synchronicity pattern
- Reality glitch
- True anomaly worth investigating

**Note**: Even with perfect randomness, 1 in 100 experiments will show p < 0.01 by pure chance.

## Recommended Testing Protocol

1. **Baseline**: Generate 1000 numbers, record deviation
2. **Focused intention**: Generate 1000 more while focusing on target
3. **Compare**: Did deviation increase or decrease?
4. **Replicate**: Repeat test on different days/times
5. **Export**: Save all data for longitudinal analysis

---

*Part of Project 89 Arsenal - Reality Hacking Technology*


