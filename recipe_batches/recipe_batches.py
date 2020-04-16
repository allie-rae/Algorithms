#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    max_batches = None
    if len(recipe) == len(ingredients):
        for i in recipe:
            for j in ingredients:
                if i == j:
                    potential_batches = math.floor(ingredients[j]/recipe[i])
                    if max_batches == None:
                        max_batches = potential_batches
                    elif max_batches > potential_batches:
                        max_batches = potential_batches
        return max_batches
    else:
        return 0


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 532, 'butter': 500, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
