def classify_person():
    age = int(input("enter your age: "))
    if 0 < age < 13:
        print("you are a kid")
    elif 12 < age < 18:
        print("You are a minor")
    elif 17 < age < 65:
        print ("You are an adult")
    elif age > 64:
        print ("You are a senior")

classify_person()