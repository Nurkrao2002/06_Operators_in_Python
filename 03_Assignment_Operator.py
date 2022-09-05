""" Assignment Operator  """

a=2 ; b=3
a=a+b
print(a) # a=2+3  a=5
a=a+a
print(a) # a=5+5 a=10


a=5
a+=3
print(a) # a=a+3 a=5+3 a=8
a-=2
print(a) # a=a-2  a=8-2  a=6
a*=4
print(a) # a=a*4 a=6*4  a=24
a/=2
print(a) # a=a/2  a=24/2  a=12.0
a**=2
print(a) # a=a**2  a=12.0**2  a=144.0

p=int(input("Enter the value of p:"))
print(f"The value of p is {p}")
p+=2   
print("The value of p after p+=2 is {}".format(p))
p-=4 
print("The value of p after p-=4 is {}".format(p))
p*=6 
print("The value of p after p*=6 is {}".format(p))
p**=2 
print("The value of p after p**=2 is {}".format(p))
p/=2 
print("The value of p after p/=2 is {}".format(p))
