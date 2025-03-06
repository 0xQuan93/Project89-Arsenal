import React, { useState, useEffect, useRef } from 'react';

const RealTimeData = ({ glitches, realityStatus, mindMirrorConnected }) => {
  const [dataPoints, setDataPoints] = useState([]);
  const [sensorData, setSensorData] = useState({
    neuralActivity: 78.4,
    perceptionShift: 12.3,
    realityCoherence: 89.7,
    temporalSync: 99.2,
    cognitiveDissonance: 15.0,
    quantumEntanglement: 45.2
  });
  const [anomalies, setAnomalies] = useState([]);
  const canvasRef = useRef(null);
  const activeGlitches = glitches.filter(g => g.active);
  
  // Generate realistic sensor data based on active glitches
  useEffect(() => {
    const interval = setInterval(() => {
      // Base fluctuation (small random changes)
      const fluctuation = () => (Math.random() * 2) - 1;
      
      // Calculate glitch effects on each sensor
      let neuralEffect = 0;
      let perceptionEffect = 0;
      let coherenceEffect = 0;
      let temporalEffect = 0;
      let cognitiveEffect = 0;
      let entanglementEffect = 0;
      
      activeGlitches.forEach(glitch => {
        const impact = glitch.intensity * 5; // Scale factor
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
          default:
            break;
        }
      });
      
      // Mind Mirror global effect on quantum entanglement
      const mindMirrorEntanglementBoost = mindMirrorConnected ? 10 + (Math.random() * 15) : 0;
      
      // Apply effects and fluctuations to sensor data with constraints
      setSensorData(prev => ({
        neuralActivity: Math.max(0, Math.min(100, prev.neuralActivity + neuralEffect * 0.1 + fluctuation())),
        perceptionShift: Math.max(0, Math.min(100, prev.perceptionShift + perceptionEffect * 0.1 + fluctuation())),
        realityCoherence: Math.max(0, Math.min(100, 
          // Reality coherence is inversely affected by glitches
          prev.realityCoherence - coherenceEffect * 0.1 + (realityStatus.safetyProtocols ? 0.2 : -0.1) + fluctuation()
        )),
        temporalSync: Math.max(0, Math.min(100, prev.temporalSync - temporalEffect * 0.1 + fluctuation())),
        cognitiveDissonance: Math.max(0, Math.min(100, prev.cognitiveDissonance + cognitiveEffect * 0.1 + fluctuation())),
        quantumEntanglement: Math.max(0, Math.min(100, 
          // Quantum entanglement is boosted by Mind Mirror integration
          prev.quantumEntanglement + entanglementEffect * 0.1 + (mindMirrorEntanglementBoost * 0.01) + fluctuation()
        ))
      }));
      
      // Add data point for waveform
      setDataPoints(prev => {
        // Create more complex waveform patterns with Mind Mirror
        const baseWave = Math.sin(Date.now() / 500) * 0.3;
        const noiseComponent = activeGlitches.length ? (Math.random() * activeGlitches.length / 10) : 0;
        const mindMirrorComponent = mindMirrorConnected ? 
          Math.sin(Date.now() / 300) * Math.cos(Date.now() / 700) * 0.15 : 0;
        
        const newPoint = baseWave + noiseComponent + mindMirrorComponent + 0.5;
        const newPoints = [...prev, newPoint];
        return newPoints.slice(-100); // Keep only the last 100 points
      });
      
      // Update anomalies
      if (activeGlitches.length > 0 && Math.random() < 0.1) {
        generateRandomAnomaly(activeGlitches);
      } else if (anomalies.length > 0 && Math.random() < 0.05) {
        // Occasionally remove an anomaly
        setAnomalies(prev => prev.slice(0, prev.length - 1));
      }
      
    }, 100); // Increased frequency for smoother animation
    
    return () => clearInterval(interval);
  }, [activeGlitches, realityStatus.safetyProtocols, mindMirrorConnected, anomalies]);
  
  // Function to generate a random anomaly based on active glitches
  const generateRandomAnomaly = (activeGlitches) => {
    if (activeGlitches.length === 0) return;
    
    const glitch = activeGlitches[Math.floor(Math.random() * activeGlitches.length)];
    const sectorNum = Math.floor(Math.random() * 1000);
    const intensity = Math.floor(glitch.intensity * 100);
    
    let anomalyType = '';
    switch(glitch.type) {
      case 'VISUAL':
        anomalyType = 'visual pattern mismatch';
        break;
      case 'AUDITORY':
        anomalyType = 'frequency resonance';
        break;
      case 'TEMPORAL':
        anomalyType = 'temporal dilation';
        break;
      case 'SPATIAL':
        anomalyType = 'spatial distortion';
        break;
      case 'COGNITIVE':
        anomalyType = 'cognitive dissonance spike';
        break;
      default:
        anomalyType = 'reality fluctuation';
    }
    
    const newAnomaly = {
      id: Date.now(),
      text: `» Sector ${sectorNum}: ${anomalyType} detected (${intensity}% intensity)`,
      timestamp: Date.now()
    };
    
    setAnomalies(prev => {
      // Keep only last 5 anomalies for display
      const updated = [...prev, newAnomaly].slice(-5);
      return updated;
    });
  };
  
  // Draw waveform on canvas
  useEffect(() => {
    if (!canvasRef.current || dataPoints.length < 2) return;
    
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    
    // Clear canvas
    ctx.clearRect(0, 0, width, height);
    
    // Draw grid
    ctx.strokeStyle = 'rgba(0, 40, 100, 0.2)';
    ctx.lineWidth = 0.5;
    
    // Vertical grid lines
    for (let x = 0; x < width; x += 20) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, height);
      ctx.stroke();
    }
    
    // Horizontal grid lines
    for (let y = 0; y < height; y += 20) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(width, y);
      ctx.stroke();
    }
    
    // Draw baseline
    ctx.strokeStyle = 'rgba(0, 60, 150, 0.3)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(0, height / 2);
    ctx.lineTo(width, height / 2);
    ctx.stroke();
    
    // Calculate average glitch intensity
    const avgIntensity = activeGlitches.length 
      ? activeGlitches.reduce((sum, g) => sum + g.intensity, 0) / activeGlitches.length
      : 0;
    
    // Count Mind Mirror glitches
    const mindMirrorGlitches = activeGlitches.filter(g => g.source === 'Mind Mirror');
    
    // Draw waveform with glitch effects
    ctx.lineWidth = 2;
    
    // Color depends on Mind Mirror connection
    const waveColor = mindMirrorGlitches.length > 0 
      ? `rgba(170, 50, 220, ${0.7 + avgIntensity * 0.3})` // Purple for Mind Mirror
      : `rgba(57, 255, 20, ${0.6 + avgIntensity * 0.4})`; // Green for normal
      
    ctx.strokeStyle = waveColor;
    ctx.beginPath();
    
    const drawGlitchy = activeGlitches.length > 0 && Math.random() < avgIntensity * 0.3;
    
    dataPoints.forEach((point, i) => {
      const x = (i / (dataPoints.length - 1)) * width;
      // Add a glitch effect to the wave depending on active glitches
      let y = point * height;
      
      if (drawGlitchy && i > 0 && i < dataPoints.length - 1 && Math.random() < 0.1) {
        // Add random vertical glitch
        y += (Math.random() * 20) - 10;
      }
      
      if (i === 0) {
        ctx.moveTo(x, y);
      } else {
        ctx.lineTo(x, y);
      }
    });
    ctx.stroke();
    
    // Add an extra echo/ghost line for Mind Mirror glitches
    if (mindMirrorGlitches.length > 0) {
      ctx.strokeStyle = 'rgba(170, 50, 220, 0.3)';
      ctx.lineWidth = 1;
      ctx.beginPath();
      
      dataPoints.forEach((point, i) => {
        const x = (i / (dataPoints.length - 1)) * width;
        // Offset the duplicate line slightly to create an echo effect
        const y = point * height - 5;
        
        if (i === 0) {
          ctx.moveTo(x, y);
        } else {
          ctx.lineTo(x, y);
        }
      });
      ctx.stroke();
    }
    
    // Add some digital noise based on active glitches
    if (activeGlitches.length > 0) {
      const noiseAmount = Math.min(300, activeGlitches.length * 40);
      
      // Different noise color for Mind Mirror glitches
      const noiseColor = mindMirrorGlitches.length > 0 
        ? 'rgba(170, 50, 220, 0.1)' 
        : 'rgba(57, 255, 20, 0.1)';
        
      ctx.fillStyle = noiseColor;
      
      for (let i = 0; i < noiseAmount; i++) {
        const x = Math.random() * width;
        const y = Math.random() * height;
        const size = Math.random() * 2 + 1;
        ctx.fillRect(x, y, size, size);
      }
    }
    
    // Add Mind Mirror specific interference patterns
    if (mindMirrorConnected) {
      ctx.strokeStyle = 'rgba(170, 50, 220, 0.2)';
      ctx.lineWidth = 0.5;
      
      // Add a sinusoidal interference pattern
      ctx.beginPath();
      for (let x = 0; x < width; x += 2) {
        const y = height / 2 + Math.sin(x / 10 + Date.now() / 1000) * 20;
        if (x === 0) {
          ctx.moveTo(x, y);
        } else {
          ctx.lineTo(x, y);
        }
      }
      ctx.stroke();
    }
    
  }, [dataPoints, activeGlitches, mindMirrorConnected]);
  
  // Get status class for display value based on whether high or low is good
  const getValueClass = (value, isHighGood = true) => {
    if (isHighGood) {
      if (value > 80) return 'data-value-good';
      if (value > 50) return 'data-value-caution';
      return 'data-value-danger';
    } else {
      if (value < 20) return 'data-value-good';
      if (value < 50) return 'data-value-caution';
      return 'data-value-danger';
    }
  };
  
  // Get bar class based on value
  const getBarClass = (value, isHighGood = true) => {
    if (isHighGood) {
      if (value > 80) return 'progress-bar-green';
      if (value > 50) return 'progress-bar-yellow';
      return 'progress-bar-red';
    } else {
      if (value < 20) return 'progress-bar-green';
      if (value < 50) return 'progress-bar-yellow';
      return 'progress-bar-red';
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
          <canvas ref={canvasRef} width={600} height={140} className="w-full h-full" />
        </div>
      </div>
      
      {/* Sensor data */}
      <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
        <div>
          <div className="text-sm text-blue-400 mb-1">Neural Activity:</div>
          <div className={getValueClass(sensorData.neuralActivity, true)}>
            {sensorData.neuralActivity.toFixed(1)}Hz
          </div>
          <div className="h-1.5 w-full bg-gray-800 rounded overflow-hidden mt-1">
            <div 
              className={getBarClass(sensorData.neuralActivity, true)}
              style={{width: `${sensorData.neuralActivity}%`}}
            />
          </div>
        </div>
        
        <div>
          <div className="text-sm text-blue-400 mb-1">Perception Shift:</div>
          <div className={getValueClass(sensorData.perceptionShift, false)}>
            {sensorData.perceptionShift.toFixed(1)}%
          </div>
          <div className="h-1.5 w-full bg-gray-800 rounded overflow-hidden mt-1">
            <div 
              className={getBarClass(sensorData.perceptionShift, false)}
              style={{width: `${sensorData.perceptionShift}%`}}
            />
          </div>
        </div>
        
        <div>
          <div className="text-sm text-blue-400 mb-1">Reality Coherence:</div>
          <div className={getValueClass(sensorData.realityCoherence, true)}>
            {sensorData.realityCoherence.toFixed(1)}%
          </div>
          <div className="h-1.5 w-full bg-gray-800 rounded overflow-hidden mt-1">
            <div 
              className={getBarClass(sensorData.realityCoherence, true)}
              style={{width: `${sensorData.realityCoherence}%`}}
            />
          </div>
        </div>
        
        <div>
          <div className="text-sm text-blue-400 mb-1">Temporal Sync:</div>
          <div className={getValueClass(sensorData.temporalSync, true)}>
            {sensorData.temporalSync.toFixed(1)}%
          </div>
          <div className="h-1.5 w-full bg-gray-800 rounded overflow-hidden mt-1">
            <div 
              className={getBarClass(sensorData.temporalSync, true)}
              style={{width: `${sensorData.temporalSync}%`}}
            />
          </div>
        </div>
        
        <div>
          <div className="text-sm text-blue-400 mb-1">Cognitive Dissonance:</div>
          <div className={getValueClass(sensorData.cognitiveDissonance, false)}>
            {sensorData.cognitiveDissonance.toFixed(1)}%
          </div>
          <div className="h-1.5 w-full bg-gray-800 rounded overflow-hidden mt-1">
            <div 
              className={getBarClass(sensorData.cognitiveDissonance, false)}
              style={{width: `${sensorData.cognitiveDissonance}%`}}
            />
          </div>
        </div>
        
        <div>
          <div className="flex items-center">
            <div className="text-sm text-blue-400 mb-1">Quantum Entanglement:</div>
            {mindMirrorConnected && (
              <div className="mind-mirror-badge ml-2 mb-1">MM</div>
            )}
          </div>
          <div className={mindMirrorConnected ? 'data-value-special' : getValueClass(sensorData.quantumEntanglement, true)}>
            {sensorData.quantumEntanglement.toFixed(1)}%
          </div>
          <div className="h-1.5 w-full bg-gray-800 rounded overflow-hidden mt-1">
            <div 
              className={mindMirrorConnected ? 'progress-bar-purple' : getBarClass(sensorData.quantumEntanglement, true)}
              style={{width: `${sensorData.quantumEntanglement}%`}}
            />
          </div>
        </div>
      </div>
      
      {/* Anomaly Detection */}
      <div className="anomaly-section">
        <div className="text-sm text-blue-400 mb-2">Detected Anomalies:</div>
        <div className="anomaly-text">
          {anomalies.length > 0 ? (
            anomalies.map((anomaly, index) => (
              <div key={anomaly.id}>
                {anomaly.text}
              </div>
            ))
          ) : (
            <div className="opacity-70">No anomalies detected in current reality matrix</div>
          )}
        </div>
      </div>
    </div>
  );
};

export default RealTimeData; 