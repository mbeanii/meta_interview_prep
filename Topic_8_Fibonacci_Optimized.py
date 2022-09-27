hashmap = {
    0: 0,
    1: 1
}

def my_fib(n: int) -> int:
    """ Computes the fibonacci sequence recursively up to the given value

    Inputs:
      n (int): The index for the fibonacci number to compute and return

    Outputs:
      The fibonacci sum in the nth position

    Raises:
      Nothing
    """
    # 0 1 1 2 3 5 8...
    # every element is the sum of the previous two elements

    if n == 0:
        return 0    ## This block is back by popular demand (tripped an edge case without it)
    if n == 1:
        return 1

    # Maybe this is all you need to optimize?
    # If n-1 is in the hashmap that implies n-2 is in there already as well. Then all we have to do is add them together
    # If n-2 is in the hashmap we know n-1 was not so compute and add n-1 to the hashmap recursively.
    # Ah. What if neither of them are in the hashmap?
    # And actually what if one is but not the other because I'm realizing my assumption above was false. I think we
    # need a truth table here.

    if   ((n - 1) in hashmap) and ((n - 2) in hashmap):
        return hashmap[n - 1] + hashmap[n - 2]
    elif ((n - 1) in hashmap) and ((n - 2) not in hashmap):
        hashmap[n - 2] = my_fib(n - 2)
    elif ((n - 1) not in hashmap) and ((n - 2) in hashmap):
        hashmap[n - 1] = my_fib(n - 1)
    elif ((n - 1) not in hashmap) and ((n - 2) not in hashmap):
        hashmap[n - 1] = my_fib(n - 1)

    return hashmap[n - 1] + hashmap[n - 2]

    # Ok, I think this is logically tight. Not going to run off the end of the function at any point
    # Also, I think there may still be some redunancy here, but if so it will be solved with lookup operations, not
    # calculations. We should just be performing each addition once now.
    # Read it over and fixed a couple of things. Running.
    # Got an infinite recursion on 1. Not a good sign. Oh, right becasue fib(-1) is undefined. Caught an edge case.
    # Lemme put those instant returns back in there.
    # 1, 2, 3 worked properly. 4 returned "None". Interesting.
    # Think I got bit by order of operations. Tightening up with more parens. Nope that wasn't it.
    # Must be an issue with my recursing in the last elif
    #
    # Ran 4 through the logic and figured out the problem. after we assign everything we need recursively to the table
    # we are not returning the result xD
    #
    # 40 was practically instant.
    # Amazing. Last time it took about 30 seconds.
    # Just did 100 in just a quick blip as well.
    # 200 was no problem
    # 300... No, it's struggling with 300. As its been a minute or so, I'm turning it off.
    # Really cool stuff here :) Pushing.




N = input()
print(my_fib(int(N) - 1))

# Optimization thoughts.
# Basically, just see if it's been computed already and if it has, just get the answer and if it hasn't memoize it.