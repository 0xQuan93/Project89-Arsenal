import React, { useEffect, useRef, useState } from 'react';

const GlitchVisualization = ({ glitch }) => {
  const canvasRef = useRef(null);
  const [visualizationMode, setVisualizationMode] = useState('default');
  
  // Effect for canvas-based visualizations
  useEffect(() => {
    if (!glitch || !glitch.active || !canvasRef.current) return;
    
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    
    let animationFrameId;
    let particles = [];
    
    // Initialize particles based on glitch type
    const initParticles = () => {
      particles = [];
      const particleCount = Math.floor(50 + (glitch.intensity * 100));
      
      for (let i = 0; i < particleCount; i++) {
        const particle = {
          x: Math.random() * width,
          y: Math.random() * height,
          size: Math.random() * 5 + 1,
          speedX: (Math.random() - 0.5) * 3 * glitch.intensity,
          speedY: (Math.random() - 0.5) * 3 * glitch.intensity,
          color: getParticleColor(glitch.type),
          opacity: Math.random() * 0.7 + 0.3
        };
        particles.push(particle);
      }
    };
    
    const getParticleColor = (type) => {
      switch(type) {
        case 'VISUAL': return `rgba(103, 232, 249, ${Math.random() * 0.5 + 0.5})`;
        case 'AUDITORY': return `rgba(167, 139, 250, ${Math.random() * 0.5 + 0.5})`;
        case 'TEMPORAL': return `rgba(251, 146, 60, ${Math.random() * 0.5 + 0.5})`;
        case 'SPATIAL': return `rgba(52, 211, 153, ${Math.random() * 0.5 + 0.5})`;
        case 'COGNITIVE': return `rgba(248, 113, 113, ${Math.random() * 0.5 + 0.5})`;
        case 'SYNCHRONISTIC': return `rgba(232, 121, 249, ${Math.random() * 0.5 + 0.5})`;
        default: return `rgba(147, 197, 253, ${Math.random() * 0.5 + 0.5})`;
      }
    };
    
    // Different visualization modes
    const renderVisualGlitch = () => {
      ctx.clearRect(0, 0, width, height);
      
      // Draw grid lines
      ctx.strokeStyle = 'rgba(0, 80, 255, 0.15)';
      ctx.lineWidth = 1;
      
      // Horizontal lines
      for (let y = 0; y < height; y += 20) {
        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(width, y);
        ctx.stroke();
      }
      
      // Vertical lines
      for (let x = 0; x < width; x += 20) {
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, height);
        ctx.stroke();
      }
      
      // Draw particles
      particles.forEach(particle => {
        ctx.globalAlpha = particle.opacity;
        ctx.fillStyle = particle.color;
        ctx.beginPath();
        ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
        ctx.fill();
        
        // Update position
        particle.x += particle.speedX;
        particle.y += particle.speedY;
        
        // Bounce off edges
        if (particle.x < 0 || particle.x > width) particle.speedX *= -1;
        if (particle.y < 0 || particle.y > height) particle.speedY *= -1;
      });
      
      // Add distortion effect based on glitch intensity
      if (Math.random() < glitch.intensity * 0.3) {
        ctx.globalAlpha = glitch.intensity * 0.2;
        ctx.fillStyle = getParticleColor(glitch.type);
        ctx.fillRect(
          Math.random() * width, 
          Math.random() * height, 
          Math.random() * 100 + 50, 
          Math.random() * 10 + 5
        );
      }
      
      ctx.globalAlpha = 1;
    };
    
    const renderTemporalGlitch = () => {
      ctx.clearRect(0, 0, width, height);
      
      // Create clock-like visualization
      const centerX = width / 2;
      const centerY = height / 2;
      const maxRadius = Math.min(width, height) * 0.4;
      
      // Draw clock face
      ctx.strokeStyle = 'rgba(251, 146, 60, 0.5)';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(centerX, centerY, maxRadius, 0, Math.PI * 2);
      ctx.stroke();
      
      // Draw distorted time markers
      const markers = 12;
      for (let i = 0; i < markers; i++) {
        const angle = (i / markers) * Math.PI * 2;
        const distortion = Math.sin(Date.now() * 0.001 + i) * glitch.intensity * 20;
        
        const outerRadius = maxRadius + distortion;
        const innerRadius = maxRadius - 10 - distortion;
        
        const outerX = centerX + Math.cos(angle) * outerRadius;
        const outerY = centerY + Math.sin(angle) * outerRadius;
        const innerX = centerX + Math.cos(angle) * innerRadius;
        const innerY = centerY + Math.sin(angle) * innerRadius;
        
        ctx.strokeStyle = `rgba(251, 146, 60, ${0.7 + Math.sin(Date.now() * 0.002 + i) * 0.3})`;
        ctx.beginPath();
        ctx.moveTo(innerX, innerY);
        ctx.lineTo(outerX, outerY);
        ctx.stroke();
      }
      
      // Draw hands with glitching
      const now = new Date();
      const hours = now.getHours() % 12;
      const minutes = now.getMinutes();
      const seconds = now.getSeconds() + (now.getMilliseconds() / 1000);
      
      // Create glitched versions
      const glitchedSeconds = (seconds + (Math.random() * 2 - 1) * glitch.intensity * 10) % 60;
      const glitchedMinutes = (minutes + (Math.random() * 2 - 1) * glitch.intensity * 5) % 60;
      const glitchedHours = (hours + (Math.random() * 2 - 1) * glitch.intensity * 2) % 12;
      
      // Draw second hand
      const secondAngle = (glitchedSeconds / 60) * Math.PI * 2 - Math.PI / 2;
      ctx.strokeStyle = 'rgba(251, 146, 60, 0.9)';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(centerX, centerY);
      ctx.lineTo(
        centerX + Math.cos(secondAngle) * maxRadius * 0.9,
        centerY + Math.sin(secondAngle) * maxRadius * 0.9
      );
      ctx.stroke();
      
      // Draw minute hand
      const minuteAngle = (glitchedMinutes / 60) * Math.PI * 2 - Math.PI / 2;
      ctx.strokeStyle = 'rgba(251, 146, 60, 0.7)';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(centerX, centerY);
      ctx.lineTo(
        centerX + Math.cos(minuteAngle) * maxRadius * 0.8,
        centerY + Math.sin(minuteAngle) * maxRadius * 0.8
      );
      ctx.stroke();
      
      // Draw hour hand
      const hourAngle = ((glitchedHours / 12) * Math.PI * 2) + ((glitchedMinutes / 60) * Math.PI / 6) - Math.PI / 2;
      ctx.strokeStyle = 'rgba(251, 146, 60, 0.8)';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(centerX, centerY);
      ctx.lineTo(
        centerX + Math.cos(hourAngle) * maxRadius * 0.5,
        centerY + Math.sin(hourAngle) * maxRadius * 0.5
      );
      ctx.stroke();
      
      // Draw center
      ctx.fillStyle = 'rgba(251, 146, 60, 0.9)';
      ctx.beginPath();
      ctx.arc(centerX, centerY, 5, 0, Math.PI * 2);
      ctx.fill();
      
      // Occasional time skip glitch
      if (Math.random() < glitch.intensity * 0.1) {
        ctx.fillStyle = 'rgba(251, 146, 60, 0.3)';
        ctx.fillRect(0, 0, width, height);
      }
    };
    
    const renderSpatialGlitch = () => {
      ctx.clearRect(0, 0, width, height);
      
      // Draw a distorted grid representing spatial warping
      const gridSize = 20;
      const timeOffset = Date.now() * 0.001;
      
      ctx.strokeStyle = 'rgba(52, 211, 153, 0.4)';
      ctx.lineWidth = 1;
      
      // Draw distorted grid
      for (let x = 0; x <= width; x += gridSize) {
        ctx.beginPath();
        for (let y = 0; y <= height; y += 5) {
          const distortionX = Math.sin(y * 0.05 + timeOffset) * glitch.intensity * 20;
          const xPos = x + distortionX;
          
          if (y === 0) {
            ctx.moveTo(xPos, y);
          } else {
            ctx.lineTo(xPos, y);
          }
        }
        ctx.stroke();
      }
      
      for (let y = 0; y <= height; y += gridSize) {
        ctx.beginPath();
        for (let x = 0; x <= width; x += 5) {
          const distortionY = Math.sin(x * 0.05 + timeOffset) * glitch.intensity * 20;
          const yPos = y + distortionY;
          
          if (x === 0) {
            ctx.moveTo(x, yPos);
          } else {
            ctx.lineTo(x, yPos);
          }
        }
        ctx.stroke();
      }
      
      // Draw floating objects
      for (let i = 0; i < 10; i++) {
        const angle = (i / 10) * Math.PI * 2 + timeOffset;
        const radius = 40 + Math.sin(timeOffset * 2 + i) * 20;
        const x = width/2 + Math.cos(angle) * radius;
        const y = height/2 + Math.sin(angle) * radius;
        
        // Draw distorted shape
        ctx.fillStyle = `rgba(52, 211, 153, ${0.4 + Math.sin(timeOffset + i) * 0.2})`;
        ctx.beginPath();
        ctx.arc(x, y, 5 + Math.sin(timeOffset * 3 + i) * 5, 0, Math.PI * 2);
        ctx.fill();
        
        // Draw connecting lines
        if (i > 0) {
          const prevAngle = ((i-1) / 10) * Math.PI * 2 + timeOffset;
          const prevRadius = 40 + Math.sin(timeOffset * 2 + (i-1)) * 20;
          const prevX = width/2 + Math.cos(prevAngle) * prevRadius;
          const prevY = height/2 + Math.sin(prevAngle) * prevRadius;
          
          ctx.strokeStyle = `rgba(52, 211, 153, ${0.2 + Math.sin(timeOffset + i) * 0.1})`;
          ctx.beginPath();
          ctx.moveTo(prevX, prevY);
          ctx.lineTo(x, y);
          ctx.stroke();
        }
      }
    };
    
    const renderAuditoryGlitch = () => {
      ctx.clearRect(0, 0, width, height);
      
      // Create audio waveform visualization
      const waveCenter = height / 2;
      const waveCount = 3;
      
      for (let wave = 0; wave < waveCount; wave++) {
        const timeOffset = Date.now() * 0.001 + wave;
        const amplitude = (20 + (wave * 10)) * glitch.intensity;
        const frequency = 0.02 + (wave * 0.01);
        const opacity = 0.7 - (wave * 0.2);
        
        ctx.strokeStyle = `rgba(167, 139, 250, ${opacity})`;
        ctx.lineWidth = 2;
        ctx.beginPath();
        
        for (let x = 0; x < width; x++) {
          const y = waveCenter + 
            Math.sin(x * frequency + timeOffset) * amplitude + 
            Math.sin(x * frequency * 2 + timeOffset * 1.5) * amplitude * 0.5;
          
          if (x === 0) {
            ctx.moveTo(x, y);
          } else {
            ctx.lineTo(x, y);
          }
        }
        
        ctx.stroke();
      }
      
      // Add frequency bars
      const barCount = 20;
      const barWidth = (width / barCount) * 0.8;
      const barSpacing = width / barCount;
      
      for (let i = 0; i < barCount; i++) {
        const timeOffset = Date.now() * 0.001;
        const barHeight = (Math.sin(i * 0.3 + timeOffset) * 0.5 + 0.5) * height * 0.4 * (1 + glitch.intensity);
        const x = i * barSpacing + (barSpacing - barWidth) / 2;
        const y = height - barHeight;
        
        ctx.fillStyle = `rgba(167, 139, 250, ${0.5 + (i / barCount) * 0.3})`;
        ctx.fillRect(x, y, barWidth, barHeight);
      }
      
      // Occasional distortion
      if (Math.random() < glitch.intensity * 0.2) {
        ctx.fillStyle = 'rgba(167, 139, 250, 0.1)';
        const y = Math.random() * height;
        ctx.fillRect(0, y, width, Math.random() * 20 + 5);
      }
    };
    
    const renderCognitiveGlitch = () => {
      ctx.clearRect(0, 0, width, height);
      
      // Neural network visualization
      const nodeCount = 15;
      const nodes = [];
      const timeOffset = Date.now() * 0.001;
      
      // Create node positions
      for (let i = 0; i < nodeCount; i++) {
        const angle = (i / nodeCount) * Math.PI * 2;
        const radius = width * 0.3;
        const x = width/2 + Math.cos(angle) * radius;
        const y = height/2 + Math.sin(angle) * radius;
        
        // Add slight animation
        const animatedX = x + Math.sin(timeOffset + i) * 5 * glitch.intensity;
        const animatedY = y + Math.cos(timeOffset * 1.3 + i) * 5 * glitch.intensity;
        
        nodes.push({
          x: animatedX,
          y: animatedY,
          size: 4 + Math.random() * 4,
          activation: Math.sin(timeOffset * 2 + i) * 0.5 + 0.5
        });
      }
      
      // Draw connections between nodes
      for (let i = 0; i < nodeCount; i++) {
        const nodeA = nodes[i];
        
        for (let j = i + 1; j < nodeCount; j++) {
          const nodeB = nodes[j];
          const distance = Math.sqrt(
            Math.pow(nodeA.x - nodeB.x, 2) + 
            Math.pow(nodeA.y - nodeB.y, 2)
          );
          
          if (distance < width * 0.3) {
            const activation = (nodeA.activation + nodeB.activation) / 2;
            ctx.strokeStyle = `rgba(248, 113, 113, ${activation * 0.5})`;
            ctx.lineWidth = activation * 2;
            
            ctx.beginPath();
            ctx.moveTo(nodeA.x, nodeA.y);
            
            // Apply distortion to connection based on glitch intensity
            if (glitch.intensity > 0.5 && Math.random() < glitch.intensity * 0.3) {
              const midX = (nodeA.x + nodeB.x) / 2 + (Math.random() * 30 - 15) * glitch.intensity;
              const midY = (nodeA.y + nodeB.y) / 2 + (Math.random() * 30 - 15) * glitch.intensity;
              ctx.quadraticCurveTo(midX, midY, nodeB.x, nodeB.y);
            } else {
              ctx.lineTo(nodeB.x, nodeB.y);
            }
            
            ctx.stroke();
          }
        }
      }
      
      // Draw nodes
      for (const node of nodes) {
        ctx.fillStyle = `rgba(248, 113, 113, ${0.7 + node.activation * 0.3})`;
        ctx.beginPath();
        ctx.arc(node.x, node.y, node.size * (0.8 + node.activation * 0.4), 0, Math.PI * 2);
        ctx.fill();
        
        // Add glow effect
        ctx.fillStyle = `rgba(248, 113, 113, ${0.1 + node.activation * 0.1})`;
        ctx.beginPath();
        ctx.arc(node.x, node.y, node.size * 2, 0, Math.PI * 2);
        ctx.fill();
      }
      
      // Occasional thought fragments
      if (Math.random() < glitch.intensity * 0.05) {
        const phrases = [
          "ERROR", "MEMORY FAULT", "COGNITION ERROR", 
          "REALITY CHECK", "PARADOX", "RECURSION"
        ];
        const phrase = phrases[Math.floor(Math.random() * phrases.length)];
        
        ctx.font = "bold 12px monospace";
        ctx.fillStyle = "rgba(248, 113, 113, 0.8)";
        ctx.fillText(
          phrase, 
          Math.random() * (width - 100) + 50, 
          Math.random() * (height - 20) + 10
        );
      }
    };
    
    const renderSynchronisticGlitch = () => {
      ctx.clearRect(0, 0, width, height);
      
      const timeOffset = Date.now() * 0.001;
      const centerX = width / 2;
      const centerY = height / 2;
      
      // Draw multiple synchronizing circular patterns
      const layerCount = 5;
      
      for (let layer = 0; layer < layerCount; layer++) {
        const radius = 30 + layer * 25;
        const dotCount = 8 + layer * 4;
        const rotationSpeed = (0.3 + layer * 0.2) * (1 + glitch.intensity);
        const rotationOffset = layer * Math.PI / layerCount;
        
        for (let i = 0; i < dotCount; i++) {
          const angle = (i / dotCount) * Math.PI * 2 + timeOffset * rotationSpeed + rotationOffset;
          
          // Create synchronized patterns that occasionally glitch
          let adjustedAngle = angle;
          if (Math.random() < glitch.intensity * 0.2) {
            adjustedAngle += Math.random() * Math.PI * glitch.intensity;
          }
          
          const x = centerX + Math.cos(adjustedAngle) * radius;
          const y = centerY + Math.sin(adjustedAngle) * radius;
          
          const dotSize = 3 + (Math.sin(timeOffset * 2 + i + layer) * 0.5 + 0.5) * 3;
          
          ctx.fillStyle = `rgba(232, 121, 249, ${0.7 - layer * 0.1})`;
          ctx.beginPath();
          ctx.arc(x, y, dotSize, 0, Math.PI * 2);
          ctx.fill();
          
          // Connect to next point when synchronicity is high
          if (glitch.intensity < 0.7 || Math.random() > glitch.intensity * 0.3) {
            const nextI = (i + 1) % dotCount;
            const nextAngle = (nextI / dotCount) * Math.PI * 2 + timeOffset * rotationSpeed + rotationOffset;
            const nextX = centerX + Math.cos(nextAngle) * radius;
            const nextY = centerY + Math.sin(nextAngle) * radius;
            
            ctx.strokeStyle = `rgba(232, 121, 249, ${0.3 - layer * 0.05})`;
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(x, y);
            ctx.lineTo(nextX, nextY);
            ctx.stroke();
          }
        }
      }
      
      // Draw connecting lines between layers to show synchronicity
      for (let layer = 0; layer < layerCount - 1; layer++) {
        if (Math.random() < 0.3 + glitch.intensity * 0.4) {
          const outerRadius = 30 + layer * 25;
          const innerRadius = 30 + (layer + 1) * 25;
          
          const outerDotCount = 8 + layer * 4;
          const innerDotCount = 8 + (layer + 1) * 4;
          
          const outerIndex = Math.floor(Math.random() * outerDotCount);
          const innerIndex = Math.floor(Math.random() * innerDotCount);
          
          const rotationSpeed = (0.3 + layer * 0.2) * (1 + glitch.intensity);
          const nextRotationSpeed = (0.3 + (layer + 1) * 0.2) * (1 + glitch.intensity);
          
          const rotationOffset = layer * Math.PI / layerCount;
          const nextRotationOffset = (layer + 1) * Math.PI / layerCount;
          
          const outerAngle = (outerIndex / outerDotCount) * Math.PI * 2 + timeOffset * rotationSpeed + rotationOffset;
          const innerAngle = (innerIndex / innerDotCount) * Math.PI * 2 + timeOffset * nextRotationSpeed + nextRotationOffset;
          
          const outerX = centerX + Math.cos(outerAngle) * outerRadius;
          const outerY = centerY + Math.sin(outerAngle) * outerRadius;
          
          const innerX = centerX + Math.cos(innerAngle) * innerRadius;
          const innerY = centerY + Math.sin(innerAngle) * innerRadius;
          
          ctx.strokeStyle = `rgba(232, 121, 249, ${0.2 * glitch.intensity})`;
          ctx.lineWidth = 1;
          ctx.beginPath();
          ctx.moveTo(outerX, outerY);
          ctx.lineTo(innerX, innerY);
          ctx.stroke();
        }
      }
      
      // Draw synchronicity field
      ctx.fillStyle = `rgba(232, 121, 249, ${0.05 + glitch.intensity * 0.05})`;
      ctx.beginPath();
      ctx.arc(centerX, centerY, 30 + layerCount * 25, 0, Math.PI * 2);
      ctx.fill();
    };
    
    // Initialize animation
    initParticles();
    
    // Animation loop
    const animate = () => {
      // Select visualization based on glitch type
      switch(glitch.type) {
        case 'VISUAL':
          renderVisualGlitch();
          break;
        case 'TEMPORAL':
          renderTemporalGlitch();
          break;
        case 'SPATIAL':
          renderSpatialGlitch();
          break;
        case 'AUDITORY':
          renderAuditoryGlitch();
          break;
        case 'COGNITIVE':
          renderCognitiveGlitch();
          break;
        case 'SYNCHRONISTIC':
          renderSynchronisticGlitch();
          break;
        default:
          renderVisualGlitch();
      }
      
      // Continue animation if glitch is active
      if (glitch.active) {
        animationFrameId = window.requestAnimationFrame(animate);
      }
    };
    
    animate();
    
    // Cleanup
    return () => {
      window.cancelAnimationFrame(animationFrameId);
    };
  }, [glitch, visualizationMode]);
  
  // Toggle between visualization modes
  const toggleVisualizationMode = () => {
    const modes = ['default', 'advanced', 'minimal'];
    const currentIndex = modes.indexOf(visualizationMode);
    const nextIndex = (currentIndex + 1) % modes.length;
    setVisualizationMode(modes[nextIndex]);
  };

  if (!glitch) {
    return (
      <div className="h-64 flex items-center justify-center text-blue-500 border border-blue-900 rounded bg-black/50">
        <div className="text-center">
          <div className="text-xl">Select a glitch to visualize</div>
          <div className="text-sm mt-2">No active visualization</div>
        </div>
      </div>
    );
  }

  return (
    <div>
      <div className="mb-4 flex justify-between items-center">
        <div>
          <h3 className="text-lg font-bold">{glitch.type} Glitch</h3>
          <div className="text-sm text-blue-400">Induced fracture in perception matrix</div>
        </div>
        
        {/* Visualization mode toggle */}
        <button 
          onClick={toggleVisualizationMode} 
          className="px-2 py-1 text-xs bg-blue-900/50 border border-blue-700 rounded hover:bg-blue-800/50"
        >
          {visualizationMode === 'default' ? 'Standard View' : 
           visualizationMode === 'advanced' ? 'Advanced View' : 'Minimal View'}
        </button>
      </div>
      
      {/* Visualization */}
      <div className="relative h-64 border border-blue-800 rounded bg-black/50 overflow-hidden">
        <canvas 
          ref={canvasRef} 
          className="absolute inset-0 w-full h-full"
          width={640}
          height={320}
        />
        
        {!glitch.active && (
          <div className="absolute inset-0 flex items-center justify-center bg-black/70">
            <div className="text-center text-gray-400">
              <div>Glitch Inactive</div>
              <div className="text-sm mt-1">Activate to visualize</div>
            </div>
          </div>
        )}
      </div>
      
      {/* Visualization stats */}
      <div className="mt-3 grid grid-cols-3 gap-2 text-xs">
        <div className="bg-blue-900/30 p-2 rounded border border-blue-800">
          <div className="text-blue-400">Intensity</div>
          <div className="text-lg">{Math.round(glitch.intensity * 100)}%</div>
        </div>
        <div className="bg-blue-900/30 p-2 rounded border border-blue-800">
          <div className="text-blue-400">Complexity</div>
          <div className="text-lg">{Math.round(glitch.complexity * 100)}%</div>
        </div>
        <div className="bg-blue-900/30 p-2 rounded border border-blue-800">
          <div className="text-blue-400">Persistence</div>
          <div className="text-lg">{Math.round(glitch.persistence * 100)}%</div>
        </div>
      </div>
      
      {/* Target information */}
      <div className="mt-3 text-xs">
        <div className="text-blue-400">Target: <span className="text-blue-300">{glitch.target}</span></div>
        <div className="text-blue-400">Source: <span className="text-blue-300">{glitch.source}</span></div>
      </div>
    </div>
  );
};

export default GlitchVisualization; 