import pandas as pd
import numpy as np

# total hours in a year = 8760, total hours in month(equal) = 730
conv = 3600 * 730 / 1e6
H = 12 #operation hour
cnv_ = 3600 * H * 30.4617 / 1e6

pet = np.full(12,0) #mm/day Evapotranspiration
inflow = [108,67,49,42,48,79,140,308,567,607,439,210] #Nov-Oct (dry = dec- may)
dry_months = [1,2,3,4,5,6] #Dec-May

inflows = np.array(inflow) * conv #convert m3/s to MM3
ET = np.array(pet) * (63 + 39) / 2000 #convert mm/day to MM3
T = 12
years = 1

env_flow = np.full(12,0)
S_in = 4467  #initial storage 
demand = [112 * cnv_, 672 * cnv_] #demand fix
max_turbine_discharge = demand[1]
S_max = 4467
S_min = 2242
gamma = 9.81
effi = 0.91
fp = gamma*effi*200/cnv_/1000 #to use for penalty in order to change into power

def calculate_head(storage):
    height = -2*10**-6*storage**2+0.0335*storage+104.26
    return min(210, height)

def calculate_power(release, head):
    """Calculate the power generated based on release and head."""
    return min(1200, head * release * gamma * effi / cnv_ / 1000)  # Convert to MW