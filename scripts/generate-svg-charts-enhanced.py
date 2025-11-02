#!/usr/bin/env python3
"""
Generate minimal, high-contrast SVG charts that match the blog's dark aesthetic.
"""
from pathlib import Path

FONT_STACK = "Inter, 'Helvetica Neue', Arial, sans-serif"
BG = "#000000"
FG = "#f8fafc"
FG_MUTED = "#cbd5f5"
ACCENT = "#38bdf8"
ACCENT_DIM = "#1f2937"
OUTLINE = "#1e293b"
SEPARATOR = "#111827"


def svg_wrapper(width: int, height: int, body: str) -> str:
    return f'''<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; background: {BG};">
{body}
</svg>'''


def create_market_structure_svg() -> str:
    width, height = 1000, 620
    body = f'''
  <rect x="0" y="0" width="{width}" height="{height}" fill="{BG}"/>
  <text x="500" y="60" text-anchor="middle" fill="{FG}" font-size="26" font-weight="600" font-family="{FONT_STACK}">Market Value Structure</text>

  <g>
    <rect x="220" y="110" width="560" height="90" rx="10" fill="none" stroke="{FG}" stroke-width="2"/>
    <text x="500" y="150" text-anchor="middle" fill="{FG}" font-size="20" font-weight="600" font-family="{FONT_STACK}">Global Market Opportunity</text>
    <text x="500" y="180" text-anchor="middle" fill="{FG_MUTED}" font-size="16" font-family="{FONT_STACK}">$0.9 - 1.1T (Services)</text>
  </g>

  <g>
    <rect x="100" y="260" width="320" height="140" rx="10" fill="none" stroke="{FG}" stroke-width="1.5"/>
    <text x="260" y="305" text-anchor="middle" fill="{FG}" font-size="18" font-weight="600" font-family="{FONT_STACK}">Application Layer</text>
    <text x="260" y="335" text-anchor="middle" fill="{FG_MUTED}" font-size="16" font-family="{FONT_STACK}">~$1T (US)</text>
    <text x="260" y="365" text-anchor="middle" fill="{FG_MUTED}" font-size="13" font-family="{FONT_STACK}">Software Products &amp; Platforms</text>
  </g>

  <g>
    <rect x="580" y="260" width="320" height="140" rx="10" fill="none" stroke="{FG}" stroke-width="1.5"/>
    <text x="740" y="305" text-anchor="middle" fill="{FG}" font-size="18" font-weight="600" font-family="{FONT_STACK}">Services Layer</text>
    <text x="740" y="335" text-anchor="middle" fill="{FG_MUTED}" font-size="16" font-family="{FONT_STACK}">$350-450B (US)</text>
    <text x="740" y="365" text-anchor="middle" fill="{FG_MUTED}" font-size="13" font-family="{FONT_STACK}">$0.9-1.1T (Global)</text>
    <text x="740" y="385" text-anchor="middle" fill="{FG_MUTED}" font-size="13" font-family="{FONT_STACK}">Implementation &amp; Support</text>
  </g>

  <line x1="500" y1="200" x2="260" y2="260" stroke="{FG_MUTED}" stroke-width="2"/>
  <line x1="500" y1="200" x2="740" y2="260" stroke="{FG_MUTED}" stroke-width="2"/>

  <rect x="400" y="440" width="200" height="60" rx="10" fill="none" stroke="{FG_MUTED}" stroke-width="1.5"/>
  <text x="500" y="470" text-anchor="middle" fill="{FG}" font-size="16" font-weight="600" font-family="{FONT_STACK}">Services : Apps</text>
  <text x="500" y="495" text-anchor="middle" fill="{FG_MUTED}" font-size="14" font-family="{FONT_STACK}">0.70 - 0.80×</text>

  <line x1="110" y1="540" x2="890" y2="540" stroke="{SEPARATOR}" stroke-width="1"/>
  <text x="500" y="570" text-anchor="middle" fill="{FG_MUTED}" font-size="13" font-family="{FONT_STACK}">Current IT Services (US): $320B</text>
'''
    return svg_wrapper(width, height, body)


def create_labor_augmentation_svg() -> str:
    width, height = 1100, 720
    labels = [
        ("Customer Service Reps", 90),
        ("Data Analysts", 88),
        ("Software Engineers", 87),
        ("Compliance Officers", 89),
        ("Supply Chain Coordinators", 86),
        ("Marketing Managers", 48),
        ("HR Coordinators", 45),
        ("Financial Analysts", 50),
        ("Strategic Planners", 18),
        ("Executive Leadership", 12),
    ]
    sections = [
        (0, 5, "High Augmentation 85-90%"),
        (5, 8, "Medium Augmentation 40-50%"),
        (8, 10, "Low Augmentation &lt;20%"),
    ]

    lines = [f'  <rect x="0" y="0" width="{width}" height="{height}" fill="{BG}"/>',
             f'  <text x="550" y="60" text-anchor="middle" fill="{FG}" font-size="26" font-weight="600" font-family="{FONT_STACK}">Labor Augmentation Potential</text>',
             f'  <text x="550" y="92" text-anchor="middle" fill="{FG_MUTED}" font-size="14" font-family="{FONT_STACK}">Share of task time addressable by agentic AI</text>']

    y_start = 140
    bar_height = 46
    gap = 18
    x_label = 180
    x_bar = 300
    max_width = 700

    for start, end, title in sections:
        y_title = y_start - 24 if start == 0 else y_start - 12
        lines.append(f'  <text x="{x_label}" y="{y_title}" fill="{FG}" font-size="16" font-weight="600" font-family="{FONT_STACK}">{title}</text>')
        for idx in range(start, end):
            label, value = labels[idx]
            y = y_start + idx * (bar_height + gap)
            width_px = max_width * (value / 100)
            lines.append(f'  <rect x="{x_bar}" y="{y}" width="{width_px:.1f}" height="{bar_height}" fill="{ACCENT}" opacity="0.85" rx="4"/>' )
            lines.append(f'  <text x="{x_label}" y="{y + bar_height - 12}" fill="{FG}" font-size="15" font-family="{FONT_STACK}" text-anchor="end">{label}</text>')
            lines.append(f'  <text x="{x_bar + width_px + 20:.1f}" y="{y + bar_height - 12}" fill="{FG}" font-size="15" font-weight="600" font-family="{FONT_STACK}">{value}%</text>')

    lines.append(f'  <line x1="{x_bar}" y1="660" x2="{x_bar + max_width}" y2="660" stroke="{SEPARATOR}" stroke-width="1"/>')
    for tick in [0, 25, 50, 75, 100]:
        tx = x_bar + max_width * (tick / 100)
        lines.append(f'  <line x1="{tx}" y1="656" x2="{tx}" y2="664" stroke="{SEPARATOR}" stroke-width="1"/>')
        lines.append(f'  <text x="{tx}" y="682" text-anchor="middle" fill="{FG_MUTED}" font-size="12" font-family="{FONT_STACK}">{tick}%</text>')

    return svg_wrapper(width, height, "\n".join(lines))


def create_evolution_timeline_svg() -> str:
    width, height = 1100, 520
    era_positions = [
        (150, "RPA Era", "Scripted Tasks", "Brittle", "Static"),
        (550, "Gen AI Era", "Isolated Assistants", "Human Dependent", ""),
        (950, "Agentic AI", "Autonomous", "Adaptive", "Self-Directed"),
    ]
    lines = [
        f'  <rect x="0" y="0" width="{width}" height="{height}" fill="{BG}"/>',
        f'  <text x="550" y="60" text-anchor="middle" fill="{FG}" font-size="26" font-weight="600" font-family="{FONT_STACK}">Automation Evolution</text>',
        f'  <line x1="120" y1="200" x2="980" y2="200" stroke="{SEPARATOR}" stroke-width="2" stroke-dasharray="6 6"/>'
    ]
    for x, title, l1, l2, l3 in era_positions:
        lines.append(f'  <rect x="{x - 120}" y="130" width="240" height="140" rx="10" fill="none" stroke="{FG}" stroke-width="1.5"/>' )
        lines.append(f'  <text x="{x}" y="170" text-anchor="middle" fill="{FG}" font-size="20" font-weight="600" font-family="{FONT_STACK}">{title}</text>')
        lines.append(f'  <text x="{x}" y="205" text-anchor="middle" fill="{FG_MUTED}" font-size="14" font-family="{FONT_STACK}">{l1}</text>')
        lines.append(f'  <text x="{x}" y="230" text-anchor="middle" fill="{FG_MUTED}" font-size="14" font-family="{FONT_STACK}">{l2}</text>')
        if l3:
            lines.append(f'  <text x="{x}" y="255" text-anchor="middle" fill="{FG_MUTED}" font-size="14" font-family="{FONT_STACK}">{l3}</text>')

    lines.append(f'  <line x1="290" y1="200" x2="410" y2="200" stroke="{FG_MUTED}" stroke-width="2" marker-end="url(#arrowSmall)"/>')
    lines.append(f'  <line x1="690" y1="200" x2="810" y2="200" stroke="{FG_MUTED}" stroke-width="2" marker-end="url(#arrowSmall)"/>')

    lines.append(f'  <rect x="120" y="320" width="840" height="150" rx="12" fill="none" stroke="{SEPARATOR}" stroke-width="1"/>' )
    lines.append(f'  <text x="540" y="355" text-anchor="middle" fill="{FG}" font-size="18" font-weight="600" font-family="{FONT_STACK}">Capabilities</text>')
    capability_blocks = [
        (220, "RPA", "Script execution", "Rule based"),
        (540, "Gen AI", "Content creation", "Decision support"),
        (860, "Agentic", "Reason + Action", "Continuous orchestration"),
    ]
    for cx, title, l1, l2 in capability_blocks:
        lines.append(f'  <text x="{cx}" y="395" text-anchor="middle" fill="{FG}" font-size="16" font-weight="600" font-family="{FONT_STACK}">{title}</text>')
        lines.append(f'  <text x="{cx}" y="425" text-anchor="middle" fill="{FG_MUTED}" font-size="13" font-family="{FONT_STACK}">{l1}</text>')
        lines.append(f'  <text x="{cx}" y="445" text-anchor="middle" fill="{FG_MUTED}" font-size="13" font-family="{FONT_STACK}">{l2}</text>')

    arrow_def = f"""
  <defs>
    <marker id="arrowSmall" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <polygon points="0 0, 6 3, 0 6" fill="{FG_MUTED}"/>
    </marker>
  </defs>"""
    return svg_wrapper(width, height, arrow_def + "\n" + "\n".join(lines))


def create_adoption_timeline_svg() -> str:
    width, height = 1100, 520
    arrow_defs = f"""
  <defs>
    <marker id="arrowSlimGreen" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <polygon points="0 0, 6 3, 0 6" fill="{ACCENT}"/>
    </marker>
    <marker id="arrowSlimGray" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <polygon points="0 0, 6 3, 0 6" fill="{FG_MUTED}"/>
    </marker>
  </defs>"""
    lines = [
        f'  <rect x="0" y="0" width="{width}" height="{height}" fill="{BG}"/>',
        f'  <text x="550" y="60" text-anchor="middle" fill="{FG}" font-size="26" font-weight="600" font-family="{FONT_STACK}">Projected Adoption Timeline</text>',
        f'  <line x1="140" y1="360" x2="960" y2="360" stroke="{SEPARATOR}" stroke-width="2"/>' ,
        f'  <circle cx="240" cy="360" r="10" fill="{ACCENT}"/>',
        f'  <text x="240" y="320" text-anchor="middle" fill="{FG}" font-size="16" font-weight="600" font-family="{FONT_STACK}">2025</text>' ,
        f'  <text x="240" y="300" text-anchor="middle" fill="{FG_MUTED}" font-size="13" font-family="{FONT_STACK}">Current state</text>' ,
        f'  <rect x="120" y="120" width="320" height="150" rx="10" fill="none" stroke="{SEPARATOR}" stroke-width="1"/>' ,
        f'  <text x="280" y="150" text-anchor="middle" fill="{FG}" font-size="16" font-weight="600" font-family="{FONT_STACK}">Acceleration signals</text>' ,
    ]
    bullets = [
        "90%+ enterprises interested",
        "Vendors prioritizing agentic AI",
        "Early ROI proof points",
        "Compressed adoption curve",
    ]
    for idx, text in enumerate(bullets):
        y = 178 + idx * 24
        lines.append(f'  <circle cx="140" cy="{y-6}" r="3" fill="{ACCENT}"/>')
        lines.append(f'  <text x="160" y="{y}" fill="{FG_MUTED}" font-size="13" font-family="{FONT_STACK}">{text}</text>')

    # Path arrows
    lines.append(f'  <path d="M 240 360 L 760 220" stroke="{ACCENT}" stroke-width="2" fill="none" marker-end="url(#arrowSlimGreen)"/>')
    lines.append(f'  <path d="M 240 360 L 760 320" stroke="{FG_MUTED}" stroke-width="2" fill="none" marker-end="url(#arrowSlimGray)"/>')

    # Boxes for timelines
    lines.append(f'  <rect x="640" y="180" width="300" height="110" rx="10" fill="none" stroke="{ACCENT}" stroke-width="1.5"/>' )
    lines.append(f'  <text x="790" y="210" text-anchor="middle" fill="{FG}" font-size="16" font-weight="600" font-family="{FONT_STACK}">Accelerated (2030-2035)</text>')
    lines.append(f'  <text x="790" y="240" text-anchor="middle" fill="{FG_MUTED}" font-size="14" font-family="{FONT_STACK}">$300-600B realized sooner</text>')

    lines.append(f'  <rect x="640" y="300" width="300" height="110" rx="10" fill="none" stroke="{FG_MUTED}" stroke-width="1.5"/>' )
    lines.append(f'  <text x="790" y="330" text-anchor="middle" fill="{FG}" font-size="16" font-weight="600" font-family="{FONT_STACK}">Conservative (2035-2040)</text>')
    lines.append(f'  <text x="790" y="360" text-anchor="middle" fill="{FG_MUTED}" font-size="14" font-family="{FONT_STACK}">Follows cloud adoption pace</text>')

    lines.append(f'  <text x="760" y="410" text-anchor="middle" fill="{FG_MUTED}" font-size="12" font-family="{FONT_STACK}">Arrow thickness represents confidence</text>')
    return svg_wrapper(width, height, arrow_defs + "\n" + "\n".join(lines))


def create_industry_impact_svg() -> str:
    width, height = 1100, 620
    industries = [
        ("Insurance", "Claims adjudication automation", "Very High"),
        ("Manufacturing", "Inventory &amp; supply chain management", "High"),
        ("Retail", "Hyper-personalization at scale", "High"),
        ("Pharmaceuticals", "Drug discovery analytics", "Medium-High"),
        ("Financial Services", "Compliance &amp; risk automation", "High"),
    ]
    lines = [
        f'  <rect x="0" y="0" width="{width}" height="{height}" fill="{BG}"/>',
        f'  <text x="550" y="60" text-anchor="middle" fill="{FG}" font-size="26" font-weight="600" font-family="{FONT_STACK}">Industry Impact Matrix</text>' ,
        f'  <line x1="120" y1="90" x2="980" y2="90" stroke="{SEPARATOR}" stroke-width="1"/>'
    ]
    y = 140
    box_height = 86
    for name, desc, impact in industries:
        lines.append(f'  <rect x="120" y="{y - 50}" width="860" height="{box_height}" rx="10" fill="none" stroke="{FG}" stroke-width="1"/>')
        lines.append(f'  <text x="150" y="{y - 15}" fill="{FG}" font-size="18" font-weight="600" font-family="{FONT_STACK}">{name}</text>')
        lines.append(f'  <text x="150" y="{y + 10}" fill="{FG_MUTED}" font-size="14" font-family="{FONT_STACK}">{desc}</text>')
        lines.append(f'  <text x="940" y="{y - 15}" text-anchor="end" fill="{FG}" font-size="16" font-weight="600" font-family="{FONT_STACK}">{impact}</text>')
        y += box_height + 20
    return svg_wrapper(width, height, "\n".join(lines))


def create_market_comparison_svg() -> str:
    width, height = 1100, 580
    bar_data = [
        ("US Application", 1000, 180),
        ("US Services", 400, 310),
        ("Global Services", 1000, 180),
        ("US Application (ref)", 1000, 310),
        ("Current IT (US)", 320, 440),
    ]
    scale = 0.6

    lines = [
        f'  <rect x="0" y="0" width="{width}" height="{height}" fill="{BG}"/>',
        f'  <text x="550" y="60" text-anchor="middle" fill="{FG}" font-size="26" font-weight="600" font-family="{FONT_STACK}">Market Comparison</text>',
        f'  <text x="280" y="100" text-anchor="middle" fill="{FG_MUTED}" font-size="14" font-family="{FONT_STACK}">United States</text>',
        f'  <text x="820" y="100" text-anchor="middle" fill="{FG_MUTED}" font-size="14" font-family="{FONT_STACK}">Global</text>'
    ]

    for label, value, y in bar_data:
        x = 180 if "Global" not in label else 720
        width_px = value * scale
        lines.append(f'  <rect x="{x}" y="{y}" width="{width_px}" height="50" fill="{ACCENT}" opacity="0.85"/>' )
        lines.append(f'  <text x="{x}" y="{y - 12}" fill="{FG}" font-size="14" font-family="{FONT_STACK}">{label}</text>')
        lines.append(f'  <text x="{x + width_px + 12}" y="{y + 30}" fill="{FG}" font-size="15" font-weight="600" font-family="{FONT_STACK}">${value if value < 1000 else "~$1T"}</text>')

    lines.append(f'  <text x="550" y="520" text-anchor="middle" fill="{FG_MUTED}" font-size="13" font-family="{FONT_STACK}">Services spend already surpasses current IT services</text>')
    return svg_wrapper(width, height, "\n".join(lines))


def main():
    output_dir = Path(__file__).parent.parent / "public" / "images" / "agentic-ai"
    output_dir.mkdir(parents=True, exist_ok=True)
    charts = {
        "market-structure.svg": create_market_structure_svg(),
        "labor-augmentation.svg": create_labor_augmentation_svg(),
        "evolution-timeline.svg": create_evolution_timeline_svg(),
        "adoption-timeline.svg": create_adoption_timeline_svg(),
        "industry-impact.svg": create_industry_impact_svg(),
        "market-comparison.svg": create_market_comparison_svg(),
    }
    print("Generating minimal SVG charts...")
    for name, svg in charts.items():
        (output_dir / name).write_text(svg, encoding="utf-8")
        print(f"✓ {name}")
    print("All charts updated.")


if __name__ == "__main__":
    main()

