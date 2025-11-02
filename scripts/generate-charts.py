#!/usr/bin/env python3
"""
Generate professional charts for the Agentic AI article using matplotlib and plotly.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path
import json

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'DejaVu Sans'

# Create output directory
output_dir = Path(__file__).parent.parent / 'public' / 'images' / 'agentic-ai'
output_dir.mkdir(parents=True, exist_ok=True)

# ============================================
# Chart 1: Market Value Structure (Tree/Hierarchical)
# ============================================
def create_market_structure_chart():
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Colors
    colors = {
        'global': '#3b82f6',
        'app': '#10b981',
        'services': '#f59e0b'
    }
    
    # Top level - Global
    global_box = FancyBboxPatch((2, 7.5), 6, 0.8, 
                                boxstyle="round,pad=0.1", 
                                facecolor=colors['global'], 
                                edgecolor='#1e40af', linewidth=2)
    ax.add_patch(global_box)
    ax.text(5, 7.9, 'Global Market Opportunity', ha='center', va='center', 
            fontsize=14, fontweight='bold', color='white')
    ax.text(5, 7.5, '$0.9 - 1.1 Trillion (Services)', ha='center', va='center',
            fontsize=12, color='white')
    
    # Middle level - Application and Services
    app_box = FancyBboxPatch((1, 5), 3.5, 1.2,
                            boxstyle="round,pad=0.1",
                            facecolor=colors['app'],
                            edgecolor='#059669', linewidth=2)
    ax.add_patch(app_box)
    ax.text(2.75, 5.8, 'Application Layer', ha='center', va='center',
            fontsize=12, fontweight='bold', color='white')
    ax.text(2.75, 5.4, '~$1 Trillion (US)', ha='center', va='center',
            fontsize=11, color='white')
    ax.text(2.75, 5.1, 'Software Products & Platforms', ha='center', va='center',
            fontsize=10, color='white')
    
    services_box = FancyBboxPatch((5.5, 5), 3.5, 1.2,
                                 boxstyle="round,pad=0.1",
                                 facecolor=colors['services'],
                                 edgecolor='#d97706', linewidth=2)
    ax.add_patch(services_box)
    ax.text(7.25, 5.8, 'Services Layer', ha='center', va='center',
            fontsize=12, fontweight='bold', color='white')
    ax.text(7.25, 5.4, '$350-450B (US)', ha='center', va='center',
            fontsize=11, color='white')
    ax.text(7.25, 5.1, '$0.9-1.1T (Global)', ha='center', va='center',
            fontsize=11, color='white')
    ax.text(7.25, 4.8, 'Implementation & Support', ha='center', va='center',
            fontsize=10, color='white')
    
    # Arrows
    arrow1 = FancyArrowPatch((5, 7.5), (2.75, 6.2), 
                            arrowstyle='->', mutation_scale=20, 
                            color='#1e40af', linewidth=2)
    arrow2 = FancyArrowPatch((5, 7.5), (7.25, 6.2),
                            arrowstyle='->', mutation_scale=20,
                            color='#1e40af', linewidth=2)
    ax.add_patch(arrow1)
    ax.add_patch(arrow2)
    
    # Ratio annotation
    ax.text(5, 4.2, 'Services/App Ratio: 0.70-0.80x', 
            ha='center', va='center', fontsize=11, 
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    # Comparison
    current_box = FancyBboxPatch((1, 2), 8, 0.6,
                                boxstyle="round,pad=0.05",
                                facecolor='#e5e7eb',
                                edgecolor='#9ca3af', linewidth=1.5)
    ax.add_patch(current_box)
    ax.text(5, 2.3, 'Current IT Services (US): $320B', 
            ha='center', va='center', fontsize=11, 
            style='italic', color='#374151')
    
    plt.tight_layout()
    plt.savefig(output_dir / 'market-value-structure.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created market-value-structure.png")

# ============================================
# Chart 2: Labor Augmentation Potential (Bar Chart)
# ============================================
def create_labor_augmentation_chart():
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Data
    roles_high = ['Customer Service\nReps', 'Data\nAnalysts', 'Software\nEngineers', 
                  'Compliance\nOfficers', 'Supply Chain\nCoordinators']
    values_high = [90, 88, 87, 89, 86]
    
    roles_medium = ['Marketing\nManagers', 'HR\nCoordinators', 'Financial\nAnalysts']
    values_medium = [48, 45, 50]
    
    roles_low = ['Strategic\nPlanners', 'Executive\nLeadership']
    values_low = [18, 12]
    
    # Colors
    colors_high = plt.cm.Blues(np.linspace(0.6, 0.9, len(roles_high)))
    colors_medium = plt.cm.Oranges(np.linspace(0.5, 0.7, len(roles_medium)))
    colors_low = plt.cm.Greys(np.linspace(0.4, 0.6, len(roles_low)))
    
    # Combine all data
    all_roles = roles_high + roles_medium + roles_low
    all_values = values_high + values_medium + values_low
    all_colors = list(colors_high) + list(colors_medium) + list(colors_low)
    
    # Create horizontal bar chart
    y_pos = np.arange(len(all_roles))
    bars = ax.barh(y_pos, all_values, color=all_colors, edgecolor='white', linewidth=1.5)
    
    # Add value labels
    for i, (bar, val) in enumerate(zip(bars, all_values)):
        width = bar.get_width()
        ax.text(width + 1, bar.get_y() + bar.get_height()/2, 
                f'{val}%', ha='left', va='center', fontweight='bold', fontsize=10)
    
    # Customize axes
    ax.set_yticks(y_pos)
    ax.set_yticklabels(all_roles, fontsize=10)
    ax.set_xlabel('Augmentation Potential (%)', fontsize=12, fontweight='bold')
    ax.set_xlim(0, 100)
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    
    # Add section labels
    ax.axhline(y=len(roles_high)-0.5, color='#3b82f6', linewidth=2, linestyle='--', alpha=0.5)
    ax.text(-5, len(roles_high)-1, 'High (85-90%)', fontsize=11, fontweight='bold', 
            color='#1e40af', va='center')
    
    ax.axhline(y=len(roles_high)+len(roles_medium)-0.5, color='#f59e0b', linewidth=2, linestyle='--', alpha=0.5)
    ax.text(-5, len(roles_high)+len(roles_medium)-1, 'Medium (40-50%)', fontsize=11, fontweight='bold',
            color='#d97706', va='center')
    
    ax.text(-5, len(all_roles)-1, 'Low (<20%)', fontsize=11, fontweight='bold',
            color='#374151', va='center')
    
    ax.set_title('Labor Augmentation Potential by Role Category', 
                fontsize=14, fontweight='bold', pad=20)
    
    # Add footer
    fig.text(0.5, 0.02, 'Based on analysis of 150 job roles with 5 key criteria', 
             ha='center', fontsize=9, style='italic', color='gray')
    
    plt.tight_layout()
    plt.savefig(output_dir / 'labor-augmentation.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created labor-augmentation.png")

# ============================================
# Chart 3: Adoption Timeline
# ============================================
def create_adoption_timeline():
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.set_xlim(2024, 2045)
    ax.set_ylim(-0.5, 3)
    ax.axis('off')
    
    # Timeline base
    ax.plot([2024, 2040], [1.5, 1.5], 'k-', linewidth=3, alpha=0.3)
    
    # Current state (2025)
    ax.plot([2025, 2025], [1.3, 1.7], 'k-', linewidth=2)
    ax.text(2025, 1.0, '2025\nCurrent State', ha='center', fontsize=10, fontweight='bold')
    
    # Acceleration factors
    factors = [
        '90%+ Enterprise\nInterest',
        'Vendor Strategic\nPriority',
        'Early ROI\nProof Points'
    ]
    y_offset = 2.2
    for i, factor in enumerate(factors):
        ax.text(2025, y_offset - i*0.3, '✓ ' + factor, ha='center', 
                fontsize=9, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    
    # Accelerated timeline (2030-2035)
    acc_box = FancyBboxPatch((2029.5, 2), 6, 0.4,
                            boxstyle="round,pad=0.1",
                            facecolor='#10b981',
                            edgecolor='#059669', linewidth=2)
    ax.add_patch(acc_box)
    ax.text(2032.5, 2.2, 'Accelerated Timeline (More Likely)', 
            ha='center', va='center', fontsize=11, fontweight='bold', color='white')
    ax.text(2032.5, 2.0, '$300-600B by 2030-2035', 
            ha='center', va='center', fontsize=10, color='white')
    
    # Conservative timeline (2035-2040)
    cons_box = FancyBboxPatch((2034.5, 0.8), 6, 0.4,
                             boxstyle="round,pad=0.1",
                             facecolor='#6b7280',
                             edgecolor='#4b5563', linewidth=2)
    ax.add_patch(cons_box)
    ax.text(2037.5, 1.0, 'Conservative Timeline', 
            ha='center', va='center', fontsize=11, fontweight='bold', color='white')
    ax.text(2037.5, 0.8, '$300-600B by 2035-2040', 
            ha='center', va='center', fontsize=10, color='white')
    
    # Arrows
    arrow1 = FancyArrowPatch((2025, 1.5), (2032.5, 2.0), 
                            arrowstyle='->', mutation_scale=25, 
                            color='#10b981', linewidth=2.5)
    arrow2 = FancyArrowPatch((2025, 1.5), (2037.5, 1.0),
                            arrowstyle='->', mutation_scale=25,
                            color='#6b7280', linewidth=2.5)
    ax.add_patch(arrow1)
    ax.add_patch(arrow2)
    
    # Market realization point
    ax.plot([2032.5], [2.2], 'o', markersize=15, color='#10b981', 
            markeredgecolor='white', markeredgewidth=2)
    ax.plot([2037.5], [1.0], 'o', markersize=15, color='#6b7280',
            markeredgecolor='white', markeredgewidth=2)
    
    ax.set_title('Projected Adoption Timeline\nMarket Realization ($300-600B Global Services)', 
                fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'adoption-timeline.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created adoption-timeline.png")

# ============================================
# Chart 4: Industry Impact Matrix (Heatmap)
# ============================================
def create_industry_impact_matrix():
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Data
    industries = ['Insurance', 'Manufacturing', 'Retail', 'Pharmaceuticals', 'Financial Services']
    impact_levels = [5, 4, 4, 3.5, 4]  # Very High, High, High, Medium-High, High
    use_cases = [
        'Claims adjudication\nautomation',
        'Inventory & supply\nchain management',
        'Hyper-personalization\nat scale',
        'Drug discovery\nanalytics',
        'Compliance & risk\nautomation'
    ]
    
    # Create horizontal bars with gradient
    colors_map = {5: '#dc2626', 4: '#f59e0b', 3.5: '#eab308', 3: '#84cc16'}
    colors = [colors_map[level] for level in impact_levels]
    
    y_pos = np.arange(len(industries))
    bars = ax.barh(y_pos, impact_levels, color=colors, edgecolor='white', linewidth=2, alpha=0.8)
    
    # Add use case labels on bars
    for i, (bar, use_case, level) in enumerate(zip(bars, use_cases, impact_levels)):
        width = bar.get_width()
        # Use case text
        ax.text(width/2, bar.get_y() + bar.get_height()/2, 
                use_case, ha='center', va='center', 
                fontsize=9, fontweight='bold', color='white')
        # Impact level badge
        level_text = 'Very High' if level == 5 else 'High' if level == 4 else 'Medium-High'
        ax.text(width + 0.2, bar.get_y() + bar.get_height()/2,
                level_text, ha='left', va='center',
                fontsize=10, fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='white', edgecolor=colors[i], linewidth=2))
    
    # Customize
    ax.set_yticks(y_pos)
    ax.set_yticklabels(industries, fontsize=12, fontweight='bold')
    ax.set_xlabel('Impact Level', fontsize=12, fontweight='bold')
    ax.set_xlim(0, 6)
    ax.set_title('Industry Impact Matrix', fontsize=14, fontweight='bold', pad=20)
    
    # Legend
    legend_elements = [
        mpatches.Patch(color='#dc2626', label='Very High Impact'),
        mpatches.Patch(color='#f59e0b', label='High Impact'),
        mpatches.Patch(color='#eab308', label='Medium-High Impact')
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=10)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'industry-impact.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created industry-impact.png")

# ============================================
# Chart 5: Evolution Timeline (Flow Diagram)
# ============================================
def create_evolution_timeline():
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.set_xlim(-1, 11)
    ax.set_ylim(0, 4)
    ax.axis('off')
    
    # Eras
    eras = [
        {'name': 'RPA Era\n(2010s)', 'x': 1.5, 'color': '#94a3b8', 'features': ['Scripted\nTasks', 'Brittle\nStatic']},
        {'name': 'Gen AI Era\n(2020s)', 'x': 5, 'color': '#60a5fa', 'features': ['Isolated\nAssistants', 'Human-\nDependent']},
        {'name': 'Agentic AI\n(2025+)', 'x': 8.5, 'color': '#10b981', 'features': ['Autonomous\nSystems', 'Self-Driven\nAdaptive']}
    ]
    
    # Draw boxes and arrows
    for i, era in enumerate(eras):
        # Main box
        box = FancyBboxPatch((era['x']-0.8, 1.5), 1.6, 1.2,
                            boxstyle="round,pad=0.15",
                            facecolor=era['color'],
                            edgecolor='white', linewidth=2.5, alpha=0.9)
        ax.add_patch(box)
        
        # Era name
        ax.text(era['x'], 2.7, era['name'], ha='center', va='center',
                fontsize=11, fontweight='bold', color='white')
        
        # Features
        for j, feature in enumerate(era['features']):
            ax.text(era['x'], 2.2 - j*0.35, feature, ha='center', va='center',
                   fontsize=9, color='white', style='italic')
        
        # Arrows between eras
        if i < len(eras) - 1:
            arrow = FancyArrowPatch((era['x']+0.8, 2.1), (eras[i+1]['x']-0.8, 2.1),
                                   arrowstyle='->', mutation_scale=30,
                                   color='#374151', linewidth=2.5)
            ax.add_patch(arrow)
    
    # Capabilities comparison
    capabilities = [
        'RPA: Script execution, rule-based',
        'Gen AI: Content creation, analysis',
        'Agentic: Reasoning + Action + Adaptation'
    ]
    ax.text(5, 0.5, 'Key Capabilities:', ha='center', fontsize=10, fontweight='bold')
    for i, cap in enumerate(capabilities):
        ax.text(1.5 + i*4, 0.2, cap, ha='center', fontsize=9,
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))
    
    # Title
    ax.text(5, 3.8, 'Automation Evolution', ha='center', 
           fontsize=16, fontweight='bold', color='#1e40af')
    ax.text(5, 3.5, 'Convergence & Evolution', ha='center',
           fontsize=11, style='italic', color='#6b7280')
    
    plt.tight_layout()
    plt.savefig(output_dir / 'evolution-timeline.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created evolution-timeline.png")

# ============================================
# Chart 6: Market Value Comparison (Grouped Bar)
# ============================================
def create_market_comparison():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Left chart - US Market
    categories_us = ['Application\nLayer', 'Services\nLayer', 'Current IT\nServices']
    values_us = [1000, 400, 320]  # Billions
    colors_us = ['#10b981', '#f59e0b', '#94a3b8']
    
    bars1 = ax1.bar(categories_us, values_us, color=colors_us, 
                    edgecolor='white', linewidth=2, alpha=0.9)
    
    for bar, val in zip(bars1, values_us):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 20,
                f'${val}B', ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    ax1.set_ylabel('Value (Billions USD)', fontsize=11, fontweight='bold')
    ax1.set_title('U.S. Market Structure', fontsize=12, fontweight='bold', pad=15)
    ax1.set_ylim(0, 1100)
    ax1.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Right chart - Global Services
    categories_global = ['Services Layer\n(Global)', 'Application Layer\n(US Only)']
    values_global = [1000, 1000]  # Trillions/Billions normalized
    colors_global = ['#3b82f6', '#10b981']
    
    bars2 = ax2.bar(categories_global, values_global, color=colors_global,
                    edgecolor='white', linewidth=2, alpha=0.9)
    
    labels = ['$0.9-1.1T', '~$1T']
    for bar, val, label in zip(bars2, values_global, labels):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 50,
                label, ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    ax2.set_ylabel('Value (Trillions USD)', fontsize=11, fontweight='bold')
    ax2.set_title('Global Market Opportunity', fontsize=12, fontweight='bold', pad=15)
    ax2.set_ylim(0, 1200)
    ax2.grid(axis='y', alpha=0.3, linestyle='--')
    
    fig.suptitle('Agentic AI Market Value Structure', 
                fontsize=14, fontweight='bold', y=1.02)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'market-comparison.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created market-comparison.png")

if __name__ == '__main__':
    print("Generating professional charts for Agentic AI article...\n")
    
    try:
        create_market_structure_chart()
        create_labor_augmentation_chart()
        create_adoption_timeline()
        create_industry_impact_matrix()
        create_evolution_timeline()
        create_market_comparison()
        
        print("\n✅ All charts generated successfully!")
        print(f"📁 Charts saved to: {output_dir}")
        
    except Exception as e:
        print(f"\n❌ Error generating charts: {e}")
        import traceback
        traceback.print_exc()

