import random as rd
import sys
import math

# This is sampe to uses genetic algorithm to maximize a function of many variables
# we need fitness funtion to define how fit an invidiual is
# selection function to choose the fitness one
# reproduction fucntion to produce new one

def fitness_function(w, x, y, z):
    return -2 * (w**2) + math.sqrt(abs(w)) - (x**2) + 6*x- (y**2) - 2*y - (z**2) + 4*z

def simple_fitness_function(x, y):
    return -(x**2) + 2*x - y**2 + 4*y

def evaluate_generation(population):
    scores = []
    total = 0
    for individual in population:
        if len(individual) == 2:
            r = simple_fitness_function(individual[0], individual[1])
            total += r
            scores.append(r)
        elif len(individual) == 4:
            r = fitness_function(individual[0], individual[1], individual[2], individual[3])
            total += r
            scores.append(r)
        else:
            print("error: wrong number of arguments")
    avg = total/len(scores)
    return scores, avg

# create child from parent
def mutate(individual):
    new = []
    for attribute in individual:
        new.append(attribute + rd.normalvariate(0, attribute + .1))
    return new

# Given a population return the best individual and the associated value
def find_best(population):
    best = None
    val = None
    for individual in population:
        if len(individual) == 2:
            r = simple_fitness_function(individual[0], individual[1])
            try:
                if r > val:
                    best = individual
                    val = r
            except:  # On the first run, set the result as best
                best = individual
                val = r
        elif len(individual) == 4:
            r = fitness_function(individual[0], individual[1], individual[2], individual[3])
            try:
                if r > val:
                    best = individual
                    val = r
            except:  # On the first run, set the result as best
                best = individual
                val = r
        else:
            print("error: Wrong number of arguments received")
    return best, val

# Create a population of p lists of [0, 0, ..., 0] of length n
def initialize(n, p):
    pop = [[0] * n]
    for i in range(p):
        pop.append(mutate(pop[0]))
    return pop

def termination(best, val, total_iterations, population_size, num_attri):
    best = [round(x, 3) for x in best]  #  Round for printing
    print("Ran", total_iterations, "iterations on a population of", population_size)
    print("The optimal input is", best, "with a value of", round(val, 3))
    if num_attributes == 2:
        print("The known maximum is at [1, 2] with a value of 5")
    elif num_attributes == 4:
        print("The known maximum is at [-.25, 3, -1, 2] with a value of 14.375")
    else:
        print("Error: Unsupported Individual Length")

if __name__ == "__main__":
    if len(sys.argv) != 4: # attrs switches between simple and full fitness_function, pop determines population size, iter determines iterations
        print("Usage: python geneticmax.py attrs(2 or 4) pop iter")
        exit()
    num_attributes = int(sys.argv[1])
    population_size = int(sys.argv[2])
    total_iterations = int(sys.argv[3])
    population = initialize(num_attributes, population_size)
    for iteration in range(total_iterations):
        scores, avg = evaluate_generation(population)
        deleted = 0
        new_population = []
        for i in range(len(population)):
            if scores[i] < avg:
                deleted += 1
            else:
                new_population.append(population[i])
        for i in range(deleted):
            new_population.append(mutate(new_population[i % len(new_population)])) # iterate over population with overflow protection
        population = new_population
    best, val = find_best(population)
    termination(best, val, total_iterations, population_size, num_attributes)
