import React from 'react';
import { render, screen } from '@testing-library/react';
import RealTimeData from './RealTimeData';

// Mock canvas functions since Jest doesn't handle canvas well
jest.mock('react', () => {
  const originalReact = jest.requireActual('react');
  return {
    ...originalReact,
    useRef: jest.fn().mockImplementation(() => ({
      current: {
        getContext: jest.fn().mockReturnValue({
          clearRect: jest.fn(),
          beginPath: jest.fn(),
          moveTo: jest.fn(),
          lineTo: jest.fn(),
          stroke: jest.fn(),
          fill: jest.fn(),
          fillRect: jest.fn(),
          fillText: jest.fn(),
          createLinearGradient: jest.fn().mockReturnValue({
            addColorStop: jest.fn()
          }),
          lineWidth: 0,
          strokeStyle: '',
          fillStyle: '',
          shadowBlur: 0,
          shadowColor: '',
          globalCompositeOperation: '',
          lineCap: '',
          lineJoin: ''
        }),
        width: 600,
        height: 130
      }
    }))
  };
});

describe('RealTimeData Component', () => {
  test('renders without crashing', () => {
    // Render with default props
    render(
      <RealTimeData 
        glitches={[]} 
        realityStatus={100} 
        mindMirrorConnected={false} 
      />
    );
    
    // Basic check for sensor labels to confirm it rendered
    expect(screen.getByText(/Neural Activity/i)).toBeInTheDocument();
    expect(screen.getByText(/Perception Shift/i)).toBeInTheDocument();
    expect(screen.getByText(/Reality Coherence/i)).toBeInTheDocument();
  });

  test('changes color when Mind Mirror is connected', () => {
    // Render with Mind Mirror connected
    render(
      <RealTimeData 
        glitches={[]} 
        realityStatus={100} 
        mindMirrorConnected={true} 
      />
    );
    
    // Check for Mind Mirror connected indicator
    expect(screen.getByText(/Mind Mirror Pattern Detected/i)).toBeInTheDocument();
  });

  test('handles glitches properly', () => {
    // Create a test glitch
    const testGlitches = [
      {
        id: 'test-glitch-1',
        type: 'visual',
        intensity: 80,
        stability: 50,
        duration: 10
      }
    ];
    
    // Render with test glitch
    render(
      <RealTimeData 
        glitches={testGlitches} 
        realityStatus={90} 
        mindMirrorConnected={false} 
      />
    );
    
    // Check for anomaly section
    expect(screen.getByText(/Anomalies Detected/i)).toBeInTheDocument();
  });
}); 