def shout(text):
    print(text.upper())

#Assigning function to a variable
yell = shout

#Passing function as an argument to another function
def whisper(text):
    print(text.lower())

#Greet takes a function as a parameter
def greet(func):
    #declaring greeting in this manner executes our function
    func("Hi, I have been created by a function passed as an arguement")

greet(shout)
greet(whisper)

#Returning functions
# We can also return a function from another function

def create_adder(x):
    print("Create Adder Called X:",str(x))

    def adder(y):
        print("Adder called,",str(x),str(y))
        return x + y

    return adder

t = create_adder(10)
t(11)
t(12)

