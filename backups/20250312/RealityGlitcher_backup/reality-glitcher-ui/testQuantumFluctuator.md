# Quantum Fluctuator Test Guide

This guide provides instructions for testing the Reality Glitcher UI quantum fluctuator component to ensure it's working correctly after our recent changes.

## Running the Application

To run the application:

1. Open a terminal in the `reality-glitcher-ui` directory
2. Run `npm start` to start the development server
3. Open your browser to `http://localhost:3000`

## Testing the Quantum Fluctuator

### Visual Verification

When the application loads, verify the following:

1. **Canvas Visibility**: The quantum fluctuator canvas should be clearly visible with a waveform line
2. **Waveform Color**: The waveform should be blue/cyan when not connected to Mind Mirror
3. **Animation**: The waveform should be moving/animating smoothly

### Mind Mirror Connection Test

To test the Mind Mirror connection:

1. Open the browser's developer console (F12 or right-click > Inspect > Console)
2. Run this code to simulate a Mind Mirror connection:
   ```javascript
   // Get the app's React root
   const rootElement = document.getElementById('root');
   const root = rootElement._reactRootContainer._internalRoot.current;
   
   // Find the RealTimeData component
   function findRealTimeDataComponent(fiber) {
     if (fiber.type && fiber.type.name === 'RealTimeData') {
       return fiber;
     }
     if (fiber.child) {
       const found = findRealTimeDataComponent(fiber.child);
       if (found) return found;
     }
     if (fiber.sibling) {
       const found = findRealTimeDataComponent(fiber.sibling);
       if (found) return found;
     }
     return null;
   }
   
   // Update the mindMirrorConnected prop
   const component = findRealTimeDataComponent(root);
   if (component && component.memoizedProps) {
     const oldProps = component.memoizedProps;
     // Trigger a re-render with Mind Mirror connected
     component.pendingProps = {...oldProps, mindMirrorConnected: true};
     // Force update
     console.log("Mind Mirror connection simulated!");
   }
   ```
3. Verify the waveform changes to purple with the text "MIND MIRROR PATTERN DETECTED"

### Emergency Draw Test

To test emergency draw functionality:

1. In the browser console, run:
   ```javascript
   // Remove the canvas
   const canvas = document.querySelector('.quantum-canvas-container canvas');
   if (canvas && canvas.parentNode) {
     canvas.parentNode.removeChild(canvas);
     console.log("Canvas removed - emergency draw should trigger within 3 seconds");
   }
   ```
2. Verify that a new canvas is automatically created within a few seconds, showing a waveform

### Testing Different Glitch Types

To test different glitch types:

1. In the browser console, run:
   ```javascript
   // Create test glitches
   window.testGlitches = [
     {
       id: 'test-visual-glitch',
       type: 'visual',
       intensity: 90,
       stability: 60,
       duration: 5
     }
   ];
   
   // Find and update the RealTimeData component
   const rootElement = document.getElementById('root');
   const root = rootElement._reactRootContainer._internalRoot.current;
   
   function findRealTimeDataComponent(fiber) {
     if (fiber.type && fiber.type.name === 'RealTimeData') {
       return fiber;
     }
     if (fiber.child) {
       const found = findRealTimeDataComponent(fiber.child);
       if (found) return found;
     }
     if (fiber.sibling) {
       const found = findRealTimeDataComponent(fiber.sibling);
       if (found) return found;
     }
     return null;
   }
   
   const component = findRealTimeDataComponent(root);
   if (component && component.memoizedProps) {
     component.pendingProps = {...component.memoizedProps, glitches: window.testGlitches};
     console.log("Test glitches applied!");
   }
   ```
2. Verify the waveform pattern changes based on the glitch type

## Automated Tests

We've also created automatic tests that can be run with:

```
npm test -- --testPathPattern=RealTimeData.test.js
```

These tests verify basic functionality like rendering and handling props changes.

## Manual Browser Tests

For more comprehensive testing, we've created a manual test script in `src/manualTest.js`. To use it:

1. Open the application in your browser
2. Open the browser console
3. Copy and paste the entire contents of `src/manualTest.js` into the console
4. Run the tests by typing `runAllTests()` or individual test functions like `testNormalOperation()`

## Expected Behavior

After our recent fixes, the quantum fluctuator should:

1. Always remain visible, never disappearing
2. Show a blue/cyan waveform during normal operation
3. Change to purple when Mind Mirror is connected
4. Automatically recover from errors and redraw itself if needed
5. Display higher frequency wave patterns, especially with certain glitch types
6. Use anti-aliasing and gradient effects for smoother appearance
7. Maintain reliable performance without memory leaks

If you encounter any issues during testing, please note:
- The specific scenario that caused the issue
- Any error messages in the console
- The visual state of the quantum fluctuator at the time of the issue 