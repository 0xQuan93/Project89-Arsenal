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
  const [lastAnomalyTime, setLastAnomalyTime] = useState(0);
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
      
      // Apply safety protocols (reduced effect if enabled)
      const safetyFactor = realityStatus.safetyProtocols ? 0.6 : 1.0;
      
      // Update sensor data
      setSensorData(prev => ({
        neuralActivity: Math.max(0, Math.min(100, prev.neuralActivity + (neuralEffect * safetyFactor) + fluctuation())),
        perceptionShift: Math.max(0, Math.min(100, prev.perceptionShift + (perceptionEffect * safetyFactor) + fluctuation())),
        realityCoherence: Math.max(0, Math.min(100, prev.realityCoherence - (coherenceEffect * safetyFactor) + fluctuation())),
        temporalSync: Math.max(0, Math.min(100, prev.temporalSync - (temporalEffect * safetyFactor) + fluctuation())),
        cognitiveDissonance: Math.max(0, Math.min(100, prev.cognitiveDissonance + (cognitiveEffect * safetyFactor) + fluctuation())),
        quantumEntanglement: Math.max(0, Math.min(100, prev.quantumEntanglement + (entanglementEffect * safetyFactor) + (mindMirrorConnected ? 1.5 : fluctuation())))
      }));
      
      // Add new data point for waveform
      setDataPoints(prev => {
        // Create more complex waveform patterns with Mind Mirror and active glitches
        const baseWave = Math.sin(Date.now() / 500) * 0.3;
        const noiseComponent = activeGlitches.length ? (Math.random() * activeGlitches.length / 10) : 0;
        const mindMirrorComponent = mindMirrorConnected ? 
          Math.sin(Date.now() / 300) * Math.cos(Date.now() / 700) * 0.15 : 0;
        
        // Add effects from glitches
        let glitchEffect = 0;
        activeGlitches.forEach(glitch => {
          // Different glitch types create different pattern effects
          switch(glitch.type) {
            case 'VISUAL':
              glitchEffect += Math.sin(Date.now() / 400) * glitch.intensity * 0.05;
              break;
            case 'TEMPORAL':
              glitchEffect += Math.sin(Date.now() / (300 - glitch.intensity * 200)) * glitch.intensity * 0.07;
              break;
            case 'SPATIAL':
              glitchEffect += Math.random() * glitch.intensity * 0.1;
              break;
            case 'COGNITIVE':
              // Cognitive glitches create more structured patterns
              glitchEffect += Math.sin(Date.now() / 600 + Math.cos(Date.now() / 400)) * glitch.intensity * 0.08;
              break;
            case 'SYNCHRONISTIC':
              // Synchronistic glitches create harmonic patterns
              glitchEffect += (Math.sin(Date.now() / 200) * Math.sin(Date.now() / 500)) * glitch.intensity * 0.1;
              break;
            default:
              glitchEffect += Math.random() * glitch.intensity * 0.03;
          }
          
          // Advanced glitches have stronger effects
          if (glitch.isAdvanced) {
            glitchEffect *= 1.5;
          }
          
          // Cross-modal glitches create interference patterns
          if (glitch.crossModal) {
            glitchEffect += Math.sin(Date.now() / 250) * Math.cos(Date.now() / 350) * glitch.intensity * 0.12;
          }
        });
        
        // Normalize value between 0 and 1 for consistent display
        const newPoint = 0.5 + baseWave + noiseComponent + mindMirrorComponent + glitchEffect;
        const clampedPoint = Math.max(0, Math.min(1, newPoint)); // Ensure value stays between 0 and 1
        
        const newPoints = [...prev, clampedPoint];
        return newPoints.slice(-100); // Keep last 100 points for smoother graph
      });
      
      // Update anomalies - with reduced frequency and limits
      const now = Date.now();
      const timeSinceLastAnomaly = now - lastAnomalyTime;
      const minimumInterval = 3000; // minimum 3 seconds between anomaly updates
      
      if (activeGlitches.length > 0 && timeSinceLastAnomaly > minimumInterval && Math.random() < 0.25) {
        // Limit to generating at most 2 anomalies per cycle
        const anomaliesToGenerate = Math.min(2, Math.ceil(Math.random() * 2));
        
        // Use a batch update approach to reduce UI jumps
        const newAnomalies = [];
        for (let i = 0; i < anomaliesToGenerate; i++) {
          if (Math.random() < 0.7) { // 70% chance for each potential anomaly
            newAnomalies.push(generateAnomaly(activeGlitches));
          }
        }
        
        if (newAnomalies.length > 0) {
          setAnomalies(prev => {
            // Keep only last 5 anomalies for display
            const updated = [...prev, ...newAnomalies].slice(-5);
            return updated;
          });
          setLastAnomalyTime(now);
        }
      } else if (anomalies.length > 0 && Math.random() < 0.05 && timeSinceLastAnomaly > minimumInterval) {
        // Occasionally remove an anomaly
        setAnomalies(prev => prev.slice(0, prev.length - 1));
        setLastAnomalyTime(now);
      }
      
    }, 1000); // Reduced from 100ms to 1000ms for less frequent updates
    
    return () => clearInterval(interval);
  }, [activeGlitches, realityStatus.safetyProtocols, mindMirrorConnected, anomalies, lastAnomalyTime]);
  
  // Function to generate a random anomaly based on active glitches
  const generateAnomaly = (activeGlitches) => {
    if (activeGlitches.length === 0) return null;
    
    const glitch = activeGlitches[Math.floor(Math.random() * activeGlitches.length)];
    const sectorNum = Math.floor(Math.random() * 1000);
    const intensity = Math.floor(glitch.intensity * 100);
    
    let anomalyType = '';
    
    // If it's an advanced glitch, make the anomaly reflect the specific type
    if (glitch.isAdvanced && glitch.type === 'COGNITIVE' && glitch.distortionType) {
      switch(glitch.distortionType) {
        case 'CONFIRMATION_BIAS':
          anomalyType = 'confirmation bias pattern';
          break;
        case 'BLACK_WHITE_THINKING':
          anomalyType = 'binary logic error';
          break;
        case 'CATASTROPHIZING':
          anomalyType = 'catastrophic prediction';
          break;
        case 'EMOTIONAL_REASONING':
          anomalyType = 'emotional reasoning cascade';
          break;
        case 'FILTERING':
          anomalyType = 'selective perception filter';
          break;
        default:
          anomalyType = 'cognitive distortion';
      }
    } else if (glitch.crossModal) {
      anomalyType = 'cross-modal interference';
    } else {
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
        case 'SYNCHRONISTIC':
          anomalyType = 'synchronicity pattern';
          break;
        default:
          anomalyType = 'reality fluctuation';
      }
    }
    
    return {
      id: Date.now() + Math.random(), // Ensure unique IDs even with rapid generation
      text: `» Sector ${sectorNum}: ${anomalyType} detected (${intensity}% intensity)`,
      timestamp: Date.now()
    };
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
    
    // Horizontal grid lines
    for (let y = 0; y < height; y += 20) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(width, y);
      ctx.stroke();
    }
    
    // Vertical grid lines
    for (let x = 0; x < width; x += 40) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, height);
      ctx.stroke();
    }
    
    // Create gradient for the line
    const gradient = ctx.createLinearGradient(0, height/2 - 50, 0, height/2 + 50);
    gradient.addColorStop(0, 'rgba(0, 200, 255, 0.7)');
    gradient.addColorStop(0.5, 'rgba(0, 150, 255, 1)');
    gradient.addColorStop(1, 'rgba(0, 100, 255, 0.7)');
    
    // Draw the waveform with smoother transitions
    ctx.strokeStyle = gradient;
    ctx.lineWidth = 2;
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
    
    // Apply a quantum effect based on active glitches
    const quantumEffect = activeGlitches.length * 0.03;
    
    ctx.beginPath();
    
    for (let i = 0; i < dataPoints.length; i++) {
      const x = (i / (dataPoints.length - 1)) * width;
      
      // Calculate y position - normalize to the canvas height
      // The dataPoints are normalized between 0 and 1
      const y = (1 - dataPoints[i]) * height;
      
      // Apply quantum distortion effects
      let distortedY = y;
      if (activeGlitches.length > 0) {
        // Add slight distortion based on active glitches
        const distortionAmount = Math.sin(i * 0.1 + Date.now() * 0.001) * quantumEffect * 20;
        distortedY += distortionAmount;
      }
      
      if (i === 0) {
        ctx.moveTo(x, distortedY);
      } else {
        ctx.lineTo(x, distortedY);
      }
    }
    
    ctx.stroke();
    
    // Add glow effect for the waveform
    ctx.shadowBlur = 10;
    ctx.shadowColor = "rgba(0, 150, 255, 0.5)";
    ctx.stroke();
    
    // Add points at data locations for quantum fluctuation visualization
    if (activeGlitches.length > 0 || mindMirrorConnected) {
      for (let i = 0; i < dataPoints.length; i += 5) { // Draw every 5th point for performance
        const x = (i / (dataPoints.length - 1)) * width;
        const y = (1 - dataPoints[i]) * height;
        
        // Determine point color based on Mind Mirror connection
        ctx.fillStyle = mindMirrorConnected ? 
          'rgba(168, 85, 247, 0.8)' : 
          'rgba(0, 150, 255, 0.8)';
        
        // Draw quantum particle
        ctx.beginPath();
        ctx.arc(x, y, 2 + (Math.random() * 2), 0, Math.PI * 2);
        ctx.fill();
      }
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
      <div className="anomaly-section mt-4">
        <div className="text-sm text-blue-400 mb-2">Detected Anomalies:</div>
        <div className="anomaly-text min-h-[100px] max-h-[120px] overflow-y-auto scrollbar">
          {anomalies.length > 0 ? (
            anomalies.map((anomaly, index) => (
              <div key={anomaly.id} className="py-1 opacity-0 animate-fade-in">
                {anomaly.text}
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