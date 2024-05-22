#write a program to find if the given number is prime no or not
def is_prime(num):
  if num<=1:
    return false
  for i in range(2,int(num**0.5):
    if num%i==0:
      return false
  return true
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
