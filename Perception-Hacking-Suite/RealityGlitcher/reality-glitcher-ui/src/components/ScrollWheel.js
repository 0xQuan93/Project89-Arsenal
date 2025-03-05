import React, { useState, useEffect, useRef } from 'react';

// Renaming component to better reflect what it does now
const IntensitySlider = ({ 
  min = 0, 
  max = 100, 
  value = 50, 
  onChange, 
  label = "Value",
  unit = "%",
  color = "#3182ce" // default blue color
}) => {
  const [currentValue, setCurrentValue] = useState(value);
  const [isDragging, setIsDragging] = useState(false);
  const sliderRef = useRef(null);
  const startX = useRef(0);
  const startValue = useRef(0);
  
  // Handle mouse down on slider
  const handleMouseDown = (e) => {
    e.preventDefault(); // Prevent text selection
    
    if (sliderRef.current) {
      const rect = sliderRef.current.getBoundingClientRect();
      startX.current = e.clientX;
      startValue.current = currentValue;
      setIsDragging(true);
      
      document.addEventListener('mousemove', handleMouseMove);
      document.addEventListener('mouseup', handleMouseUp);
      
      // If clicked directly on the slider, immediately update to that position
      updateValueFromPosition(e.clientX, rect);
    }
  };
  
  // Update value based on click/drag position
  const updateValueFromPosition = (clientX, rect) => {
    // Calculate relative position (0 to 1)
    const relativePos = Math.max(0, Math.min(1, (clientX - rect.left) / rect.width));
    
    // Convert to value in range
    const newValue = min + (relativePos * (max - min));
    
    // Update value
    setCurrentValue(newValue);
    onChange && onChange(newValue);
  };
  
  // Handle mouse move for dragging
  const handleMouseMove = (e) => {
    if (!isDragging || !sliderRef.current) return;
    
    const rect = sliderRef.current.getBoundingClientRect();
    updateValueFromPosition(e.clientX, rect);
  };
  
  // Handle mouse up to stop dragging
  const handleMouseUp = () => {
    setIsDragging(false);
    document.removeEventListener('mousemove', handleMouseMove);
    document.removeEventListener('mouseup', handleMouseUp);
  };
  
  // Clean up event listeners
  useEffect(() => {
    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('mouseup', handleMouseUp);
    };
  }, []);
  
  // Update value if external value changes
  useEffect(() => {
    setCurrentValue(value);
  }, [value]);
  
  // Format display value (round to whole number)
  const formattedValue = Math.round(currentValue);
  
  // Calculate position for the slider thumb
  const thumbPosition = ((currentValue - min) / (max - min)) * 100;
  
  return (
    <div className="text-center select-none w-full">
      {label && <div className="text-sm text-blue-400 mb-2">{label}</div>}
      
      {/* Value display */}
      <div className="text-xl font-bold mb-2" style={{ color }}>
        {formattedValue}{unit}
      </div>
      
      {/* Slider track and thumb */}
      <div 
        className="relative h-6 mx-auto mb-4 cursor-pointer"
        onMouseDown={handleMouseDown}
        ref={sliderRef}
      >
        {/* Background track */}
        <div className="absolute inset-0 rounded-full h-2 top-2 bg-blue-900/40 border border-blue-800"></div>
        
        {/* Filled portion */}
        <div 
          className="absolute h-2 top-2 left-0 rounded-full"
          style={{ 
            width: `${thumbPosition}%`,
            background: `linear-gradient(to right, rgba(0,0,0,0.2), ${color})`,
            boxShadow: `0 0 5px ${color}`
          }}
        ></div>
        
        {/* Thumb */}
        <div 
          className={`absolute w-5 h-5 rounded-full -ml-2.5 top-0.5 ${isDragging ? 'dial-active' : 'dial-indicator'}`}
          style={{ 
            left: `${thumbPosition}%`,
            backgroundColor: color,
            boxShadow: `0 0 5px ${color}`
          }}
        ></div>
        
        {/* Tick marks */}
        {[...Array(5)].map((_, i) => (
          <div 
            key={i}
            className="absolute w-0.5 h-3 bg-blue-500/30 top-1.5"
            style={{ left: `${i * 25}%` }}
          ></div>
        ))}
      </div>
      
      {/* Min/Max labels */}
      <div className="flex justify-between text-xs text-blue-400 opacity-70 px-1">
        <div>{min}{unit}</div>
        <div>{max}{unit}</div>
      </div>
    </div>
  );
};

export default IntensitySlider; 