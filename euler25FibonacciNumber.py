#The Fibonacci sequence is defined by the recurrence relation:

#Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#The 12th term, F12, is the first term to contain three digits.

#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


def FibonacciNumber(n):
    #n number of digits
    a = 1
    b = 0
    i = 1
    while len(str(a)) != n:
        a, b = a +b, a
        i += 1
    return i



final = FibonacciNumber(1000)
print(final)