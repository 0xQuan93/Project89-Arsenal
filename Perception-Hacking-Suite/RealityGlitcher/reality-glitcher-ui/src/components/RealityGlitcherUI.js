import React, { useState, useEffect, useRef } from 'react';
import { v4 as uuidv4 } from 'uuid';
import '../RealityGlitcher.css';
import RealTimeData from './RealTimeData';
import GlitchCard from './GlitchCard';
import CreateGlitchModal from './CreateGlitchModal';
import GlitchVisualization from './GlitchVisualization';

// Set a fixed maximum height constant for the control panel
const MAX_CONTROL_PANEL_HEIGHT = 1116;

const RealityGlitcherUI = () => {
  // State for reality status
  const [realityStatus, setRealityStatus] = useState({
    coherence: 'STABLE',
    stability: 0.85,
    safetyProtocols: true,
    activeSince: new Date().getTime()
  });

  // State for glitches
  const [glitches, setGlitches] = useState([
    { 
      id: uuidv4(), 
      type: 'VISUAL', 
      intensity: 0.4, 
      duration: 5, 
      complexity: 0.3, 
      persistence: 0.5, 
      active: true, 
      target: 'Visual Field',
      source: 'Manual Creation',
      isAdvanced: false,
      isPersistent: false,
      crossModal: false
    },
    { 
      id: uuidv4(), 
      type: 'AUDITORY', 
      intensity: 0.3, 
      duration: 3, 
      complexity: 0.2, 
      persistence: 0.3, 
      active: false, 
      target: 'Auditory Processing',
      source: 'Manual Creation',
      isAdvanced: false,
      isPersistent: false,
      crossModal: false
    }
  ]);
  
  // State for selected glitch
  const [selectedGlitch, setSelectedGlitch] = useState(null);
  
  // State for modal
  const [modalOpen, setModalOpen] = useState(false);
  
  // State for console messages
  const [consoleMessages, setConsoleMessages] = useState([
    { text: 'Reality Glitcher initialized', timestamp: new Date().getTime(), type: 'info' },
    { text: 'Safety protocols active', timestamp: new Date().getTime(), type: 'success' },
    { text: 'Ready to manipulate perception', timestamp: new Date().getTime(), type: 'info' }
  ]);

  // Mind Mirror Integration State
  const [mindMirrorIntegrated, setMindMirrorIntegrated] = useState(false);
  const [mindMirrorStatus, setMindMirrorStatus] = useState({
    connected: false,
    nodeCount: 0,
    connectionCount: 0,
    lastSyncTime: new Date().getTime() - 3600000 // 1 hour ago
  });
  
  // Refs
  const consoleRef = useRef(null);
  
  // Fullscreen mode state
  const [isFullscreen, setIsFullscreen] = useState(false);
  const appContainerRef = useRef(null);
  
  // Function to add console message
  const addConsoleMessage = (text, type = 'info') => {
    const newMessage = {
      text,
      timestamp: new Date().getTime(),
      type
    };
    
    setConsoleMessages(prev => [newMessage, ...prev]);
    
    // Scroll to bottom of console
    setTimeout(() => {
      if (consoleRef.current) {
        consoleRef.current.scrollTop = 0;
      }
    }, 100);
  };
  
  // Function to toggle safety protocols
  const toggleSafetyProtocols = () => {
    setRealityStatus(prev => ({
      ...prev,
      safetyProtocols: !prev.safetyProtocols
    }));
    
    addConsoleMessage(
      `Safety protocols ${realityStatus.safetyProtocols ? 'deactivated' : 'activated'}`,
      realityStatus.safetyProtocols ? 'warning' : 'success'
    );
  };
  
  // Function to create a new glitch
  const createGlitch = (glitchData) => {
    const newGlitch = {
      id: uuidv4(),
      ...glitchData,
      active: false,
      source: 'Manual Creation'
    };
    
    setGlitches(prev => [...prev, newGlitch]);
    addConsoleMessage(
      `New ${newGlitch.isAdvanced ? 'Advanced ' : ''}${newGlitch.type} glitch created` + 
      `${newGlitch.crossModal ? ' with cross-modal effects' : ''}` +
      `${newGlitch.isPersistent ? ' (Persistent Reality Overlay)' : ''}`, 
      'success'
    );
    setModalOpen(false);
  };
  
  // Function to toggle glitch active state
  const toggleGlitch = (id) => {
    setGlitches(prev => 
      prev.map(glitch => 
        glitch.id === id 
          ? { ...glitch, active: !glitch.active } 
          : glitch
      )
    );
    
    const glitch = glitches.find(g => g.id === id);
    if (glitch) {
      addConsoleMessage(
        `${glitch.isAdvanced ? 'Advanced ' : ''}${glitch.type} glitch ${glitch.id.substring(0, 8)} ${glitch.active ? 'deactivated' : 'activated'}` +
        `${glitch.isPersistent ? ' (Persistent Overlay)' : ''}`,
        'info'
      );
      
      // Update reality status based on active glitches
      updateRealityStatus();
    }
  };
  
  // Function to adjust glitch intensity
  const adjustIntensity = (id, newIntensity) => {
    setGlitches(prev => 
      prev.map(glitch => 
        glitch.id === id 
          ? { ...glitch, intensity: newIntensity } 
          : glitch
      )
    );
    
    // Update reality status based on glitch intensity
    updateRealityStatus();
  };
  
  // Function to amplify glitch (increase intensity by 10%)
  const amplifyGlitch = (id) => {
    setGlitches(prev => 
      prev.map(glitch => 
        glitch.id === id 
          ? { ...glitch, intensity: Math.min(1, glitch.intensity + 0.1) } 
          : glitch
      )
    );
    
    addConsoleMessage(`Amplifying glitch intensity`, 'info');
    updateRealityStatus();
  };
  
  // Function to update reality status based on active glitches
  const updateRealityStatus = () => {
    const activeGlitches = glitches.filter(g => g.active);
    
    // Calculate total impact based on glitch properties
    let totalImpact = 0;
    let hasAdvancedGlitches = false;
    let hasPersistentOverlay = false;
    
    activeGlitches.forEach(glitch => {
      // Basic glitches affect stability less than advanced ones
      const intensityFactor = glitch.intensity * (1 + glitch.complexity * 0.5);
      
      // Advanced glitches have greater impact
      if (glitch.isAdvanced) {
        hasAdvancedGlitches = true;
        totalImpact += intensityFactor * 1.5;
        
        // Cross-modal glitches have even greater impact
        if (glitch.crossModal) {
          totalImpact += intensityFactor * 0.5;
        }
        
        // Track if we have any persistent overlays
        if (glitch.isPersistent) {
          hasPersistentOverlay = true;
        }
      } else {
        totalImpact += intensityFactor;
      }
    });
    
    // Calculate new stability (inversely proportional to total impact)
    // Maximum stability is 0.95, minimum is 0.1
    let newStability = Math.max(0.1, 0.95 - (totalImpact * 0.15));
    
    // Safety protocols help maintain stability
    if (!realityStatus.safetyProtocols) {
      newStability -= 0.2;
    }
    
    // Determine coherence status based on stability
    let newCoherence = 'STABLE';
    if (newStability < 0.4) {
      newCoherence = 'UNSTABLE';
    } else if (newStability < 0.7) {
      newCoherence = 'FLUCTUATING';
    }
    
    // Update reality status
    setRealityStatus(prev => ({
      ...prev,
      stability: newStability,
      coherence: newCoherence,
      hasAdvancedGlitches,
      hasPersistentOverlay
    }));
  };
  
  // Function to integrate with Mind Mirror
  const integrateWithMindMirror = () => {
    if (mindMirrorIntegrated) return;
    
    addConsoleMessage('Initiating connection to Mind Mirror...', 'info');
    
    // Simulate connection process
    setTimeout(() => {
      addConsoleMessage('Neural handshake established with Mind Mirror', 'success');
      
      setMindMirrorStatus({
        connected: true,
        nodeCount: Math.floor(Math.random() * 80) + 40, // 40-120 nodes
        connectionCount: Math.floor(Math.random() * 200) + 100, // 100-300 connections
        lastSyncTime: new Date().getTime()
      });
      
      setMindMirrorIntegrated(true);
      
      // Add a new glitch from Mind Mirror data
      const mindMirrorGlitch = {
        id: uuidv4(),
        type: ['COGNITIVE', 'SYNCHRONISTIC', 'TEMPORAL'][Math.floor(Math.random() * 3)],
        intensity: 0.6 + (Math.random() * 0.3), // 0.6-0.9
        duration: 10,
        complexity: 0.7 + (Math.random() * 0.3), // 0.7-1.0
        persistence: 0.5 + (Math.random() * 0.4), // 0.5-0.9
        active: false,
        target: 'Neural Patterns',
        source: 'Mind Mirror',
        isAdvanced: true,
        isPersistent: Math.random() > 0.7, // 30% chance of persistent
        crossModal: Math.random() > 0.5, // 50% chance of cross-modal
        secondaryTarget: Math.random() > 0.5 ? 'VISUAL' : 'AUDITORY',
        distortionType: ['CONFIRMATION_BIAS', 'EMOTIONAL_REASONING', 'FILTERING'][Math.floor(Math.random() * 3)]
      };
      
      setGlitches(prev => [...prev, mindMirrorGlitch]);
      
      addConsoleMessage('Mind Mirror neural pattern imported as glitch template', 'success');
    }, 2000);
  };
  
  // Function to toggle fullscreen mode
  const toggleFullscreen = () => {
    if (!document.fullscreenElement) {
      if (appContainerRef.current.requestFullscreen) {
        appContainerRef.current.requestFullscreen();
      } else if (appContainerRef.current.webkitRequestFullscreen) { /* Safari */
        appContainerRef.current.webkitRequestFullscreen();
      } else if (appContainerRef.current.msRequestFullscreen) { /* IE11 */
        appContainerRef.current.msRequestFullscreen();
      }
      setIsFullscreen(true);
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      } else if (document.webkitExitFullscreen) { /* Safari */
        document.webkitExitFullscreen();
      } else if (document.msExitFullscreen) { /* IE11 */
        document.msExitFullscreen();
      }
      setIsFullscreen(false);
    }
  };
  
  // Listen for fullscreen change events
  useEffect(() => {
    const handleFullscreenChange = () => {
      setIsFullscreen(!!document.fullscreenElement);
    };
    
    document.addEventListener('fullscreenchange', handleFullscreenChange);
    document.addEventListener('webkitfullscreenchange', handleFullscreenChange);
    document.addEventListener('mozfullscreenchange', handleFullscreenChange);
    document.addEventListener('MSFullscreenChange', handleFullscreenChange);
    
    return () => {
      document.removeEventListener('fullscreenchange', handleFullscreenChange);
      document.removeEventListener('webkitfullscreenchange', handleFullscreenChange);
      document.removeEventListener('mozfullscreenchange', handleFullscreenChange);
      document.removeEventListener('MSFullscreenChange', handleFullscreenChange);
    };
  }, []);
  
  // Function to clear console messages
  const clearConsole = () => {
    setConsoleMessages([{
      text: 'Console cleared',
      timestamp: new Date().getTime(),
      type: 'info'
    }]);
  };
  
  // Function to delete a glitch
  const deleteGlitch = (id) => {
    // Remove the glitch with the specified ID
    setGlitches(prev => prev.filter(glitch => glitch.id !== id));
    
    // If the deleted glitch was selected, clear the selection
    if (selectedGlitch && selectedGlitch.id === id) {
      setSelectedGlitch(null);
    }
    
    // Add a console message
    addConsoleMessage(`Glitch ${id.substring(0, 8)} deleted from reality matrix`, 'info');
    
    // Update reality status after deletion
    updateRealityStatus();
  };
  
  // Get persistent overlay glitches
  const persistentOverlays = glitches.filter(g => g.active && g.isPersistent);
  
  // Generate classes for persistent overlay effects
  const generatePersistentOverlayClasses = () => {
    let classes = '';
    
    persistentOverlays.forEach(glitch => {
      switch(glitch.type) {
        case 'VISUAL':
          classes += ' reality-overlay-visual';
          break;
        case 'AUDITORY':
          classes += ' reality-overlay-auditory';
          break;
        case 'TEMPORAL':
          classes += ' reality-overlay-temporal';
          break;
        case 'SPATIAL':
          classes += ' reality-overlay-spatial';
          break;
        case 'COGNITIVE':
          classes += ' reality-overlay-cognitive';
          if (glitch.distortionType) {
            classes += ` reality-overlay-${glitch.distortionType.toLowerCase()}`;
          }
          break;
        case 'SYNCHRONISTIC':
          classes += ' reality-overlay-synchronistic';
          break;
        default:
          break;
      }
      
      // Add intensity class
      if (glitch.intensity > 0.7) {
        classes += ' reality-overlay-intense';
      } else if (glitch.intensity > 0.4) {
        classes += ' reality-overlay-moderate';
      } else {
        classes += ' reality-overlay-subtle';
      }
      
      // Add cross-modal class
      if (glitch.crossModal && glitch.secondaryTarget) {
        classes += ` reality-overlay-cross-${glitch.secondaryTarget.toLowerCase()}`;
      }
    });
    
    return classes;
  };
  
  // Update effect based on reality status and persistent overlays
  useEffect(() => {
    // Apply persistent overlay effects
    if (persistentOverlays.length > 0) {
      addConsoleMessage(
        `${persistentOverlays.length} persistent overlay${persistentOverlays.length > 1 ? 's' : ''} affecting reality perception`,
        'warning'
      );
    }
  }, [persistentOverlays.length]);
  
  return (
    <div 
      ref={appContainerRef}
      className={`cyber-bg min-h-screen text-blue-300 p-4 md:p-6 transition-all duration-300 ${
        isFullscreen ? 'fullscreen-mode' : ''
      } ${generatePersistentOverlayClasses()}`}
    >
      <div className="max-w-7xl mx-auto">
        <header className="flex flex-col md:flex-row justify-between items-center mb-6 gap-4">
          <div className="text-center md:text-left">
            <h1 className="text-3xl md:text-4xl font-bold text-blue-400 cyber-text-glow">REALITY GLITCHER</h1>
            <p className="text-sm text-blue-500">Perception Manipulation System v0.9.2</p>
          </div>
          
          <div className="flex gap-3">
            {/* Fullscreen button */}
            <button 
              onClick={toggleFullscreen}
              className="cyber-button flex items-center"
              aria-label={isFullscreen ? "Exit fullscreen" : "Enter fullscreen"}
            >
              {isFullscreen ? (
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M22 3H2v18h20V3zM16 17H8" />
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 17H8V5H6zM16 17h2V5h-2" />
                </svg>
              ) : (
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5v-4m0 4h-4m4 0l-5-5" />
                </svg>
              )}
              <span className="ml-2 hidden sm:inline">{isFullscreen ? "Exit Fullscreen" : "Fullscreen"}</span>
            </button>
            
            <button 
              onClick={toggleSafetyProtocols}
              className={`cyber-button ${!realityStatus.safetyProtocols ? 'bg-red-900/50 border-red-700' : ''}`}
            >
              {realityStatus.safetyProtocols ? 'Disable' : 'Enable'} <span className="hidden sm:inline">Safety</span>
            </button>
          </div>
        </header>

        {/* Main content grid */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Left column - Controls and Status */}
          <div className="lg:col-span-1 space-y-6">
            {/* Reality status panel */}
            <div className="p-4 border border-blue-800 rounded-lg bg-gradient-to-b from-blue-900/30 to-purple-900/30 cyber-border">
              <h2 className="text-xl mb-3 border-b border-blue-700 pb-1">Reality Status</h2>
              
              <div className="space-y-4">
                {/* Status indicators */}
                <div className="flex justify-between items-center">
                  <div className="text-sm">Coherence:</div>
                  <div className={`text-sm font-bold ${
                    realityStatus.coherence === 'UNSTABLE' ? 'text-red-400' : 
                    realityStatus.coherence === 'FLUCTUATING' ? 'text-yellow-400' : 
                    'text-green-400'
                  }`}>
                    {realityStatus.coherence}
                  </div>
                </div>
                
                {/* Safety status */}
                <div className="flex justify-between items-center">
                  <div className="text-sm">Safety Protocols:</div>
                  <div className={`text-sm font-bold ${realityStatus.safetyProtocols ? 'text-green-400' : 'text-red-400'}`}>
                    {realityStatus.safetyProtocols ? 'ACTIVE' : 'DISABLED'}
                  </div>
                </div>
                
                {/* Persistent overlay status - new! */}
                <div className="flex justify-between items-center">
                  <div className="text-sm">Persistent Overlays:</div>
                  <div className={`text-sm font-bold ${persistentOverlays.length > 0 ? 'text-purple-400 animate-pulse' : 'text-gray-400'}`}>
                    {persistentOverlays.length > 0 ? `${persistentOverlays.length} ACTIVE` : 'NONE'}
                  </div>
                </div>
                
                {/* Advanced glitches status - new! */}
                {glitches.some(g => g.active && g.isAdvanced) && (
                  <div className="flex justify-between items-center">
                    <div className="text-sm">Advanced Glitches:</div>
                    <div className="text-sm font-bold text-cyan-400">
                      {glitches.filter(g => g.active && g.isAdvanced).length} ACTIVE
                    </div>
                  </div>
                )}
                
                {/* Time active */}
                <div className="flex justify-between items-center">
                  <div className="text-sm">Active Since:</div>
                  <div className="text-sm">
                    {new Date(realityStatus.activeSince).toLocaleTimeString()}
                  </div>
                </div>
                
                {/* Stability bar */}
                <div>
                  <div className="flex justify-between items-center mb-1">
                    <div className="text-sm">Reality Stability:</div>
                    <div className="text-sm">{(realityStatus.stability * 100).toFixed(1)}%</div>
                  </div>
                  <div className="h-2 w-full bg-blue-900/50 rounded overflow-hidden">
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
                
                {/* Mind Mirror Integration Status */}
                <div className="mt-5 border-t border-blue-800 pt-3">
                  <div className="flex justify-between items-center mb-2">
                    <div className="text-sm text-blue-400">Mind Mirror Integration:</div>
                    <div className={`text-sm font-bold ${mindMirrorStatus.connected ? 'text-purple-400' : 'text-gray-500'}`}>
                      {mindMirrorStatus.connected ? 'CONNECTED' : 'DISCONNECTED'}
                    </div>
                  </div>
                  
                  {mindMirrorStatus.connected && (
                    <div className="grid grid-cols-2 gap-3 text-xs mt-2">
                      <div>
                        <span className="text-purple-400">Neural Nodes:</span> {mindMirrorStatus.nodeCount}
                      </div>
                      <div>
                        <span className="text-purple-400">Connections:</span> {mindMirrorStatus.connectionCount}
                      </div>
                      <div className="col-span-2">
                        <span className="text-purple-400">Last Sync:</span> {new Date(mindMirrorStatus.lastSyncTime).toLocaleTimeString()}
                      </div>
                    </div>
                  )}
                  
                  <button 
                    className={`mt-2 w-full py-2 rounded text-center ${
                      mindMirrorIntegrated 
                        ? 'bg-purple-800/50 border border-purple-600 text-purple-200' 
                        : 'bg-blue-800/50 border border-blue-600 hover:bg-blue-700/50'
                    }`}
                    onClick={integrateWithMindMirror}
                    disabled={mindMirrorIntegrated}
                  >
                    {mindMirrorIntegrated ? 'NEURAL LINK ACTIVE' : 'CONNECT TO MIND MIRROR'}
                  </button>
                </div>
              </div>
            </div>
            
            {/* Console */}
            <div className="p-4 border border-blue-800 rounded-lg bg-gradient-to-b from-blue-900/30 to-purple-900/30 cyber-border">
              <div className="flex justify-between items-center mb-3 border-b border-blue-700 pb-1">
                <h2 className="text-xl">System Console</h2>
                <button 
                  onClick={clearConsole}
                  className="text-xs text-blue-400 hover:text-blue-300"
                >
                  Clear
                </button>
              </div>
              
              <div 
                className="h-36 md:h-48 overflow-y-auto scrollbar terminal-bg p-2 font-mono text-xs"
                ref={consoleRef}
              >
                {consoleMessages.map((msg, i) => (
                  <div key={i} className={`mb-1 ${
                    msg.type === 'error' ? 'text-red-400' : 
                    msg.type === 'success' ? 'text-green-400' : 
                    msg.type === 'warning' ? 'text-yellow-400' : 
                    'text-blue-300'
                  }`}>
                    &gt; [{new Date(msg.timestamp).toLocaleTimeString()}] {msg.text}
                  </div>
                ))}
              </div>
            </div>
          </div>
          
          {/* Middle and Right columns - Visualization and Glitches */}
          <div className="lg:col-span-2 space-y-6">
            {/* Real-time Data Visualization */}
            <div className="p-4 border border-blue-800 rounded-lg bg-gradient-to-b from-blue-900/30 to-purple-900/30 cyber-border">
              <h2 className="text-xl mb-3 border-b border-blue-700 pb-1">Quantum Fluctuation Analysis</h2>
              <RealTimeData 
                glitches={glitches} 
                realityStatus={realityStatus}
                mindMirrorConnected={mindMirrorStatus.connected}
              />
            </div>
            
            {/* Glitch Management */}
            <div className="p-4 border border-blue-800 rounded-lg bg-gradient-to-b from-blue-900/30 to-purple-900/30 cyber-border">
              <div className="flex justify-between items-center mb-3 border-b border-blue-700 pb-1">
                <h2 className="text-xl">Reality Manipulations</h2>
                <button 
                  onClick={() => setModalOpen(true)}
                  className="cyber-button-primary text-sm"
                >
                  Create New
                </button>
              </div>
              
              {/* Advanced Glitches Section - new! */}
              {glitches.some(g => g.isAdvanced) && (
                <div className="mb-4">
                  <h3 className="text-lg text-purple-300 mb-2 flex items-center">
                    <span className="inline-block w-2 h-2 rounded-full bg-purple-500 mr-2"></span>
                    Advanced Glitches
                  </h3>
                  
                  <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-1 xl:grid-cols-2 gap-4 mb-4">
                    {glitches.filter(g => g.isAdvanced).map((glitch) => (
                      <GlitchCard 
                        key={glitch.id}
                        glitch={glitch}
                        selected={selectedGlitch?.id === glitch.id}
                        onSelect={() => setSelectedGlitch(glitch)}
                        onToggle={() => toggleGlitch(glitch.id)}
                        onAdjustIntensity={(newIntensity) => adjustIntensity(glitch.id, newIntensity)}
                        onDelete={() => deleteGlitch(glitch.id)}
                        onAmplify={() => amplifyGlitch(glitch.id)}
                      />
                    ))}
                  </div>
                </div>
              )}
              
              {/* Standard Glitches */}
              <div className="mb-4">
                {glitches.some(g => g.isAdvanced) && (
                  <h3 className="text-lg text-blue-300 mb-2 flex items-center">
                    <span className="inline-block w-2 h-2 rounded-full bg-blue-500 mr-2"></span>
                    Standard Glitches
                  </h3>
                )}
                
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-1 xl:grid-cols-2 gap-4 mb-4">
                  {glitches.filter(g => !g.isAdvanced).map((glitch) => (
                    <GlitchCard 
                      key={glitch.id}
                      glitch={glitch}
                      selected={selectedGlitch?.id === glitch.id}
                      onSelect={() => setSelectedGlitch(glitch)}
                      onToggle={() => toggleGlitch(glitch.id)}
                      onAdjustIntensity={(newIntensity) => adjustIntensity(glitch.id, newIntensity)}
                      onDelete={() => deleteGlitch(glitch.id)}
                      onAmplify={() => amplifyGlitch(glitch.id)}
                    />
                  ))}
                </div>
                
                {glitches.length === 0 && (
                  <div className="col-span-full text-center py-6 text-blue-400">
                    No active glitches. Create one to begin manipulating reality.
                  </div>
                )}
              </div>
              
              {/* Selected Glitch Visualization */}
              <div className="border-t border-blue-800 pt-4">
                <h3 className="text-lg mb-2">Glitch Visualization</h3>
                <div className="glitch-visualization">
                  <GlitchVisualization glitch={selectedGlitch} />
                </div>
              </div>
            </div>
          </div>
        </div>
        
        {/* Footer */}
        <footer className="mt-8 text-center text-xs text-blue-500 border-t border-blue-900 pt-4">
          <p>PROJECT89 REALITY GLITCHER v0.9.2 | Perception Manipulation System | Neural Link Protocol Active</p>
          <p className="mt-1">Warning: Unauthorized reality manipulation may lead to cognitive dissonance</p>
        </footer>
      </div>
      
      {/* Create Glitch Modal */}
      {modalOpen && (
        <CreateGlitchModal 
          isOpen={modalOpen}
          onClose={() => setModalOpen(false)}
          onCreateGlitch={createGlitch}
        />
      )}
    </div>
  );
};

export default RealityGlitcherUI;