from utils_june import *
from fitness import fitness_calculate
import numpy as np

def PSO():
    num_particles = 500 #number of particles
    iterations = 200
    particles = np.random.uniform(demand[0], demand[1], (num_particles, T)) 
    c1_initial, c2_initial = 2.5, 0.5
    c1_final, c2_final = 0.5, 2.5
    w_max, w_min = 0.9, 0.4
    velocity = np.random.uniform(-1, 1, (num_particles, T))
    pbest = np.copy(particles)
    pbest_fitness = np.full(num_particles, -np.inf)
    gbest = np.copy(pbest[0])
    gbest_fitness = -np.inf
    for i in range(iterations):
        # Update c1 and c2 adaptively
        c1 = c1_initial - (c1_initial - c1_final) * (i / iterations)
        c2 = c2_initial + (c2_final - c2_initial) * (i / iterations)

        # Update inertia weight adaptively
        w = w_max - (w_max - w_min) * (i / iterations)

        for j in range(num_particles):
            r1 = np.random.uniform(0, 1)
            r2 = np.random.uniform(0, 1)

            inertia_weight = w * velocity[j]
            cognitive_part = c1 * r1 * (pbest[j] - particles[j])
            social_part = c2 * r2 * (gbest - particles[j])

            velocity[j] = inertia_weight + cognitive_part + social_part
            particles[j] += velocity[j]

            # Keep particles within bounds
            particles[j] = np.clip(particles[j], demand[0], demand[1])

            fitness = fitness_calculate(particles[j])
            if fitness > pbest_fitness[j]:
                pbest[j] = particles[j]
                pbest_fitness[j] = fitness
                

        # Update global best
        gbest_candidate = pbest[np.argmax(pbest_fitness)]
        gbest_fitness_candidate = np.max(pbest_fitness)
        if gbest_fitness_candidate > gbest_fitness:
            gbest = gbest_candidate
            gbest_fitness = gbest_fitness_candidate
        
    return gbest