#!/usr/bin/env python

import os, sys, inspect
sys.path.append(os.getcwd())
from selection_schemes import *
from myplot import *
from fitness_scaling import *
from sample_fitness import *

labels = 'Individual 1', 'Individual 2', 'Individual 3', 'Individual 4'
individuals = [13, 24, 8, 19]

fitness_list = []
for x in individuals:
  fitness_list.append(quadratic_fitness(x))

scaled_fitness_list = simple_fitness_scaling(fitness_list)
plot_pie(roulette_wheel_selection(scaled_fitness_list), labels, 'lec3-scaled_roulette_wheel_selection')

sigma_fitness_list = sigma_fitness_scaling(fitness_list)
plot_pie(roulette_wheel_selection(sigma_fitness_list), labels, 'lec3-sigma_roulette_wheel_selection')

power_fitness_list = power_fitness_scaling(fitness_list)
plot_pie(roulette_wheel_selection(power_fitness_list), labels, 'lec3-power_roulette_wheel_selection')
