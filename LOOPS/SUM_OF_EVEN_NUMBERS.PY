# CALCULATE THE SUM OF EVEN NUMBERS UP TO A GIVEN NUMBER N
num=int(input("Enter the number:"))
sum=0
for i in range(1, num+1):
    if i%2==0:
        sum+=i
print(sum)
        