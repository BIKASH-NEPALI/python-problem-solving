def sumall(*args):
    print(args)# treats as tuples
    for el in args:
        print(el*2)
    return sum(args)
print(sumall(3,4,5))
print(sumall(4,5))