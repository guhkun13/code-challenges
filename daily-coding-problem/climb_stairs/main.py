"""_summary_
There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X.

"""

def my_func(N:int, X:set) :
  print(f"N stairs = {N} | allowed steps : {X}")

  fs = []  
  for x in X:
    print("===============")
    print(f"fx = {x}")  

    gs = []
    tn = N 
    while tn > 0:
      print(f"{tn} - {x}")  
      tn = tn - x
      print(f"= {tn}")  
      gs.append(x)
      print(f"gs = {gs}")  

    fs.append(gs)
  
  print(f"found_steps = {fs}")

my_func(4, {2,1})