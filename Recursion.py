#Re


#  def Recursion(n):
#  if n==0 or n ==1 :
#     return 1
#  else:
#    return n* Recursion(n-1)
# print(Recursion(5))
    

# // ibonacci
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(11))  # Output: 5
