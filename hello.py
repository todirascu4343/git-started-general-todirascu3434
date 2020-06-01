#Task 1 

def hello_world():
    return "Hello, World!"


message = hello_world()
print("1.")
print(message)
print()



#Task 2

def hello(name):
    if name == None or name == "":
        return 'Hello, World!'
    return 'Hello, ' + name + '!'

print("2.")


name = input("Insert a name: ")
print("Output: ", hello(name))

#Task 3 

def print_hello(name):
    print(hello(name))

print()
print("3.")

print_hello("human")