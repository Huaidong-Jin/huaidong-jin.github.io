#!/usr/bin/env python3
"""
Generate SVG charts for MDX embedding - no external dependencies needed for SVG strings
"""
from pathlib import Path

def create_market_structure_svg():
    """Create market value structure as SVG"""
    svg = '''<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto;">
  <!-- Global Market -->
  <rect x="200" y="50" width="400" height="80" rx="10" fill="#3b82f6" stroke="#1e40af" stroke-width="3"/>
  <text x="400" y="85" text-anchor="middle" fill="white" font-size="18" font-weight="bold">Global Market Opportunity</text>
  <text x="400" y="110" text-anchor="middle" fill="white" font-size="14">$0.9 - 1.1 Trillion (Services)</text>
  
  <!-- Application Layer -->
  <rect x="80" y="200" width="280" height="120" rx="10" fill="#10b981" stroke="#059669" stroke-width="3"/>
  <text x="220" y="235" text-anchor="middle" fill="white" font-size="16" font-weight="bold">Application Layer</text>
  <text x="220" y="265" text-anchor="middle" fill="white" font-size="13">~$1 Trillion (US)</text>
  <text x="220" y="290" text-anchor="middle" fill="white" font-size="11">Software Products &amp; Platforms</text>
  
  <!-- Services Layer -->
  <rect x="440" y="200" width="280" height="120" rx="10" fill="#f59e0b" stroke="#d97706" stroke-width="3"/>
  <text x="580" y="235" text-anchor="middle" fill="white" font-size="16" font-weight="bold">Services Layer</text>
  <text x="580" y="265" text-anchor="middle" fill="white" font-size="13">$350-450B (US)</text>
  <text x="580" y="290" text-anchor="middle" fill="white" font-size="13">$0.9-1.1T (Global)</text>
  <text x="580" y="310" text-anchor="middle" fill="white" font-size="11">Implementation &amp; Support</text>
  
  <!-- Arrows -->
  <path d="M 400 130 L 220 200" stroke="#1e40af" stroke-width="3" fill="none" marker-end="url(#arrowhead)"/>
  <path d="M 400 130 L 580 200" stroke="#1e40af" stroke-width="3" fill="none" marker-end="url(#arrowhead)"/>
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#1e40af"/>
    </marker>
  </defs>
  
  <!-- Ratio -->
  <text x="400" y="380" text-anchor="middle" fill="#374151" font-size="14" font-weight="bold">Services/App Ratio: 0.70-0.80x</text>
  
  <!-- Current IT Services -->
  <rect x="80" y="420" width="640" height="50" rx="8" fill="#e5e7eb" stroke="#9ca3af" stroke-width="2"/>
  <text x="400" y="450" text-anchor="middle" fill="#374151" font-size="14" font-style="italic">Current IT Services (US): $320B</text>
</svg>'''
    return svg

def create_labor_augmentation_svg():
    """Create labor augmentation bar chart as SVG"""
    svg = '''<svg viewBox="0 0 900 700" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto;">
  <text x="450" y="30" text-anchor="middle" fill="#1e40af" font-size="20" font-weight="bold">Labor Augmentation Potential by Role Category</text>
  
  <!-- High Augmentation (85-90%) -->
  <text x="50" y="60" fill="#1e40af" font-size="14" font-weight="bold">High Augmentation (85-90%)</text>
  <line x1="50" y1="70" x2="850" y2="70" stroke="#3b82f6" stroke-width="2" stroke-dasharray="5,5"/>
  
  <!-- Bars for High -->
  <g id="high-bars">
    <rect x="280" y="100" width="540" height="35" rx="5" fill="#2563eb"/>
    <text x="270" y="122" text-anchor="end" fill="#1e40af" font-size="12" font-weight="bold">Customer Service Reps</text>
    <text x="830" y="122" fill="white" font-size="12" font-weight="bold">90%</text>
    
    <rect x="300" y="150" width="528" height="35" rx="5" fill="#3b82f6"/>
    <text x="270" y="172" text-anchor="end" fill="#1e40af" font-size="12" font-weight="bold">Data Analysts</text>
    <text x="838" y="172" fill="white" font-size="12" font-weight="bold">88%</text>
    
    <rect x="315" y="200" width="513" height="35" rx="5" fill="#60a5fa"/>
    <text x="270" y="222" text-anchor="end" fill="#1e40af" font-size="12" font-weight="bold">Software Engineers</text>
    <text x="838" y="222" fill="white" font-size="12" font-weight="bold">87%</text>
    
    <rect x="290" y="250" width="538" height="35" rx="5" fill="#2563eb"/>
    <text x="270" y="272" text-anchor="end" fill="#1e40af" font-size="12" font-weight="bold">Compliance Officers</text>
    <text x="838" y="272" fill="white" font-size="12" font-weight="bold">89%</text>
    
    <rect x="324" y="300" width="504" height="35" rx="5" fill="#3b82f6"/>
    <text x="270" y="322" text-anchor="end" fill="#1e40af" font-size="12" font-weight="bold">Supply Chain Coordinators</text>
    <text x="838" y="322" fill="white" font-size="12" font-weight="bold">86%</text>
  </g>
  
  <!-- Medium Augmentation (40-50%) -->
  <text x="50" y="370" fill="#d97706" font-size="14" font-weight="bold">Medium Augmentation (40-50%)</text>
  <line x1="50" y1="380" x2="850" y2="380" stroke="#f59e0b" stroke-width="2" stroke-dasharray="5,5"/>
  
  <rect x="456" y="400" width="384" height="35" rx="5" fill="#f59e0b"/>
  <text x="270" y="422" text-anchor="end" fill="#1e40af" font-size="12" font-weight="bold">Marketing Managers</text>
  <text x="850" y="422" fill="white" font-size="12" font-weight="bold">48%</text>
  
  <rect x="450" y="450" width="378" height="35" rx="5" fill="#fb923c"/>
  <text x="270" y="472" text-anchor="end" fill="#1e40af" font-size="12" font-weight="bold">HR Coordinators</text>
  <text x="838" y="472" fill="white" font-size="12" font-weight="bold">45%</text>
  
  <rect x="450" y="500" width="450" height="35" rx="5" fill="#f59e0b"/>
  <text x="270" y="522" text-anchor="end" fill="#1e40af" font-size="12" font-weight="bold">Financial Analysts</text>
  <text x="730" y="522" fill="white" font-size="12" font-weight="bold">50%</text>
  
  <!-- Low Augmentation (<20%) -->
  <text x="50" y="560" fill="#374151" font-size="14" font-weight="bold">Low Augmentation (&lt;20%)</text>
  <line x1="50" y1="570" x2="850" y2="570" stroke="#6b7280" stroke-width="2" stroke-dasharray="5,5"/>
  
  <rect x="162" y="590" width="180" height="35" rx="5" fill="#6b7280"/>
  <text x="270" y="612" text-anchor="end" fill="#1e40af" font-size="12" font-weight="bold">Strategic Planners</text>
  <text x="352" y="612" fill="white" font-size="12" font-weight="bold">18%</text>
  
  <rect x="108" y="640" width="120" height="35" rx="5" fill="#9ca3af"/>
  <text x="270" y="662" text-anchor="end" fill="#1e40af" font-size="12" font-weight="bold">Executive Leadership</text>
  <text x="238" y="662" fill="white" font-size="12" font-weight="bold">12%</text>
  
  <!-- X-axis scale -->
  <line x1="270" y1="680" x2="870" y2="680" stroke="#374151" stroke-width="2"/>
  <text x="270" y="695" text-anchor="middle" fill="#6b7280" font-size="10">0%</text>
  <text x="570" y="695" text-anchor="middle" fill="#6b7280" font-size="10">50%</text>
  <text x="870" y="695" text-anchor="middle" fill="#6b7280" font-size="10">100%</text>
  
  <!-- Footer -->
  <text x="450" y="720" text-anchor="middle" fill="#6b7280" font-size="10" font-style="italic">Based on analysis of 150 job roles with 5 key criteria</text>
</svg>'''
    return svg

def create_evolution_timeline_svg():
    """Create evolution timeline as SVG"""
    svg = '''<svg viewBox="0 0 900 500" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto;">
  <text x="450" y="30" text-anchor="middle" fill="#1e40af" font-size="22" font-weight="bold">Automation Evolution</text>
  <text x="450" y="55" text-anchor="middle" fill="#6b7280" font-size="14" font-style="italic">Convergence &amp; Evolution</text>
  
  <!-- RPA Era -->
  <rect x="80" y="120" width="200" height="140" rx="12" fill="#94a3b8" stroke="#64748b" stroke-width="3"/>
  <text x="180" y="155" text-anchor="middle" fill="white" font-size="16" font-weight="bold">RPA Era</text>
  <text x="180" y="180" text-anchor="middle" fill="white" font-size="12">(2010s)</text>
  <text x="180" y="210" text-anchor="middle" fill="white" font-size="13" font-style="italic">Scripted Tasks</text>
  <text x="180" y="235" text-anchor="middle" fill="white" font-size="13" font-style="italic">Brittle Static</text>
  
  <!-- Gen AI Era -->
  <rect x="350" y="120" width="200" height="140" rx="12" fill="#60a5fa" stroke="#3b82f6" stroke-width="3"/>
  <text x="450" y="155" text-anchor="middle" fill="white" font-size="16" font-weight="bold">Gen AI Era</text>
  <text x="450" y="180" text-anchor="middle" fill="white" font-size="12">(2020s)</text>
  <text x="450" y="210" text-anchor="middle" fill="white" font-size="13" font-style="italic">Isolated Assistants</text>
  <text x="450" y="235" text-anchor="middle" fill="white" font-size="13" font-style="italic">Human-Dependent</text>
  
  <!-- Agentic AI Era -->
  <rect x="620" y="120" width="200" height="140" rx="12" fill="#10b981" stroke="#059669" stroke-width="3"/>
  <text x="720" y="155" text-anchor="middle" fill="white" font-size="16" font-weight="bold">Agentic AI</text>
  <text x="720" y="180" text-anchor="middle" fill="white" font-size="12">(2025+)</text>
  <text x="720" y="210" text-anchor="middle" fill="white" font-size="13" font-style="italic">Autonomous Systems</text>
  <text x="720" y="235" text-anchor="middle" fill="white" font-size="13" font-style="italic">Self-Driven Adaptive</text>
  
  <!-- Arrows -->
  <path d="M 280 190 L 350 190" stroke="#374151" stroke-width="4" fill="none" marker-end="url(#arrow)"/>
  <path d="M 550 190 L 620 190" stroke="#374151" stroke-width="4" fill="none" marker-end="url(#arrow)"/>
  <defs>
    <marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto">
      <polygon points="0 0, 12 6, 0 12" fill="#374151"/>
    </marker>
  </defs>
  
  <!-- Key Capabilities -->
  <rect x="80" y="300" width="740" height="160" rx="10" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>
  <text x="450" y="330" text-anchor="middle" fill="#92400e" font-size="16" font-weight="bold">Key Capabilities</text>
  
  <rect x="100" y="350" width="220" height="90" rx="8" fill="#e0e7ff"/>
  <text x="210" y="375" text-anchor="middle" fill="#3730a3" font-size="13" font-weight="bold">RPA</text>
  <text x="210" y="400" text-anchor="middle" fill="#4338ca" font-size="11">Script execution</text>
  <text x="210" y="420" text-anchor="middle" fill="#4338ca" font-size="11">Rule-based</text>
  
  <rect x="340" y="350" width="220" height="90" rx="8" fill="#dbeafe"/>
  <text x="450" y="375" text-anchor="middle" fill="#1e40af" font-size="13" font-weight="bold">Gen AI</text>
  <text x="450" y="400" text-anchor="middle" fill="#2563eb" font-size="11">Content creation</text>
  <text x="450" y="420" text-anchor="middle" fill="#2563eb" font-size="11">Analysis</text>
  
  <rect x="580" y="350" width="220" height="90" rx="8" fill="#d1fae5"/>
  <text x="690" y="375" text-anchor="middle" fill="#065f46" font-size="13" font-weight="bold">Agentic</text>
  <text x="690" y="400" text-anchor="middle" fill="#047857" font-size="11">Reasoning + Action</text>
  <text x="690" y="420" text-anchor="middle" fill="#047857" font-size="11">+ Adaptation</text>
</svg>'''
    return svg

def create_adoption_timeline_svg():
    """Create adoption timeline as SVG"""
    svg = '''<svg viewBox="0 0 1000 500" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto;">
  <text x="500" y="30" text-anchor="middle" fill="#065f46" font-size="20" font-weight="bold">Projected Adoption Timeline</text>
  <text x="500" y="55" text-anchor="middle" fill="#6b7280" font-size="14">Market Realization ($300-600B Global Services)</text>
  
  <!-- Timeline base -->
  <line x1="100" y1="350" x2="900" y2="350" stroke="#9ca3af" stroke-width="4" opacity="0.5"/>
  
  <!-- 2025 Current State -->
  <line x1="200" y1="320" x2="200" y2="380" stroke="#374151" stroke-width="3"/>
  <circle cx="200" cy="350" r="8" fill="#10b981"/>
  <text x="200" y="310" text-anchor="middle" fill="#374151" font-size="14" font-weight="bold">2025</text>
  <text x="200" y="295" text-anchor="middle" fill="#6b7280" font-size="11">Current State</text>
  
  <!-- Acceleration factors -->
  <rect x="50" y="100" width="300" height="140" rx="8" fill="#dbeafe" stroke="#3b82f6" stroke-width="2"/>
  <text x="200" y="125" text-anchor="middle" fill="#1e40af" font-size="13" font-weight="bold">Key Acceleration Factors</text>
  <text x="70" y="155" fill="#1e3a8a" font-size="11">✓ 90%+ enterprises interested</text>
  <text x="70" y="180" fill="#1e3a8a" font-size="11">✓ Major vendors prioritizing agentic AI</text>
  <text x="70" y="205" fill="#1e3a8a" font-size="11">✓ Early implementations showing ROI</text>
  <text x="70" y="230" fill="#1e3a8a" font-size="11">✓ Compressed adoption curve expected</text>
  
  <!-- Accelerated Timeline -->
  <rect x="550" y="150" width="350" height="100" rx="10" fill="#10b981" stroke="#059669" stroke-width="3"/>
  <text x="725" y="180" text-anchor="middle" fill="white" font-size="15" font-weight="bold">Accelerated Timeline (More Likely)</text>
  <text x="725" y="210" text-anchor="middle" fill="white" font-size="13">$300-600B by 2030-2035</text>
  <text x="725" y="235" text-anchor="middle" fill="white" font-size="11">Early adoption signals strong</text>
  
  <!-- Conservative Timeline -->
  <rect x="550" y="280" width="350" height="100" rx="10" fill="#6b7280" stroke="#4b5563" stroke-width="3"/>
  <text x="725" y="310" text-anchor="middle" fill="white" font-size="15" font-weight="bold">Conservative Timeline</text>
  <text x="725" y="340" text-anchor="middle" fill="white" font-size="13">$300-600B by 2035-2040</text>
  <text x="725" y="365" text-anchor="middle" fill="white" font-size="11">Following cloud computing path</text>
  
  <!-- Arrows -->
  <path d="M 200 350 L 700 200" stroke="#10b981" stroke-width="4" fill="none" marker-end="url(#arrow-green)"/>
  <path d="M 200 350 L 700 330" stroke="#6b7280" stroke-width="4" fill="none" marker-end="url(#arrow-gray)"/>
  
  <defs>
    <marker id="arrow-green" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto">
      <polygon points="0 0, 12 6, 0 12" fill="#10b981"/>
    </marker>
    <marker id="arrow-gray" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto">
      <polygon points="0 0, 12 6, 0 12" fill="#6b7280"/>
    </marker>
  </defs>
  
  <!-- Milestone markers -->
  <circle cx="700" cy="200" r="12" fill="#10b981" stroke="white" stroke-width="3"/>
  <circle cx="700" cy="330" r="12" fill="#6b7280" stroke="white" stroke-width="3"/>
  
  <!-- Year labels -->
  <text x="550" y="410" text-anchor="middle" fill="#6b7280" font-size="11">2030-2035</text>
  <text x="750" y="410" text-anchor="middle" fill="#6b7280" font-size="11">2035-2040</text>
</svg>'''
    return svg

def create_industry_impact_svg():
    """Create industry impact matrix as SVG"""
    svg = '''<svg viewBox="0 0 900 600" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto;">
  <text x="450" y="30" text-anchor="middle" fill="#92400e" font-size="20" font-weight="bold">Industry Impact Matrix</text>
  
  <!-- Insurance - Very High -->
  <rect x="50" y="80" width="800" height="80" rx="10" fill="#dc2626" stroke="#991b1b" stroke-width="3"/>
  <text x="70" y="110" fill="white" font-size="16" font-weight="bold">Insurance</text>
  <text x="70" y="135" fill="white" font-size="12" font-style="italic">Claims adjudication automation</text>
  <text x="750" y="125" text-anchor="end" fill="white" font-size="14" font-weight="bold">🔴 Very High Impact</text>
  
  <!-- Manufacturing - High -->
  <rect x="50" y="180" width="800" height="80" rx="10" fill="#f59e0b" stroke="#d97706" stroke-width="3"/>
  <text x="70" y="210" fill="white" font-size="16" font-weight="bold">Manufacturing</text>
  <text x="70" y="235" fill="white" font-size="12" font-style="italic">Inventory &amp; supply chain management</text>
  <text x="750" y="225" text-anchor="end" fill="white" font-size="14" font-weight="bold">🟠 High Impact</text>
  
  <!-- Retail - High -->
  <rect x="50" y="280" width="800" height="80" rx="10" fill="#f59e0b" stroke="#d97706" stroke-width="3"/>
  <text x="70" y="310" fill="white" font-size="16" font-weight="bold">Retail</text>
  <text x="70" y="335" fill="white" font-size="12" font-style="italic">Hyper-personalization at scale</text>
  <text x="750" y="325" text-anchor="end" fill="white" font-size="14" font-weight="bold">🟠 High Impact</text>
  
  <!-- Pharmaceuticals - Medium-High -->
  <rect x="50" y="380" width="800" height="80" rx="10" fill="#eab308" stroke="#ca8a04" stroke-width="3"/>
  <text x="70" y="410" fill="white" font-size="16" font-weight="bold">Pharmaceuticals</text>
  <text x="70" y="435" fill="white" font-size="12" font-style="italic">Drug discovery analytics</text>
  <text x="750" y="425" text-anchor="end" fill="white" font-size="14" font-weight="bold">🟡 Medium-High Impact</text>
  
  <!-- Financial Services - High -->
  <rect x="50" y="480" width="800" height="80" rx="10" fill="#f59e0b" stroke="#d97706" stroke-width="3"/>
  <text x="70" y="510" fill="white" font-size="16" font-weight="bold">Financial Services</text>
  <text x="70" y="535" fill="white" font-size="12" font-style="italic">Compliance &amp; risk automation</text>
  <text x="750" y="525" text-anchor="end" fill="white" font-size="14" font-weight="bold">🟠 High Impact</text>
</svg>'''
    return svg

def create_market_comparison_svg():
    """Create market comparison chart as SVG"""
    svg = '''<svg viewBox="0 0 1000 500" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto;">
  <text x="500" y="30" text-anchor="middle" fill="#1e40af" font-size="20" font-weight="bold">Market Value Comparison</text>
  
  <!-- US Market Bars -->
  <text x="250" y="80" text-anchor="middle" fill="#374151" font-size="16" font-weight="bold">U.S. Market (Billions USD)</text>
  
  <!-- Application Layer -->
  <rect x="100" y="120" width="300" height="80" rx="8" fill="#10b981" stroke="#059669" stroke-width="2"/>
  <text x="250" y="160" text-anchor="middle" fill="white" font-size="18" font-weight="bold">Application Layer</text>
  <text x="250" y="185" text-anchor="middle" fill="white" font-size="14">~$1 Trillion</text>
  
  <!-- Services Layer -->
  <rect x="100" y="230" width="240" height="80" rx="8" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
  <text x="220" y="270" text-anchor="middle" fill="white" font-size="18" font-weight="bold">Services Layer</text>
  <text x="220" y="295" text-anchor="middle" fill="white" font-size="14">$350-450B</text>
  
  <!-- Current IT Services -->
  <rect x="100" y="340" width="192" height="80" rx="8" fill="#94a3b8" stroke="#64748b" stroke-width="2"/>
  <text x="196" y="380" text-anchor="middle" fill="white" font-size="18" font-weight="bold">Current IT Services</text>
  <text x="196" y="405" text-anchor="middle" fill="white" font-size="14">$320B</text>
  
  <!-- Global Market Bars -->
  <text x="750" y="80" text-anchor="middle" fill="#374151" font-size="16" font-weight="bold">Global Market (Trillions USD)</text>
  
  <!-- Global Services -->
  <rect x="600" y="120" width="300" height="80" rx="8" fill="#3b82f6" stroke="#2563eb" stroke-width="2"/>
  <text x="750" y="160" text-anchor="middle" fill="white" font-size="18" font-weight="bold">Services Layer</text>
  <text x="750" y="185" text-anchor="middle" fill="white" font-size="14">$0.9-1.1 Trillion</text>
  
  <!-- US Application (for scale) -->
  <rect x="600" y="230" width="300" height="80" rx="8" fill="#10b981" stroke="#059669" stroke-width="2"/>
  <text x="750" y="270" text-anchor="middle" fill="white" font-size="18" font-weight="bold">Application Layer</text>
  <text x="750" y="295" text-anchor="middle" fill="white" font-size="14">~$1 Trillion (US)</text>
  
  <!-- Note -->
  <text x="500" y="450" text-anchor="middle" fill="#6b7280" font-size="12" font-style="italic">
    Services/App Ratio: 0.70-0.80x | Services opportunity ($350-450B US) exceeds current IT services ($320B US)
  </text>
</svg>'''
    return svg

# Generate SVG files
if __name__ == '__main__':
    output_dir = Path(__file__).parent.parent / 'public' / 'images' / 'agentic-ai'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Write SVG files
    with open(output_dir / 'market-structure.svg', 'w') as f:
        f.write(create_market_structure_svg())
    
    with open(output_dir / 'labor-augmentation.svg', 'w') as f:
        f.write(create_labor_augmentation_svg())
    
    with open(output_dir / 'evolution-timeline.svg', 'w') as f:
        f.write(create_evolution_timeline_svg())
    
    with open(output_dir / 'adoption-timeline.svg', 'w') as f:
        f.write(create_adoption_timeline_svg())
    
    with open(output_dir / 'industry-impact.svg', 'w') as f:
        f.write(create_industry_impact_svg())
    
    with open(output_dir / 'market-comparison.svg', 'w') as f:
        f.write(create_market_comparison_svg())
    
    print("✅ All SVG charts generated!")
    print(f"📁 Saved to: {output_dir}")

