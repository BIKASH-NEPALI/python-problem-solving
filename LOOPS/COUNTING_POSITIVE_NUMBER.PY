#GIVEN NUMBER OF LIST , COUNT HOW MANY NUMBERS ARE POSITIVE.
numbers=[4,5,3,-3,-7,0,-1]
count_postive=0
for el in numbers:
    if el>0:
        count_postive+=1
print(f"total postive numbers are: {count_postive}")