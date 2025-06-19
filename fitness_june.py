from utils_june import *
def fitness_calculate(release, st=S_in):
    total_objective = 0
    storage = np.zeros(len(release) + 1)
    storage[0] = st
    D_max = demand[1]
    dem = np.full(T,demand[1])
    
    for t in range(len(release)):

        # Calculate storage before overflow (Equation 18)
        S_before_overflow = storage[t] + inflows[t] - release[t] - ET[t] - env_flow[t]
        
        # Calculate overflow (Equation 22)
        overflow = max(0, S_before_overflow - S_max)
        
        # Update storage after overflow
        S = S_before_overflow - overflow
        
        # Calculate penalties
        # P1: Minimum storage violation (Equation 23)
        P1 = 0
        if S < S_min:
            P1 = ((S_min - S) / S_min) ** 2
        
        # P2: Maximum storage violation (Equation 24)
        P2 = 0
        if S > S_max:
            P2 = ((S - S_max) / S_max) ** 2
        
        
        
        P3 = 0
        if release[t] < env_flow[t]:
            P3 = ((release[t] - env_flow[t]) / env_flow[t]) ** 2
        
        # Objective function component for current timestep (Equation in 2.4.6)
        deficit_term = ((release[t] - dem[t]) / D_max) ** 2
        
        # Sum up the objective for this timestep
        total_objective += deficit_term + P1 + P2 + P3 
        
        # Update storage for next timestep
        storage[t + 1] = S
    
    return -total_objective