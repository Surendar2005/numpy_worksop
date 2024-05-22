#write a program to find the sum of digits of a given number'
def sum_of_digits(num):
num_str=str(num)
digit_sum=0
for digit in num_str:
  digit_sum += int(digit)
  return digit_sum
num = int(input("Enter a number: "))
sum_digits = sum_of_digits(num)
print(f"The sum of digits of {num} is {sum_digits}.")
