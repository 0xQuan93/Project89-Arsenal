import React, { useState, useEffect, useRef } from 'react';
import '../RealityGlitcher.css';
import IntensitySlider from './ScrollWheel';
import RealTimeData from './RealTimeData';

// Set a fixed maximum height constant for the control panel
const MAX_CONTROL_PANEL_HEIGHT = 1116;

const RealityGlitcherUI = () => {
  // State for reality status
  const [realityStatus, setRealityStatus] = useState({
    stability: 0.78,
    coherence: 'STABLE',
    safetyProtocols: true,
    activeSince: new Date().toISOString()
  });

  // State for glitches
  const [glitches, setGlitches] = useState([
    { id: 'g-001', type: 'VISUAL', intensity: 0.7, active: true, target: 'consensus_reality' },
    { id: 'g-002', type: 'AUDITORY', intensity: 0.4, active: false, target: 'local_perception' },
  ]);
  
  // State for selected glitch
  const [selectedGlitch, setSelectedGlitch] = useState(null);
  
  // State for console messages
  const [consoleMessages, setConsoleMessages] = useState([
    "✧ " + new Date().toLocaleTimeString() + " ┃ INFO ┃ Reality Glitcher initialized ✧",
    "✧ " + new Date().toLocaleTimeString() + " ┃ INFO ┃ Scanning for reality distortions... ✧",
  ]);

  // Refs for containers
  const glitchListRef = useRef(null);
  const controlPanelRef = useRef(null);
  const resizeObserverRef = useRef(null);
  
  // State to track if glitch list is scrollable
  const [isGlitchListScrollable, setIsGlitchListScrollable] = useState(false);
  
  // State to store the control panel's height
  const [controlPanelHeight, setControlPanelHeight] = useState(MAX_CONTROL_PANEL_HEIGHT);

  // Function to add console message
  const addConsoleMessage = (message, type = 'INFO') => {
    const timestamp = new Date().toLocaleTimeString();
    const formattedMessage = `✧ ${timestamp} ┃ ${type} ┃ ${message} ✧`;
    setConsoleMessages(prev => [...prev, formattedMessage]);
  };

  // Function to toggle glitch activation
  const toggleGlitch = (id) => {
    setGlitches(prev => 
      prev.map(g => {
        if (g.id === id) {
          const newActive = !g.active;
          addConsoleMessage(`Glitch ${g.id} ${newActive ? 'activated' : 'deactivated'}`);
          return {...g, active: newActive};
        }
        return g;
      })
    );
  };

  // Function to select a glitch
  const selectGlitch = (glitch) => {
    setSelectedGlitch(glitch);
    addConsoleMessage(`Selected glitch: ${glitch.id}`);
  };

  // Function to create a new glitch
  const createGlitch = () => {
    const newId = `g-${Math.floor(Math.random() * 900) + 100}`;
    const types = ['VISUAL', 'AUDITORY', 'TEMPORAL', 'SPATIAL', 'COGNITIVE'];
    const type = types[Math.floor(Math.random() * types.length)];
    const intensity = Math.round(Math.random() * 100) / 100;
    
    const newGlitch = {
      id: newId,
      type,
      intensity,
      active: false,
      target: Math.random() > 0.5 ? 'consensus_reality' : 'local_perception'
    };
    
    setGlitches(prev => [...prev, newGlitch]);
    addConsoleMessage(`Created new ${type} glitch: ${newId}`);
    
    // We no longer need to manually check overflow since ResizeObserver handles it
  };

  // Function to check if the glitch list container has overflow compared to control panel
  const checkGlitchListOverflow = () => {
    if (glitchListRef.current) {
      // Get the content height of the glitch list
      const { scrollHeight } = glitchListRef.current;
      
      // Check if list content is taller than the max control panel height
      setIsGlitchListScrollable(scrollHeight > MAX_CONTROL_PANEL_HEIGHT);
    }
  };

  // Function to toggle safety protocols
  const toggleSafetyProtocols = () => {
    setRealityStatus(prev => {
      const newStatus = {...prev, safetyProtocols: !prev.safetyProtocols};
      addConsoleMessage(
        `Safety protocols ${newStatus.safetyProtocols ? 'enabled' : 'disabled'}`,
        newStatus.safetyProtocols ? 'INFO' : 'WARNING'
      );
      return newStatus;
    });
  };

  // Function to handle intensity change via slider
  const handleIntensityChange = (newIntensity) => {
    if (!selectedGlitch) return;
    
    // Convert the 0-100 scale to 0-1
    const normalizedIntensity = newIntensity / 100;
    
    setGlitches(prev => 
      prev.map(g => {
        if (g.id === selectedGlitch.id) {
          return {...g, intensity: normalizedIntensity};
        }
        return g;
      })
    );
    
    // Update selected glitch
    setSelectedGlitch(prev => ({...prev, intensity: normalizedIntensity}));
    
    // Log significant changes (not every small change)
    if (Math.abs(normalizedIntensity - selectedGlitch.intensity) > 0.05) {
      addConsoleMessage(`Adjusted glitch ${selectedGlitch.id} intensity to ${(normalizedIntensity * 100).toFixed(0)}%`);
    }
  };

  // Effect to simulate reality fluctuations
  useEffect(() => {
    const timer = setInterval(() => {
      // Calculate new stability based on active glitches
      const activeGlitches = glitches.filter(g => g.active);
      let newStability = 0.95 - (activeGlitches.length * 0.05);
      
      // Add some randomness
      newStability += (Math.random() * 0.1) - 0.05;
      newStability = Math.max(0.1, Math.min(0.95, newStability));
      
      setRealityStatus(prev => ({
        ...prev,
        stability: newStability,
        coherence: newStability > 0.7 ? 'STABLE' : 
                 newStability > 0.4 ? 'UNSTABLE' : 'CRITICAL'
      }));
    }, 3000);
    
    return () => clearInterval(timer);
  }, [glitches]);

  // Effect to check overflow whenever glitches change
  useEffect(() => {
    // Small delay to ensure DOM is updated first
    const timer = setTimeout(checkGlitchListOverflow, 50);
    return () => clearTimeout(timer);
  }, [glitches]);

  // Initial check after mount
  useEffect(() => {
    checkGlitchListOverflow();
    // Add resize listener to adjust scrollability on window resize
    window.addEventListener('resize', checkGlitchListOverflow);
    return () => {
      window.removeEventListener('resize', checkGlitchListOverflow);
    };
  }, []);

  return (
    // Changed to auto height instead of min-h-screen to ensure proper scrolling
    <div className="bg-black text-blue-300 p-6 font-mono cyber-bg" style={{minHeight: '100%', paddingBottom: '60px'}}>
      {/* Header with glitch effect */}
      <header className="text-center mb-8">
        <h1 className="text-3xl font-bold bg-gradient-to-r from-purple-400 via-blue-500 to-purple-400 bg-clip-text text-transparent cyber-text-glow visual-glitch" data-text="PROJECT89 REALITY GLITCHER">
          PROJECT89 REALITY GLITCHER
        </h1>
        <div className="mt-2 text-sm text-blue-400">Perception Manipulation Interface v3.9.1</div>
      </header>
      
      {/* Reality Status Dashboard */}
      <div className="mb-8 p-4 border border-blue-800 rounded-lg bg-gradient-to-b from-blue-900/30 to-purple-900/30 cyber-border">
        <h2 className="text-xl mb-3 border-b border-blue-700 pb-1">Reality Status</h2>
        <div className="grid grid-cols-2 gap-4">
          <div>
            <div className="text-sm text-blue-400">Coherence Status:</div>
            <div className={`text-lg font-bold ${
              realityStatus.coherence === 'STABLE' ? 'text-green-400' : 
              realityStatus.coherence === 'UNSTABLE' ? 'text-yellow-400' : 
              'text-red-400 animate-pulse'
            }`}>
              {realityStatus.coherence}
            </div>
          </div>
          <div>
            <div className="text-sm text-blue-400">Stability Index:</div>
            <div className="text-lg font-bold">{(realityStatus.stability * 100).toFixed(1)}%</div>
          </div>
          <div>
            <div className="text-sm text-blue-400">Safety Protocols:</div>
            <div 
              className={`text-lg font-bold ${realityStatus.safetyProtocols ? 'text-green-400' : 'text-red-400'} cursor-pointer`}
              onClick={toggleSafetyProtocols}
            >
              {realityStatus.safetyProtocols ? 'ACTIVE' : 'DISABLED'}
            </div>
          </div>
          <div>
            <div className="text-sm text-blue-400">Session Active Since:</div>
            <div className="text-lg font-bold">{new Date(realityStatus.activeSince).toLocaleTimeString()}</div>
          </div>
        </div>
        
        {/* Stability Bar */}
        <div className="mt-4">
          <div className="h-2 w-full bg-gray-800 rounded overflow-hidden">
            <div 
              className={`h-full transition-all duration-1000 ${
                realityStatus.stability > 0.7 ? 'bg-green-500' : 
                realityStatus.stability > 0.4 ? 'bg-yellow-500' : 
                'bg-red-500'
              }`}
              style={{width: `${realityStatus.stability * 100}%`}}
            />
          </div>
        </div>
      </div>
      
      {/* Real-time Data Display */}
      <div className="mb-8">
        <RealTimeData glitches={glitches} realityStatus={realityStatus} />
      </div>
      
      {/* Main Content Area - FIXED: Ensuring this section is visible */}
      <h2 className="text-2xl text-center mb-3 mt-6 border-b border-blue-700 pb-1 cyber-text-glow">Glitch Management System</h2>
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-6">
        {/* Glitch List */}
        <div className="p-4 border border-blue-800 rounded-lg bg-gradient-to-b from-blue-900/30 to-purple-900/30 cyber-border">
          <div className="flex justify-between items-center mb-3 border-b border-blue-700 pb-1">
            <h2 className="text-xl">Glitch List</h2>
            <div className="flex items-center">
              <div className={`mr-2 text-xs ${isGlitchListScrollable ? 'text-blue-400' : 'text-blue-800'}`}>
                {isGlitchListScrollable ? 'SCROLL ENABLED' : 'AUTO-EXPANDING'}
              </div>
              <button 
                className="px-3 py-1 text-sm bg-blue-900/50 border border-blue-600 rounded hover:bg-blue-800/50 transition"
                onClick={createGlitch}
              >
                + CREATE
              </button>
            </div>
          </div>
          
          {glitches.length === 0 ? (
            <div className="p-4 text-center text-blue-500 border border-blue-900/50 rounded bg-blue-950/20">
              No glitches detected in reality matrix
            </div>
          ) : (
            <div 
              ref={glitchListRef}
              className="space-y-3 overflow-y-auto pr-2" 
              style={{ 
                maxHeight: isGlitchListScrollable ? `${MAX_CONTROL_PANEL_HEIGHT}px` : 'auto',
                transition: 'all 0.3s ease',
                height: isGlitchListScrollable ? `${MAX_CONTROL_PANEL_HEIGHT}px` : 'auto'
              }}
            >
              {glitches.map(glitch => (
                <div 
                  key={glitch.id}
                  className={`p-3 border rounded cursor-pointer transition-all duration-300 ${
                    selectedGlitch?.id === glitch.id 
                      ? 'border-blue-400 bg-blue-900/40 shadow-lg shadow-blue-900/50' 
                      : 'border-blue-800 bg-blue-900/20 hover:bg-blue-900/30'
                  }`}
                  onClick={() => selectGlitch(glitch)}
                >
                  <div className="flex justify-between">
                    <div className="font-bold">{glitch.id}</div>
                    <div className={`px-2 py-0.5 text-xs rounded ${
                      glitch.active ? 'bg-green-900/50 text-green-400' : 'bg-red-900/50 text-red-400'
                    }`}>
                      {glitch.active ? 'ACTIVE' : 'INACTIVE'}
                    </div>
                  </div>
                  <div className="mt-1 text-sm">Type: {glitch.type}</div>
                  <div className="mt-1 text-sm">Target: {glitch.target}</div>
                  <div className="mt-2">
                    <div className="text-xs text-blue-400">Intensity: {(glitch.intensity * 100).toFixed(0)}%</div>
                    <div className="h-1.5 w-full bg-gray-800 rounded overflow-hidden mt-1">
                      <div 
                        className="h-full bg-blue-500"
                        style={{width: `${glitch.intensity * 100}%`}}
                      />
                    </div>
                  </div>
                  <div className="mt-2 pt-2 border-t border-blue-800/50">
                    <button
                      className={`px-2 py-1 text-xs mr-2 rounded ${
                        glitch.active ? 'bg-red-900/30 text-red-400 border border-red-800' : 'bg-green-900/30 text-green-400 border border-green-800'
                      }`}
                      onClick={(e) => {
                        e.stopPropagation();
                        toggleGlitch(glitch.id);
                      }}
                    >
                      {glitch.active ? 'DEACTIVATE' : 'ACTIVATE'}
                    </button>
                  </div>
                </div>
              ))}
            </div>
          )}
          
          {/* Height indicator */}
          <div className="mt-2 text-xs text-blue-800 opacity-60">
            Max height: {MAX_CONTROL_PANEL_HEIGHT}px
          </div>
        </div>
        
        {/* Glitch Control Panel */}
        <div 
          ref={controlPanelRef}
          className="p-4 border border-blue-800 rounded-lg bg-gradient-to-b from-blue-900/30 to-purple-900/30 cyber-border"
          style={{ maxHeight: `${MAX_CONTROL_PANEL_HEIGHT}px`, overflowY: 'auto' }}
        >
          <h2 className="text-xl mb-3 border-b border-blue-700 pb-1">Glitch Control</h2>
          
          {selectedGlitch ? (
            <div>
              <div className="mb-4 p-3 border border-blue-700 rounded bg-blue-900/20">
                <div className="text-lg mb-2 font-bold">Glitch {selectedGlitch.id}</div>
                <div className="grid grid-cols-2 gap-3 text-sm">
                  <div>Type: <span className="text-blue-300">{selectedGlitch.type}</span></div>
                  <div>Target: <span className="text-blue-300">{selectedGlitch.target}</span></div>
                  <div>Status: <span className={selectedGlitch.active ? 'text-green-400' : 'text-red-400'}>
                    {selectedGlitch.active ? 'ACTIVE' : 'INACTIVE'}
                  </span></div>
                  <div>Intensity: <span className="text-blue-300">{(selectedGlitch.intensity * 100).toFixed(0)}%</span></div>
                </div>
              </div>
              
              {/* Control panel with slider instead of scroll wheel */}
              <div className="grid grid-cols-1 gap-4">
                <div className="p-4 border border-blue-800 rounded-lg bg-blue-900/20">
                  <div className="text-center mb-2">
                    <div className="text-sm text-blue-400 opacity-70">INTENSITY CONTROL</div>
                  </div>
                  <IntensitySlider 
                    value={selectedGlitch.intensity * 100}
                    onChange={handleIntensityChange}
                    unit="%"
                    color={
                      selectedGlitch.type === 'VISUAL' ? '#39ff14' : 
                      selectedGlitch.type === 'AUDITORY' ? '#ff3977' : 
                      selectedGlitch.type === 'TEMPORAL' ? '#39c8ff' :
                      selectedGlitch.type === 'SPATIAL' ? '#ff9839' : '#a239ff'
                    }
                  />
                </div>
                
                {/* Visualization area */}
                <div className="aspect-square border border-blue-700 rounded overflow-hidden relative cyber-grid">
                  {selectedGlitch.active && (
                    <div className="absolute inset-0 flex items-center justify-center">
                      <div className={`w-1/2 h-1/2 rounded-full opacity-70 neon-pulse`} 
                        style={{
                          backgroundColor: selectedGlitch.type === 'VISUAL' ? '#39ff14' : 
                                        selectedGlitch.type === 'AUDITORY' ? '#ff3977' : 
                                        selectedGlitch.type === 'TEMPORAL' ? '#39c8ff' :
                                        selectedGlitch.type === 'SPATIAL' ? '#ff9839' : '#a239ff',
                          transform: `scale(${0.5 + selectedGlitch.intensity})`
                        }}
                      />
                    </div>
                  )}
                </div>
              </div>
              
              {/* Control buttons */}
              <div className="mt-4 flex justify-center space-x-3">
                <button 
                  className="px-3 py-1 bg-blue-900/50 border border-blue-600 rounded hover:bg-blue-800/50 transition"
                  onClick={() => toggleGlitch(selectedGlitch.id)}
                >
                  {selectedGlitch.active ? 'DEACTIVATE' : 'ACTIVATE'}
                </button>
                {selectedGlitch.active && (
                  <button 
                    className="px-3 py-1 bg-purple-900/50 border border-purple-600 rounded hover:bg-purple-800/50 transition"
                    onClick={() => {
                      setGlitches(prev => prev.map(g => 
                        g.id === selectedGlitch.id 
                          ? {...g, intensity: Math.min(1, g.intensity + 0.1)} 
                          : g
                      ));
                      addConsoleMessage(`Amplifying glitch ${selectedGlitch.id} intensity`);
                    }}
                  >
                    AMPLIFY
                  </button>
                )}
              </div>
            </div>
          ) : (
            <div className="h-64 flex items-center justify-center border border-blue-900/50 rounded bg-blue-950/20">
              <p className="text-blue-400">Select a glitch to control</p>
            </div>
          )}
        </div>
      </div>
      
      {/* Console Output */}
      <div className="mt-6 p-4 border border-blue-800 rounded-lg bg-gradient-to-b from-blue-900/30 to-purple-900/30 cyber-border">
        <h2 className="text-xl mb-3 border-b border-blue-700 pb-1">System Console</h2>
        <div className="h-32 overflow-y-auto font-mono text-xs space-y-1 p-2 bg-black/50 border border-blue-900 rounded">
          {consoleMessages.map((msg, idx) => (
            <div key={idx} className={msg.includes('WARNING') ? 'text-yellow-400' : msg.includes('ERROR') ? 'text-red-400' : 'text-blue-300'}>
              {msg}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default RealityGlitcherUI;