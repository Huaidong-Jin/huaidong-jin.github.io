#!/usr/bin/env python3
"""
Generate enhanced professional SVG charts with modern design elements
"""
from pathlib import Path

def create_market_structure_svg():
    """Create enhanced market value structure with gradients and shadows"""
    svg = '''<svg viewBox="0 0 1000 650" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%);">
  <defs>
    <!-- Gradients -->
    <linearGradient id="globalGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#2563eb;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#1e40af;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="appGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#10b981;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#059669;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="servicesGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#f59e0b;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#d97706;stop-opacity:1" />
    </linearGradient>
    <!-- Shadow filter -->
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="3"/>
      <feOffset dx="2" dy="2" result="offsetblur"/>
      <feComponentTransfer>
        <feFuncA type="linear" slope="0.3"/>
      </feComponentTransfer>
      <feMerge>
        <feMergeNode/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <!-- Arrow marker -->
    <marker id="arrowhead" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto">
      <polygon points="0 0, 12 6, 0 12" fill="#1e40af"/>
    </marker>
  </defs>
  
  <!-- Title -->
  <text x="500" y="40" text-anchor="middle" fill="#1e293b" font-size="24" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Market Value Structure</text>
  
  <!-- Global Market -->
  <g filter="url(#shadow)">
    <rect x="250" y="80" width="500" height="90" rx="12" fill="url(#globalGrad)" stroke="#1e3a8a" stroke-width="2"/>
    <circle cx="270" cy="105" r="8" fill="rgba(255,255,255,0.3)"/>
    <text x="500" y="115" text-anchor="middle" fill="white" font-size="22" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Global Market Opportunity</text>
    <text x="500" y="145" text-anchor="middle" fill="rgba(255,255,255,0.95)" font-size="16" font-weight="500">$0.9 - 1.1 Trillion (Services)</text>
  </g>
  
  <!-- Application Layer -->
  <g filter="url(#shadow)">
    <rect x="80" y="240" width="380" height="130" rx="12" fill="url(#appGrad)" stroke="#047857" stroke-width="2"/>
    <circle cx="100" cy="265" r="8" fill="rgba(255,255,255,0.3)"/>
    <text x="270" y="280" text-anchor="middle" fill="white" font-size="20" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Application Layer</text>
    <text x="270" y="310" text-anchor="middle" fill="rgba(255,255,255,0.95)" font-size="18" font-weight="600">~$1 Trillion (US)</text>
    <text x="270" y="340" text-anchor="middle" fill="rgba(255,255,255,0.9)" font-size="13">Software Products &amp; Platforms</text>
  </g>
  
  <!-- Services Layer -->
  <g filter="url(#shadow)">
    <rect x="540" y="240" width="380" height="130" rx="12" fill="url(#servicesGrad)" stroke="#b45309" stroke-width="2"/>
    <circle cx="560" cy="265" r="8" fill="rgba(255,255,255,0.3)"/>
    <text x="730" y="280" text-anchor="middle" fill="white" font-size="20" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Services Layer</text>
    <text x="730" y="310" text-anchor="middle" fill="rgba(255,255,255,0.95)" font-size="18" font-weight="600">$350-450B (US)</text>
    <text x="730" y="335" text-anchor="middle" fill="rgba(255,255,255,0.95)" font-size="16" font-weight="600">$0.9-1.1T (Global)</text>
    <text x="730" y="355" text-anchor="middle" fill="rgba(255,255,255,0.9)" font-size="13">Implementation &amp; Support</text>
  </g>
  
  <!-- Arrows with glow effect -->
  <path d="M 500 170 L 270 240" stroke="#1e40af" stroke-width="4" fill="none" marker-end="url(#arrowhead)" opacity="0.8"/>
  <path d="M 500 170 L 730 240" stroke="#1e40af" stroke-width="4" fill="none" marker-end="url(#arrowhead)" opacity="0.8"/>
  
  <!-- Ratio badge -->
  <rect x="400" y="410" width="200" height="45" rx="8" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="2"/>
  <text x="500" y="435" text-anchor="middle" fill="#475569" font-size="14" font-weight="600">Services/App Ratio</text>
  <text x="500" y="455" text-anchor="middle" fill="#1e40af" font-size="16" font-weight="700">0.70-0.80x</text>
  
  <!-- Current IT Services comparison -->
  <rect x="80" y="490" width="840" height="60" rx="10" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2"/>
  <text x="100" y="515" fill="#64748b" font-size="13" font-weight="600">COMPARISON:</text>
  <text x="500" y="535" text-anchor="middle" fill="#334155" font-size="16" font-weight="700">Current IT Services (US): $320B</text>
  <text x="500" y="555" text-anchor="middle" fill="#64748b" font-size="13" font-style="italic">Services opportunity exceeds current IT services spending</text>
</svg>'''
    return svg

def create_labor_augmentation_svg():
    """Create enhanced labor augmentation chart with better design"""
    svg = '''<svg viewBox="0 0 1100 750" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);">
  <defs>
    <!-- Gradients for bars -->
    <linearGradient id="highGrad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#2563eb;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#3b82f6;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="highGrad2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#3b82f6;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#60a5fa;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="mediumGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#f59e0b;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#fbbf24;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="lowGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#6b7280;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#9ca3af;stop-opacity:1" />
    </linearGradient>
    <filter id="barShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="2"/>
      <feOffset dx="1" dy="2" result="offsetblur"/>
      <feComponentTransfer>
        <feFuncA type="linear" slope="0.25"/>
      </feComponentTransfer>
      <feMerge>
        <feMergeNode/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <!-- Title -->
  <text x="550" y="45" text-anchor="middle" fill="#1e293b" font-size="26" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Labor Augmentation Potential</text>
  <text x="550" y="70" text-anchor="middle" fill="#64748b" font-size="14" font-weight="500">By Role Category</text>
  
  <!-- Background grid -->
  <g opacity="0.1">
    <line x1="300" y1="100" x2="300" y2="680" stroke="#475569" stroke-width="1"/>
    <line x1="550" y1="100" x2="550" y2="680" stroke="#475569" stroke-width="1"/>
    <line x1="800" y1="100" x2="800" y2="680" stroke="#475569" stroke-width="1"/>
  </g>
  
  <!-- High Augmentation Section -->
  <rect x="40" y="95" width="1020" height="220" rx="10" fill="#eff6ff" stroke="#bfdbfe" stroke-width="2" opacity="0.5"/>
  <text x="60" y="120" fill="#1e40af" font-size="16" font-weight="700" font-family="system-ui, -apple-system, sans-serif">High Augmentation (85-90%)</text>
  
  <g filter="url(#barShadow)">
    <rect x="300" y="145" width="600" height="38" rx="6" fill="url(#highGrad1)"/>
    <text x="285" y="168" text-anchor="end" fill="#1e293b" font-size="13" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Customer Service Reps</text>
    <text x="920" y="168" fill="white" font-size="14" font-weight="700">90%</text>
    
    <rect x="300" y="195" width="584" height="38" rx="6" fill="url(#highGrad2)"/>
    <text x="285" y="218" text-anchor="end" fill="#1e293b" font-size="13" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Data Analysts</text>
    <text x="904" y="218" fill="white" font-size="14" font-weight="700">88%</text>
    
    <rect x="300" y="245" width="572" height="38" rx="6" fill="url(#highGrad2)"/>
    <text x="285" y="268" text-anchor="end" fill="#1e293b" font-size="13" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Software Engineers</text>
    <text x="892" y="268" fill="white" font-size="14" font-weight="700">87%</text>
    
    <rect x="300" y="295" width="592" height="38" rx="6" fill="url(#highGrad1)"/>
    <text x="285" y="318" text-anchor="end" fill="#1e293b" font-size="13" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Compliance Officers</text>
    <text x="912" y="318" fill="white" font-size="14" font-weight="700">89%</text>
  </g>
  
  <!-- Medium Augmentation Section -->
  <rect x="40" y="340" width="1020" height="160" rx="10" fill="#fffbeb" stroke="#fde68a" stroke-width="2" opacity="0.5"/>
  <text x="60" y="365" fill="#d97706" font-size="16" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Medium Augmentation (40-50%)</text>
  
  <g filter="url(#barShadow)">
    <rect x="456" y="390" width="456" height="38" rx="6" fill="url(#mediumGrad)"/>
    <text x="285" y="413" text-anchor="end" fill="#1e293b" font-size="13" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Marketing Managers</text>
    <text x="932" y="413" fill="white" font-size="14" font-weight="700">48%</text>
    
    <rect x="450" y="440" width="450" height="38" rx="6" fill="url(#mediumGrad)"/>
    <text x="285" y="463" text-anchor="end" fill="#1e293b" font-size="13" font-weight="600" font-family="system-ui, -apple-system, sans-serif">HR Coordinators</text>
    <text x="920" y="463" fill="white" font-size="14" font-weight="700">45%</text>
    
    <rect x="450" y="490" width="500" height="38" rx="6" fill="url(#mediumGrad)"/>
    <text x="285" y="513" text-anchor="end" fill="#1e293b" font-size="13" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Financial Analysts</text>
    <text x="970" y="513" fill="white" font-size="14" font-weight="700">50%</text>
  </g>
  
  <!-- Low Augmentation Section -->
  <rect x="40" y="520" width="1020" height="120" rx="10" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2" opacity="0.5"/>
  <text x="60" y="545" fill="#475569" font-size="16" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Low Augmentation (&lt;20%)</text>
  
  <g filter="url(#barShadow)">
    <rect x="162" y="570" width="180" height="38" rx="6" fill="url(#lowGrad)"/>
    <text x="285" y="593" text-anchor="end" fill="#1e293b" font-size="13" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Strategic Planners</text>
    <text x="362" y="593" fill="white" font-size="14" font-weight="700">18%</text>
    
    <rect x="108" y="620" width="120" height="38" rx="6" fill="url(#lowGrad)"/>
    <text x="285" y="643" text-anchor="end" fill="#1e293b" font-size="13" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Executive Leadership</text>
    <text x="248" y="643" fill="white" font-size="14" font-weight="700">12%</text>
  </g>
  
  <!-- X-axis with scale -->
  <line x1="300" y1="680" x2="900" y2="680" stroke="#334155" stroke-width="3"/>
  <line x1="300" y1="675" x2="300" y2="685" stroke="#334155" stroke-width="2"/>
  <line x1="600" y1="675" x2="600" y2="685" stroke="#334155" stroke-width="2"/>
  <line x1="900" y1="675" x2="900" y2="685" stroke="#334155" stroke-width="2"/>
  <text x="300" y="700" text-anchor="middle" fill="#64748b" font-size="12" font-weight="600">0%</text>
  <text x="600" y="700" text-anchor="middle" fill="#64748b" font-size="12" font-weight="600">50%</text>
  <text x="900" y="700" text-anchor="middle" fill="#64748b" font-size="12" font-weight="600">100%</text>
  
  <!-- Footer -->
  <text x="550" y="735" text-anchor="middle" fill="#94a3b8" font-size="11" font-style="italic">Based on analysis of 150 job roles with 5 key criteria</text>
</svg>'''
    return svg

def create_evolution_timeline_svg():
    """Create enhanced evolution timeline with modern design"""
    svg = '''<svg viewBox="0 0 1100 520" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%);">
  <defs>
    <linearGradient id="rpaGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#94a3b8;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#64748b;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="genaiGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#60a5fa;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#3b82f6;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="agenticGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#10b981;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#059669;stop-opacity:1" />
    </linearGradient>
    <filter id="cardShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="4"/>
      <feOffset dx="3" dy="4" result="offsetblur"/>
      <feComponentTransfer>
        <feFuncA type="linear" slope="0.35"/>
      </feComponentTransfer>
      <feMerge>
        <feMergeNode/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <marker id="arrow" markerWidth="14" markerHeight="14" refX="12" refY="7" orient="auto">
      <polygon points="0 0, 14 7, 0 14" fill="#475569"/>
    </marker>
  </defs>
  
  <!-- Title -->
  <text x="550" y="45" text-anchor="middle" fill="#1e293b" font-size="28" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Automation Evolution</text>
  <text x="550" y="70" text-anchor="middle" fill="#64748b" font-size="15" font-weight="500" font-style="italic">Convergence &amp; Evolution</text>
  
  <!-- Timeline path -->
  <path d="M 120 200 L 980 200" stroke="#cbd5e1" stroke-width="4" stroke-dasharray="8,4" opacity="0.6"/>
  
  <!-- RPA Era -->
  <g filter="url(#cardShadow)">
    <rect x="80" y="130" width="240" height="150" rx="14" fill="url(#rpaGrad)" stroke="#475569" stroke-width="2"/>
    <circle cx="105" cy="155" r="10" fill="rgba(255,255,255,0.4)"/>
    <text x="200" y="165" text-anchor="middle" fill="white" font-size="22" font-weight="700" font-family="system-ui, -apple-system, sans-serif">RPA Era</text>
    <text x="200" y="190" text-anchor="middle" fill="rgba(255,255,255,0.9)" font-size="14" font-weight="500">(2010s)</text>
    <text x="200" y="220" text-anchor="middle" fill="white" font-size="15" font-weight="600" font-style="italic">Scripted Tasks</text>
    <text x="200" y="245" text-anchor="middle" fill="rgba(255,255,255,0.95)" font-size="15" font-weight="600" font-style="italic">Brittle Static</text>
  </g>
  
  <!-- Gen AI Era -->
  <g filter="url(#cardShadow)">
    <rect x="430" y="130" width="240" height="150" rx="14" fill="url(#genaiGrad)" stroke="#2563eb" stroke-width="2"/>
    <circle cx="455" cy="155" r="10" fill="rgba(255,255,255,0.4)"/>
    <text x="550" y="165" text-anchor="middle" fill="white" font-size="22" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Gen AI Era</text>
    <text x="550" y="190" text-anchor="middle" fill="rgba(255,255,255,0.9)" font-size="14" font-weight="500">(2020s)</text>
    <text x="550" y="220" text-anchor="middle" fill="white" font-size="15" font-weight="600" font-style="italic">Isolated Assistants</text>
    <text x="550" y="245" text-anchor="middle" fill="rgba(255,255,255,0.95)" font-size="15" font-weight="600" font-style="italic">Human-Dependent</text>
  </g>
  
  <!-- Agentic AI Era -->
  <g filter="url(#cardShadow)">
    <rect x="780" y="130" width="240" height="150" rx="14" fill="url(#agenticGrad)" stroke="#047857" stroke-width="2"/>
    <circle cx="805" cy="155" r="10" fill="rgba(255,255,255,0.4)"/>
    <text x="900" y="165" text-anchor="middle" fill="white" font-size="22" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Agentic AI</text>
    <text x="900" y="190" text-anchor="middle" fill="rgba(255,255,255,0.9)" font-size="14" font-weight="500">(2025+)</text>
    <text x="900" y="220" text-anchor="middle" fill="white" font-size="15" font-weight="600" font-style="italic">Autonomous Systems</text>
    <text x="900" y="245" text-anchor="middle" fill="rgba(255,255,255,0.95)" font-size="15" font-weight="600" font-style="italic">Self-Driven Adaptive</text>
  </g>
  
  <!-- Arrows -->
  <path d="M 320 205 L 430 205" stroke="#475569" stroke-width="5" fill="none" marker-end="url(#arrow)" opacity="0.8"/>
  <path d="M 670 205 L 780 205" stroke="#475569" stroke-width="5" fill="none" marker-end="url(#arrow)" opacity="0.8"/>
  
  <!-- Key Capabilities Section -->
  <rect x="80" y="310" width="940" height="180" rx="14" fill="#fefce8" stroke="#fde047" stroke-width="2" opacity="0.8"/>
  <text x="550" y="340" text-anchor="middle" fill="#713f12" font-size="18" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Key Capabilities</text>
  
  <rect x="110" y="360" width="260" height="110" rx="10" fill="#eff6ff" stroke="#bfdbfe" stroke-width="2"/>
  <text x="240" y="385" text-anchor="middle" fill="#1e40af" font-size="16" font-weight="700" font-family="system-ui, -apple-system, sans-serif">RPA</text>
  <text x="240" y="410" text-anchor="middle" fill="#2563eb" font-size="13" font-weight="500">Script execution</text>
  <text x="240" y="430" text-anchor="middle" fill="#2563eb" font-size="13" font-weight="500">Rule-based</text>
  <text x="240" y="450" text-anchor="middle" fill="#3b82f6" font-size="12">Automated workflows</text>
  
  <rect x="410" y="360" width="260" height="110" rx="10" fill="#dbeafe" stroke="#93c5fd" stroke-width="2"/>
  <text x="540" y="385" text-anchor="middle" fill="#1e40af" font-size="16" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Gen AI</text>
  <text x="540" y="410" text-anchor="middle" fill="#2563eb" font-size="13" font-weight="500">Content creation</text>
  <text x="540" y="430" text-anchor="middle" fill="#2563eb" font-size="13" font-weight="500">Analysis &amp; insights</text>
  <text x="540" y="450" text-anchor="middle" fill="#3b82f6" font-size="12">Intelligent assistants</text>
  
  <rect x="710" y="360" width="260" height="110" rx="10" fill="#d1fae5" stroke="#86efac" stroke-width="2"/>
  <text x="840" y="385" text-anchor="middle" fill="#065f46" font-size="16" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Agentic</text>
  <text x="840" y="410" text-anchor="middle" fill="#047857" font-size="13" font-weight="500">Reasoning + Action</text>
  <text x="840" y="430" text-anchor="middle" fill="#047857" font-size="13" font-weight="500">+ Adaptation</text>
  <text x="840" y="450" text-anchor="middle" fill="#10b981" font-size="12">Autonomous decision-making</text>
</svg>'''
    return svg

def create_adoption_timeline_svg():
    """Create enhanced adoption timeline"""
    svg = '''<svg viewBox="0 0 1200 550" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; background: linear-gradient(135deg, #f0fdf4 0%, #ffffff 100%);">
  <defs>
    <linearGradient id="accelGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#10b981;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#059669;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="consGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#6b7280;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#4b5563;stop-opacity:1" />
    </linearGradient>
    <filter id="timelineShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="3"/>
      <feOffset dx="2" dy="3" result="offsetblur"/>
      <feComponentTransfer>
        <feFuncA type="linear" slope="0.3"/>
      </feComponentTransfer>
      <feMerge>
        <feMergeNode/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <marker id="arrowGreen" markerWidth="14" markerHeight="14" refX="12" refY="7" orient="auto">
      <polygon points="0 0, 14 7, 0 14" fill="#10b981"/>
    </marker>
    <marker id="arrowGray" markerWidth="14" markerHeight="14" refX="12" refY="7" orient="auto">
      <polygon points="0 0, 14 7, 0 14" fill="#6b7280"/>
    </marker>
  </defs>
  
  <!-- Title -->
  <text x="600" y="45" text-anchor="middle" fill="#065f46" font-size="26" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Projected Adoption Timeline</text>
  <text x="600" y="72" text-anchor="middle" fill="#64748b" font-size="15" font-weight="500">Market Realization ($300-600B Global Services)</text>
  
  <!-- Timeline base -->
  <line x1="120" y1="380" x2="1080" y2="380" stroke="#cbd5e1" stroke-width="5" opacity="0.4"/>
  
  <!-- 2025 Current State -->
  <g filter="url(#timelineShadow)">
    <circle cx="240" cy="380" r="15" fill="#10b981" stroke="white" stroke-width="3"/>
    <line x1="240" y1="340" x2="240" y2="420" stroke="#10b981" stroke-width="3"/>
  </g>
  <text x="240" y="325" text-anchor="middle" fill="#334155" font-size="16" font-weight="700" font-family="system-ui, -apple-system, sans-serif">2025</text>
  <text x="240" y="305" text-anchor="middle" fill="#64748b" font-size="13" font-weight="500">Current State</text>
  
  <!-- Acceleration factors -->
  <rect x="60" y="110" width="360" height="160" rx="12" fill="#dbeafe" stroke="#3b82f6" stroke-width="2"/>
  <text x="240" y="135" text-anchor="middle" fill="#1e40af" font-size="15" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Key Acceleration Factors</text>
  <text x="80" y="165" fill="#1e3a8a" font-size="12" font-weight="500">✓ 90%+ enterprises interested</text>
  <text x="80" y="190" fill="#1e3a8a" font-size="12" font-weight="500">✓ Major vendors prioritizing agentic AI</text>
  <text x="80" y="215" fill="#1e3a8a" font-size="12" font-weight="500">✓ Early implementations showing ROI</text>
  <text x="80" y="240" fill="#1e3a8a" font-size="12" font-weight="500">✓ Compressed adoption curve expected</text>
  <text x="80" y="265" fill="#1e3a8a" font-size="12" font-weight="500">✓ Strong enterprise demand signals</text>
  
  <!-- Accelerated Timeline -->
  <g filter="url(#timelineShadow)">
    <rect x="660" y="160" width="420" height="120" rx="12" fill="url(#accelGrad)" stroke="#047857" stroke-width="2"/>
    <circle cx="680" cy="180" r="8" fill="rgba(255,255,255,0.4)"/>
    <text x="870" y="195" text-anchor="middle" fill="white" font-size="18" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Accelerated Timeline</text>
    <text x="870" y="220" text-anchor="middle" fill="rgba(255,255,255,0.95)" font-size="16" font-weight="600">(More Likely)</text>
    <text x="870" y="250" text-anchor="middle" fill="white" font-size="20" font-weight="700">$300-600B by 2030-2035</text>
    <text x="870" y="275" text-anchor="middle" fill="rgba(255,255,255,0.9)" font-size="13">Early adoption signals strong</text>
  </g>
  
  <!-- Conservative Timeline -->
  <g filter="url(#timelineShadow)">
    <rect x="660" y="300" width="420" height="120" rx="12" fill="url(#consGrad)" stroke="#374151" stroke-width="2"/>
    <circle cx="680" cy="320" r="8" fill="rgba(255,255,255,0.4)"/>
    <text x="870" y="335" text-anchor="middle" fill="white" font-size="18" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Conservative Timeline</text>
    <text x="870" y="360" text-anchor="middle" fill="white" font-size="20" font-weight="700">$300-600B by 2035-2040</text>
    <text x="870" y="385" text-anchor="middle" fill="rgba(255,255,255,0.9)" font-size="13">Following cloud computing path</text>
    <text x="870" y="405" text-anchor="middle" fill="rgba(255,255,255,0.85)" font-size="12">Gradual market penetration</text>
  </g>
  
  <!-- Arrows -->
  <path d="M 240 380 L 840 220" stroke="#10b981" stroke-width="5" fill="none" marker-end="url(#arrowGreen)" opacity="0.9"/>
  <path d="M 240 380 L 840 360" stroke="#6b7280" stroke-width="5" fill="none" marker-end="url(#arrowGray)" opacity="0.9"/>
  
  <!-- Milestone markers -->
  <circle cx="840" cy="220" r="18" fill="#10b981" stroke="white" stroke-width="4" filter="url(#timelineShadow)"/>
  <circle cx="840" cy="360" r="18" fill="#6b7280" stroke="white" stroke-width="4" filter="url(#timelineShadow)"/>
  
  <!-- Year labels -->
  <text x="720" y="440" text-anchor="middle" fill="#64748b" font-size="13" font-weight="600">2030-2035</text>
  <text x="960" y="440" text-anchor="middle" fill="#64748b" font-size="13" font-weight="600">2035-2040</text>
</svg>'''
    return svg

def create_industry_impact_svg():
    """Create enhanced industry impact matrix"""
    svg = '''<svg viewBox="0 0 1100 650" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; background: linear-gradient(135deg, #fff7ed 0%, #ffffff 100%);">
  <defs>
    <linearGradient id="veryHighGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#dc2626;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ef4444;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="highGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#f59e0b;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#fbbf24;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="medHighGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#eab308;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#fde047;stop-opacity:1" />
    </linearGradient>
    <filter id="impactShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="3"/>
      <feOffset dx="2" dy="3" result="offsetblur"/>
      <feComponentTransfer>
        <feFuncA type="linear" slope="0.35"/>
      </feComponentTransfer>
      <feMerge>
        <feMergeNode/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <!-- Title -->
  <text x="550" y="45" text-anchor="middle" fill="#92400e" font-size="26" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Industry Impact Matrix</text>
  <text x="550" y="70" text-anchor="middle" fill="#78716c" font-size="14" font-weight="500">Agentic AI Impact Across Key Industries</text>
  
  <!-- Insurance - Very High -->
  <g filter="url(#impactShadow)">
    <rect x="80" y="100" width="940" height="95" rx="12" fill="url(#veryHighGrad)" stroke="#991b1b" stroke-width="2"/>
    <circle cx="110" cy="130" r="12" fill="rgba(255,255,255,0.4)"/>
    <text x="130" y="135" fill="white" font-size="20" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Insurance</text>
    <text x="130" y="160" fill="rgba(255,255,255,0.95)" font-size="14" font-weight="500" font-style="italic">Claims adjudication automation</text>
    <circle cx="980" cy="147" r="8" fill="rgba(255,255,255,0.3)"/>
    <text x="940" y="150" text-anchor="end" fill="white" font-size="16" font-weight="700">🔴 Very High Impact</text>
  </g>
  
  <!-- Manufacturing - High -->
  <g filter="url(#impactShadow)">
    <rect x="80" y="210" width="940" height="95" rx="12" fill="url(#highGrad)" stroke="#d97706" stroke-width="2"/>
    <circle cx="110" cy="240" r="12" fill="rgba(255,255,255,0.4)"/>
    <text x="130" y="245" fill="white" font-size="20" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Manufacturing</text>
    <text x="130" y="270" fill="rgba(255,255,255,0.95)" font-size="14" font-weight="500" font-style="italic">Inventory &amp; supply chain management</text>
    <circle cx="980" cy="257" r="8" fill="rgba(255,255,255,0.3)"/>
    <text x="940" y="260" text-anchor="end" fill="white" font-size="16" font-weight="700">🟠 High Impact</text>
  </g>
  
  <!-- Retail - High -->
  <g filter="url(#impactShadow)">
    <rect x="80" y="320" width="940" height="95" rx="12" fill="url(#highGrad)" stroke="#d97706" stroke-width="2"/>
    <circle cx="110" cy="350" r="12" fill="rgba(255,255,255,0.4)"/>
    <text x="130" y="355" fill="white" font-size="20" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Retail</text>
    <text x="130" y="380" fill="rgba(255,255,255,0.95)" font-size="14" font-weight="500" font-style="italic">Hyper-personalization at scale</text>
    <circle cx="980" cy="367" r="8" fill="rgba(255,255,255,0.3)"/>
    <text x="940" y="370" text-anchor="end" fill="white" font-size="16" font-weight="700">🟠 High Impact</text>
  </g>
  
  <!-- Pharmaceuticals - Medium-High -->
  <g filter="url(#impactShadow)">
    <rect x="80" y="430" width="940" height="95" rx="12" fill="url(#medHighGrad)" stroke="#ca8a04" stroke-width="2"/>
    <circle cx="110" cy="460" r="12" fill="rgba(255,255,255,0.4)"/>
    <text x="130" y="465" fill="white" font-size="20" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Pharmaceuticals</text>
    <text x="130" y="490" fill="rgba(255,255,255,0.95)" font-size="14" font-weight="500" font-style="italic">Drug discovery analytics</text>
    <circle cx="980" cy="477" r="8" fill="rgba(255,255,255,0.3)"/>
    <text x="940" y="480" text-anchor="end" fill="white" font-size="16" font-weight="700">🟡 Medium-High Impact</text>
  </g>
  
  <!-- Financial Services - High -->
  <g filter="url(#impactShadow)">
    <rect x="80" y="540" width="940" height="95" rx="12" fill="url(#highGrad)" stroke="#d97706" stroke-width="2"/>
    <circle cx="110" cy="570" r="12" fill="rgba(255,255,255,0.4)"/>
    <text x="130" y="575" fill="white" font-size="20" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Financial Services</text>
    <text x="130" y="600" fill="rgba(255,255,255,0.95)" font-size="14" font-weight="500" font-style="italic">Compliance &amp; risk automation</text>
    <circle cx="980" cy="587" r="8" fill="rgba(255,255,255,0.3)"/>
    <text x="940" y="590" text-anchor="end" fill="white" font-size="16" font-weight="700">🟠 High Impact</text>
  </g>
</svg>'''
    return svg

def create_market_comparison_svg():
    """Create enhanced market comparison chart"""
    svg = '''<svg viewBox="0 0 1200 580" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%);">
  <defs>
    <linearGradient id="appGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#10b981;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#059669;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="servicesGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#f59e0b;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#d97706;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="globalGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#3b82f6;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#2563eb;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="currentGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#94a3b8;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#64748b;stop-opacity:1" />
    </linearGradient>
    <filter id="barShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="3"/>
      <feOffset dx="2" dy="3" result="offsetblur"/>
      <feComponentTransfer>
        <feFuncA type="linear" slope="0.3"/>
      </feComponentTransfer>
      <feMerge>
        <feMergeNode/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <!-- Title -->
  <text x="600" y="45" text-anchor="middle" fill="#1e293b" font-size="26" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Market Value Comparison</text>
  
  <!-- US Market Section -->
  <text x="300" y="100" text-anchor="middle" fill="#334155" font-size="18" font-weight="700" font-family="system-ui, -apple-system, sans-serif">U.S. Market</text>
  <text x="300" y="125" text-anchor="middle" fill="#64748b" font-size="13" font-weight="500">(Billions USD)</text>
  
  <g filter="url(#barShadow)">
    <rect x="100" y="150" width="400" height="90" rx="10" fill="url(#appGrad)" stroke="#047857" stroke-width="2"/>
    <circle cx="125" cy="175" r="10" fill="rgba(255,255,255,0.3)"/>
    <text x="300" y="195" text-anchor="middle" fill="white" font-size="22" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Application Layer</text>
    <text x="300" y="225" text-anchor="middle" fill="rgba(255,255,255,0.95)" font-size="18" font-weight="600">~$1 Trillion</text>
    
    <rect x="100" y="270" width="320" height="90" rx="10" fill="url(#servicesGrad)" stroke="#b45309" stroke-width="2"/>
    <circle cx="125" cy="295" r="10" fill="rgba(255,255,255,0.3)"/>
    <text x="260" y="315" text-anchor="middle" fill="white" font-size="22" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Services Layer</text>
    <text x="260" y="345" text-anchor="middle" fill="rgba(255,255,255,0.95)" font-size="18" font-weight="600">$350-450B</text>
    
    <rect x="100" y="390" width="256" height="90" rx="10" fill="url(#currentGrad)" stroke="#475569" stroke-width="2"/>
    <circle cx="125" cy="415" r="10" fill="rgba(255,255,255,0.3)"/>
    <text x="228" y="435" text-anchor="middle" fill="white" font-size="22" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Current IT Services</text>
    <text x="228" y="465" text-anchor="middle" fill="rgba(255,255,255,0.95)" font-size="18" font-weight="600">$320B</text>
  </g>
  
  <!-- Global Market Section -->
  <text x="900" y="100" text-anchor="middle" fill="#334155" font-size="18" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Global Market</text>
  <text x="900" y="125" text-anchor="middle" fill="#64748b" font-size="13" font-weight="500">(Trillions USD)</text>
  
  <g filter="url(#barShadow)">
    <rect x="700" y="150" width="400" height="90" rx="10" fill="url(#globalGrad)" stroke="#1e40af" stroke-width="2"/>
    <circle cx="725" cy="175" r="10" fill="rgba(255,255,255,0.3)"/>
    <text x="900" y="195" text-anchor="middle" fill="white" font-size="22" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Services Layer</text>
    <text x="900" y="225" text-anchor="middle" fill="rgba(255,255,255,0.95)" font-size="18" font-weight="600">$0.9-1.1 Trillion</text>
    
    <rect x="700" y="270" width="400" height="90" rx="10" fill="url(#appGrad)" stroke="#047857" stroke-width="2"/>
    <circle cx="725" cy="295" r="10" fill="rgba(255,255,255,0.3)"/>
    <text x="900" y="315" text-anchor="middle" fill="white" font-size="22" font-weight="700" font-family="system-ui, -apple-system, sans-serif">Application Layer</text>
    <text x="900" y="345" text-anchor="middle" fill="rgba(255,255,255,0.95)" font-size="18" font-weight="600">~$1 Trillion (US)</text>
  </g>
  
  <!-- Note -->
  <rect x="200" y="510" width="800" height="60" rx="10" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="2"/>
  <text x="600" y="535" text-anchor="middle" fill="#475569" font-size="14" font-weight="600">Services/App Ratio: 0.70-0.80x</text>
  <text x="600" y="560" text-anchor="middle" fill="#64748b" font-size="13" font-style="italic">Services opportunity ($350-450B US) exceeds current IT services ($320B US)</text>
</svg>'''
    return svg

if __name__ == '__main__':
    output_dir = Path(__file__).parent.parent / 'public' / 'images' / 'agentic-ai'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("Generating enhanced professional SVG charts...\n")
    
    with open(output_dir / 'market-structure.svg', 'w') as f:
        f.write(create_market_structure_svg())
    print("✓ Created market-structure.svg")
    
    with open(output_dir / 'labor-augmentation.svg', 'w') as f:
        f.write(create_labor_augmentation_svg())
    print("✓ Created labor-augmentation.svg")
    
    with open(output_dir / 'evolution-timeline.svg', 'w') as f:
        f.write(create_evolution_timeline_svg())
    print("✓ Created evolution-timeline.svg")
    
    with open(output_dir / 'adoption-timeline.svg', 'w') as f:
        f.write(create_adoption_timeline_svg())
    print("✓ Created adoption-timeline.svg")
    
    with open(output_dir / 'industry-impact.svg', 'w') as f:
        f.write(create_industry_impact_svg())
    print("✓ Created industry-impact.svg")
    
    with open(output_dir / 'market-comparison.svg', 'w') as f:
        f.write(create_market_comparison_svg())
    print("✓ Created market-comparison.svg")
    
    print("\n✅ All enhanced SVG charts generated!")
    print(f"📁 Saved to: {output_dir}")

