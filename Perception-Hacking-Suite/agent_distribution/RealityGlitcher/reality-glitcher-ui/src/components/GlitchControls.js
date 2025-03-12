import React from 'react';

const GlitchControls = ({ glitch, onAmplify, onModulate, onStabilize, onTerminate }) => {
  if (!glitch) return null;

  return (
    <div className="mt-4 flex flex-wrap gap-2">
      <button 
        onClick={() => onAmplify(glitch.id)}
        className="px-3 py-1 border border-blue-600 rounded-md bg-blue-900/50 text-blue-300 hover:bg-blue-800/50 transition"
        disabled={!glitch.active}
      >
        Amplify
      </button>
      <button 
        onClick={() => onModulate(glitch.id)}
        className="px-3 py-1 border border-blue-600 rounded-md bg-blue-900/50 text-blue-300 hover:bg-blue-800/50 transition"
        disabled={!glitch.active}
      >
        Modulate
      </button>
      <button 
        onClick={() => onStabilize(glitch.id)}
        className="px-3 py-1 border border-blue-600 rounded-md bg-blue-900/50 text-blue-300 hover:bg-blue-800/50 transition"
        disabled={!glitch.active}
      >
        Stabilize
      </button>
      <button 
        onClick={() => onTerminate(glitch.id)}
        className="px-3 py-1 border border-red-800 rounded-md bg-red-900/30 text-red-300 hover:bg-red-800/50 transition"
      >
        Terminate
      </button>
    </div>
  );
};

export default GlitchControls; 