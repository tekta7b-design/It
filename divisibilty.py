def divisibilty_check5(num):
    if num % 5 == 0:
        return True
    else:
        return False        
number = int(input("Enter a number: "))
if divisibilty_check5(number):
    print(f"{number} is divisible by 5")
else:
    print(f"{number} is not divisible by 5")