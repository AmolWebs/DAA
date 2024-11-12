# def recursive_fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)


# fibo_range = int (input ("Enter fibonacci series range : "))
# for i in range(fibo_range):
#     print(recursive_fibonacci(i))













def fibonacci_series(n):
    if n<=1:
        return n
    else:
        return fibonacci_series(n-1) + fibonacci_series(n-2)

fibo_input = int(input("Enter fibonacci series range : "))
for i in range(fibo_input+1):
    print(fibonacci_series(i))




















