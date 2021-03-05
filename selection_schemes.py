#!/usr/bin/env python

import math
# Selection schemes

def roulette_wheel_selection( fitness_list ):
  sum_fitness = sum(fitness_list)
  prob_list = []
  for fitness in fitness_list:
    prob_list.append(fitness/sum_fitness)
  print ('Output of roulette_wheel_selection: ')
  print(prob_list)
  return prob_list

def rank_based_selection (fitness_list):
  ascending_rank = sorted(range(len(fitness_list)), key=lambda k: fitness_list[k], reverse=True)
  prob_list = []
  sum_rank = sum(ascending_rank) + len(ascending_rank)  
  for rank in ascending_rank:
    prob_list.append((rank+1)/sum_rank)
  print ('Output of rank_based_selection: ')
  print(prob_list)
  return prob_list

def linear_ranking_selection (fitness_list, alpha=0):
  ascending_rank = sorted(range(len(fitness_list)), key=lambda k: fitness_list[k], reverse=True)
  beta = 2 - alpha
  mu = len(fitness_list)
  offset = alpha/mu
  coef = (beta-alpha) / (mu-1) / mu
  prob_list = []
  for rank in ascending_rank:
    prob_list.append( coef * rank + offset)
  print ('Output of linear_ranking_selection: ')
  print(prob_list)
  return prob_list

def exponential_ranking_selection (fitness_list):
  ascending_rank = sorted(range(len(fitness_list)), key=lambda k: fitness_list[k], reverse=True)
  mu = len(fitness_list)
  C = mu - ( math.exp(1) - math.exp(1-mu) ) / ( math.exp(1) -1 )
  prob_list = []
  for rank in ascending_rank:
    prob_list.append( ( 1 - math.exp(-rank)) / C )
  print ('Output of exponential_ranking_selection: ')
  print(prob_list)
  return prob_list

