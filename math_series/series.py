def fibonacci(n):
    if n <=0:
      print("")
    elif n==1:
      return 0
    elif n==2:
      return 1
    else:
      return fibonacci(n-1) + fibonacci(n-2)



def lucas(n):
    if (n == 0):
        return 2
    if (n == 1):
        return 1

    return lucas(n-1) + lucas(n-2)


def sum_series(i, a=0, b=1):
    if(a == 0 and b == 1):
      if i - 1 == 0:
        return a
      if i - 1 == 1:
        return b
      return sum_series(i - 1, a, b) + sum_series(i - 1, a, b)
    else:
      if i == 1:
        return a
      if i == 2:
        return b
      return sum_series(i - 1, a, b) + sum_series(i - 2, a, b)
