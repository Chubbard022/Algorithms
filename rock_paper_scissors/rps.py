#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  outcome = []
  plays = ["rock","paper","scissors"]

  def rounds_played(round_left,result):
    #base case
    if round_left == 0:
      outcome.append(result)
      return
    for play in plays:
      rounds_played(round_left -1,result + [play])
  
  rounds_played(n,[])

  return outcome


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')


  test1 = rock_paper_scissors(0)
  print(test1)



# create a function that takes in the number of plays per round
  # create an empty list that holds the outcome
  # create a list that holds all possible plays


 