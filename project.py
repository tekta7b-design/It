import sys
todo = [] 
co = [] 
def ex(): 
    sys.exit(ex) 
def new(): 
        add = input("add new todo list: ") 
        todo.append(add) 
def mrt(): 
    remove = input("remove to do list:") 
    todo.remove(remove) 
def tyu(): 
        todo.clear() 
def mac():
    for b in todo: 
      print(b) 
    c = input("Choose:")
    todo.remove(c) 
    co.append(c) 
    
def front(): 
    print("hello welcome back to task tracker!")
    print("=== TO-DO LIST ===") 
    for b in todo: 
        print(b)
    print("=== Tasks COMPLETED ===") 
    for h in co: 
        print(h) 
            
    print("=== MAIN MENU ===") 
    print("1. Add New Task") 
    print("2. Remove Task") 
    print("3. Edit Task") 
    print("4. Mark Task as completed") 
    print("5. Exit") 
    c = input("choose from 1 to 5):") 
    if c == "1": 
        new() 
        print("Task added")
    elif c == "2": mrt() 
    elif c == "3": tyu() 
    elif c == "4": mac() 
    elif c == "5": ex() 
            
    else: 
        print("Invalid result") 
            
            
while True: 
    front( )
