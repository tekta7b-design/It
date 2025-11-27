income  = int(input("enter the amount of income:"))

if 0<= income <=2000:
    print("your tax is " + str(income*0))
elif 2001<= income <= 4000:
    print("your tax is " + str(income*0.15))
elif 4001 <= income <= 7000:
    print("your tax is " + str(income* 0.2))
elif 7001<= income <= 10000:
    print("your tax is " + str(income* 0.25))
elif 10001<= income<= 14000:
    print("your tax is " + str(income* 0.3))
elif income > 14001:
    print("your tax is " + str(income* 0.35))

   