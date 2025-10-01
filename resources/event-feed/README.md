# Global Event Feed Dashboard

Real-time monitoring framework for tracking global events, technological developments, and pattern detection across multiple data sources.

## Overview

This tool provides **live RSS feed monitoring** out of the box, with no configuration required. It aggregates news from NY Times, BBC, Al Jazeera, Wired, TechCrunch, HackerNews, Science.org, and more. You can easily add additional RSS feeds or API keys for enhanced functionality.

## Features

✅ **Multi-source aggregation** - News, tech, anomalies, patterns  
✅ **Real-time updates** - Auto-refresh every 5 minutes  
✅ **Category filtering** - Organized by feed type  
✅ **Timestamp tracking** - "Time ago" display for all events  
✅ **Manual refresh** - Per-feed or all-feeds refresh  
✅ **Mobile responsive** - Monitor events on any device  
✅ **Extensible architecture** - Easy to add new feeds  

## Feed Types

### 🌍 Breaking News
General world news from major outlets. Tracks:
- Global politics
- Economic developments
- Major scientific breakthroughs
- International events

### 💻 Tech & AI
Technology and artificial intelligence updates. Tracks:
- AI/ML developments
- Quantum computing
- Neural interfaces
- Open source projects
- Computing breakthroughs

### ⚡ Anomalies
Filtered feed focusing on unusual/unprecedented events. Tracks:
- Unexplained phenomena
- Scientific anomalies
- Network/system irregularities
- Pattern breaks in normal systems

### 🎯 Pattern Detection
Synchronicity and pattern recognition. Tracks:
- Recurring numbers/symbols
- Correlation in unrelated events
- Emergent patterns in data
- Synchronicity events

## Configuration

### Current RSS Feeds (Works Immediately)

The tool comes pre-configured with these RSS feeds:

**News**:
- NY Times World News
- BBC World News
- Al Jazeera RSS

**Technology**:
- Wired RSS
- TechCrunch RSS
- HackerNews RSS

**Science**:
- Science.org News
- Phys.org RSS

### Adding More RSS Feeds

Edit the `CONFIG` object in the script section (around line 109):

```javascript
const CONFIG = {
  rssFeeds: {
    news: [
      'https://rss.nytimes.com/services/xml/rss/nyt/World.xml',
      'https://YOUR_RSS_FEED_HERE.xml'  // Add your own
    ],
    tech: [
      'https://www.wired.com/feed/rss',
      'https://YOUR_TECH_RSS_FEED_HERE.xml'
    ],
    // Add new categories
    crypto: [
      'https://cointelegraph.com/rss',
      'https://decrypt.co/feed'
    ]
  },
  
  // Use RSS2JSON service (default) or direct CORS proxy
  useRss2Json: true,  // Set to false to use allorigins.win instead
  
  // Customize keyword filters
  anomalyKeywords: ['breakthrough', 'unprecedented', 'anomaly'],
  patternKeywords: ['89', 'synchronicity', 'pattern']
};
```

### Adding API Keys (Optional)

For NewsAPI integration:

```javascript
const CONFIG = {
  newsApiKey: 'YOUR_API_KEY_HERE',  // Get free key at newsapi.org
  // ... rest of config
};
```

### Finding More RSS Feeds

#### Popular News RSS Feeds
```javascript
// World News
'https://rss.nytimes.com/services/xml/rss/nyt/World.xml'
'https://feeds.bbci.co.uk/news/world/rss.xml'
'https://www.aljazeera.com/xml/rss/all.xml'
'https://www.theguardian.com/world/rss'
'https://www.reddit.com/r/worldnews/.rss'

// Technology
'https://www.wired.com/feed/rss'
'https://feeds.feedburner.com/TechCrunch/'
'https://news.ycombinator.com/rss'
'https://www.theverge.com/rss/index.xml'
'https://techxplore.com/rss-feed/'

// Science
'https://www.science.org/rss/news_current.xml'
'https://phys.org/rss-feed/'
'https://www.scientificamerican.com/feed/'

// Crypto/Web3
'https://cointelegraph.com/rss'
'https://decrypt.co/feed'

// AI/ML
'https://venturebeat.com/category/ai/feed/'
```

#### How to Find RSS Feeds
1. **Look for RSS icon** on websites (orange RSS symbol)
2. **Add /rss or /feed** to site URL (e.g., `example.com/rss`)
3. **Check page source** for `<link type="application/rss+xml">`
4. **Use RSS finder tools**: feedly.com, rss.app

#### Free APIs (No auth required)
- **Reddit JSON**: `https://www.reddit.com/r/SUBREDDIT/.json`
- **HackerNews API**: `https://hacker-news.firebaseio.com/v0/topstories.json`

#### Free APIs (Auth required)
- **NewsAPI**: 100 requests/day free tier
- **OpenWeather**: Weather anomalies
- **GitHub Trending**: `https://api.github.com/search/repositories`

#### Premium APIs (Paid)
- **Reuters**: Professional news feed
- **Bloomberg**: Financial data
- **Associated Press**: Global news

### Implementing Live Feeds

Replace placeholder functions with real API calls:

```javascript
async function fetchNews() {
  const response = await fetch(
    `https://newsapi.org/v2/top-headlines?country=us&apiKey=${CONFIG.newsApiKey}`
  );
  const data = await response.json();
  return data.articles.map(article => ({
    title: article.title,
    source: article.source.name,
    time: article.publishedAt,
    category: article.category || 'News',
    url: article.url
  }));
}
```

## Squarespace Integration

### Method 1: Code Block
1. Add a **Code** block to your page
2. Copy entire contents of `index.html`
3. Configure API keys in the CONFIG section
4. Paste into code block
5. Save and publish

### Method 2: Full Page Dashboard
1. Create a dedicated "Events" page
2. Use full-width layout
3. Add HTML in Code Injection
4. Link from main navigation

## RSS Feed Parsing

The tool includes **two RSS parsing methods**:

### Method 1: RSS2JSON (Default)
Uses `https://api.rss2json.com` - free service, no auth required, CORS-friendly:

```javascript
// Already implemented in the tool
const apiUrl = `https://api.rss2json.com/v1/api.json?rss_url=${encodeURIComponent(url)}`;
```

**Pros**: Easy, reliable, handles most RSS formats  
**Cons**: External service dependency, 10k requests/day limit

### Method 2: AllOrigins Proxy  
Uses `https://api.allorigins.win` - CORS proxy with XML parsing:

```javascript
// Enable by setting CONFIG.useRss2Json = false
const proxyUrl = `https://api.allorigins.win/get?url=${encodeURIComponent(url)}`;
```

**Pros**: No rate limits, parses XML directly  
**Cons**: Slightly slower, may have occasional downtime

### Switching Between Methods

In the CONFIG section:
```javascript
const CONFIG = {
  useRss2Json: true,  // Use RSS2JSON service
  // OR
  useRss2Json: false, // Use AllOrigins proxy
};
```

## Anomaly Detection

The tool can automatically flag entries with anomaly keywords:

```javascript
function detectAnomaly(title, description) {
  const text = (title + ' ' + description).toLowerCase();
  return CONFIG.anomalyKeywords.some(keyword => 
    text.includes(keyword.toLowerCase())
  );
}
```

## Pattern Detection

Tracks recurring patterns across feeds:

```javascript
function detectPatterns(allFeeds) {
  // Look for recurring numbers, words, themes
  const wordFrequency = {};
  allFeeds.forEach(item => {
    const words = item.title.split(' ');
    words.forEach(word => {
      wordFrequency[word] = (wordFrequency[word] || 0) + 1;
    });
  });
  return wordFrequency;
}
```

## Auto-Refresh

The dashboard auto-refreshes every 5 minutes by default. To change:

```javascript
// Change interval (value in milliseconds)
setInterval(refreshAllFeeds, 10 * 60 * 1000); // 10 minutes
```

## CORS Issues

If you encounter CORS errors when fetching external feeds:

1. **Use CORS proxy**: `https://corsproxy.io/?${encodeURIComponent(url)}`
2. **Server-side fetch**: Create a backend endpoint
3. **Browser extension**: Use a CORS-unblocker extension for testing
4. **RSS-to-JSON services**: Use services like rss2json.com

## Privacy & Data

- All processing happens client-side
- No data stored permanently (refresh reloads)
- API keys stored only in your HTML (not transmitted)
- External API calls follow their respective privacy policies

## Performance

- **Initial load**: ~1-2 seconds with API calls
- **Refresh**: ~500ms per feed
- **Memory usage**: ~5-10MB for 100 items
- **Auto-refresh impact**: Minimal (background fetch)

## Troubleshooting

**"Loading feed..." stuck?**
- Check browser console for errors
- Verify API keys are correct
- Check if API rate limit exceeded
- Test API endpoint directly in browser

**No data appearing?**
- APIs may require authentication
- CORS issues (see CORS section)
- RSS feeds may be blocked
- Check network tab in DevTools

**Slow performance?**
- Reduce auto-refresh interval
- Limit number of items per feed
- Use pagination/lazy loading
- Cache results in localStorage

## Extending the Dashboard

### Adding New Feed Panels

1. Add HTML panel in feed-grid
2. Create fetch function for data source
3. Add to refreshAllFeeds()
4. Update CONFIG with any needed keys

### Custom Styling

All colors use CSS variables:
```css
--accent: #00ff88;    /* Primary green */
--accent-alt: #3cffea; /* Cyan */
--warning: #ff4f6d;   /* Red for alerts */
```

## 📡 Curated Feed Collections

### Consciousness & Esoteric
```javascript
consciousness: [
  'https://www.vice.com/en/rss',
  'https://mysteriousuniverse.org/feed/',
  'https://www.reddit.com/r/Glitch_in_the_Matrix/.rss'
]
```

### Crypto & Web3
```javascript
crypto: [
  'https://cointelegraph.com/rss',
  'https://decrypt.co/feed',
  'https://www.coindesk.com/arc/outboundfeeds/rss/'
]
```

### AI & Singularity
```javascript
ai: [
  'https://venturebeat.com/category/ai/feed/',
  'https://www.technologyreview.com/feed/',
  'https://www.reddit.com/r/singularity/.rss'
]
```

### Space & Physics
```javascript
space: [
  'https://www.nasa.gov/rss/dyn/breaking_news.rss',
  'https://www.space.com/feeds/all',
  'https://phys.org/rss-feed/space-news/'
]
```

Copy any of these collections into your CONFIG to expand monitoring coverage.

---

*Part of Project 89 Arsenal - Reality Hacking Technology*


