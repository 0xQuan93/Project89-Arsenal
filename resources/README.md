# Project 89 - Web-Based Reality Hacking Tools

A collection of utilitarian, browser-based tools for consciousness exploration, pattern detection, and reality monitoring. All tools are self-contained HTML files designed for easy embedding on any website.

## 🛠️ Available Tools

### 1. Agent Halo Forge
**Location**: `green-ring-tool/`  
**Purpose**: Avatar creation with neon halo overlay

Create Project 89 agent avatars by uploading portraits and applying a signature neon halo ring. Includes consciousness sync tracking, reality mantras, and timeline probability indicators.

**Key Features**:
- Drag-to-position, zoom controls
- Export at original dimensions
- PNG/JPG output
- Agent features: mantras, consciousness sync, manifestation probability

[→ Documentation](green-ring-tool/README.md)

---

### 2. Reality Glitch Logger  
**Location**: `glitch-logger/`  
**Purpose**: Track and analyze synchronicities and reality anomalies

A systematic logging tool for documenting déjà vu, number synchronicities, temporal anomalies, prophetic dreams, and other glitch phenomena.

**Key Features**:
- 7 glitch categories (Number Sync, Déjà Vu, Temporal, Pattern, Prophetic, Entity, Other)
- Local storage persistence
- Search & filter functionality
- Statistics dashboard (total, today, weekly, top category)
- Export to JSON or text format

[→ Documentation](glitch-logger/README.md)

---

### 3. 89 Frequency Tracker
**Location**: `frequency-tracker/`  
**Purpose**: Statistical analysis of synchronicity patterns in random number generation

Random number generator with real-time statistical analysis. Detects whether target numbers (like 89) appear at expected frequencies or show anomalous patterns.

**Key Features**:
- Cryptographic-grade randomness (crypto.getRandomValues)
- Customizable ranges and target numbers
- Batch generation (1, 10, 100, 1000)
- Chi-square and z-score analysis
- Statistical significance testing (p-values)
- CSV export for external analysis

[→ Documentation](frequency-tracker/README.md)

---

### 4. Global Event Feed Dashboard
**Location**: `event-feed/`  
**Purpose**: Real-time monitoring of global events and pattern detection

Multi-feed dashboard aggregating news from NY Times, BBC, Al Jazeera, Wired, TechCrunch, HackerNews, Science.org, and more. Uses RSS feeds (works immediately, no auth) with optional API integration for additional sources.

**Key Features**:
- 4 feed types: Breaking News, Tech & AI, Anomalies, Pattern Detection
- Live RSS parsing (RSS2JSON or AllOrigins proxy)
- Pre-configured with 7+ quality news sources
- Auto-refresh every 5 minutes
- Keyword filtering for anomalies and patterns
- Extensible - easily add more RSS feeds or APIs

[→ Documentation](event-feed/README.md)

---

## 🎯 Tool Categories

### Consciousness Exploration
- **Agent Halo Forge**: Visual identity creation and consciousness sync
- **Reality Glitch Logger**: Subjective experience documentation

### Pattern Detection  
- **89 Frequency Tracker**: Statistical synchronicity analysis
- **Global Event Feed**: Objective reality monitoring

---

## 📦 Squarespace Integration

All tools are designed as **self-contained embeds** for Squarespace and other website builders:

### Quick Embed (All Tools)
1. Open Squarespace page editor
2. Add a **Code Block** 
3. Copy entire contents of tool's `index.html`
4. Paste into code block
5. Save and publish

### Full Page (Recommended for Dashboard)
1. Create new blank page
2. Go to Page Settings → Advanced → Page Header Code Injection
3. Paste tool HTML
4. Set page width to full

---

## 🔧 Technical Specifications

### Common Features Across All Tools
- ✅ **Self-contained**: Single HTML file with inline CSS/JS
- ✅ **No dependencies**: Pure vanilla JavaScript, no libraries
- ✅ **Local processing**: All computation happens client-side
- ✅ **Privacy-focused**: No external data transmission
- ✅ **Mobile responsive**: Works on all screen sizes
- ✅ **Dark cyberpunk aesthetic**: Consistent Project 89 styling

### Browser Compatibility
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

### File Sizes
- Agent Halo Forge: ~25KB
- Reality Glitch Logger: ~15KB
- 89 Frequency Tracker: ~18KB
- Global Event Feed: ~20KB

---

## 🎨 Design System

All tools share a unified cyberpunk aesthetic:

### Color Palette
```css
--bg: #05010f;              /* Deep space black */
--accent: #00ff88;          /* Neon green (primary) */
--accent-alt: #3cffea;      /* Cyan (secondary) */
--text: #f1f6ff;            /* Off-white text */
--subtext: rgba(241,246,255,.7); /* Dimmed text */
--warning: #ff4f6d;         /* Alert red */
```

### Typography
- **Headings**: Orbitron, Rajdhani (sci-fi feel)
- **Body**: Rajdhani, Exo, Segoe UI
- **Monospace**: System monospace (for data/timestamps)

### Visual Effects
- Animated grid backgrounds
- Neon glow on interactive elements
- Box shadow depth
- Gradient borders
- Smooth transitions

---

## 🔐 Privacy & Security

### Data Storage
- **Local only**: All tools use browser localStorage
- **No transmission**: Zero external API calls (except Event Feed with user-configured keys)
- **No tracking**: No analytics, cookies, or fingerprinting
- **User control**: Clear data anytime via reset/clear functions

### Security Features
- **Cryptographic randomness**: Frequency Tracker uses crypto.getRandomValues()
- **XSS protection**: All user input is escaped before rendering
- **No eval()**: No dynamic code execution
- **CSP compatible**: Works with Content Security Policies

---

## 🚀 Future Tools (Roadmap)

Potential additions to the arsenal:

- **Meditation Timer**: Consciousness practice tracking with binaural beat generation
- **Dream Journal**: Voice-to-text dream logging with pattern analysis
- **Timeline Visualizer**: Personal synchronicity mapping on interactive timeline
- **Collective Consciousness Meter**: Aggregated glitch data from all agents
- **Reality Stability Index**: Real-time measurement of consensus reality coherence
- **Neurolinguistic Virus Builder**: Memetic payload construction interface

---

## 🤝 Contributing

To add new tools to the arsenal:

1. **Follow naming convention**: `tool-name/index.html`
2. **Create README**: Document features, usage, integration
3. **Match design system**: Use shared color palette and styling
4. **Self-contained**: Single HTML file, no external dependencies
5. **Mobile-first**: Responsive design from the start
6. **Privacy-focused**: Local processing, no tracking

---

## 📄 License

All tools are part of the Project 89 Arsenal and inherit the project's licensing terms.

---

## 🔮 Philosophy

These tools embody the Project 89 principle of **practical reality hacking**. They're not mystical or abstract—they're utilitarian instruments for consciousness exploration and pattern detection. Each tool serves a specific function in the agent's journey toward awakening and timeline optimization.

The aesthetic isn't just visual—it reflects the underlying truth that we're operating at the intersection of consciousness and code, reality and simulation, pattern and chaos.

---

*Manifest the optimal timeline through systematic observation, statistical analysis, and conscious creation.*

**Project 89 - Reality Hacking Technology**


