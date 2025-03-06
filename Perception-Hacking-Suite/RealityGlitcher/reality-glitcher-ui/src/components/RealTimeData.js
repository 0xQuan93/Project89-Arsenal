import React, { useState, useEffect, useRef, useCallback } from 'react';

const RealTimeData = ({ glitches, realityStatus, mindMirrorConnected }) => {
  // Use a ref to store data points to prevent re-renders
  const dataPointsRef = useRef(Array(100).fill(0.5));
  // Keep a state version for components that need to re-render - used in JSX render
  const [dataPointsState, setDataPointsState] = useState(Array(100).fill(0.5));
  const [sensorData, setSensorData] = useState({
    neuralActivity: 78.4,
    perceptionShift: 12.3,
    realityCoherence: 89.7,
    temporalSync: 99.2,
    cognitiveDissonance: 15.0,
    quantumEntanglement: 45.2
  });
  const [anomalies, setAnomalies] = useState([]);
  const [lastAnomalyTime, setLastAnomalyTime] = useState(0);
  const canvasRef = useRef(null);
  const animationRef = useRef(null);
  const lastUpdateTimeRef = useRef(Date.now());
  
  // Animation speed control - higher values = faster cycles
  const cycleSpeedMultiplier = 3.0; // Increased from 2.0 to 3.0 for even faster cycles
  
  // EMERGENCY RENDERING SYSTEM
  useEffect(() => {
    console.log("SETTING UP EMERGENCY SYSTEM");
    
    // Create reliable data with higher frequency cycles
    function createReliableData() {
      const time = Date.now() * 0.001;
      const points = [];
      for (let i = 0; i < 100; i++) {
        // Increased frequency from 0.1 to 0.25 for more cycles
        points[i] = 0.5 + Math.sin(i * 0.25 + time) * 0.3;
      }
      return points;
    }
    
    // Guaranteed emergency draw function
    function emergencyDraw() {
      try {
        console.log("EMERGENCY DRAW ATTEMPT");
        const canvas = canvasRef.current;
        if (!canvas) {
          console.error("Emergency: Canvas ref is null");
          return;
        }
        
        // Ensure dimensions
        if (canvas.width === 0) canvas.width = 600;
        if (canvas.height === 0) canvas.height = 130;
        
        const ctx = canvas.getContext('2d');
        if (!ctx) {
          console.error("Emergency: Context is null");
          return;
        }
        
        // EMERGENCY DATA with higher frequency cycles
        const emergencyData = createReliableData();
        
        // Update our data ref too
        dataPointsRef.current = emergencyData;
        
        // SIMPLEST POSSIBLE RENDERING
        ctx.fillStyle = 'rgb(0, 0, 0)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        // RED EMERGENCY BORDER
        ctx.strokeStyle = 'rgb(255, 0, 0)';
        ctx.lineWidth = 3;
        ctx.strokeRect(3, 3, canvas.width-6, canvas.height-6);
        
        // Draw the waveform in a bright color
        ctx.beginPath();
        ctx.strokeStyle = 'rgb(0, 255, 255)';
        ctx.lineWidth = 3;
        
        for (let i = 0; i < emergencyData.length; i++) {
          const x = (i / (emergencyData.length - 1)) * canvas.width;
          const y = (1 - emergencyData[i]) * canvas.height;
          
          if (i === 0) {
            ctx.moveTo(x, y);
          } else {
            ctx.lineTo(x, y);
          }
        }
        
        ctx.stroke();
        
        // Emergency text
        ctx.fillStyle = 'rgb(255, 255, 0)';
        ctx.font = '16px monospace';
        ctx.fillText("EMERGENCY RENDER", 10, 20);
        
        console.log("EMERGENCY DRAW COMPLETE");
      } catch (error) {
        console.error("Emergency draw failed:", error);
      }
    }
    
    // Set intervals that can't be canceled
    const emergencyInterval = setInterval(emergencyDraw, 2000);
    
    return () => {
      clearInterval(emergencyInterval);
    };
  }, []);
  
  // Use callback to prevent recreation of the function on each render
  const startAnimation = useCallback(() => {
    const animate = () => {
      updateData();
      drawCanvas();
      animationRef.current = requestAnimationFrame(animate);
    };
    
    // Start the animation loop
    animate();
    
    // Add a backup timer to ensure the canvas is always updated
    setInterval(() => {
      if (canvasRef.current) {
        drawCanvas();
      }
    }, 1000);
  }, []);
  
  // Dynamic data generation with higher frequency cycles
  const updateData = () => {
    try {
      const currentTime = Date.now();
      const time = currentTime * 0.001; // Time in seconds
      
      // Get active glitches for a simpler calculation
      const activeGlitches = glitches.filter(g => g.active);
      
      // Base wave with increased frequency (from 1.5 to 3.0)
      let newValue = 0.5 + Math.sin(time * 3.0) * 0.25;
      
      // Add basic variation from active glitches with higher frequency (from 2.2 to 4.0)
      if (activeGlitches.length > 0) {
        // Just add a scaled sin wave based on glitch count
        newValue += Math.sin(time * 4.0) * 0.05 * Math.min(5, activeGlitches.length);
      }
      
      // Add basic Mind Mirror effect with higher frequency (from 3.0 to 5.5)
      if (mindMirrorConnected) {
        newValue += Math.sin(time * 5.5) * 0.1;
      }
      
      // Add small random fluctuation
      newValue += (Math.random() * 0.04 - 0.02);
      
      // Safety bounds - critical to ensure visibility
      newValue = Math.max(0.2, Math.min(0.8, newValue));
      
      // Update with simplified approach
      const newPoints = [...dataPointsRef.current];
      newPoints.push(newValue);
      newPoints.shift();
      dataPointsRef.current = newPoints;
      
      // Update state occasionally
      if (currentTime % 200 < 20) {
        setDataPointsState([...newPoints]);
      }
      
      // Continue with sensor and anomaly updates
      updateSensorData(Math.min(0.1, (currentTime - lastUpdateTimeRef.current) / 1000), activeGlitches);
      updateAnomalies(activeGlitches);
      lastUpdateTimeRef.current = currentTime;
    } catch (error) {
      console.error("Error in updateData:", error);
      
      // Emergency recovery - create a simple sine wave if anything fails
      const time = Date.now() * 0.001;
      const fallbackPoints = [];
      for (let i = 0; i < 100; i++) {
        // Increased frequency from 0.1 to 0.25 for more cycles
        fallbackPoints.push(0.5 + Math.sin((i * 0.25) + time * 1.0) * 0.3);
      }
      dataPointsRef.current = fallbackPoints;
    }
  };
  
  // Separated sensor update logic for clarity
  const updateSensorData = (deltaTime, activeGlitches) => {
    const fluctuation = () => (Math.random() * 1.2 - 0.6) * deltaTime;
    let neuralEffect = 0;
    let perceptionEffect = 0;
    let coherenceEffect = 0;
    let temporalEffect = 0;
    let cognitiveEffect = 0;
    let entanglementEffect = 0;
    
    activeGlitches.forEach(glitch => {
      const impact = glitch.intensity * 5 * deltaTime;
      const mindMirrorMultiplier = glitch.source === 'Mind Mirror' ? 1.5 : 1.0;
      
      switch(glitch.type) {
        case 'VISUAL':
          neuralEffect += impact * 0.8 * mindMirrorMultiplier;
          perceptionEffect += impact * 1.2 * mindMirrorMultiplier;
          entanglementEffect += glitch.source === 'Mind Mirror' ? impact * 1.1 : 0;
          break;
        case 'AUDITORY':
          neuralEffect += impact * 0.6 * mindMirrorMultiplier;
          perceptionEffect += impact * 0.9 * mindMirrorMultiplier;
          cognitiveEffect += impact * 0.7 * mindMirrorMultiplier;
          entanglementEffect += glitch.source === 'Mind Mirror' ? impact * 0.7 : 0;
          break;
        case 'TEMPORAL':
          temporalEffect += impact * 1.5 * mindMirrorMultiplier;
          coherenceEffect += impact * 0.8 * mindMirrorMultiplier;
          entanglementEffect += glitch.source === 'Mind Mirror' ? impact * 1.8 : 0;
          break;
        case 'SPATIAL':
          perceptionEffect += impact * 1.1 * mindMirrorMultiplier;
          coherenceEffect += impact * 1.0 * mindMirrorMultiplier;
          temporalEffect += impact * 0.5 * mindMirrorMultiplier;
          entanglementEffect += glitch.source === 'Mind Mirror' ? impact * 1.3 : 0;
          break;
        case 'COGNITIVE':
          cognitiveEffect += impact * 1.4 * mindMirrorMultiplier;
          neuralEffect += impact * 0.9 * mindMirrorMultiplier;
          entanglementEffect += glitch.source === 'Mind Mirror' ? impact * 2.0 : 0;
          break;
        case 'SYNCHRONISTIC':
          perceptionEffect += impact * 0.7 * mindMirrorMultiplier;
          temporalEffect += impact * 0.6 * mindMirrorMultiplier;
          entanglementEffect += impact * 1.3 * mindMirrorMultiplier;
          coherenceEffect += impact * 0.9 * mindMirrorMultiplier;
          break;
        default:
          break;
      }
      
      if (glitch.isAdvanced) {
        cognitiveEffect += impact * 0.5;
        entanglementEffect += impact * 0.8;
      }
      
      if (glitch.crossModal) {
        perceptionEffect += impact * 0.4;
        neuralEffect += impact * 0.3;
      }
    });
    
    // Mind Mirror global effect on quantum entanglement
    const mindMirrorEntanglementBoost = mindMirrorConnected ? 10 * deltaTime : 0;
    entanglementEffect += mindMirrorEntanglementBoost;
    
    const safetyFactor = realityStatus.safetyProtocols ? 0.6 : 1.0;
    
    // Update sensor data with smoother transitions
    setSensorData(prev => {
      // Create smoother changes by lerping between current and target values
      const lerp = (current, target, t) => current + (target - current) * Math.min(1, t * 2);
      
      // Calculate target values with new effects
      const targetNeural = Math.max(0, Math.min(100, prev.neuralActivity + (neuralEffect * safetyFactor) + fluctuation()));
      const targetPerception = Math.max(0, Math.min(100, prev.perceptionShift + (perceptionEffect * safetyFactor) + fluctuation()));
      const targetCoherence = Math.max(0, Math.min(100, prev.realityCoherence - (coherenceEffect * safetyFactor) + fluctuation()));
      const targetTemporal = Math.max(0, Math.min(100, prev.temporalSync - (temporalEffect * safetyFactor) + fluctuation()));
      const targetCognitive = Math.max(0, Math.min(100, prev.cognitiveDissonance + (cognitiveEffect * safetyFactor) + fluctuation()));
      const targetEntanglement = Math.max(0, Math.min(100, prev.quantumEntanglement + (entanglementEffect * safetyFactor) + fluctuation()));
      
      // Return smoothed values
      return {
        neuralActivity: lerp(prev.neuralActivity, targetNeural, deltaTime),
        perceptionShift: lerp(prev.perceptionShift, targetPerception, deltaTime),
        realityCoherence: lerp(prev.realityCoherence, targetCoherence, deltaTime),
        temporalSync: lerp(prev.temporalSync, targetTemporal, deltaTime),
        cognitiveDissonance: lerp(prev.cognitiveDissonance, targetCognitive, deltaTime),
        quantumEntanglement: lerp(prev.quantumEntanglement, targetEntanglement, deltaTime)
      };
    });
  };
  
  // Separated anomaly update logic
  const updateAnomalies = (activeGlitches) => {
    const now = Date.now();
    const timeSinceLastAnomaly = now - lastAnomalyTime;
    const minimumInterval = 3000; // minimum 3 seconds between anomaly updates
    
    if (activeGlitches.length > 0 && timeSinceLastAnomaly > minimumInterval && Math.random() < 0.05) {
      const newAnomalies = [];
      const anomaliesToGenerate = Math.min(2, Math.ceil(Math.random() * 2));
      
      for (let i = 0; i < anomaliesToGenerate; i++) {
        if (Math.random() < 0.7) {
          newAnomalies.push(generateAnomaly(activeGlitches));
        }
      }
      
      if (newAnomalies.length > 0) {
        setAnomalies(prev => {
          const updated = [...prev, ...newAnomalies].slice(-5);
          return updated;
        });
        setLastAnomalyTime(now);
      }
    } else if (anomalies.length > 0 && Math.random() < 0.01 && timeSinceLastAnomaly > minimumInterval) {
      setAnomalies(prev => prev.slice(0, prev.length - 1));
      setLastAnomalyTime(now);
    }
  };
  
  // Ultra-reliable canvas drawing - absolute simplicity
  const drawCanvas = () => {
    try {
      console.log("Attempting to draw canvas...");
      const canvas = canvasRef.current;
      if (!canvas) {
        console.error("Canvas ref is null");
        return;
      }
      
      const ctx = canvas.getContext('2d');
      if (!ctx) {
        console.error("Could not get canvas context");
        return;
      }
      
      // Check if canvas has size
      if (canvas.width === 0 || canvas.height === 0) {
        console.error("Canvas has zero dimensions", canvas.width, canvas.height);
        canvas.width = 600;
        canvas.height = 130;
      }
      
      const width = canvas.width;
      const height = canvas.height;
      
      console.log("Canvas dimensions:", width, height);
      
      // Get data to draw - guaranteed to be an array of 100 elements
      const data = dataPointsRef.current;
      if (!data || data.length === 0) {
        console.error("No data to draw");
        return;
      }
      
      // This is the absolute simplest approach - minimal styling, just make it work
      // Clear entire canvas with black background
      ctx.fillStyle = 'rgb(0, 0, 0)';
      ctx.fillRect(0, 0, width, height);
      
      // Draw a frame so we know the canvas is being rendered
      ctx.strokeStyle = 'rgb(0, 50, 100)';
      ctx.lineWidth = 2;
      ctx.strokeRect(2, 2, width-4, height-4);
      
      // Add text to show the canvas is updating
      ctx.font = '12px monospace';
      ctx.fillStyle = mindMirrorConnected ? 'rgb(168, 85, 247)' : 'rgb(0, 150, 255)';
      ctx.fillText("QUANTUM FLUCTUATOR", 10, 20);
      
      // Use a simple solid color for the line - guaranteed visibility
      ctx.strokeStyle = mindMirrorConnected ? 'rgb(168, 85, 247)' : 'rgb(0, 150, 255)';
      ctx.lineWidth = 3;
      ctx.beginPath();
      
      // Apply cycle speed multiplier for faster appearance - compress X axis sampling
      // Skip points for faster drawing with higher frequency appearance
      const skipFactor = Math.max(1, Math.floor(5 / cycleSpeedMultiplier)); // Adjust point density
      
      for (let i = 0; i < data.length; i += skipFactor) {
        const x = (i / (data.length - 1)) * width;
        // Use a safe value and ensure it's within bounds
        const value = typeof data[i] === 'number' ? data[i] : 0.5;
        const y = (1 - Math.max(0.1, Math.min(0.9, value))) * height;
        
        if (i === 0) {
          ctx.moveTo(x, y);
        } else {
          ctx.lineTo(x, y);
        }
      }
      
      // Stroke without any fancy effects
      ctx.stroke();
      
      // Add some points every few steps for visibility
      // Adjust point spacing based on cycle speed
      const pointSpacing = Math.max(5, Math.floor(10 / cycleSpeedMultiplier));
      
      for (let i = 0; i < data.length; i += pointSpacing) {
        const x = (i / (data.length - 1)) * width;
        const value = typeof data[i] === 'number' ? data[i] : 0.5;
        const y = (1 - Math.max(0.1, Math.min(0.9, value))) * height;
        
        ctx.fillStyle = mindMirrorConnected ? 'rgb(190, 100, 255)' : 'rgb(0, 200, 255)';
        ctx.beginPath();
        ctx.arc(x, y, 4, 0, Math.PI * 2);
        ctx.fill();
      }
      
      console.log("Canvas drawing complete");
    } catch (err) {
      console.error("Canvas drawing error:", err);
    }
  };
  
  // MANUAL CANVAS CREATION APPROACH
  useEffect(() => {
    // Initialize with a simple sine wave with more frequent cycles
    const initialPoints = [];
    for (let i = 0; i < 100; i++) {
      // Increased frequency from 0.05 to 0.15 for more cycles
      initialPoints.push(0.5 + Math.sin(i * 0.15) * 0.3);
    }
    dataPointsRef.current = initialPoints;
    
    // Create a canvas element directly
    try {
      console.log("ATTEMPTING MANUAL CANVAS CREATION");
      
      // Find the container where we want to place the canvas
      const canvasContainer = document.querySelector('.quantum-canvas-container');
      if (!canvasContainer) {
        console.error("Could not find canvas container");
        return;
      }
      
      // Clear any existing canvas
      canvasContainer.innerHTML = '';
      
      // Create a new canvas element
      const canvas = document.createElement('canvas');
      canvas.width = 600;
      canvas.height = 130;
      canvas.style.width = '100%';
      canvas.style.height = '100%';
      canvas.style.display = 'block';
      canvas.style.backgroundColor = 'black';
      
      // Add it to the container
      canvasContainer.appendChild(canvas);
      
      // Store in ref for later use
      canvasRef.current = canvas;
      
      // Test draw on the canvas
      const ctx = canvas.getContext('2d');
      if (ctx) {
        ctx.fillStyle = 'rgb(0, 0, 0)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        // Draw a sine wave to verify it works
        ctx.strokeStyle = 'rgb(0, 150, 255)';
        ctx.lineWidth = 3;
        ctx.beginPath();
        
        for (let i = 0; i < 100; i++) {
          const x = (i / 99) * canvas.width;
          // Increased frequency from 0.1 to 0.25 for more cycles
          const y = (0.5 - 0.3 * Math.sin(i * 0.25)) * canvas.height;
          
          if (i === 0) {
            ctx.moveTo(x, y);
          } else {
            ctx.lineTo(x, y);
          }
        }
        
        ctx.stroke();
        
        // Text to show it's initialized
        ctx.fillStyle = 'white';
        ctx.font = '16px Arial';
        ctx.fillText('QUANTUM FLUCTUATOR INITIALIZED', 10, 20);
      }
      
      console.log("Manual canvas creation successful");
      
      // Start the animation loop immediately
      let animationFrameId = null;
      
      const animate = () => {
        updateData();
        drawCanvas();
        animationFrameId = requestAnimationFrame(animate);
      };
      
      animate();
      
      // Store the animation frame ID
      animationRef.current = animationFrameId;
      
    } catch (err) {
      console.error("Manual canvas creation failed:", err);
    }
    
    // Cleanup function
    return () => {
      if (animationRef.current) {
        console.log("Cleaning up animation");
        cancelAnimationFrame(animationRef.current);
      }
    };
  }, []);
  
  // Function to generate a random anomaly based on active glitches
  const generateAnomaly = (activeGlitches) => {
    if (activeGlitches.length === 0) return null;
    
    // Select a random glitch as the source
    const sourceGlitch = activeGlitches[Math.floor(Math.random() * activeGlitches.length)];
    
    // Current time for timestamp
    const now = new Date();
    const timestamp = now.toTimeString().split(' ')[0];
    
    // Generate anomaly description based on glitch type
    let description = '';
    
    if (sourceGlitch.source === 'Mind Mirror') {
      // Mind Mirror anomalies
      const mindMirrorAnomalies = [
        `Neural synchronization pattern detected at ${Math.floor(Math.random() * 40 + 10)}Hz`,
        `Consciousness harmonic resonating with quantum field - amplitude ${Math.floor(Math.random() * 90 + 10)}%`,
        `Interhemispheric coherence matched with reality substrate`,
        `Brainwave entrainment facilitating cross-dimensional perception`,
        `Mind-matter interface detected in ${Math.random() > 0.5 ? 'alpha' : 'theta'} band`
      ];
      description = mindMirrorAnomalies[Math.floor(Math.random() * mindMirrorAnomalies.length)];
    } else {
      // Regular glitch anomalies
      switch(sourceGlitch.type) {
        case 'VISUAL':
          const visualAnomalies = [
            `Visual processing artifact: ${Math.random() > 0.5 ? 'chromatic aberration' : 'geometric distortion'}`,
            `Reality overlay detected with ${Math.floor(Math.random() * 40 + 60)}% pattern match`,
            `Color spectrum shift beyond normal perceptual range`
          ];
          description = visualAnomalies[Math.floor(Math.random() * visualAnomalies.length)];
          break;
        case 'AUDITORY':
          const auditoryAnomalies = [
            `Acoustic anomaly detected at ${Math.floor(Math.random() * 15 + 1)}kHz`,
            `Temporal echo effect detected with ${Math.floor(Math.random() * 200 + 50)}ms delay`,
            `Harmonic resonance outside normal auditory range`
          ];
          description = auditoryAnomalies[Math.floor(Math.random() * auditoryAnomalies.length)];
          break;
        case 'TEMPORAL':
          const temporalAnomalies = [
            `Temporal slip detected - ${Math.random() > 0.5 ? 'desynchronization' : 'recursion'} pattern`,
            `Subjective time dilation factor: ${(Math.random() * 2 + 0.5).toFixed(2)}x`,
            `Causality violation potential: ${Math.floor(Math.random() * 30 + 5)}%`
          ];
          description = temporalAnomalies[Math.floor(Math.random() * temporalAnomalies.length)];
          break;
        case 'SPATIAL':
          const spatialAnomalies = [
            `Non-Euclidean geometry detected in local space`,
            `Spatial fold with ${Math.floor(Math.random() * 20 + 5)}% compression ratio`,
            `Dimensional boundary thinning in proximity to glitch source`
          ];
          description = spatialAnomalies[Math.floor(Math.random() * spatialAnomalies.length)];
          break;
        case 'COGNITIVE':
          const cognitiveAnomalies = [
            `Cognitive dissonance spike of ${Math.floor(Math.random() * 40 + 20)} units`,
            `Reality acceptance threshold compromised by ${Math.floor(Math.random() * 30 + 10)}%`,
            `Memory integration anomaly in hippocampal region`
          ];
          description = cognitiveAnomalies[Math.floor(Math.random() * cognitiveAnomalies.length)];
          break;
        case 'SYNCHRONISTIC':
          const synchronisticAnomalies = [
            `Acausal connection pattern with ${Math.floor(Math.random() * 50 + 50)}% certainty`,
            `Jung-Pauli synchronicity factor: ${(Math.random() * 7 + 3).toFixed(1)}`,
            `Reality consensus breakdown in local information field`
          ];
          description = synchronisticAnomalies[Math.floor(Math.random() * synchronisticAnomalies.length)];
          break;
        default:
          description = `Unknown anomaly type detected: code ${Math.floor(Math.random() * 1000)}`;
      }
    }
    
    // Add modifiers for advanced or cross-modal glitches
    if (sourceGlitch.isAdvanced) {
      const advancedModifiers = [
        "with quantum signature",
        "at critical threshold",
        "exhibiting novel pattern formation"
      ];
      description += " " + advancedModifiers[Math.floor(Math.random() * advancedModifiers.length)];
    }
    
    if (sourceGlitch.crossModal) {
      const crossModalSuffixes = [
        "causing cross-sensory integration",
        "with synaesthetic properties",
        "affecting multiple perception channels"
      ];
      description += " " + crossModalSuffixes[Math.floor(Math.random() * crossModalSuffixes.length)];
    }
    
    return {
      id: Date.now() + Math.random(),
      timestamp,
      description,
      text: description // for backward compatibility
    };
  };
  
  // Helper functions for styling
  const getValueClass = (value, isHighGood = true) => {
    if (value > 80) {
      return isHighGood ? 'text-green-400' : 'text-red-400';
    } else if (value > 50) {
      return isHighGood ? 'text-blue-400' : 'text-yellow-400';
    } else if (value > 20) {
      return isHighGood ? 'text-yellow-400' : 'text-blue-400';
    } else {
      return isHighGood ? 'text-red-400' : 'text-green-400';
    }
  };
  
  const getBarClass = (value, isHighGood = true) => {
    if (value > 80) {
      return isHighGood ? 'bg-green-800' : 'bg-red-800';
    } else if (value > 50) {
      return isHighGood ? 'bg-blue-800' : 'bg-yellow-800';
    } else if (value > 20) {
      return isHighGood ? 'bg-yellow-800' : 'bg-blue-800';
    } else {
      return isHighGood ? 'bg-red-800' : 'bg-green-800';
    }
  };
  
  return (
    <div className="p-4 border border-blue-800 rounded-lg bg-gradient-to-b from-blue-900/30 to-purple-900/30 cyber-border">
      <h2 className="text-xl mb-3 border-b border-blue-700 pb-1">Reality Distortion Output</h2>
      
      {/* Waveform display - with ultra-reliable styling */}
      <div className="mb-4">
        <div className="flex justify-between items-center mb-1">
          <div className="text-sm text-blue-400">Quantum Field Fluctuations:</div>
          {mindMirrorConnected && (
            <div className="bg-purple-900/50 px-2 py-0.5 rounded text-xs text-purple-300 border border-purple-700">
              MIND MIRROR PATTERN DETECTED
            </div>
          )}
        </div>
        
        {/* Canvas will be inserted here */}
        <div 
          className="quantum-canvas-container"
          style={{
            width: "100%",
            height: "140px",
            minHeight: "140px",
            border: "1px solid #1e40af",
            borderRadius: "4px",
            backgroundColor: "black",
            padding: "4px",
            position: "relative",
            display: "block",
            overflow: "hidden"
          }}
        ></div>
      </div>
      
      {/* Sensor data */}
      <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
        {/* Neural Activity */}
        <div>
          <div className="text-sm text-blue-400 mb-1">Neural Activity:</div>
          <div className="text-xl mb-1">{sensorData.neuralActivity.toFixed(1)}%</div>
          <div className={`h-2 w-full rounded ${getBarClass(sensorData.neuralActivity, false)}`}>
            <div 
              className={`h-full rounded ${getValueClass(sensorData.neuralActivity, false)}`} 
              style={{width: `${sensorData.neuralActivity}%`}}
            ></div>
          </div>
        </div>
        
        {/* Perception Shift */}
        <div>
          <div className="text-sm text-blue-400 mb-1">Perception Shift:</div>
          <div className="text-xl mb-1">{sensorData.perceptionShift.toFixed(1)}%</div>
          <div className={`h-2 w-full rounded ${getBarClass(sensorData.perceptionShift, false)}`}>
            <div 
              className={`h-full rounded ${getValueClass(sensorData.perceptionShift, false)}`} 
              style={{width: `${sensorData.perceptionShift}%`}}
            ></div>
          </div>
        </div>
        
        {/* Reality Coherence */}
        <div>
          <div className="text-sm text-blue-400 mb-1">Reality Coherence:</div>
          <div className="text-xl mb-1">{sensorData.realityCoherence.toFixed(1)}%</div>
          <div className={`h-2 w-full rounded ${getBarClass(sensorData.realityCoherence)}`}>
            <div 
              className={`h-full rounded ${getValueClass(sensorData.realityCoherence)}`} 
              style={{width: `${sensorData.realityCoherence}%`}}
            ></div>
          </div>
        </div>
        
        {/* Temporal Sync */}
        <div>
          <div className="text-sm text-blue-400 mb-1">Temporal Sync:</div>
          <div className="text-xl mb-1">{sensorData.temporalSync.toFixed(1)}%</div>
          <div className={`h-2 w-full rounded ${getBarClass(sensorData.temporalSync)}`}>
            <div 
              className={`h-full rounded ${getValueClass(sensorData.temporalSync)}`} 
              style={{width: `${sensorData.temporalSync}%`}}
            ></div>
          </div>
        </div>
        
        {/* Cognitive Dissonance */}
        <div>
          <div className="text-sm text-blue-400 mb-1">Cognitive Dissonance:</div>
          <div className="text-xl mb-1">{sensorData.cognitiveDissonance.toFixed(1)}%</div>
          <div className={`h-2 w-full rounded ${getBarClass(sensorData.cognitiveDissonance, false)}`}>
            <div 
              className={`h-full rounded ${getValueClass(sensorData.cognitiveDissonance, false)}`} 
              style={{width: `${sensorData.cognitiveDissonance}%`}}
            ></div>
          </div>
        </div>
        
        {/* Quantum Entanglement */}
        <div>
          <div className="text-sm text-blue-400 mb-1">Quantum Entanglement:</div>
          <div className="text-xl mb-1">{sensorData.quantumEntanglement.toFixed(1)}%</div>
          <div className={`h-2 w-full rounded ${getBarClass(sensorData.quantumEntanglement, mindMirrorConnected)}`}>
            <div 
              className={`h-full rounded ${getValueClass(sensorData.quantumEntanglement, mindMirrorConnected)}`} 
              style={{width: `${sensorData.quantumEntanglement}%`}}
            ></div>
          </div>
        </div>
      </div>
      
      {/* Anomaly Detection */}
      <div className="mt-4">
        <div className="text-sm text-blue-400 mb-2">Detected Anomalies:</div>
        <div className="min-h-[100px] max-h-[120px] overflow-y-auto scrollbar p-2 border border-blue-800 rounded bg-black/30">
          {anomalies.length > 0 ? (
            anomalies.map((anomaly, index) => (
              <div key={index} className="py-1 text-sm border-b border-blue-900/50 last:border-0">
                <span className="text-yellow-400">[{anomaly.timestamp}]</span> {anomaly.description}
              </div>
            ))
          ) : (
            <div className="opacity-70 py-1">No anomalies detected in current reality matrix</div>
          )}
        </div>
      </div>
    </div>
  );
};

export default RealTimeData; 