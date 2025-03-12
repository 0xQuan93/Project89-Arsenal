import React from 'react';

const GlitchCard = ({ glitch, isSelected, onSelect, onToggle }) => {
  const isMindMirror = glitch.source === 'Mind Mirror';
  
  // Determine card classes based on selection and source
  const cardClasses = `glitch-card ${isSelected ? 'selected' : ''} ${isMindMirror ? 'mind-mirror' : ''}`;
  
  return (
    <div 
      className={cardClasses}
      onClick={() => onSelect(glitch)}
    >
      <div className="flex justify-between items-start">
        <div>
          <div className="font-bold text-blue-200 flex items-center">
            {glitch.type} 
            <span className="text-xs text-blue-400 ml-1">
              #{glitch.id.substring(0, 8)}
            </span>
            {isMindMirror && <span className="mind-mirror-badge ml-2">MM</span>}
          </div>
          <div className="text-xs text-blue-400 mt-1">Target: {glitch.target}</div>
        </div>
        <div className={`px-2 py-0.5 text-xs rounded ${
          glitch.active ? 'bg-green-900/50 text-green-400 border border-green-800/50' : 'bg-red-900/50 text-red-400 border border-red-800/50'
        }`}>
          {glitch.active ? 'ACTIVE' : 'INACTIVE'}
        </div>
      </div>
      
      <div className="mt-2">
        <div className="flex justify-between text-xs text-blue-400">
          <span>Intensity:</span>
          <span>{(glitch.intensity * 100).toFixed(0)}%</span>
        </div>
        <div className="h-1.5 w-full bg-gray-800 rounded overflow-hidden mt-1">
          <div 
            className={isMindMirror ? 'progress-bar-purple' : 'progress-bar-green'}
            style={{width: `${glitch.intensity * 100}%`}}
          />
        </div>
      </div>
      
      {isSelected && (
        <div className="mt-2 grid grid-cols-2 gap-x-2 gap-y-1 text-xs">
          <div>
            <span className="text-blue-400">Complexity:</span>
            <span className="ml-1">{(glitch.complexity * 100).toFixed(0)}%</span>
          </div>
          <div>
            <span className="text-blue-400">Duration:</span>
            <span className="ml-1">{glitch.duration.toFixed(1)}s</span>
          </div>
          <div>
            <span className="text-blue-400">Persistence:</span>
            <span className="ml-1">{(glitch.persistence * 100).toFixed(0)}%</span>
          </div>
          <div>
            <span className="text-blue-400">Source:</span>
            <span className={`ml-1 ${isMindMirror ? 'text-purple-400' : 'text-blue-300'}`}>
              {glitch.source}
            </span>
          </div>
        </div>
      )}
      
      <div className="mt-2 pt-2 border-t border-blue-800/50">
        <button
          className={`w-full py-1 text-xs rounded ${
            glitch.active 
              ? 'cyber-button border-red-800/50 text-red-400' 
              : 'cyber-button border-green-800/50 text-green-400'
          }`}
          onClick={(e) => {
            e.stopPropagation();
            onToggle(glitch.id);
          }}
        >
          {glitch.active ? 'DEACTIVATE' : 'ACTIVATE'}
        </button>
      </div>
    </div>
  );
};

export default GlitchCard; 