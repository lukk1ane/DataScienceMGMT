age=40
name="Mero Oboladze"
length=10.5
def greet(name):
    return name
def is_even(age):
    if(age%2==0):
        return True
    else:
        return False    
def fizz_buzz(age):
    n=20
    while(n!=age):
        if(n%3==0 and n%5==0):
            print("FizzBuzz")
        elif(n%5==0):
            print("Buzz") 
        elif(n%3==0):
            print("Fizz")  
        else:
            print(n)
        n+=1
             
print(greet(name))
print(is_even(age))
print(fizz_buzz(age))