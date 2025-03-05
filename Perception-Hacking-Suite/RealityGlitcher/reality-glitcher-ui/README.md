# Reality Glitcher UI

The frontend interface for PROJECT89's Reality Glitcher perception manipulation system. This cyberpunk-themed React application provides an immersive and intuitive interface for monitoring and controlling reality glitches.

## Architecture

The Reality Glitcher UI is built as a standalone React application that communicates with the Reality Glitcher backend API. The project follows a component-based architecture with the following key features:

### Core Components

- **RealityGlitcherUI**: The main container component that orchestrates all UI elements and manages application state
- **IntensitySlider**: A customizable slider component for controlling glitch intensity
- **RealTimeData**: Visualizes real-time data about reality stability and glitch impacts
- **ScrollWheel**: (Legacy component) Previously used for intensity control, now replaced by a horizontal slider

### State Management

The application uses React's built-in state management with useState and useEffect hooks:
- Glitches state (create, activate, select, modify)
- Reality status (stability, coherence, safety protocols)
- Console messages (system logs)
- UI state (scrollable containers, selected elements)

### Smart Features

- **Auto-expanding Glitch List**: Dynamically resizes based on content with maximum height constraints
- **Real-time monitoring**: Updates stability and coherence metrics based on active glitches
- **Responsive Design**: Adapts to different screen sizes while maintaining the cyberpunk aesthetic

## Development

### Project Structure

```
reality-glitcher-ui/
├── public/
├── src/
│   ├── components/
│   │   ├── RealityGlitcherUI.js  # Main component
│   │   ├── ScrollWheel.js        # Intensity slider component
│   │   └── RealTimeData.js       # Data visualization component
│   ├── RealityGlitcher.css       # Main styles
│   ├── App.js                    # Root component
│   ├── index.js                  # Entry point
│   └── ...
├── package.json
└── ...
```

### Available Scripts

- **npm start**: Runs the app in development mode at [http://localhost:3000](http://localhost:3000)
- **npm test**: Launches the test runner in interactive watch mode
- **npm run build**: Builds the app for production to the `build` folder
- **npm run eject**: Ejects from Create React App configuration (use with caution)

### Technologies Used

- **React**: UI library for building component-based interfaces
- **Tailwind CSS**: Utility-first CSS framework for styling
- **craco**: Configuration layer for Create React App
- **Chart.js** (via react-chartjs-2): For data visualizations

## Styling

The UI follows a cyberpunk aesthetic with:
- Neon color highlights (blue, purple, green)
- Dark backgrounds with subtle gradients
- Grid patterns and glowing effects
- Custom animations for reality glitches

## Browser Compatibility

The Reality Glitcher UI is optimized for modern browsers:
- Chrome/Edge (latest versions)
- Firefox (latest version)
- Safari (latest version)

Certain visual effects may have degraded performance on older browsers or lower-end hardware.

## Future Development

Planned features for future releases:
- Glitch templates and presets
- Advanced visualization options
- User profiles and saved configurations
- Expanded reality monitoring metrics
- Integration with external perception systems

## Contributing

Please refer to the main [Reality Glitcher README](../README.md) for contribution guidelines.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
