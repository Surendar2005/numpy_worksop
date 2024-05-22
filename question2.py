# find if the given number is a palindrome or not?
def is_palindrome(num)
num_str=str(num)
if num_str==num_str[::-1]:
  return true
else:
  return false
num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
