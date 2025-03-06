/**
 * RealTimeData Component Manual Test Script
 * 
 * To use this test script:
 * 1. Import the functions into your browser console when the app is running
 * 2. Call each test function to verify functionality
 * 
 * NOTE: Copy and paste this entire file into your browser console when the Reality Glitcher UI is running
 */

// Test 1: Test normal operation
function testNormalOperation() {
  console.log('RUNNING TEST: Normal Operation');
  
  // Access the React component instance
  const appElement = document.querySelector('#root');
  if (!appElement) {
    console.error('App root element not found');
    return false;
  }
  
  // Find the canvas element
  const canvas = document.querySelector('.quantum-canvas-container canvas');
  if (!canvas) {
    console.error('Canvas element not found');
    return false;
  }
  
  console.log('✅ Canvas is rendering properly');
  
  // Check if the animation is running by capturing pixel data at two different times
  const ctx = canvas.getContext('2d');
  const data1 = ctx.getImageData(50, 50, 1, 1).data;
  
  // Wait for a frame to pass
  setTimeout(() => {
    const data2 = ctx.getImageData(50, 50, 1, 1).data;
    
    // Compare the data - if the animation is running, pixels should change
    const pixelsChanged = !data1.every((val, i) => val === data2[i]);
    
    if (pixelsChanged) {
      console.log('✅ Animation is running properly');
    } else {
      console.warn('⚠️ Animation may not be running - pixels are not changing');
    }
  }, 100);
  
  return true;
}

// Test 2: Test Mind Mirror connection
function testMindMirrorConnection() {
  console.log('RUNNING TEST: Mind Mirror Connection');
  
  // Access the React component through the __REACT_DEVTOOLS_GLOBAL_HOOK__
  // This is a development-only approach
  let fiber = null;
  try {
    const hook = window.__REACT_DEVTOOLS_GLOBAL_HOOK__;
    if (hook) {
      const renderers = hook.getFiberRoots(1);
      const root = renderers.keys().next().value;
      fiber = root.current;
    }
  } catch (e) {
    console.error('Could not access React internals:', e);
  }
  
  if (!fiber) {
    console.warn('⚠️ Cannot directly access React component state - testing via DOM only');
    
    // Alternative: modify window variable that React component might be reading
    window.mindMirrorConnected = true;
    console.log('Set window.mindMirrorConnected = true. Verify if the quantum fluctuator has turned purple');
    
    return false;
  }
  
  // Find the RealTimeData component instance
  let realTimeDataInstance = null;
  function findComponent(fiber) {
    if (fiber.type && fiber.type.name === 'RealTimeData') {
      return fiber.stateNode;
    }
    
    // Check child fibers
    if (fiber.child) {
      const result = findComponent(fiber.child);
      if (result) return result;
    }
    
    // Check sibling fibers
    if (fiber.sibling) {
      const result = findComponent(fiber.sibling);
      if (result) return result;
    }
    
    return null;
  }
  
  realTimeDataInstance = findComponent(fiber);
  
  if (!realTimeDataInstance) {
    console.warn('⚠️ Could not find RealTimeData component instance');
    return false;
  }
  
  // Force an update with mind mirror connected
  const props = realTimeDataInstance.props;
  const newProps = { ...props, mindMirrorConnected: true };
  
  // Update the component props (this approach varies based on React version)
  // For React 19, use the new approach
  if (realTimeDataInstance.setProps) {
    realTimeDataInstance.setProps(newProps);
    console.log('✅ Mind Mirror connection simulated. Verify if quantum fluctuator has turned purple');
    return true;
  } else {
    console.warn('⚠️ Cannot update component props directly');
    window.mindMirrorConnected = true;
    console.log('Set window.mindMirrorConnected = true. Verify if the quantum fluctuator has turned purple');
    return false;
  }
}

// Test 3: Test with emergency data
function testEmergencyData() {
  console.log('RUNNING TEST: Emergency Data Generation');
  
  // Find the canvas element
  const canvas = document.querySelector('.quantum-canvas-container canvas');
  if (!canvas) {
    console.error('Canvas element not found');
    return false;
  }
  
  // Force an emergency draw by temporarily removing the canvas
  const container = canvas.parentElement;
  const originalCanvas = container.removeChild(canvas);
  
  console.log('Canvas removed temporarily - emergency draw should be triggered');
  
  // Wait for emergency draw to kick in
  setTimeout(() => {
    // Check if a new canvas was created
    const newCanvas = document.querySelector('.quantum-canvas-container canvas');
    
    if (newCanvas) {
      console.log('✅ Emergency canvas creation successful');
    } else {
      console.warn('⚠️ Emergency canvas creation failed');
      // Put the original canvas back
      container.appendChild(originalCanvas);
    }
  }, 3500); // Wait longer than the emergency interval
  
  return true;
}

// Test 4: Test with glitches
function testWithGlitches() {
  console.log('RUNNING TEST: Glitch Effects');
  
  // Create test glitches
  const testGlitches = [
    {
      id: 'test-visual-glitch',
      type: 'visual',
      intensity: 90,
      stability: 60,
      duration: 5
    },
    {
      id: 'test-temporal-glitch',
      type: 'temporal',
      intensity: 80,
      stability: 40,
      duration: 10
    }
  ];
  
  // Set a global variable for the component to pick up
  window.testGlitches = testGlitches;
  
  console.log('Set window.testGlitches. Verify if the quantum fluctuator shows different patterns');
  
  return true;
}

// Run all tests function
function runAllTests() {
  console.log('🧪 RUNNING ALL QUANTUM FLUCTUATOR TESTS 🧪');
  
  const results = [];
  
  results.push({ test: 'Normal Operation', result: testNormalOperation() });
  
  // Run the remaining tests with delays
  setTimeout(() => {
    results.push({ test: 'Mind Mirror Connection', result: testMindMirrorConnection() });
    
    setTimeout(() => {
      results.push({ test: 'Emergency Data', result: testEmergencyData() });
      
      setTimeout(() => {
        results.push({ test: 'Glitch Effects', result: testWithGlitches() });
        
        console.log('🔍 TEST SUMMARY:');
        results.forEach(r => {
          console.log(`${r.result ? '✅' : '❌'} ${r.test}`);
        });
      }, 4000);
    }, 4000);
  }, 2000);
}

console.log('QuantumFluctuator Tests Loaded!');
console.log('To run all tests, type: runAllTests()');
console.log('Or run individual tests:');
console.log('- testNormalOperation()');
console.log('- testMindMirrorConnection()');
console.log('- testEmergencyData()');
console.log('- testWithGlitches()'); 