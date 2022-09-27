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
        return 0
    if n == 1:
        return 1

    return my_fib(n - 1) + my_fib(n - 2)


N = input()
print(my_fib(int(N) - 1))

# I think this will run as is. Guessing there are some optimization issues I'll hit,
# but I did write it myself without looking at anything, so I'm pleased with that.
# A quick proofread walkthrough is in order.

# Walkthrough has caught two issues. Go walkthrough!
# And a third!
# And a fourth!

# Happy with it :) Walked it through. Running. Then will try some memoization

# The language choices for this one are kind of weird. clojure. elixer. F#. Lisp.
# Random...

# Will run a few in pycharm and check against the internet for accuracy. Then will optimize.
# Boo. I seem to have gotten caught in an infinite loop somehow.
# Ah yes, I overcompensated for my off by one error so when I passed 1 it ran 0 and I also incremented my ifs to look
# for 1 and 2 so it recursed 0 a billion times til I told it to stop. Running again.
# Still...
# Something strange is afoot. Pycharm mistake. I am running the wrong file.

# Ok cool it works!! Pushing and optimizing in a new file.
