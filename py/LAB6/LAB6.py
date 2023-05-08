print("e^n Calculator v.0.0.1")
n=int(input("Please enter a number n: "))
x=int(input("Please enter a number x: "))
factorial = lambda a: a*factorial(a-1) if a > 1 else 1
term = lambda up, down: up**down/factorial(down)
terms = sum([term(n,i) for i in range (x+1)])
print(terms)


result=0
def recursive(m):
    """This function calculates(-1^(k-1)/k) until a given m from 1."""
    global result
    if m == 0:
        print (result)
    else:
        result += (((-1)**(m+1))/m)
        recursive(m-1)
m = int(input("Please enter an m:"))
recursive(m)




