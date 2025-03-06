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
  
  // Use callback to prevent recreation of the function on each render
  const startAnimation = useCallback(() => {
    const animate = () => {
      updateData();
      drawCanvas();
      animationRef.current = requestAnimationFrame(animate);
    };
    animate();
  }, []);
  
  // Dynamic data generation responsive to glitches
  const updateData = () => {
    const currentTime = Date.now();
    const deltaTime = Math.min(0.1, (currentTime - lastUpdateTimeRef.current) / 1000);
    lastUpdateTimeRef.current = currentTime;
    
    // Time value for wave calculations
    const time = currentTime * 0.001;
    
    // Get active glitches
    const activeGlitches = glitches.filter(g => g.active);
    
    // Base wave that's always visible
    let newValue = 0.5 + Math.sin(time * 1.5) * 0.2;
    
    // Process each active glitch
    activeGlitches.forEach(glitch => {
      const intensity = glitch.intensity * 0.01;
      const glitchId = glitch.id || 1;
      const frequencyOffset = (glitchId % 10) * 0.1;
      
      // Different wave patterns for each glitch type
      switch(glitch.type) {
        case 'VISUAL':
          newValue += Math.sin(time * (1.7 + frequencyOffset)) * intensity * 0.15;
          break;
        case 'AUDITORY':
          newValue += Math.cos(time * (2.1 + frequencyOffset)) * intensity * 0.12;
          break;
        case 'TEMPORAL':
          newValue += Math.sin(time * (0.9 + frequencyOffset)) * intensity * 0.18;
          break;
        case 'SPATIAL':
          newValue += Math.sin(time * (1.5 + frequencyOffset) + Math.cos(time)) * intensity * 0.14;
          break;
        case 'COGNITIVE':
          newValue += Math.sin(time * (1.8 + frequencyOffset) + Math.sin(time * 0.7)) * intensity * 0.16;
          break;
        case 'SYNCHRONISTIC':
          newValue += Math.sin(time * (1.2 + frequencyOffset)) * Math.cos(time * 0.8) * intensity * 0.17;
          break;
        default:
          newValue += Math.sin(time * (1.4 + frequencyOffset)) * intensity * 0.1;
      }
      
      // Advanced glitches create more complex patterns
      if (glitch.isAdvanced) {
        newValue += Math.sin(time * 2.5) * Math.cos(time * 1.3) * intensity * 0.2;
      }
      
      // Cross-modal glitches affect the waveform differently
      if (glitch.crossModal) {
        newValue += Math.sin(time * 1.9 + Math.cos(time * 0.7)) * intensity * 0.15;
      }
    });
    
    // Mind Mirror creates distinctive pattern
    if (mindMirrorConnected) {
      newValue += Math.sin(time * 2.2) * 0.12;
      newValue += Math.sin(time * 3.7) * Math.cos(time * 0.9) * 0.08;
    }
    
    // Add subtle quantum randomness
    newValue += (Math.random() * 0.04 - 0.02);
    
    // Safety bounds to keep waveform visible
    newValue = Math.max(0.2, Math.min(0.8, newValue));
    
    // Update data points
    const points = [...dataPointsRef.current];
    points.push(newValue);
    points.shift();
    dataPointsRef.current = points;
    
    // Update state occasionally for components that need it
    if (currentTime % 100 < 20) {
      setDataPointsState([...points]);
    }
    
    // Continue with sensor updates
    updateSensorData(deltaTime, activeGlitches);
    updateAnomalies(activeGlitches);
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
  
  // Enhanced canvas drawing with reliable visibility
  const drawCanvas = () => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    if (!ctx) return;
    
    const width = canvas.width;
    const height = canvas.height;
    
    // Get data to draw - guaranteed to be an array of 100 elements
    const data = dataPointsRef.current;
    
    // Clear canvas
    ctx.clearRect(0, 0, width, height);
    
    // Fill background
    ctx.fillStyle = 'rgba(1, 10, 30, 0.7)';
    ctx.fillRect(0, 0, width, height);
    
    // Draw grid
    ctx.strokeStyle = 'rgba(0, 40, 100, 0.25)';
    ctx.lineWidth = 0.5;
    
    for (let y = 0; y < height; y += 30) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(width, y);
      ctx.stroke();
    }
    
    for (let x = 0; x < width; x += 60) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, height);
      ctx.stroke();
    }
    
    // Create gradient for waveform
    const gradient = ctx.createLinearGradient(0, 0, 0, height);
    if (mindMirrorConnected) {
      gradient.addColorStop(0, 'rgba(190, 120, 255, 0.9)');
      gradient.addColorStop(0.5, 'rgba(168, 85, 247, 1)');
      gradient.addColorStop(1, 'rgba(130, 60, 200, 0.9)');
    } else {
      gradient.addColorStop(0, 'rgba(0, 220, 255, 0.9)');
      gradient.addColorStop(0.5, 'rgba(0, 180, 255, 1)');
      gradient.addColorStop(1, 'rgba(0, 140, 255, 0.9)');
    }
    
    // Draw line with attractive styling
    ctx.strokeStyle = gradient;
    ctx.lineWidth = 3;
    ctx.beginPath();
    
    // Draw the main waveform
    for (let i = 0; i < data.length; i++) {
      const x = (i / (data.length - 1)) * width;
      const y = height - (data[i] * height);
      
      if (i === 0) {
        ctx.moveTo(x, y);
      } else {
        ctx.lineTo(x, y);
      }
    }
    
    ctx.stroke();
    
    // Add glow effect
    ctx.shadowBlur = 10;
    ctx.shadowColor = mindMirrorConnected ? 
      'rgba(168, 85, 247, 0.7)' : 
      'rgba(0, 180, 255, 0.7)';
    ctx.stroke();
    
    // Draw particles on the line
    for (let i = 0; i < data.length; i += 8) {
      const x = (i / (data.length - 1)) * width;
      const y = height - (data[i] * height);
      
      const particleColor = mindMirrorConnected ? 
        'rgba(190, 120, 255, 0.9)' : 
        'rgba(50, 200, 255, 0.9)';
      
      ctx.fillStyle = particleColor;
      ctx.beginPath();
      ctx.arc(x, y, 2, 0, Math.PI * 2);
      ctx.fill();
    }
    
    // Draw Mind Mirror indicator if connected
    if (mindMirrorConnected) {
      ctx.font = '11px monospace';
      ctx.fillStyle = 'rgba(168, 85, 247, 1)';
      ctx.textAlign = 'right';
      ctx.fillText("MIND MIRROR PATTERN DETECTED", width - 10, 15);
    }
  };
  
  // Initialize and start animation
  useEffect(() => {
    // Initialize with a sine wave
    const initialPoints = [];
    for (let i = 0; i < 100; i++) {
      initialPoints.push(0.5 + Math.sin(i * 0.05) * 0.25);
    }
    dataPointsRef.current = initialPoints;
    setDataPointsState(initialPoints);
    
    // Start animation loop
    startAnimation();
    
    return () => {
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current);
      }
    };
  }, [startAnimation]);
  
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
      
      {/* Waveform display */}
      <div className="mb-4">
        <div className="flex justify-between items-center mb-1">
          <div className="text-sm text-blue-400">Quantum Field Fluctuations:</div>
          {mindMirrorConnected && (
            <div className="bg-purple-900/50 px-2 py-0.5 rounded text-xs text-purple-300 border border-purple-700">
              MIND MIRROR PATTERN DETECTED
            </div>
          )}
        </div>
        <div className="border border-blue-800 bg-black/50 rounded p-1 h-36">
          <canvas ref={canvasRef} width={600} height={130} className="w-full h-full" />
        </div>
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