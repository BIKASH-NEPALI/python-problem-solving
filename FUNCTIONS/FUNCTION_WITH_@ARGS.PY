# write a function that takes variable number of sum arguments and returns theri sum.
def sum_all(*args):
    for i in args:
        print(i*2)
    return sum(args)
print(sum_all(1,2))
print(sum_all(4,5,6,3))