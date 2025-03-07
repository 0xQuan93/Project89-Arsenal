# PROJECT89 REALITY GLITCHER v1.0.0

## Overview
Reality Glitcher is a cutting-edge perception manipulation interface developed as part of Project89's Perception-Hacking Suite. This cyberpunk-themed application provides a sophisticated UI for monitoring and altering reality perception through the implementation of various glitch types.

![Project89 Reality Glitcher](https://github.com/0xQuan93/Project89-Arsenal/raw/main/screenshots/reality-glitcher-preview.png)

## Features

### Reality Status Dashboard
- Real-time monitoring of coherence status and stability index
- Safety protocols toggle
- Session activity tracking
- Enhanced data visualization with glitch sensitivity

### Glitch Management System
- Create, activate, and modify perception glitches
- Support for multiple glitch types:
  - Visual
  - Auditory
  - Temporal
  - Spatial
  - Cognitive
  - Synchronistic
- Glitch intensity control via intuitive slider interface
- Advanced visualization of glitch effects
- Smart auto-expanding glitch list with scrolling capability

### Enhanced Quantum Fluctuations Graph
- **Advanced Real-Time Visualization**: Displays quantum fluctuations with smooth Bezier curves
- **Glitch-Specific Effects**:
  - Visual glitches create vibrant line effects with glow
  - Temporal glitches generate phase shifts and ghost echoes
  - Spatial glitches add distortion patterns and position jitter
  - Cognitive glitches create interference wave patterns
  - Synchronistic glitches generate mirrored line effects
- **Observer Effect**: Interactive elements that respond to user hovering
- **Fallback Rendering**: Robust emergency visualization if normal rendering fails
- **Enhanced Styling**: Glitch-responsive container styling and animations

### Real-time Data Visualization
- Repositioned quantum fluctuations graph for improved visibility
- Advanced sensor data displaying reality stability metrics
- Glitch impact visualization through sensor readouts
- System status indicators with real-time updates

### System Console
- Comprehensive logging of all system activities
- Color-coded messages by severity (INFO, WARNING, ERROR)
- Helpful status messages and guidance

## Technical Stack

- React.js frontend (v18.2.0)
- Tailwind CSS for styling
- Custom cyberpunk UI components
- Canvas API for advanced visualizations
- Integration with perception manipulation APIs

## Getting Started

### Prerequisites
- Node.js (v14.0.0 or higher)
- npm (v6.0.0 or higher)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/0xQuan93/Project89-Arsenal.git
cd Project89-Arsenal/Perception-Hacking-Suite/RealityGlitcher
```

2. Install dependencies:
```bash
cd reality-glitcher-ui
npm install
```

3. Start the development server:
```bash
npm start
```

The application will be available at http://localhost:3000

## Usage Guide

### Creating New Glitches
1. Navigate to the Glitch List panel
2. Click the "+ CREATE" button to open the glitch creation modal
3. Select parameters for your new glitch, or use the randomizer
4. Click "CREATE" to generate the glitch
5. The glitch list will auto-expand to accommodate new glitches, with scrolling enabled when necessary

### Controlling Glitches
1. Click on a glitch from the Glitch List to load it into the Control Panel
2. Use the intensity slider to adjust the glitch strength (0-100%)
3. Click "ACTIVATE" to apply the glitch to the reality matrix
4. Monitor effects in the visualization panel, quantum fluctuations graph, and reality status dashboard
5. Click "AMPLIFY" to temporarily boost a glitch's effect (available for active glitches)
6. Click "DELETE" to remove unwanted glitches

### Monitoring Reality Status
1. The quantum fluctuations graph at the top shows the real-time stability of reality
2. Observe how different glitch types create unique patterns in the graph
3. Sensor bars below the graph provide detailed metrics on specific aspects of reality
4. The coherence level and stability index in the status dashboard provide overall system status

### Safety Protocols
- It's recommended to keep safety protocols ACTIVE during normal operation
- Disabling safety protocols allows for more extreme glitch effects but may lead to unpredictable results
- The system will emit warnings when operating in an unsafe state
- Emergency protocols automatically engage if stability drops too low

## Mind Mirror Integration

RealityGlitcher can integrate with the Mind Mirror application to create reality glitches based on your neural patterns and consciousness data.

### Enhanced Integration Features

1. **Visual Transformation**: When Mind Mirror is connected, the quantum fluctuations graph transforms with a purple color scheme
2. **Neural Pattern Analysis**: RealityGlitcher analyzes the neural patterns, nodes, and connections in the exported data
3. **Glitch Generation**: Based on your consciousness data, RealityGlitcher generates personalized glitches that reflect your neural patterns
4. **Reality Alteration**: These glitches affect reality in ways that resonate with your consciousness patterns
5. **Focused Styling**: Mind Mirror connection effects are focused only on the quantum graph, not the sensor bars

### How Integration Works

1. **Data Export**: Mind Mirror exports your consciousness data to the `imports/mind_mirror_data.json` file within the RealityGlitcher directory.
2. **Data Detection**: RealityGlitcher automatically detects new Mind Mirror data and establishes a connection
3. **Neural Pattern Analysis**: RealityGlitcher analyzes the neural patterns, nodes, and connections in the exported data
4. **Glitch Generation**: Based on your consciousness data, RealityGlitcher generates personalized glitches that reflect your neural patterns
5. **Reality Alteration**: These glitches then affect reality in ways that resonate with your consciousness patterns

### Running the Integration Demo

To experience the integration between Mind Mirror and RealityGlitcher:

1. Run Mind Mirror and use the integration feature to export your data
2. Launch the integration demo:
   ```
   cd examples
   python integration_demo.py
   ```
3. Observe how your consciousness patterns influence the reality glitches

## Troubleshooting

### Black Screen on Launch
If you encounter a black screen when launching the application:
1. Check browser console for JavaScript errors
2. Verify that all CSS files are loading correctly
3. Ensure your browser supports all required features (Canvas API, CSS Grid, etc.)
4. Try clearing your browser cache and reloading

### Performance Issues
For optimal performance:
1. Close unnecessary browser tabs and applications
2. Ensure your graphics drivers are up to date
3. Reduce the number of active glitches if experiencing lag
4. Consider disabling some visual effects if needed

### Mind Mirror Connection Issues
If you're having trouble connecting to Mind Mirror:
1. Ensure the Mind Mirror application is running and has exported data
2. Check that the data files are in the correct location (imports directory)
3. Restart both applications if the connection doesn't establish
4. Verify data file format integrity

## Contributing

We welcome contributions to the Reality Glitcher project! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b new-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin new-feature`
5. Submit a pull request

Please ensure all code passes ESLint validation before submitting.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

Reality Glitcher is a creative fictional project. Any resemblance to actual reality manipulation technology is purely coincidental. The developers assume no responsibility for any perceived alterations to your reality. 