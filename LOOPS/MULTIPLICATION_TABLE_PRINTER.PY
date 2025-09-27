#PRINT THE MULTIPLICATION TABLE FOR A GIVEN NUMBER UP TO 10.BUT SKIP THE FIFTH ITERATION.

num=int(input("Enter number whose table you want to calculate:\n"))
for i in range(1,11):
        if i==5:
            continue
        print(f"{num}X{i}={num*i}")
        
        