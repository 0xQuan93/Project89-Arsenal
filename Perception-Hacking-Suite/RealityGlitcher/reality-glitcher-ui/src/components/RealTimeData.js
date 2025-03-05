import React, { useState, useEffect, useRef } from 'react';

const RealTimeData = ({ glitches, realityStatus }) => {
  const [dataPoints, setDataPoints] = useState([]);
  const [sensorData, setSensorData] = useState({
    neuralActivity: 78.4,
    perceptionShift: 12.3,
    realityCoherence: 89.7,
    temporalSync: 99.2,
    cognitiveDissonance: 15.0
  });
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
      
      activeGlitches.forEach(glitch => {
        const impact = glitch.intensity * 5; // Scale factor
        
        switch(glitch.type) {
          case 'VISUAL':
            neuralEffect += impact * 0.8;
            perceptionEffect += impact * 1.2;
            break;
          case 'AUDITORY':
            neuralEffect += impact * 0.6;
            perceptionEffect += impact * 0.9;
            cognitiveEffect += impact * 0.7;
            break;
          case 'TEMPORAL':
            temporalEffect += impact * 1.5;
            coherenceEffect += impact * 0.8;
            break;
          case 'SPATIAL':
            perceptionEffect += impact * 1.1;
            coherenceEffect += impact * 1.0;
            temporalEffect += impact * 0.5;
            break;
          case 'COGNITIVE':
            cognitiveEffect += impact * 1.4;
            neuralEffect += impact * 0.9;
            break;
          default:
            break;
        }
      });
      
      // Apply effects and fluctuations to sensor data with constraints
      setSensorData(prev => ({
        neuralActivity: Math.max(0, Math.min(100, prev.neuralActivity + neuralEffect * 0.1 + fluctuation())),
        perceptionShift: Math.max(0, Math.min(100, prev.perceptionShift + perceptionEffect * 0.1 + fluctuation())),
        realityCoherence: Math.max(0, Math.min(100, 
          // Reality coherence is inversely affected by glitches
          prev.realityCoherence - coherenceEffect * 0.1 + (realityStatus.safetyProtocols ? 0.2 : -0.1) + fluctuation()
        )),
        temporalSync: Math.max(0, Math.min(100, prev.temporalSync - temporalEffect * 0.1 + fluctuation())),
        cognitiveDissonance: Math.max(0, Math.min(100, prev.cognitiveDissonance + cognitiveEffect * 0.1 + fluctuation()))
      }));
      
      // Add data point for waveform
      setDataPoints(prev => {
        const newPoint = (Math.sin(Date.now() / 500) * 0.3) + 
                        (activeGlitches.length ? (Math.random() * activeGlitches.length / 10) : 0) + 0.5;
        const newPoints = [...prev, newPoint];
        return newPoints.slice(-100); // Keep only the last 100 points
      });
    }, 200);
    
    return () => clearInterval(interval);
  }, [activeGlitches, realityStatus.safetyProtocols]);
  
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
    ctx.strokeStyle = 'rgba(0, 80, 150, 0.2)';
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
    ctx.strokeStyle = 'rgba(0, 100, 180, 0.4)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(0, height / 2);
    ctx.lineTo(width, height / 2);
    ctx.stroke();
    
    // Calculate average glitch intensity
    const avgIntensity = activeGlitches.length 
      ? activeGlitches.reduce((sum, g) => sum + g.intensity, 0) / activeGlitches.length
      : 0;
    
    // Draw waveform with glitch effects
    ctx.lineWidth = 2;
    ctx.strokeStyle = `rgba(57, 255, 20, ${0.3 + avgIntensity * 0.7})`;
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
    
    // Add some digital noise based on active glitches
    if (activeGlitches.length > 0) {
      const noiseAmount = Math.min(200, activeGlitches.length * 40);
      ctx.fillStyle = 'rgba(57, 255, 20, 0.1)';
      
      for (let i = 0; i < noiseAmount; i++) {
        const x = Math.random() * width;
        const y = Math.random() * height;
        const size = Math.random() * 2 + 1;
        ctx.fillRect(x, y, size, size);
      }
    }
    
  }, [dataPoints, activeGlitches]);
  
  // Get status class based on value
  const getStatusClass = (value) => {
    if (value > 80) return 'text-green-400';
    if (value > 50) return 'text-yellow-400';
    return 'text-red-400';
  };
  
  // Get inverted status class (where lower is better)
  const getInvertedStatusClass = (value) => {
    if (value < 20) return 'text-green-400';
    if (value < 50) return 'text-yellow-400';
    return 'text-red-400';
  };
  
  return (
    <div className="p-4 border border-blue-800 rounded-lg bg-gradient-to-b from-blue-900/30 to-purple-900/30 cyber-border">
      <h2 className="text-xl mb-3 border-b border-blue-700 pb-1">Reality Distortion Output</h2>
      
      {/* Waveform display */}
      <div className="mb-4">
        <div className="text-sm text-blue-400 mb-1">Quantum Field Fluctuations:</div>
        <div className="border border-blue-800 bg-black/50 rounded p-1 h-32">
          <canvas ref={canvasRef} width={600} height={120} className="w-full h-full" />
        </div>
      </div>
      
      {/* Sensor data */}
      <div className="grid grid-cols-2 gap-4">
        <div>
          <div className="text-sm text-blue-400 mb-1">Neural Activity:</div>
          <div className={`text-lg font-bold ${getStatusClass(sensorData.neuralActivity)}`}>
            {sensorData.neuralActivity.toFixed(1)}Hz
          </div>
          <div className="h-1.5 w-full bg-gray-800 rounded overflow-hidden mt-1">
            <div 
              className={`h-full ${
                sensorData.neuralActivity > 80 ? 'bg-green-500' : 
                sensorData.neuralActivity > 50 ? 'bg-yellow-500' : 
                'bg-red-500'
              }`}
              style={{width: `${sensorData.neuralActivity}%`}}
            />
          </div>
        </div>
        
        <div>
          <div className="text-sm text-blue-400 mb-1">Perception Shift:</div>
          <div className={`text-lg font-bold ${getInvertedStatusClass(sensorData.perceptionShift)}`}>
            {sensorData.perceptionShift.toFixed(1)}%
          </div>
          <div className="h-1.5 w-full bg-gray-800 rounded overflow-hidden mt-1">
            <div 
              className={`h-full ${
                sensorData.perceptionShift < 20 ? 'bg-green-500' : 
                sensorData.perceptionShift < 50 ? 'bg-yellow-500' : 
                'bg-red-500'
              }`}
              style={{width: `${sensorData.perceptionShift}%`}}
            />
          </div>
        </div>
        
        <div>
          <div className="text-sm text-blue-400 mb-1">Reality Coherence:</div>
          <div className={`text-lg font-bold ${getStatusClass(sensorData.realityCoherence)}`}>
            {sensorData.realityCoherence.toFixed(1)}%
          </div>
          <div className="h-1.5 w-full bg-gray-800 rounded overflow-hidden mt-1">
            <div 
              className={`h-full ${
                sensorData.realityCoherence > 80 ? 'bg-green-500' : 
                sensorData.realityCoherence > 50 ? 'bg-yellow-500' : 
                'bg-red-500'
              }`}
              style={{width: `${sensorData.realityCoherence}%`}}
            />
          </div>
        </div>
        
        <div>
          <div className="text-sm text-blue-400 mb-1">Temporal Sync:</div>
          <div className={`text-lg font-bold ${getStatusClass(sensorData.temporalSync)}`}>
            {sensorData.temporalSync.toFixed(1)}%
          </div>
          <div className="h-1.5 w-full bg-gray-800 rounded overflow-hidden mt-1">
            <div 
              className={`h-full ${
                sensorData.temporalSync > 80 ? 'bg-green-500' : 
                sensorData.temporalSync > 50 ? 'bg-yellow-500' : 
                'bg-red-500'
              }`}
              style={{width: `${sensorData.temporalSync}%`}}
            />
          </div>
        </div>
        
        <div className="col-span-2">
          <div className="text-sm text-blue-400 mb-1">Cognitive Dissonance:</div>
          <div className={`text-lg font-bold ${getInvertedStatusClass(sensorData.cognitiveDissonance)}`}>
            {sensorData.cognitiveDissonance.toFixed(1)} units
          </div>
          <div className="h-1.5 w-full bg-gray-800 rounded overflow-hidden mt-1">
            <div 
              className={`h-full ${
                sensorData.cognitiveDissonance < 20 ? 'bg-green-500' : 
                sensorData.cognitiveDissonance < 50 ? 'bg-yellow-500' : 
                'bg-red-500'
              }`}
              style={{width: `${sensorData.cognitiveDissonance}%`}}
            />
          </div>
        </div>
      </div>
      
      {/* Current anomalies */}
      <div className="mt-4">
        <div className="text-sm text-blue-400 mb-1">Detected Anomalies:</div>
        <div className="border border-blue-800 bg-black/50 rounded p-2 h-16 overflow-y-auto font-mono text-xs space-y-1">
          {activeGlitches.length === 0 ? (
            <div className="text-blue-500">No anomalies detected in monitored sectors</div>
          ) : (
            activeGlitches.map(glitch => (
              <div key={glitch.id} className="text-blue-300">
                » Sector {Math.floor(Math.random() * 900) + 100}: {glitch.type.toLowerCase()} distortion detected ({(glitch.intensity * 100).toFixed(0)}% intensity)
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
};

export default RealTimeData; 