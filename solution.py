#!/usr/bin/env python3

"""
The Short-Bread Problem

The goal of this exercise is to write a function `find_shortest_path` that can,
given a start and end word and dictionary of valid words as inputs, return the
shortest path from start to end as a list.

For this exercise:
    - Two words are defined as adjacent if they are the same length, are both
      valid words (members of the dictionary), and have exactly one letter
      difference between them.
    - A path between two words is defined as any list where the given words
      are the first and last members of the list, and all adjacent items in the
      list are adjacent words as defined above.

If there is no valid path from the start word to the end word, the function
should instead return an empty list. If multiple paths of the same length exist
you should return any one of them.

For example, given inputs 'shirt' and 'shore', your function could return
`['shirt', 'short', 'shore']` or `['shirt', 'shire', 'shore']`.

You should focus on correctness over performance for this exercise. You can
test your solution at any time by running this Python file.
"""

import csv


def load_dictionary():
    dictionary = []
    with open('words.csv') as csvfile:
        reader = csv.reader(csvfile)
        dictionary = [row[0] for row in reader if len(row) > 0]
    return dictionary


def find_shortest_path(start, end, dictionary):
    """
    Please complete this function. You may also define new functions as required.
    """
    adjacents = breadth_first_search(start,dictionary)
    print(adjacents)

def breadth_first_search(start,dictionary):
        adjacents = []

        for word in dictionary:
            if len(word) ==  5:
                 counter = 0

                 for a in range(0,len(start)):
                    if counter == len(word) - 1:
                        adjacents.append(word)
                        break
                    
                    for i in range(0,len(word)):
                        if word[i] == start[a]:
                            counter = counter + 1
                            break

        return adjacents


if __name__ == '__main__':
    dictionary = load_dictionary()
    path = find_shortest_path('short', 'bread', dictionary)
    print(path)
