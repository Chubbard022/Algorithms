#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  count = []
  batch_count = 0

  if len(recipe) != len(ingredients):
    return batch_count

  for ingredient in recipe:
    count.append(ingredients[ingredient]//recipe[ingredient])
  
  batch_count = min(count)
  return batch_count
  # for item in recipe:



# batch = []
# num = { 'milk': 2, 'sugar': 40, 'butter': 20 }

# ing =  { 'milk': 5, 'sugar': 120, 'butter': 500 }

# for item in num:
#  batch.append(ing[item]//num[item])

# print(batch)

# print(min(batch))


