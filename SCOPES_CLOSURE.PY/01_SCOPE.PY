# username="BIKASH-NEPALI"
# print(username)  
x=99
# def function(y):
#     z=x+y
#     return z 
# print(function(4))
# def function3():
#     global x
#     x=88
# function3()  
# print(x)
def fun4():
    #x=88
    def func2():
        print(x)
    return func2
result=fun4()
result()