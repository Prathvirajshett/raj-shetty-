#sum of odd and even numbers
sum_even=0
odd_sum=0
for number in range(12,38):
 if (number %2==0):
    sum_even=sum_even+number
 else:
    odd_sum=odd_sum+number
print("even sum is:",sum_even)
print("odd sum is:",odd_sum)
 

