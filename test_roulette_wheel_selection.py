#!/usr/bin/env python

import os, sys, inspect
sys.path.append(os.getcwd())
from selection_schemes import *
from myplot import *
import sample_fitness

individuals = [13, 24, 8, 19]


labels = 'Individual 1', 'Individual 2', 'Individual 3', 'Individual 4'

for fitness_name in ['quadratic_fitness', 'quadratic_fitness1000', 'quadratic_fitness10000']:
  fitness_to_call = getattr(sample_fitness, fitness_name)
  fitness_list = []
  for x in individuals:
    fitness_list.append(fitness_to_call(x))
  plot_pie(roulette_wheel_selection(fitness_list), labels, 'lec3-'+fitness_name)

