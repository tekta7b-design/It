def selection():
   x = int(input("Enter 1 to convert from celsius to fahrenheit or 2 to convert from fahrenheit to celsius: "))
   if x == 1:
        celsius = float(input("Enter temperature in celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} degree celsius is equal to {fahrenheit} degree fahrenheit") 
   elif x == 2:
        fahrenheit = float(input("Enter temperature in fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} degree fahrenheit is equal to {celsius} degree celsius")
   else:   
        print("Invalid input")      
selection()