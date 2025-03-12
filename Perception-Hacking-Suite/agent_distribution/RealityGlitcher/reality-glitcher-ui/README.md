# Reality Glitcher UI

The frontend interface for Project 89's Reality Glitcher application, providing a quantum-styled UI for manipulating reality perception.

## Overview

This UI provides a bridge between the user's consciousness and the Reality Glitcher backend, enabling:

- Creation and management of various reality glitches
- Integration with Mind Mirror consciousness data
- Visualization of quantum fluctuations and reality distortions
- Monitoring of reality stability metrics

## Development Setup

Follow these steps to set up the development environment:

```bash
# Navigate to the UI directory
cd Perception-Hacking-Suite/RealityGlitcher/reality-glitcher-ui

# Install dependencies
npm install

# Start the development server
npm start
```

The development server will run on port 3000. However, the Reality Glitcher Python application serves the UI directly, so you typically don't need to run the development server separately.

## Building for Production

To create an optimized production build:

```bash
# Navigate to the UI directory
cd Perception-Hacking-Suite/RealityGlitcher/reality-glitcher-ui

# Create production build
npm run build
```

This will create a `build` folder with optimized files. The Reality Glitcher application will automatically use this folder if it exists.

## UI Architecture

The UI consists of:

1. **React Frontend** - Modern, responsive interface built with React
2. **Quantum Styling** - Custom CSS with quantum-inspired visual effects
3. **Reality API Integration** - Communication with the Python backend

## Fallback UI

The application includes a static HTML fallback UI that will be displayed if:

- The React application fails to load
- The `build` directory does not exist
- There are issues with the React application

This ensures agents always have a functional interface, even if the full React experience isn't available.

## Development Notes

- **CSS Files**: The UI uses multiple CSS files for styling:
  - `index.css` - Base styles
  - `tailwind.css` - Utility classes
  - `custom.css` - Project-specific styles
  - `RealityGlitcher.css` - Component-specific styles

- **Components**: The main UI components can be found in the `src/components` directory:
  - `RealityGlitcherUI.js` - Main UI container
  - `GlitchVisualization.js` - Visual representation of glitches
  - `RealTimeData.js` - Real-time data visualization
  - `GlitchControls.js` - Interface for creating and managing glitches

## Troubleshooting

If you encounter issues with the UI:

1. **Missing build directory**: Run `npm run build` to create it
2. **CSS not loading**: Check that all CSS files are present in the src directory
3. **Black screen**: Make sure the fallback UI is properly configured
4. **Network errors**: Verify the Python server is running correctly

## Creating a Custom Glitch UI

To create a custom glitch effect in the UI:

1. Add a new component in the `src/components` directory
2. Import and use the component in `RealityGlitcherUI.js`
3. Add appropriate CSS in `RealityGlitcher.css`
4. Connect to backend through the REST API

## Security Notes

The Reality Glitcher UI has several security features:

- Cross-Origin Resource Sharing (CORS) restrictions
- Input validation to prevent XSS attacks
- Protection against quantum consciousness injection

Always use caution when creating reality glitches, as they can have unpredictable effects on perception.

---

*Project 89: Reality is a canvas. Perception is the brush.*
