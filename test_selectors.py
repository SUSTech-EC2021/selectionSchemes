#!/usr/bin/env python

import os, sys, inspect
sys.path.append(os.getcwd())
import selection_schemes
from myplot import *
from fitness_scaling import *
from sample_fitness import *

labels = 'Individual 1', 'Individual 2', 'Individual 3', 'Individual 4'
individuals = [13, 24, 8, 19]

fitness_list = []
for x in individuals:
  fitness_list.append(quadratic_fitness(x))


for selector_name in ['roulette_wheel_selection', 'rank_based_selection', 'linear_ranking_selection', 'exponential_ranking_selection']:
  selector_to_call = getattr(selection_schemes, selector_name)
  plot_pie(selector_to_call(fitness_list), labels, 'lec3-'+selector_name)
  print (sum(selector_to_call(fitness_list)))
