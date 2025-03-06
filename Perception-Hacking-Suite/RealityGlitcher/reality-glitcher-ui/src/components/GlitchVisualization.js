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
          color: getParticleColor(glitch.type, glitch.isAdvanced, glitch.distortionType),
          opacity: Math.random() * 0.7 + 0.3,
          // Additional properties for advanced effects
          pulse: Math.random() * 2 * Math.PI,
          pulseSpeed: Math.random() * 0.05 + 0.02,
          shape: glitch.isAdvanced ? getAdvancedShapeType(glitch.distortionType) : 'circle',
          rotation: Math.random() * Math.PI * 2,
          rotationSpeed: (Math.random() - 0.5) * 0.02
        };
        particles.push(particle);
      }
    };
    
    const getParticleColor = (type, isAdvanced, distortionType) => {
      // Base color based on glitch type
      let baseColor;
      switch(type) {
        case 'VISUAL': baseColor = [103, 232, 249]; break; // Cyan
        case 'AUDITORY': baseColor = [167, 139, 250]; break; // Purple
        case 'TEMPORAL': baseColor = [251, 146, 60]; break; // Orange
        case 'SPATIAL': baseColor = [52, 211, 153]; break; // Teal
        case 'COGNITIVE': baseColor = [248, 113, 113]; break; // Red
        case 'SYNCHRONISTIC': baseColor = [232, 121, 249]; break; // Pink
        default: baseColor = [147, 197, 253]; break; // Blue
      }
      
      // Modify colors for advanced glitches
      if (isAdvanced) {
        switch(distortionType) {
          case 'CONFIRMATION_BIAS':
            baseColor = [255, 153, 102]; // Orange-red for confirmation bias
            break;
          case 'BLACK_WHITE_THINKING':
            // High contrast colors for black-white thinking
            return Math.random() > 0.5 ? 'rgba(240, 240, 240, 0.9)' : 'rgba(20, 20, 20, 0.9)';
          case 'CATASTROPHIZING':
            baseColor = [239, 68, 68]; // More intense red for catastrophizing
            break;
          case 'EMOTIONAL_REASONING':
            baseColor = [236, 72, 153]; // Pink-red for emotional reasoning
            break;
          case 'FILTERING':
            // Return a filtered version of original color
            return `rgba(${baseColor[0]}, ${baseColor[1] * 0.7}, ${baseColor[2] * 0.7}, ${Math.random() * 0.6 + 0.4})`;
        }
      }
      
      // Add slight randomization for natural variation
      const r = baseColor[0] + Math.random() * 30 - 15;
      const g = baseColor[1] + Math.random() * 30 - 15;
      const b = baseColor[2] + Math.random() * 30 - 15;
      const a = Math.random() * 0.5 + 0.5;
      
      return `rgba(${r}, ${g}, ${b}, ${a})`;
    };
    
    const getAdvancedShapeType = (distortionType) => {
      if (!distortionType) return 'circle';
      
      // Different shapes for different cognitive distortions
      switch(distortionType) {
        case 'CONFIRMATION_BIAS': return 'triangle';
        case 'BLACK_WHITE_THINKING': return 'square';
        case 'CATASTROPHIZING': return 'star';
        case 'EMOTIONAL_REASONING': return 'pulse';
        case 'FILTERING': return 'line';
        default: return 'circle';
      }
    };
    
    // Different visualization modes
    const renderVisualGlitch = () => {
      ctx.clearRect(0, 0, width, height);
      
      // Base effect for all visual glitches
      if (visualizationMode === 'advanced') {
        // Create scan line effect
        for (let y = 0; y < height; y += 4) {
          if (Math.random() > 0.97) {
            const lineHeight = Math.random() * 2 + 1;
            const opacity = Math.random() * 0.2 + 0.1;
            ctx.fillStyle = `rgba(103, 232, 249, ${opacity})`;
            ctx.fillRect(0, y, width, lineHeight);
          }
        }
      }
      
      // Draw each particle
      particles.forEach(particle => {
        ctx.save();
        ctx.globalAlpha = particle.opacity;
        ctx.fillStyle = particle.color;
        
        // For cross-modal effects (Visual + Another type)
        if (glitch.crossModal) {
          const timeFactor = Date.now() * 0.001;
          // Create wave distortion effect
          const amplitude = 10 * glitch.intensity;
          const waveX = Math.sin(timeFactor + particle.y * 0.01) * amplitude;
          
          // Apply distortion to particle position
          particle.x += waveX * 0.05;
          
          // Advanced visual effects
          ctx.shadowBlur = 10 * glitch.intensity;
          ctx.shadowColor = particle.color;
        }
        
        // Draw different shapes based on visualization mode and advanced properties
        if (visualizationMode === 'advanced' && particle.shape !== 'circle') {
          ctx.translate(particle.x, particle.y);
          ctx.rotate(particle.rotation);
          
          switch(particle.shape) {
            case 'triangle':
              drawTriangle(ctx, 0, 0, particle.size * 1.5);
              break;
            case 'square':
              ctx.fillRect(-particle.size, -particle.size, particle.size * 2, particle.size * 2);
              break;
            case 'star':
              drawStar(ctx, 0, 0, 5, particle.size * 0.5, particle.size);
              break;
            case 'pulse':
              ctx.beginPath();
              ctx.arc(0, 0, particle.size * (1 + Math.sin(particle.pulse) * 0.3), 0, Math.PI * 2);
              ctx.fill();
              break;
            case 'line':
              ctx.lineWidth = 2;
              ctx.strokeStyle = particle.color;
              ctx.beginPath();
              ctx.moveTo(-particle.size * 2, 0);
              ctx.lineTo(particle.size * 2, 0);
              ctx.stroke();
              break;
            default:
              ctx.beginPath();
              ctx.arc(0, 0, particle.size, 0, Math.PI * 2);
              ctx.fill();
          }
        } else {
          // Default circle
          ctx.beginPath();
          ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
          ctx.fill();
        }
        
        ctx.restore();
        
        // Update particle for next frame
        particle.x += particle.speedX;
        particle.y += particle.speedY;
        
        // Apply pulse effect
        particle.pulse += particle.pulseSpeed;
        particle.rotation += particle.rotationSpeed;
        
        // Bounce off edges
        if (particle.x < 0 || particle.x > width) particle.speedX *= -1;
        if (particle.y < 0 || particle.y > height) particle.speedY *= -1;
      });
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
      
      // Base gridlines to represent thought patterns
      const gridSize = Math.max(10, 30 - glitch.intensity * 20);
      
      // Check for advanced cognitive distortions
      if (glitch.isAdvanced && glitch.distortionType) {
        renderAdvancedCognitiveDistortion(gridSize);
      } else {
        // Basic cognitive glitch visualization
        ctx.strokeStyle = 'rgba(248, 113, 113, 0.3)';
        ctx.lineWidth = 1;
        
        // Draw distorted grid
        for (let x = 0; x < width; x += gridSize) {
          ctx.beginPath();
          for (let y = 0; y < height; y += 5) {
            const offsetX = Math.sin(y * 0.05 + Date.now() * 0.001) * 5 * glitch.intensity;
            
            if (y === 0) {
              ctx.moveTo(x + offsetX, y);
            } else {
              ctx.lineTo(x + offsetX, y);
            }
          }
          ctx.stroke();
        }
        
        for (let y = 0; y < height; y += gridSize) {
          ctx.beginPath();
          for (let x = 0; x < width; x += 5) {
            const offsetY = Math.sin(x * 0.05 + Date.now() * 0.001) * 5 * glitch.intensity;
            
            if (x === 0) {
              ctx.moveTo(x, y + offsetY);
            } else {
              ctx.lineTo(x, y + offsetY);
            }
          }
          ctx.stroke();
        }
      }
      
      // Draw particles on top
      particles.forEach(particle => {
        ctx.globalAlpha = particle.opacity;
        ctx.fillStyle = particle.color;
        
        ctx.beginPath();
        ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
        ctx.fill();
        
        // Update particle position
        particle.x += particle.speedX;
        particle.y += particle.speedY;
        
        // Bounce off edges
        if (particle.x < 0 || particle.x > width) particle.speedX *= -1;
        if (particle.y < 0 || particle.y > height) particle.speedY *= -1;
      });
    };
    
    // Specialized rendering for different cognitive distortion types
    const renderAdvancedCognitiveDistortion = (gridSize) => {
      const time = Date.now() * 0.001;
      
      switch(glitch.distortionType) {
        case 'CONFIRMATION_BIAS':
          // Visualization for confirmation bias - shows only selective "pathways"
          ctx.strokeStyle = 'rgba(255, 153, 102, 0.4)';
          ctx.lineWidth = 2;
          
          // Draw main "chosen" pathways more prominently
          for (let i = 0; i < 5; i++) {
            const pathX = width * (i / 4);
            const pathWidth = 10 + glitch.intensity * 10;
            
            ctx.beginPath();
            for (let y = 0; y < height; y += 5) {
              // Path follows a sine wave
              const offsetX = Math.sin(y * 0.02 + time + i) * 50 * glitch.intensity;
              
              if (y === 0) {
                ctx.moveTo(pathX + offsetX, y);
              } else {
                ctx.lineTo(pathX + offsetX, y);
              }
            }
            ctx.stroke();
            
            // Draw path highlight
            ctx.strokeStyle = 'rgba(255, 153, 102, 0.8)';
            ctx.lineWidth = pathWidth * Math.sin(time * 0.5 + i) * 0.5 + pathWidth * 0.5;
            ctx.globalAlpha = 0.3;
            ctx.stroke();
            ctx.globalAlpha = 1;
            ctx.strokeStyle = 'rgba(255, 153, 102, 0.4)';
            ctx.lineWidth = 2;
          }
          break;
          
        case 'BLACK_WHITE_THINKING':
          // Stark contrasts with only black and white lines
          for (let x = 0; x < width; x += gridSize) {
            ctx.beginPath();
            ctx.strokeStyle = x % (gridSize * 2) === 0 ? 'rgba(240, 240, 240, 0.7)' : 'rgba(20, 20, 20, 0.7)';
            ctx.lineWidth = 3;
            
            ctx.moveTo(x, 0);
            ctx.lineTo(x, height);
            ctx.stroke();
          }
          
          for (let y = 0; y < height; y += gridSize) {
            ctx.beginPath();
            ctx.strokeStyle = y % (gridSize * 2) === 0 ? 'rgba(240, 240, 240, 0.7)' : 'rgba(20, 20, 20, 0.7)';
            
            ctx.moveTo(0, y);
            ctx.lineTo(width, y);
            ctx.stroke();
          }
          
          // Add flashing effect for extreme thinking
          if (Math.sin(time * 3) > 0.9) {
            ctx.fillStyle = 'rgba(255, 255, 255, 0.3)';
            ctx.fillRect(0, 0, width, height);
          } else if (Math.sin(time * 3) < -0.9) {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.3)';
            ctx.fillRect(0, 0, width, height);
          }
          break;
          
        case 'CATASTROPHIZING':
          // Effect grows more intense/chaotic over time
          const catastropheIntensity = (Math.sin(time * 0.5) * 0.5 + 0.5) * glitch.intensity * 2;
          
          // Draw expanding circular waves
          for (let i = 0; i < 8; i++) {
            const radius = (time * 50 + i * 50) % (Math.sqrt(width * width + height * height));
            ctx.beginPath();
            ctx.arc(width / 2, height / 2, radius, 0, Math.PI * 2);
            ctx.strokeStyle = `rgba(239, 68, 68, ${0.6 - radius / (width + height)})`;
            ctx.lineWidth = 2 + catastropheIntensity * 3;
            ctx.stroke();
          }
          
          // Add warning symbols
          if (visualizationMode === 'advanced') {
            for (let i = 0; i < 5; i++) {
              const x = width * (0.3 + Math.sin(time + i) * 0.2);
              const y = height * (0.3 + Math.cos(time + i) * 0.2);
              const size = 15 + catastropheIntensity * 10;
              
              ctx.save();
              ctx.translate(x, y);
              ctx.rotate(Math.PI / 4);
              
              // Draw warning triangle
              ctx.beginPath();
              ctx.moveTo(0, -size);
              ctx.lineTo(size, size);
              ctx.lineTo(-size, size);
              ctx.closePath();
              
              ctx.strokeStyle = 'rgba(239, 68, 68, 0.8)';
              ctx.lineWidth = 2;
              ctx.stroke();
              
              ctx.fillStyle = 'rgba(239, 68, 68, 0.3)';
              ctx.fill();
              
              ctx.restore();
            }
          }
          break;
          
        case 'EMOTIONAL_REASONING':
          // Pulsing emotional waves that distort thinking
          ctx.globalAlpha = 0.7;
          
          // Draw emotional "heat map"
          const gradient = ctx.createRadialGradient(
            width / 2, height / 2, 0,
            width / 2, height / 2, width / 2
          );
          
          const pulseIntensity = Math.sin(time * 2) * 0.5 + 0.5;
          
          gradient.addColorStop(0, `rgba(236, 72, 153, ${0.7 * pulseIntensity})`);
          gradient.addColorStop(0.6, `rgba(236, 72, 153, ${0.3 * pulseIntensity})`);
          gradient.addColorStop(1, 'rgba(236, 72, 153, 0)');
          
          ctx.fillStyle = gradient;
          ctx.fillRect(0, 0, width, height);
          
          // Draw emotional thought patterns
          ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)';
          ctx.lineWidth = 1;
          
          for (let i = 0; i < 12; i++) {
            const centerX = width / 2;
            const centerY = height / 2;
            const angle = (i / 12) * Math.PI * 2 + time * 0.2;
            const radius = 50 + Math.sin(time * 3 + i) * 20 * glitch.intensity;
            
            ctx.beginPath();
            for (let j = 0; j < Math.PI * 2; j += 0.1) {
              const x = centerX + Math.cos(j + angle) * radius;
              const y = centerY + Math.sin(j + angle) * radius;
              
              if (j === 0) {
                ctx.moveTo(x, y);
              } else {
                ctx.lineTo(x, y);
              }
            }
            ctx.closePath();
            ctx.stroke();
          }
          break;
          
        case 'FILTERING':
          // Only shows certain "filtered" information, rest is dimmed
          
          // Draw full grid first (dimmed)
          ctx.strokeStyle = 'rgba(180, 180, 180, 0.1)';
          ctx.lineWidth = 1;
          
          for (let x = 0; x < width; x += gridSize) {
            ctx.beginPath();
            ctx.moveTo(x, 0);
            ctx.lineTo(x, height);
            ctx.stroke();
          }
          
          for (let y = 0; y < height; y += gridSize) {
            ctx.beginPath();
            ctx.moveTo(0, y);
            ctx.lineTo(width, y);
            ctx.stroke();
          }
          
          // Now highlight only specific regions (the "filtered" view)
          ctx.strokeStyle = 'rgba(248, 113, 113, 0.6)';
          ctx.lineWidth = 2;
          
          // Create 3-5 "filtered" regions that stand out
          for (let i = 0; i < 4; i++) {
            const regionX = width * 0.2 + (width * 0.6) * (i / 3);
            const regionY = height * (0.3 + 0.4 * Math.sin(time + i));
            const regionSize = 30 + Math.sin(time * 2 + i) * 10;
            
            ctx.strokeRect(
              regionX - regionSize / 2,
              regionY - regionSize / 2,
              regionSize,
              regionSize
            );
            
            // Fill with subtle highlight
            ctx.fillStyle = 'rgba(248, 113, 113, 0.1)';
            ctx.fillRect(
              regionX - regionSize / 2,
              regionY - regionSize / 2,
              regionSize,
              regionSize
            );
            
            // Connect these regions with lines to show filtering
            if (i > 0) {
              const prevX = width * 0.2 + (width * 0.6) * ((i - 1) / 3);
              const prevY = height * (0.3 + 0.4 * Math.sin(time + i - 1));
              
              ctx.beginPath();
              ctx.moveTo(prevX, prevY);
              ctx.lineTo(regionX, regionY);
              ctx.stroke();
            }
          }
          break;
          
        default:
          // Fallback to basic cognitive visualization
          ctx.strokeStyle = 'rgba(248, 113, 113, 0.3)';
          ctx.lineWidth = 1;
          
          for (let x = 0; x < width; x += gridSize) {
            ctx.beginPath();
            for (let y = 0; y < height; y += 5) {
              const offsetX = Math.sin(y * 0.05 + time) * 5 * glitch.intensity;
              
              if (y === 0) {
                ctx.moveTo(x + offsetX, y);
              } else {
                ctx.lineTo(x + offsetX, y);
              }
            }
            ctx.stroke();
          }
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
    
    // Additional utility drawing functions
    const drawTriangle = (ctx, x, y, size) => {
      ctx.beginPath();
      ctx.moveTo(x, y - size);
      ctx.lineTo(x + size * 0.866, y + size * 0.5);
      ctx.lineTo(x - size * 0.866, y + size * 0.5);
      ctx.closePath();
      ctx.fill();
    };
    
    const drawStar = (ctx, x, y, points, innerRadius, outerRadius) => {
      ctx.beginPath();
      for (let i = 0; i < points * 2; i++) {
        const radius = i % 2 === 0 ? outerRadius : innerRadius;
        const angle = (Math.PI * 2 * i) / (points * 2);
        const pointX = x + radius * Math.sin(angle);
        const pointY = y + radius * Math.cos(angle);
        if (i === 0) {
          ctx.moveTo(pointX, pointY);
        } else {
          ctx.lineTo(pointX, pointY);
        }
      }
      ctx.closePath();
      ctx.fill();
    };
    
    // Update the animation function for cross-modal effects
    const animate = () => {
      // Clear the canvas
      ctx.clearRect(0, 0, width, height);
      
      // Draw effects based on glitch type
      if (glitch.type === 'VISUAL') {
        renderVisualGlitch();
      } else if (glitch.type === 'TEMPORAL') {
        renderTemporalGlitch();
      } else if (glitch.type === 'SPATIAL') {
        renderSpatialGlitch();
      } else if (glitch.type === 'AUDITORY') {
        renderAuditoryGlitch();
      } else if (glitch.type === 'COGNITIVE') {
        renderCognitiveGlitch();
      } else if (glitch.type === 'SYNCHRONISTIC') {
        renderSynchronisticGlitch();
      }
      
      // Handle cross-modal effects by adding additional layers
      if (glitch.crossModal && glitch.secondaryTarget) {
        // Add overlay effects based on secondary target
        ctx.globalAlpha = 0.4; // Make the overlay semi-transparent
        
        // Determine the secondary effect to apply
        const secondaryType = glitch.secondaryTarget.split('_')[0]; // Extract type from target
        
        if (secondaryType === 'VISUAL' && glitch.type !== 'VISUAL') {
          // Add visual noise overlay
          for (let i = 0; i < 50; i++) {
            const x = Math.random() * width;
            const y = Math.random() * height;
            const size = Math.random() * 3 + 1;
            
            ctx.fillStyle = `rgba(103, 232, 249, ${Math.random() * 0.3 + 0.1})`;
            ctx.fillRect(x, y, size, size);
          }
        } else if (secondaryType === 'AUDITORY' && glitch.type !== 'AUDITORY') {
          // Add wave pattern overlay for auditory
          ctx.strokeStyle = 'rgba(167, 139, 250, 0.3)';
          ctx.lineWidth = 2;
          
          const amplitude = 10 * glitch.intensity;
          const frequency = 0.02;
          
          ctx.beginPath();
          for (let x = 0; x < width; x += 2) {
            const y = height / 2 + Math.sin(x * frequency + Date.now() * 0.001) * amplitude;
            if (x === 0) {
              ctx.moveTo(x, y);
            } else {
              ctx.lineTo(x, y);
            }
          }
          ctx.stroke();
        } else if (secondaryType === 'COGNITIVE' && glitch.type !== 'COGNITIVE') {
          // Add thought pattern overlay for cognitive
          ctx.strokeStyle = 'rgba(248, 113, 113, 0.2)';
          ctx.lineWidth = 1;
          
          for (let i = 0; i < 5; i++) {
            const centerX = width / 2;
            const centerY = height / 2;
            const radius = 30 + i * 20;
            
            ctx.beginPath();
            ctx.arc(centerX, centerY, radius, 0, Math.PI * 2);
            ctx.stroke();
            
            // Connect with radiating lines
            if (i > 0) {
              for (let j = 0; j < 8; j++) {
                const angle = (j / 8) * Math.PI * 2;
                const innerX = centerX + Math.cos(angle) * (radius - 20);
                const innerY = centerY + Math.sin(angle) * (radius - 20);
                const outerX = centerX + Math.cos(angle) * radius;
                const outerY = centerY + Math.sin(angle) * radius;
                
                ctx.beginPath();
                ctx.moveTo(innerX, innerY);
                ctx.lineTo(outerX, outerY);
                ctx.stroke();
              }
            }
          }
        }
        
        ctx.globalAlpha = 1.0; // Reset alpha
      }
      
      // Call next frame
      animationFrameId = window.requestAnimationFrame(animate);
    };
    
    // Initialize and start animation
    initParticles();
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
          <h3 className="text-lg font-bold">
            {glitch.isAdvanced ? 'Advanced ' : ''}{glitch.type} Glitch
            {glitch.isAdvanced && glitch.distortionType && glitch.type === 'COGNITIVE' && (
              <span className="ml-2 text-sm text-red-400">({glitch.distortionType.replace('_', ' ')})</span>
            )}
          </h3>
          <div className="text-sm text-blue-400">
            {glitch.crossModal ? 'Cross-modal sensory disruption' : 'Induced fracture in perception matrix'}
          </div>
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
      <div className={`relative h-64 border ${glitch.isAdvanced ? 'border-purple-800' : 'border-blue-800'} rounded ${glitch.isAdvanced ? 'bg-black/60' : 'bg-black/50'} overflow-hidden`}>
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
        <div className={`${glitch.isAdvanced ? 'bg-purple-900/30' : 'bg-blue-900/30'} p-2 rounded border ${glitch.isAdvanced ? 'border-purple-800' : 'border-blue-800'}`}>
          <div className={glitch.isAdvanced ? 'text-purple-400' : 'text-blue-400'}>Intensity</div>
          <div className="text-lg">{Math.round(glitch.intensity * 100)}%</div>
        </div>
        <div className={`${glitch.isAdvanced ? 'bg-purple-900/30' : 'bg-blue-900/30'} p-2 rounded border ${glitch.isAdvanced ? 'border-purple-800' : 'border-blue-800'}`}>
          <div className={glitch.isAdvanced ? 'text-purple-400' : 'text-blue-400'}>Complexity</div>
          <div className="text-lg">{Math.round(glitch.complexity * 100)}%</div>
        </div>
        <div className={`${glitch.isAdvanced ? 'bg-purple-900/30' : 'bg-blue-900/30'} p-2 rounded border ${glitch.isAdvanced ? 'border-purple-800' : 'border-blue-800'}`}>
          <div className={glitch.isAdvanced ? 'text-purple-400' : 'text-blue-400'}>Persistence</div>
          <div className="text-lg">{Math.round(glitch.persistence * 100)}%</div>
        </div>
      </div>
      
      {/* Target information */}
      <div className="mt-3 text-xs">
        <div className={glitch.isAdvanced ? 'text-purple-400' : 'text-blue-400'}>
          Target: <span className={glitch.isAdvanced ? 'text-purple-300' : 'text-blue-300'}>{glitch.target}</span>
        </div>
        {glitch.crossModal && glitch.secondaryTarget && (
          <div className={glitch.isAdvanced ? 'text-purple-400' : 'text-blue-400'}>
            Secondary: <span className={glitch.isAdvanced ? 'text-purple-300' : 'text-blue-300'}>{glitch.secondaryTarget}</span>
          </div>
        )}
        <div className={glitch.isAdvanced ? 'text-purple-400' : 'text-blue-400'}>
          Source: <span className={glitch.isAdvanced ? 'text-purple-300' : 'text-blue-300'}>{glitch.source}</span>
        </div>
        {glitch.isPersistent && (
          <div className="text-purple-400 mt-1">
            <span className="px-2 py-0.5 bg-purple-900/50 rounded text-purple-300 text-xs">
              Persistent Reality Overlay
            </span>
          </div>
        )}
      </div>
    </div>
  );
};

export default GlitchVisualization; 