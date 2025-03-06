import React, { useState, useEffect, useRef } from 'react';
import './RealTimeData.css';

const RealTimeData = ({ glitches, realityStatus, mindMirrorConnected }) => {
  // Use a ref to store data points to prevent re-renders
  const dataPointsRef = useRef(Array(100).fill(0.5));
  const [dataPointsState, setDataPointsState] = useState(Array(100).fill(0.5));
  const [sensorData, setSensorData] = useState({
    neuralActivity: 78.4,
    perceptionShift: 12.3,
    realityCoherence: 89.7,
    temporalSync: 99.2,
    cognitiveDissonance: 15.0,
    quantumEntanglement: 45.2
  });
  const [anomalyData, setAnomalyData] = useState({});
  
  // Refs for canvas and animation
  const canvasRef = useRef(null);
  const animationRef = useRef(null);
  const canvasContainerRef = useRef(null);
  const backupTimerRef = useRef(null);
  
  // Debug flag - set to false for production
  const debug = process.env.NODE_ENV === 'development';
  
  // Function to create emergency data
  const createReliableData = () => {
    try {
      // Create a simple sine wave with more oscillations
      const points = [];
      for (let i = 0; i < 100; i++) {
        const value = 0.5 + 0.3 * Math.sin(i * 0.3);
        points.push(value);
      }
      return points;
    } catch (err) {
      console.error("Emergency data creation failed:", err);
      return Array(100).fill(0.5);
    }
  };
  
  // Emergency draw function with higher frequency cycles
  const emergencyDraw = () => {
    try {
      if (debug) console.log("Emergency draw triggered");
      
      // Find the canvas container
      const container = canvasContainerRef.current || document.querySelector('.quantum-canvas-container');
      if (!container) {
        if (debug) console.log("Container not found in emergency draw");
        return;
      }
      
      // Check if we have a canvas, create one if not
      let canvas = canvasRef.current;
      if (!canvas || !container.contains(canvas)) {
        if (debug) console.log("Canvas not found in emergency draw, creating one");
        canvas = document.createElement('canvas');
        canvas.width = 600;
        canvas.height = 130;
        canvas.style.width = '100%';
        canvas.style.height = '100%';
        container.innerHTML = '';
        container.appendChild(canvas);
        canvasRef.current = canvas;
      }
      
      // Generate emergency data if needed
      if (!dataPointsRef.current || dataPointsRef.current.length === 0) {
        dataPointsRef.current = createReliableData();
      }
      
      // Draw on the canvas
      const ctx = canvas.getContext('2d');
      if (!ctx) return;
      
      // Clear canvas
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.fillStyle = '#000';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      
      // Draw data as a line
      ctx.beginPath();
      ctx.strokeStyle = mindMirrorConnected ? '#a020f0' : '#00aaff';
      ctx.lineWidth = 3;
      
      // Draw points
      const points = dataPointsRef.current;
      for (let i = 0; i < points.length; i++) {
        const x = (i / (points.length - 1)) * canvas.width;
        const y = (1 - points[i]) * canvas.height;
        
        if (i === 0) {
          ctx.moveTo(x, y);
        } else {
          ctx.lineTo(x, y);
        }
      }
      
      ctx.stroke();
      
      // Add text
      ctx.fillStyle = '#fff';
      ctx.font = '14px monospace';
      ctx.fillText('EMERGENCY QUANTUM FLUCTUATOR', 10, 20);
      
      if (debug) console.log("Emergency draw complete");
    } catch (err) {
      console.error("Emergency draw failed:", err);
    }
  };
  
  // Create canvas function
  const createCanvas = () => {
    try {
      if (debug) console.log("Creating canvas");
      
      // Find or create container
      if (!canvasContainerRef.current) {
        canvasContainerRef.current = document.querySelector('.quantum-canvas-container');
      }
      
      if (!canvasContainerRef.current) {
        console.error("Canvas container not found");
        return;
      }
      
      // Create canvas
      const canvas = document.createElement('canvas');
      canvas.width = 600;
      canvas.height = 130;
      canvas.style.width = '100%';
      canvas.style.height = '100%';
      canvas.style.backgroundColor = 'black';
      
      // Clear container and add canvas
      canvasContainerRef.current.innerHTML = '';
      canvasContainerRef.current.appendChild(canvas);
      
      // Store ref
      canvasRef.current = canvas;
      
      if (debug) console.log("Canvas created");
    } catch (err) {
      console.error("Canvas creation failed:", err);
    }
  };
  
  // Animation speed multiplier - higher values = faster cycles
  const cycleSpeedMultiplier = 3.0;
  
  // Update data function
  const updateData = () => {
    try {
      const time = Date.now() * 0.001;
      const newPoints = [];
      
      // Base frequency and amplitude
      const baseFreq = 1.8;
      const baseAmp = 0.3;
      
      // Mind Mirror effect
      const mindMirrorEffect = mindMirrorConnected ? 0.15 : 0;
      
      // Get active glitches
      let activeGlitches = [];
      if (glitches && Array.isArray(glitches)) {
        activeGlitches = glitches.filter(g => g && g.active);
      }
      
      // Generate wave data
      for (let i = 0; i < 100; i++) {
        const x = i / 100;
        
        // Base wave
        let y = 0.5 + Math.sin(x * baseFreq * Math.PI * 2 + time * 2) * baseAmp;
        
        // Add randomness
        y += (Math.random() * 0.04 - 0.02);
        
        // Mind Mirror effect - strong pattern
        if (mindMirrorConnected) {
          const mindMirrorFreq = 5.5;
          y += Math.sin(x * mindMirrorFreq * Math.PI + time * 3) * 0.2;
        }
        
        // Apply glitch effects
        if (activeGlitches.length > 0) {
          activeGlitches.forEach(glitch => {
            if (!glitch) return;
            
            const intensity = glitch.intensity || 0.5;
            const type = glitch.type || 'visual';
            
            // Different patterns based on glitch type
            switch(type.toLowerCase()) {
              case 'visual':
                y += Math.sin(x * 7.3 + time * 1.5) * 0.1 * intensity;
                break;
              case 'auditory':
                y += Math.cos(x * 5.2 + time * 2.2) * 0.12 * intensity;
                break;
              case 'temporal':
                y += Math.sin(x * 3.1 + time * 0.8) * 0.15 * intensity;
                break;
              case 'spatial':
                y += Math.cos(x * 8.4 + time * 1.1) * 0.08 * intensity;
                break;
              case 'cognitive':
                y += Math.sin(x * 4.7 + time * 2.5) * 0.14 * intensity;
                break;
              case 'synchronistic':
                y += Math.cos(x * 6.6 + time * 1.7) * 0.11 * intensity;
                break;
              default:
                y += Math.sin(x * 5.5 + time * 1.9) * 0.1 * intensity;
            }
          });
        }
        
        // Ensure value is in range [0.1, 0.9]
        y = Math.max(0.1, Math.min(0.9, y));
        
        newPoints.push(y);
      }
      
      // Update state and ref
      dataPointsRef.current = newPoints;
      setDataPointsState([...newPoints]);
    } catch (err) {
      console.error("Data update failed:", err);
      // Use emergency data if update fails
      dataPointsRef.current = createReliableData();
    }
  };
  
  // Draw canvas function
  const drawCanvas = () => {
    try {
      // Check if canvas exists
      if (!canvasRef.current) {
        createCanvas();
        if (!canvasRef.current) return;
      }
      
      const canvas = canvasRef.current;
      const ctx = canvas.getContext('2d');
      
      if (!ctx) return;
      
      // Ensure canvas dimensions
      if (canvas.width === 0 || canvas.height === 0) {
        canvas.width = 600;
        canvas.height = 130;
      }
      
      // Get data points
      const points = dataPointsRef.current;
      if (!points || points.length === 0) {
        dataPointsRef.current = createReliableData();
      }
      
      // Clear canvas
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.fillStyle = 'rgba(0, 0, 0, 1)';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      
      // Set drawing properties
      ctx.lineWidth = 3;
      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';
      
      // Create gradient based on Mind Mirror connection
      const gradient = ctx.createLinearGradient(0, 0, canvas.width, 0);
      if (mindMirrorConnected) {
        gradient.addColorStop(0, '#8a2be2');
        gradient.addColorStop(0.5, '#a020f0');
        gradient.addColorStop(1, '#9370db');
      } else {
        gradient.addColorStop(0, '#00aaff');
        gradient.addColorStop(0.5, '#0088cc');
        gradient.addColorStop(1, '#00ccff');
      }
      
      ctx.strokeStyle = gradient;
      
      // Add glow effect
      ctx.shadowBlur = 10;
      ctx.shadowColor = mindMirrorConnected ? '#a020f0' : '#00aaff';
      
      // Draw waveform
      ctx.beginPath();
      
      // Calculate point spacing based on cycle speed
      const pointSpacing = Math.max(1, Math.round(cycleSpeedMultiplier / 2));
      
      for (let i = 0; i < points.length; i += pointSpacing) {
        const x = (i / (points.length - 1)) * canvas.width;
        const y = (1 - points[i]) * canvas.height;
        
        if (i === 0) {
          ctx.moveTo(x, y);
        } else {
          ctx.lineTo(x, y);
        }
      }
      
      ctx.stroke();
      
      // Add mind mirror text if connected
      if (mindMirrorConnected) {
        ctx.font = '16px monospace';
        ctx.fillStyle = '#a020f0';
        ctx.fillText('MIND MIRROR PATTERN DETECTED', 10, 25);
      }
    } catch (err) {
      console.error("Canvas drawing failed:", err);
      // Try emergency draw if normal drawing fails
      emergencyDraw();
    }
  };
  
  // Main animation function
  const animate = () => {
    updateData();
    drawCanvas();
    animationRef.current = requestAnimationFrame(animate);
  };
  
  // Set up at component mount
  useEffect(() => {
    // Create canvas first
    createCanvas();
    
    // Start animation
    animate();
    
    // Set up emergency interval
    backupTimerRef.current = setInterval(emergencyDraw, 3000);
    
    // Clean up on unmount
    return () => {
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current);
      }
      
      if (backupTimerRef.current) {
        clearInterval(backupTimerRef.current);
      }
    };
  }, [mindMirrorConnected, glitches, realityStatus]);
  
  // Render the component
  return (
    <div className="reality-data-container">
      <div className="section-heading">
        <h3>QUANTUM FLUCTUATOR</h3>
        <div className="status-indicator">
          {mindMirrorConnected && 
            <span className="mind-mirror-status">MIND MIRROR ONLINE</span>
          }
        </div>
      </div>
      
      <div className="quantum-canvas-container" ref={canvasContainerRef}>
        {/* Canvas created in effect */}
      </div>
      
      <div className="sensor-data-container">
        <div className="section-heading-secondary">
          <h4>REALITY SENSORS</h4>
        </div>
        
        <div className="sensor-grid">
          <div className="sensor-item">
            <div className="sensor-label">Neural Activity</div>
            <div className="sensor-value">{sensorData.neuralActivity.toFixed(1)}%</div>
            <div className="sensor-bar">
              <div className="sensor-bar-fill" style={{width: `${sensorData.neuralActivity}%`}}></div>
            </div>
          </div>
          
          <div className="sensor-item">
            <div className="sensor-label">Perception Shift</div>
            <div className="sensor-value">{sensorData.perceptionShift.toFixed(1)}%</div>
            <div className="sensor-bar">
              <div className="sensor-bar-fill" style={{width: `${sensorData.perceptionShift}%`}}></div>
            </div>
          </div>
          
          <div className="sensor-item">
            <div className="sensor-label">Reality Coherence</div>
            <div className="sensor-value">{sensorData.realityCoherence.toFixed(1)}%</div>
            <div className="sensor-bar">
              <div className="sensor-bar-fill" style={{width: `${sensorData.realityCoherence}%`}}></div>
            </div>
          </div>
          
          <div className="sensor-item">
            <div className="sensor-label">Temporal Sync</div>
            <div className="sensor-value">{sensorData.temporalSync.toFixed(1)}%</div>
            <div className="sensor-bar">
              <div className="sensor-bar-fill" style={{width: `${sensorData.temporalSync}%`}}></div>
            </div>
          </div>
          
          <div className="sensor-item">
            <div className="sensor-label">Cognitive Dissonance</div>
            <div className="sensor-value">{sensorData.cognitiveDissonance.toFixed(1)}%</div>
            <div className="sensor-bar">
              <div className="sensor-bar-fill" style={{width: `${sensorData.cognitiveDissonance}%`}}></div>
            </div>
          </div>
          
          <div className="sensor-item">
            <div className="sensor-label">Quantum Entanglement</div>
            <div className="sensor-value">{sensorData.quantumEntanglement.toFixed(1)}%</div>
            <div className="sensor-bar">
              <div className="sensor-bar-fill" style={{width: `${sensorData.quantumEntanglement}%`}}></div>
            </div>
          </div>
        </div>
      </div>
      
      {Object.keys(anomalyData).length > 0 && (
        <div className="anomalies-container">
          <div className="section-heading-secondary">
            <h4>Anomalies Detected</h4>
          </div>
          <div className="anomalies-grid">
            {Object.entries(anomalyData).map(([key, value]) => (
              <div key={key} className="anomaly-item">
                <div className="anomaly-label">{key}</div>
                <div className="anomaly-value">{value.toFixed(2)}</div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default RealTimeData; 