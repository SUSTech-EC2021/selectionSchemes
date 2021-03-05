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

selector_to_call = getattr(selection_schemes, 'linear_ranking_selection') 
for alpha in [0, 0.5, 1]:
  plot_pie(selector_to_call(fitness_list, alpha), labels, 'lec3-linear_ranking_selection-alpha'+str(alpha))