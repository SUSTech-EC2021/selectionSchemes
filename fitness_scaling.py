#!/usr/bin/env python
import numpy as np
import math

def simple_fitness_scaling (fitness_list):
  worst_fitness = min(fitness_list)
  scaled_fitness_list = []
  for fitness in fitness_list:
    scaled_fitness_list.append(fitness - worst_fitness)
  print ('Output of simple_fitness_scaling: ')
  print(scaled_fitness_list)
  return scaled_fitness_list

# the worst_fitness_sliding_window is calculated outside of this function
def fitness_scaling_sliding_window (fitness_list, worst_fitness_sliding_window):
  sliding_window_fitness_list = []
  for fitness in fitness_list:
    sliding_window_fitness_list.append(fitness - worst_fitness_sliding_window)
  print ('Output of simple_fitness_scaling: ')
  print(sliding_window_fitness_list)
  return sliding_window_fitness_list

def sigma_fitness_scaling (fitness_list, c=1):
  offset = np.mean(fitness_list) - ( c * np.std(fitness_list) )
  sigma_fitness_list = []
  for fitness in fitness_list:
    sigma_fitness_list.append(max(fitness - offset, 0))
  print ('Output of sigma_fitness_scaling: ')
  print (sigma_fitness_list)
  return sigma_fitness_list

def power_fitness_scaling (fitness_list, power=2):
  power_fitness_list = []
  for fitness in fitness_list:
    power_fitness_list.append(math.pow(fitness, power))
  print ('Output of power_fitness_scaling: ')
  print (power_fitness_list)
  return power_fitness_list

def exponential_fitness_scaling (fitness_list, T=0.1):
  exponential_fitness_list = []
  for fitness in fitness_list:
    exponential_fitness_list.append(math.exp(fitness/T))
  print ('Output of exponential_fitness_scaling: ')
  print (exponential_fitness_list)
  return exponential_fitness_list