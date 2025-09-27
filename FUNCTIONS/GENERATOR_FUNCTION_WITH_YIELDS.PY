#WRITE A GENERATOR FUNCTION THAT YEILDS EVEN NUMBERS UP TO A SPECIFIC LIMIT.
def even_generator(lim):
    
    for i in range(1,lim+1):
        if i%2==0:
            #print(i)
            yield i
            
for num in even_generator(20):
    print(num)