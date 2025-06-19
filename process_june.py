import numpy as np
import matplotlib.pyplot as plt
from utils_june import *


def processing(best_release):  
    # Initialize variables
    St = np.zeros(T + 1)
    spill = np.zeros(T)
    head = np.zeros(T)
    power = np.zeros(T)
    dry_energy = 0
    wet_energy = 0
    
    St[0] = S_in  # Initial storage
    
    # Loop over time periods (months)
    for t in range(T):
        R = best_release[t]
        
        # Update storage
        St[t + 1] = St[t] + inflows[t] - R - env_flow[t] - ET[t]
        
        # Check for spill and adjust storage
        if St[t + 1] > S_max:
            R = demand[1]
            St[t + 1] = St[t] + inflows[t] - R - env_flow[t] - ET[t]
            if St[t + 1] > S_max:
                spill[t] = St[t + 1] - S_max
                St[t + 1] = S_max
        elif St[t + 1] < S_min:
            R = demand[0]
            St[t + 1] = St[t] + inflows[t] - R - env_flow[t] - ET[t]
            if St[t + 1] < S_min:
                R = 0
                St[t + 1] = max(S_min, St[t] + inflows[t] - R - env_flow[t] - ET[t])
        
        # Calculate head and power
        head[t] = calculate_head(0.5 * (St[t] + St[t + 1]))
        power[t] = calculate_power(R, head[t])
        
        # Seasonal energy calculation
        if t % 12 in dry_months:
            dry_energy += power[t] * 30.416 * H / 1000
        else:
            wet_energy += power[t] * 30.416 * H / 1000
    
    # Energy calculations
    avg_dry_energy = dry_energy / years
    avg_wet_energy = wet_energy / years
    total_energy = avg_dry_energy + avg_wet_energy
    
    # Display results
    print("\n" + "="*50)
    print("ENERGY PRODUCTION SUMMARY".center(50))
    print("="*50)
    print(f"{'Dry Season Energy:':<25} {avg_dry_energy:>10.2f} GWh")
    print(f"{'Wet Season Energy:':<25} {avg_wet_energy:>10.2f} GWh")
    print("-"*50)
    print(f"{'Total Annual Energy:':<25} {total_energy:>10.2f} GWh")
    print("="*50)

    
    # Plotting
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    months = np.arange(1, T + 1)
    
    ax1.plot(months, power, marker='o', linestyle='-', color='#2ecc71', 
             linewidth=2, markersize=4, label='Power')
    ax1.set_title('Power Generation Over Time', fontsize=12)
    ax1.set_ylabel('Power (MW)', fontsize=10)
    ax1.grid(True, linestyle='--', alpha=0.7)
    ax1.legend()
    
    ax2.plot(months, St[:-1], marker='o', linestyle='-', color='#3498db', 
             linewidth=2, markersize=4, label='Storage')
    ax2.fill_between(months, St[:-1], alpha=0.3, color='#3498db')
    ax2.axhline(y=S_max, color='r', linestyle='--', label='Max Storage')
    ax2.axhline(y=S_min, color='orange', linestyle='--', label='Min Storage')
    ax2.set_title('Reservoir Storage Volume', fontsize=12)
    ax2.set_xlabel('Months', fontsize=10)
    ax2.set_ylabel('Storage (Million m³)', fontsize=10)
    ax2.grid(True, linestyle='--', alpha=0.7)
    ax2.legend()
    
    plt.tight_layout()
    plt.show()
    
    # Convert units if conversion factors are provided
    inf = inflows/conv if 'conv' in globals() else inflows
    rel = best_release/cnv_ if 'cnv_' in globals() else best_release
    
    # Monthly report for shorter simulations
    if T <= 12:
        print("\nDETAILED MONTHLY REPORT")
        print("="*80)
        print(f"{'Month':^8}{'Inflow':^15}{'Release':^15}{'Storage':^15}{'Power':^15}")
        print("-"*80)
        for t in range(T):
            print(f"{t+1:^8}{inf[t]:^15.2f}{rel[t]:^15.2f}{St[t]:^15.2f}{power[t]:^15.2f}")
        print("="*80)
    
    print(f"\nAverage Annual Release: {sum(rel) / years:.2f} Million m³")
    