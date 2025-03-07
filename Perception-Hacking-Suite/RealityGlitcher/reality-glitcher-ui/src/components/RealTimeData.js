import React, { useState, useEffect, useRef, useCallback } from "react";
import "./RealTimeData.css";

// New SensorItem component to properly use React Hooks
const SensorItem = ({
  label,
  valueProp,
  sensorValue,
  maxValue = 100,
  isMindMirrorConnected,
}) => {
  // Apply quantum uncertainty effect - value fluctuates slightly
  // This simulates the Heisenberg uncertainty principle
  const [quantumState, setQuantumState] = useState({
    observed: false,
    value: sensorValue,
    // Create a unique random seed for each sensor
    seed: Math.random() * 1000,
  });

  // Use a ref to track previous Mind Mirror state to prevent erratic updates
  const prevMindMirrorRef = useRef(isMindMirrorConnected);

  // Update quantum state with uncertainty when value changes
  useEffect(() => {
    // IMPORTANT: When Mind Mirror state changes, don't immediately change values
    // This prevents layout shifts and erratic behavior
    if (prevMindMirrorRef.current !== isMindMirrorConnected) {
      // Gradually adapt to the mind mirror state change rather than instantly changing
      prevMindMirrorRef.current = isMindMirrorConnected;
    }

    const quantumTimer = setInterval(() => {
      if (!quantumState.observed) {
        // When not being observed, value has uncertainty
        // FIXED: Use more stable fluctuation with Mind Mirror
        const fluctuationAmount = isMindMirrorConnected ? 1.0 : 2.0; // Less fluctuation with Mind Mirror
        setQuantumState((prev) => ({
          ...prev,
          value:
            sensorValue +
            Math.sin(Date.now() * 0.001 + prev.seed) * fluctuationAmount,
        }));
      }
    }, 100);

    return () => clearInterval(quantumTimer);
  }, [
    sensorValue,
    quantumState.observed,
    quantumState.seed,
    isMindMirrorConnected,
  ]);

  // Observe/collapse function - called when user hovers
  const observeValue = () => {
    // When observed, value "collapses" to the actual measurement
    setQuantumState((prev) => ({
      ...prev,
      observed: true,
      value: sensorValue,
    }));
  };

  // Stop observing function
  const stopObserving = () => {
    // When observation stops, value becomes uncertain again
    setQuantumState((prev) => ({
      ...prev,
      observed: false,
    }));
  };

  // Calculate percentage for the progress bar
  const percent = Math.min(
    100,
    Math.max(0, (quantumState.value / maxValue) * 100),
  );

  // FIX: Remove Mind Mirror styling from sensor bars - use standard blue styling
  // regardless of Mind Mirror connection state
  const valueStyle = {
    transform: `translateX(${percent}%)`,
    // Always use the standard blue styling for sensor bars
    backgroundColor: "rgba(120, 200, 255, 0.75)",
  };

  // UPDATED: No label or class changes when Mind Mirror is connected
  // This keeps the regular view with just color shifts in the progress area
  return (
    <div
      className="sensor-item"
      onMouseEnter={observeValue}
      onMouseLeave={stopObserving}
    >
      <div className="sensor-label">{label}</div>
      <div className="sensor-bar">
        <div className="sensor-value" style={valueStyle}></div>
      </div>
      <div className="sensor-reading">{Math.round(quantumState.value)}</div>
    </div>
  );
};

const RealTimeData = ({ glitches, realityStatus, mindMirrorConnected }) => {
  // Sensor data for visualization
  const sensorDataRef = useRef({
    neuralActivity: 78.4,
    perceptionShift: 12.3,
    realityCoherence: 89.7,
    temporalSync: 99.2,
    cognitiveDissonance: 15.0,
    quantumEntanglement: 45.2,
    realityVector: 65.7, // New combined vector
  });

  // Timeline data for visualization
  const timelineDataRef = useRef({
    // Store the last 100 data points (for 10-second history at 100ms updates)
    // Initialize with data points properly distributed across time
    history: (() => {
      const now = Date.now();
      // Create evenly distributed timestamps across the full 10-second window
      return Array.from({ length: 100 }, (_, i) => {
        // Distribute timestamps with most recent at index 99
        const timeOffset = (99 - i) * 100; // Exactly 100ms intervals
        // Create smooth sine waves for initial data
        const sineValue = 0.5 + Math.sin((i / 100) * Math.PI * 4) * 0.2;
        const cosValue = 0.5 + Math.cos((i / 100) * Math.PI * 3) * 0.15;
        return {
          timestamp: now - timeOffset,
          value: sineValue,
          vectorValue: cosValue,
          quantumEffects: [],
          observed: false,
        };
      }).sort((a, b) => a.timestamp - b.timestamp); // Sort by timestamp to ensure proper order
    })(),
    // Quantum observation window - when user hovers over a time segment
    observationWindow: {
      start: -1,
      end: -1,
      center: -1, // Track cursor center for gradual effect
      active: false,
      // Add transition zones for smoother effect
      fadeInStart: -1,
      fadeOutEnd: -1,
    },
    // Add update interval tracking to ensure consistent history
    lastUpdateTime: Date.now(),
    updateInterval: 100, // Target 100ms between history points
  });

  // Vector data for combined probability visualization
  const vectorDataRef = useRef({
    points: Array(100).fill(0.5),
    lastUpdateTime: Date.now(),
    influence: 0.5, // How strongly the vector influences the main graph
    glitchInfluenceMap: {}, // Maps glitch IDs to their influence on the vector
  });

  // Creating a simple state to track if we're in emergency mode
  const [isEmergencyMode, setIsEmergencyMode] = useState(false);

  // Refs for canvas
  const canvasRef = useRef(null);
  const canvasContainerRef = useRef(null);

  // Debug flag - set to false for production
  const isDebugMode = process.env.NODE_ENV === "development";

  // Function to create emergency data
  const createReliableData = useCallback(() => {
    // Generate high-frequency, naturally flowing data points
    const time = Date.now() * 0.001;
    const reliablePoints = [];

    // Generate 100 continuous flowing points
    for (let i = 0; i < 100; i++) {
      const x = i / 100;
      // Use multiple overlapping wave patterns for natural flow
      let y = 0.5;

      // Add multiple harmonic waves with different phases
      y += Math.sin(x * 10 + time) * 0.1;
      y += Math.sin(x * 7 + time * 0.7) * 0.15;
      y += Math.sin(x * 13 + time * 1.3) * 0.05;

      // Ensure point is within valid range
      y = Math.max(0.1, Math.min(0.9, y));
      reliablePoints.push(y);
    }

    return reliablePoints;
  }, []);

  // Function to calculate reality vector based on sensors and glitches
  const calculateRealityVector = useCallback(() => {
    try {
      // Get all relevant sensor values
      const {
        neuralActivity,
        perceptionShift,
        realityCoherence,
        temporalSync,
        cognitiveDissonance,
        quantumEntanglement,
      } = sensorDataRef.current;

      // Calculate weighted vector from sensor data
      // Higher weights are given to more significant indicators
      let vectorValue = 0;

      // Neural activity (moderate positive contribution)
      vectorValue += (neuralActivity / 100) * 0.15;

      // Perception shift (high negative contribution - more shift means less stable reality)
      vectorValue -= (perceptionShift / 100) * 0.25;

      // Reality coherence (very high positive contribution)
      vectorValue += (realityCoherence / 100) * 0.30;

      // Temporal sync (high positive contribution)
      vectorValue += (temporalSync / 100) * 0.20;

      // Cognitive dissonance (moderate negative contribution)
      vectorValue -= (cognitiveDissonance / 100) * 0.15;

      // Quantum entanglement (low positive contribution)
      vectorValue += (quantumEntanglement / 100) * 0.10;

      // Normalize to 0-1 range (from our potentially -0.4 to +0.6 calculation)
      vectorValue = (vectorValue + 0.4) / 1.0;
      vectorValue = Math.max(0.1, Math.min(0.9, vectorValue));

      // Factor in active glitches
      if (glitches && glitches.length > 0) {
        // Create influence map if it doesn't exist
        if (
          Object.keys(vectorDataRef.current.glitchInfluenceMap).length === 0
        ) {
          // Initialize influence map for consistent effects
          glitches.forEach((glitch) => {
            const glitchId =
              glitch.id || Math.random().toString(36).substring(7);

            // Use hash function to create a consistent influence pattern
            const hash = (str) =>
              str.split("").reduce((a, b) => (a << 5) - a + b.charCodeAt(0), 0);
            const hashValue = hash(glitchId);

            // Generate a random but consistent influence pattern
            const pattern = [];
            for (let i = 0; i < 100; i++) {
              // Use sine wave with unique frequency based on hash
              const freq = 0.05 + (Math.abs(hashValue) % 20) / 100;
              const phase = (Math.abs(hashValue) % 628) / 100;
              pattern.push(Math.sin(i * freq + phase) * 0.2);
            }

            vectorDataRef.current.glitchInfluenceMap[glitchId] = {
              strength: (Math.abs(hashValue) % 50) / 100 + 0.3, // 0.3 to 0.8
              pattern,
            };
          });
        }

        // Apply each glitch's influence
        glitches.forEach((glitch) => {
          const glitchId = glitch.id || "";
          const influence = vectorDataRef.current.glitchInfluenceMap[glitchId];

          if (influence) {
            const now = Date.now() * 0.001;
            const timeIndex = Math.floor(now * 10) % 100;
            const influenceValue =
              influence.pattern[timeIndex] * influence.strength;

            // Apply the influence to our vector
            vectorValue += influenceValue;
            vectorValue = Math.max(0.1, Math.min(0.9, vectorValue));
          }
        });
      }

      return vectorValue;
    } catch (error) {
      console.error("Error calculating reality vector:", error);
      return 0.5; // Fallback to neutral value
    }
  }, [glitches]);

  // Emergency draw function used as a fallback when the main drawing fails
  const emergencyDraw = useCallback(() => {
    try {
      // Set emergency mode
      setIsEmergencyMode(true);
      
      // Attempt to restore canvas with simpler, more reliable drawing
      const canvas = canvasRef.current;
      if (!canvas) return;
      
      const ctx = canvas.getContext('2d');
      if (!ctx) return;
      
      // Clear canvas for emergency draw
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      
      // Get reliable data for emergency mode
      const reliableData = createReliableData();
      
      // Check for active glitches to adjust emergency visuals
      const activeGlitches = glitches ? glitches.filter(g => g.active) : [];
      const hasGlitches = activeGlitches.length > 0;
      
      // Add a simple background gradient for emergency mode
      const gradient = ctx.createLinearGradient(0, 0, 0, canvas.height);
      gradient.addColorStop(0, 'rgba(40, 10, 10, 0.2)'); // Red tint at top
      gradient.addColorStop(1, 'rgba(10, 10, 40, 0.1)'); // Blue tint at bottom
      ctx.fillStyle = gradient;
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      
      // Draw emergency warning indicators
      ctx.fillStyle = 'rgba(255, 50, 50, 0.15)';
      for (let i = 0; i < 3; i++) {
        const size = 50 + (i * 30);
        ctx.beginPath();
        ctx.arc(canvas.width - 50, 50, size, 0, Math.PI * 2);
        ctx.fill();
      }
      
      // Simple drawing - smooth line with Mind Mirror colors when connected
      ctx.strokeStyle = mindMirrorConnected ? 
        'rgba(220, 130, 255, 0.9)' : // Purple for Mind Mirror
        'rgba(120, 200, 255, 0.9)';  // Blue for standard
      
      // Thicker line with glitches
      const lineThickness = hasGlitches ? 
        (mindMirrorConnected ? 3.0 : 2.5) : 
        (mindMirrorConnected ? 2.5 : 2.0);
      ctx.lineWidth = lineThickness;
      
      // Add a glow effect when in emergency mode
      ctx.shadowBlur = 5;
      ctx.shadowColor = mindMirrorConnected ? 
        'rgba(220, 130, 255, 0.5)' : 
        'rgba(120, 200, 255, 0.5)';
      
      ctx.beginPath();
      
      // Convert the data to points
      const points = reliableData.map((value, index) => ({
        x: (index / (reliableData.length - 1)) * canvas.width,
        y: (1 - value) * canvas.height
      }));
      
      // Start with the first point
      if (points.length > 0) {
        ctx.moveTo(points[0].x, points[0].y);
        
        // For each point after the first one, draw a bezier curve with added jitter for glitches
        for (let i = 1; i < points.length - 2; i++) {
          let xOffset = 0, yOffset = 0;
          
          // Add jitter if there are active glitches
          if (hasGlitches && Math.random() < 0.15) {
            xOffset = (Math.random() - 0.5) * 5;
            yOffset = (Math.random() - 0.5) * 5;
          }
          
          const xc = (points[i].x + points[i + 1].x) / 2 + xOffset;
          const yc = (points[i].y + points[i + 1].y) / 2 + yOffset;
          ctx.quadraticCurveTo(points[i].x, points[i].y, xc, yc);
        }
        
        // Curve to the last two points
        if (points.length > 2) {
          ctx.quadraticCurveTo(
            points[points.length - 2].x,
            points[points.length - 2].y,
            points[points.length - 1].x,
            points[points.length - 1].y
          );
        } else if (points.length === 2) {
          // If we only have two points, just draw a line
          ctx.lineTo(points[1].x, points[1].y);
        }
        
        ctx.stroke();
        
        // Reset shadow for dots
        ctx.shadowBlur = 0;
        
        // Add highlight dots at intervals to represent emergency data points
        const dotInterval = hasGlitches ? 10 : 15; // More dots when glitches are active
        for (let i = 0; i < points.length; i += dotInterval) {
          if (i < points.length) {
            // Use alert color for emergency dots
            ctx.fillStyle = 'rgba(255, 100, 100, 0.9)';
            ctx.beginPath();
            ctx.arc(points[i].x, points[i].y, 2.5, 0, Math.PI * 2);
            ctx.fill();
          }
        }
      }
      
      if (isDebugMode) {
        console.log("Emergency draw completed with " + activeGlitches.length + " active glitches");
      }
    } catch (error) {
      console.error("Even emergency draw failed:", error);
    }
  }, [createReliableData, isDebugMode, mindMirrorConnected, glitches]);

  // Mouse handlers for canvas interaction
  const handleCanvasMouseMove = useCallback((e) => {
    // Implementation for mouse movement handling on the canvas
    const canvas = canvasRef.current;
    if (!canvas) return;

    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const relativeX = x / rect.width;

    // Update observation window in timeline data
    timelineDataRef.current.observationWindow.active = true;
    timelineDataRef.current.observationWindow.center = x;
    timelineDataRef.current.observationWindow.start = Math.max(0, x - 30);
    timelineDataRef.current.observationWindow.end = Math.min(canvas.width, x + 30);
    timelineDataRef.current.observationWindow.fadeInStart = Math.max(0, x - 60);
    timelineDataRef.current.observationWindow.fadeOutEnd = Math.min(canvas.width, x + 60);

    // Mark data points in observation window as observed
    const history = timelineDataRef.current.history;
    if (history.length > 0) {
      const startTime = history[0].timestamp;
      const endTime = history[history.length - 1].timestamp;
      const timespan = endTime - startTime;

      const observeStartTime = startTime + timespan * Math.max(0, relativeX - 0.1);
      const observeEndTime = startTime + timespan * Math.min(1, relativeX + 0.1);

      history.forEach((point) => {
        point.observed = point.timestamp >= observeStartTime && point.timestamp <= observeEndTime;
      });
    }
  }, []);

  const handleCanvasMouseLeave = useCallback(() => {
    // Handle when mouse leaves the canvas
    timelineDataRef.current.observationWindow.active = false;

    // Clear observed states
    timelineDataRef.current.history.forEach((point) => {
      point.observed = false;
    });
  }, []);

  // DrawCanvas function with enhanced glitch visualization
  const drawCanvas = useCallback(() => {
    try {
      const canvas = canvasRef.current;
      if (!canvas) return;
      
      const ctx = canvas.getContext('2d');
      if (!ctx) return;
      
      // Clear canvas
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      
      // Get history data
      const history = timelineDataRef.current.history;
      
      // Check for active glitches
      const activeGlitches = glitches ? glitches.filter(g => g.active) : [];
      const glitchTypes = new Set(activeGlitches.map(g => g.type));
      
      // Draw background effects based on active glitches
      if (activeGlitches.length > 0) {
        // Apply different background effects based on glitch types
        if (glitchTypes.has('SPATIAL')) {
          // Spatial distortion background
          const gradient = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
          gradient.addColorStop(0, 'rgba(0, 20, 50, 0.15)');
          gradient.addColorStop(0.5, 'rgba(0, 40, 70, 0.1)');
          gradient.addColorStop(1, 'rgba(0, 20, 50, 0.15)');
          ctx.fillStyle = gradient;
          ctx.fillRect(0, 0, canvas.width, canvas.height);
          
          // Add distortion grid
          ctx.strokeStyle = 'rgba(50, 200, 180, 0.07)';
          ctx.lineWidth = 0.5;
          const gridSize = 20;
          const time = Date.now() * 0.001;
          
          for (let i = 0; i < canvas.width; i += gridSize) {
            const offset = Math.sin(i * 0.01 + time) * 5;
            ctx.beginPath();
            ctx.moveTo(i, 0);
            ctx.lineTo(i + offset, canvas.height);
            ctx.stroke();
          }
        }
        
        if (glitchTypes.has('TEMPORAL')) {
          // Temporal echoes - subtle ghost images
          ctx.fillStyle = 'rgba(255, 180, 50, 0.03)';
          const time = Date.now() * 0.0005;
          const echoCount = 3;
          
          for (let e = 0; e < echoCount; e++) {
            const echoOffset = Math.sin(time + e) * 10;
            ctx.beginPath();
            ctx.ellipse(
              canvas.width / 2 + echoOffset, 
              canvas.height / 2, 
              canvas.width * 0.4, 
              canvas.height * 0.2, 
              0, 0, Math.PI * 2
            );
            ctx.fill();
          }
        }
        
        if (glitchTypes.has('COGNITIVE')) {
          // Cognitive interference patterns
          ctx.strokeStyle = 'rgba(200, 50, 50, 0.05)';
          ctx.lineWidth = 0.7;
          const time = Date.now() * 0.0003;
          
          for (let i = 0; i < 5; i++) {
            const y = canvas.height * (0.3 + i * 0.1);
            ctx.beginPath();
            for (let x = 0; x < canvas.width; x += 5) {
              const offset = Math.sin(x * 0.05 + time + i) * 5;
              if (x === 0) {
                ctx.moveTo(x, y + offset);
              } else {
                ctx.lineTo(x, y + offset);
              }
            }
            ctx.stroke();
          }
        }
      }
      
      // Draw baseline - thickness varies with glitch intensity
      const baselineThickness = Math.max(1, Math.min(3, 1 + activeGlitches.length * 0.2));
      // Use a slightly different baseline color when Mind Mirror is connected
      ctx.strokeStyle = mindMirrorConnected ? 
        'rgba(147, 51, 234, 0.3)' : // Subtle purple for Mind Mirror 
        'rgba(100, 100, 100, 0.5)'; // Normal gray
      ctx.lineWidth = baselineThickness;
      ctx.beginPath();
      ctx.moveTo(0, canvas.height * 0.5);
      ctx.lineTo(canvas.width, canvas.height * 0.5);
      ctx.stroke();
      
      // Draw history if available
      if (history.length > 0) {
        // Draw data line
        // Enhanced purple colors for Mind Mirror connection
        ctx.strokeStyle = mindMirrorConnected ?
          "rgba(240, 150, 255, 0.95)" : // Brighter purple for mind mirror
          "rgba(120, 200, 255, 0.9)";   // Blue for standard
        
        // Thicker line when glitches are active
        const lineWidth = mindMirrorConnected ? 
          2.5 + (activeGlitches.length * 0.3) : 
          2.0 + (activeGlitches.length * 0.2);
        ctx.lineWidth = Math.min(4, lineWidth); // Cap at maximum thickness
        
        ctx.beginPath();

        const timespan = history[history.length - 1].timestamp - history[0].timestamp;
        
        // Data points for drawing smooth curve
        const points = history.map((point, index) => {
          return {
            x: ((point.timestamp - history[0].timestamp) / timespan) * canvas.width,
            y: (1 - point.value) * canvas.height,
            observed: point.observed,
            effects: point.quantumEffects
          };
        });
        
        // Draw a smooth curve using cardinal spline interpolation
        if (points.length > 0) {
          // Apply line effects based on glitch types
          if (glitchTypes.has('VISUAL')) {
            // Visual glitches make the line more vibrant
            ctx.shadowBlur = 5;
            ctx.shadowColor = mindMirrorConnected ? 
              "rgba(220, 150, 255, 0.7)" : 
              "rgba(100, 180, 255, 0.7)";
          }
          
          if (glitchTypes.has('SYNCHRONISTIC')) {
            // Synchronistic glitches create a double line effect
            const mainColor = ctx.strokeStyle;
            // Draw echo line first
            ctx.strokeStyle = mindMirrorConnected ?
              "rgba(240, 150, 255, 0.4)" : 
              "rgba(120, 200, 255, 0.4)";
            ctx.beginPath();
            
            // Start with the first point with slight offset
            ctx.moveTo(points[0].x, points[0].y - 5);
            
            // For each point after the first one, draw a bezier curve
            for (let i = 1; i < points.length - 2; i++) {
              const xc = (points[i].x + points[i + 1].x) / 2;
              const yc = (points[i].y + points[i + 1].y) / 2 - 5 * Math.sin(i * 0.2);
              ctx.quadraticCurveTo(points[i].x, points[i].y - 5, xc, yc);
            }
            
            // Curve to the last two points
            if (points.length > 2) {
              ctx.quadraticCurveTo(
                points[points.length - 2].x,
                points[points.length - 2].y - 5,
                points[points.length - 1].x,
                points[points.length - 1].y - 5
              );
            }
            
            ctx.stroke();
            // Reset to main color
            ctx.strokeStyle = mainColor;
            ctx.beginPath();
          }
          
          // Start with the first point
          ctx.moveTo(points[0].x, points[0].y);
          
          // For each point after the first one, draw a bezier curve
          for (let i = 1; i < points.length - 2; i++) {
            // Add more variation to curves when spatial glitches are active
            let xOffset = 0, yOffset = 0;
            
            if (glitchTypes.has('SPATIAL') && Math.random() < 0.2) {
              xOffset = (Math.random() - 0.5) * 4;
              yOffset = (Math.random() - 0.5) * 4;
            }
            
            const xc = (points[i].x + points[i + 1].x) / 2 + xOffset;
            const yc = (points[i].y + points[i + 1].y) / 2 + yOffset;
            ctx.quadraticCurveTo(points[i].x, points[i].y, xc, yc);
          }
          
          // Curve to the last two points
          if (points.length > 2) {
            ctx.quadraticCurveTo(
              points[points.length - 2].x,
              points[points.length - 2].y,
              points[points.length - 1].x,
              points[points.length - 1].y
            );
          } else {
            // If we only have two points, just draw a line
            ctx.lineTo(points[points.length - 1].x, points[points.length - 1].y);
          }
        }
        
        // Complete the main curve
        ctx.stroke();
        
        // Reset shadow effects
        if (glitchTypes.has('VISUAL')) {
          ctx.shadowBlur = 0;
        }
        
        // Draw dots for observed points
        points.forEach((point) => {
          if (point.observed) {
            // Make observed points more vibrant with Mind Mirror
            ctx.fillStyle = mindMirrorConnected ?
              "rgba(255, 180, 255, 0.95)" : // Brighter, more saturated purple for Mind Mirror
              "rgba(200, 225, 255, 0.9)";   // Standard blue
            
            // Add a subtle glow effect for Mind Mirror points
            if (mindMirrorConnected) {
              ctx.shadowBlur = 8;
              ctx.shadowColor = "rgba(200, 100, 255, 0.7)";
            }
            
            // Larger dots when glitches are active
            const dotSizeMultiplier = 1.0 + (activeGlitches.length * 0.1);
            const dotSize = mindMirrorConnected ? 
              3.5 * dotSizeMultiplier : 
              3.0 * dotSizeMultiplier;
            
            ctx.beginPath();
            ctx.arc(point.x, point.y, dotSize, 0, Math.PI * 2);
            ctx.fill();
            
            // Reset shadow
            if (mindMirrorConnected) {
              ctx.shadowBlur = 0;
            }
          }
        });
        
        // Add glitch-specific markers at graph edges when active
        if (activeGlitches.length > 0) {
          activeGlitches.forEach((glitch, index) => {
            const xPos = canvas.width - 10 - (index * 15);
            const yPos = 10;
            const color = getGlitchColor(glitch.type);
            
            // Draw a small indicator for each active glitch
            ctx.fillStyle = color;
            ctx.beginPath();
            ctx.arc(xPos, yPos, 3, 0, Math.PI * 2);
            ctx.fill();
          });
        }
      }
    } catch (error) {
      console.error("Error drawing canvas:", error);
      emergencyDraw();
    }
  }, [mindMirrorConnected, emergencyDraw, glitches]);

  // Helper function to get color based on glitch type
  const getGlitchColor = (type) => {
    switch(type) {
      case 'VISUAL': return 'rgba(100, 180, 255, 0.9)'; // Blue
      case 'TEMPORAL': return 'rgba(255, 160, 50, 0.9)'; // Orange
      case 'SPATIAL': return 'rgba(50, 200, 180, 0.9)'; // Teal
      case 'COGNITIVE': return 'rgba(255, 100, 100, 0.9)'; // Red
      case 'SYNCHRONISTIC': return 'rgba(230, 120, 250, 0.9)'; // Pink
      default: return 'rgba(180, 180, 180, 0.9)'; // Gray
    }
  };

  // Function to update canvas size
  const updateCanvasSize = useCallback(() => {
    try {
      const canvas = canvasRef.current;
      const container = canvasContainerRef.current;
      if (!canvas || !container) return;

      // Get container dimensions
      const rect = container.getBoundingClientRect();

      // Update canvas size to match container
      canvas.width = rect.width;
      canvas.height = rect.height;

      // Redraw after resize
      drawCanvas();
    } catch (error) {
      console.error("Error updating canvas size:", error);
    }
  }, [drawCanvas]);

  // Function to create and initialize canvas
  const createCanvas = useCallback(() => {
    try {
      const container = canvasContainerRef.current;
      if (!container) return;

      // Create canvas if it doesn't exist
      if (!canvasRef.current) {
        const canvas = document.createElement("canvas");
        canvas.className = "quantum-canvas";
        container.appendChild(canvas);
        canvasRef.current = canvas;

        // Add event listeners for mouse interaction
        canvas.addEventListener("mousemove", handleCanvasMouseMove);
        canvas.addEventListener("mouseleave", handleCanvasMouseLeave);
      }

      // Initialize canvas size
      updateCanvasSize();
    } catch (error) {
      console.error("Error creating canvas:", error);
    }
  }, [handleCanvasMouseMove, handleCanvasMouseLeave, updateCanvasSize]);

  // Function to update data with enhanced glitch sensitivity
  const updateData = useCallback(() => {
    try {
      const now = Date.now();
      
      // Count active glitches for intensity calculations
      const activeGlitches = glitches ? glitches.filter(g => g.active) : [];
      const activeGlitchCount = activeGlitches.length;
      
      // Calculate glitch intensity factor - more intense effects with more glitches
      const glitchIntensityFactor = activeGlitchCount > 0 ? 
        Math.min(3.0, 1.0 + (activeGlitchCount * 0.4)) : 1.0; // Cap at 3x intensity
      
      // Update sensor data with small random changes, affected by glitches
      Object.keys(sensorDataRef.current).forEach(key => {
        // Random walk with constraints
        const currentValue = sensorDataRef.current[key];
        // Larger random changes when glitches are active
        const changeMagnitude = activeGlitchCount > 0 ? 2.8 : 2.0;
        const change = (Math.random() - 0.5) * changeMagnitude;
        
        // Different constraints for different sensors
        let newValue;
        if (key === 'neuralActivity') {
          // Keep neural activity high (70-90)
          newValue = Math.max(70, Math.min(90, currentValue + change));
        } else if (key === 'realityCoherence') {
          // Reality coherence fluctuates more with glitches
          const glitchFactor = activeGlitchCount * 2;
          newValue = Math.max(70 - glitchFactor, Math.min(95 - glitchFactor, currentValue + change));
        } else if (key === 'perceptionShift') {
          // Perception shift increases with glitches
          const glitchFactor = activeGlitchCount * 3;
          newValue = Math.max(5 + glitchFactor, Math.min(20 + glitchFactor, currentValue + change));
        } else if (key === 'temporalSync') {
          // Temporal sync stays very high (95-100) but can dip with temporal glitches
          const temporalGlitches = activeGlitches.filter(g => g.type === 'TEMPORAL');
          const temporalFactor = temporalGlitches.length * 3;
          newValue = Math.max(95 - temporalFactor, Math.min(100, currentValue + change * 0.5));
        } else if (key === 'cognitiveDissonance') {
          // Cognitive dissonance increases with glitches
          const glitchFactor = activeGlitchCount * 2.5;
          newValue = Math.max(10 + glitchFactor, Math.min(25 + glitchFactor, currentValue + change));
        } else if (key === 'quantumEntanglement') {
          // Quantum entanglement varies more (30-60)
          newValue = Math.max(30, Math.min(60, currentValue + change * 1.5));
        } else if (key === 'realityVector') {
          // Use the calculateRealityVector function
          newValue = calculateRealityVector() * 100;
        } else {
          // Default constraints (0-100)
          newValue = Math.max(0, Math.min(100, currentValue + change));
        }
        
        sensorDataRef.current[key] = newValue;
      });
      
      // Update timeline data
      const history = timelineDataRef.current.history;
      
      // Calculate new values with enhanced glitch effects
      // Base sine wave pattern
      let newValue = 0.5 + 
        Math.sin(now * 0.001) * 0.1 + 
        Math.sin(now * 0.0017) * 0.15 + 
        Math.sin(now * 0.0031) * 0.05;
      
      // Add glitch-specific effects to the wave pattern
      if (activeGlitchCount > 0) {
        activeGlitches.forEach((glitch, index) => {
          const glitchSeed = glitch.id ? glitch.id.charCodeAt(0) * 0.01 : index * 0.1;
          const intensity = glitch.intensity || 0.5;
          
          // Different glitch types create different wave effects
          switch(glitch.type) {
            case 'VISUAL':
              // Visual glitches add high-frequency noise
              newValue += Math.sin(now * 0.01 * (index + 1)) * 0.08 * intensity * glitchIntensityFactor;
              break;
            case 'TEMPORAL':
              // Temporal glitches create phase shifts and time warps
              newValue += Math.sin((now * 0.002) + (Math.sin(now * 0.0005) * 5)) * 0.12 * intensity * glitchIntensityFactor;
              break;
            case 'SPATIAL':
              // Spatial glitches create sudden jumps and discontinuities
              if (Math.random() < 0.05 * intensity) {
                newValue += (Math.random() - 0.5) * 0.25 * glitchIntensityFactor;
              }
              break;
            case 'COGNITIVE':
              // Cognitive glitches create pattern disruptions
              newValue += Math.tan(Math.sin(now * 0.0007 * (glitchSeed + 1))) * 0.05 * intensity * glitchIntensityFactor;
              break;
            case 'SYNCHRONISTIC':
              // Synchronistic glitches create mirrored patterns
              const syncWave = Math.sin(now * 0.002 * (glitchSeed + 1));
              newValue += (syncWave > 0 ? syncWave : -syncWave * 0.8) * 0.1 * intensity * glitchIntensityFactor;
              break;
            default:
              // Other glitches add general noise
              newValue += (Math.random() - 0.5) * 0.04 * intensity * glitchIntensityFactor;
          }
        });
      }
      
      // Ensure value stays in range
      newValue = Math.max(0.05, Math.min(0.95, newValue));
      
      // Calculate vector value with glitch effects
      const newVectorValue = calculateRealityVector();
      
      // Add new point to history
      const newPoint = {
        timestamp: now,
        value: newValue,
        vectorValue: newVectorValue,
        quantumEffects: activeGlitches.map(g => g.type), // Track active glitch types
        observed: false
      };
      
      // Remove oldest point
      history.shift();
      
      // Add new point
      history.push(newPoint);
      
      if (isDebugMode) {
        console.log("Data updated:", { 
          newValue, 
          newVectorValue,
          historyLength: history.length,
          activeGlitches: activeGlitchCount
        });
      }
    } catch (error) {
      console.error("Error updating data:", error);
    }
  }, [glitches, isDebugMode, calculateRealityVector]);

  // Handle visibility changes (page focus/blur)
  const handleVisibilityChange = useCallback(() => {
    if (document.visibilityState === "visible") {
      // Page is now visible - update data
      updateData();
      drawCanvas();
    }
  }, [updateData, drawCanvas]);

  // Set up update interval
  useEffect(() => {
    const updateInterval = setInterval(() => {
      updateData();
      drawCanvas();
    }, 100);

    return () => clearInterval(updateInterval);
  }, [updateData, drawCanvas]);

  // Initialize canvas and set up event listeners
  useEffect(() => {
    // Create canvas if it doesn't exist
    if (!canvasRef.current) {
      createCanvas();
    }

    // Set up event listeners
    window.addEventListener("resize", updateCanvasSize);
    document.addEventListener("visibilitychange", handleVisibilityChange);

    // Do initial update
    updateData();
    drawCanvas();

    return () => {
      window.removeEventListener("resize", updateCanvasSize);
      document.removeEventListener("visibilitychange", handleVisibilityChange);
    };
  }, [createCanvas, updateData, drawCanvas, updateCanvasSize, handleVisibilityChange]);

  // MODIFIED: For Mind Mirror connection, only adjust the quantum canvas - not the entire UI
  // This keeps the same layout and just changes the visualization colors
  return (
    <div className="real-time-data-container">
      {/* Quantum fluctuation graph moved above the sensor bars */}
      {/* Apply Mind Mirror class only to the quantum container */}
      {/* Apply glitch-specific classes based on active glitches */}
      <div 
        className={`
          quantum-container 
          ${mindMirrorConnected ? 'mind-mirror-connected' : ''} 
          ${glitches && glitches.some(g => g.active) ? 'has-glitches' : ''}
          ${glitches && glitches.some(g => g.active && g.type === 'VISUAL') ? 'has-visual-glitch' : ''}
          ${glitches && glitches.some(g => g.active && g.type === 'TEMPORAL') ? 'has-temporal-glitch' : ''}
          ${glitches && glitches.some(g => g.active && g.type === 'SPATIAL') ? 'has-spatial-glitch' : ''}
          ${glitches && glitches.some(g => g.active && g.type === 'COGNITIVE') ? 'has-cognitive-glitch' : ''}
          ${glitches && glitches.some(g => g.active && g.type === 'SYNCHRONISTIC') ? 'has-synchronistic-glitch' : ''}
        `} 
        ref={canvasContainerRef}
      >
        {/* Canvas created programmatically */}
        {isEmergencyMode && <div className="emergency-mode-indicator">EMERGENCY MODE</div>}
        
        {/* Render active glitch indicators */}
        {glitches && glitches.some(g => g.active) && (
          <div className="glitch-indicator">
            {glitches.filter(g => g.active).map((glitch, index) => (
              <div 
                key={glitch.id || index} 
                className={`glitch-dot ${glitch.type?.toLowerCase() || 'default'}`} 
                title={`${glitch.type || 'Unknown'} Glitch Active`}
              ></div>
            ))}
          </div>
        )}
      </div>

      <div className="sensor-container">
        <SensorItem
          label="Neural Activity"
          valueProp="neuralActivity"
          sensorValue={sensorDataRef.current.neuralActivity}
          maxValue={100}
          isMindMirrorConnected={mindMirrorConnected}
        />
        <SensorItem
          label="Perception Shift"
          valueProp="perceptionShift"
          sensorValue={sensorDataRef.current.perceptionShift}
          maxValue={100}
          isMindMirrorConnected={mindMirrorConnected}
        />
        <SensorItem
          label="Reality Coherence"
          valueProp="realityCoherence"
          sensorValue={sensorDataRef.current.realityCoherence}
          maxValue={100}
          isMindMirrorConnected={mindMirrorConnected}
        />
        <SensorItem
          label="Temporal Sync"
          valueProp="temporalSync"
          sensorValue={sensorDataRef.current.temporalSync}
          maxValue={100}
          isMindMirrorConnected={mindMirrorConnected}
        />
        <SensorItem
          label="Cognitive Dissonance"
          valueProp="cognitiveDissonance"
          sensorValue={sensorDataRef.current.cognitiveDissonance}
          maxValue={100}
          isMindMirrorConnected={mindMirrorConnected}
        />
        <SensorItem
          label="Quantum Entanglement"
          valueProp="quantumEntanglement"
          sensorValue={sensorDataRef.current.quantumEntanglement}
          maxValue={100}
          isMindMirrorConnected={mindMirrorConnected}
        />
        <SensorItem
          label="Reality Vector"
          valueProp="realityVector"
          sensorValue={sensorDataRef.current.realityVector}
          maxValue={100}
          isMindMirrorConnected={mindMirrorConnected}
        />
      </div>
    </div>
  );
};

export default RealTimeData;
