""" Logical Operator  """

a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print("The value of a<b and b>a is {}".format(a<b and b>a)) 
print("The value of a>b and a<b is {}".format(a>b and a<b)) 
print("The value of a!=b and a==b is {}".format(a!=b and a==b)) 
print("The value of a==b or a>b is {}".format(a==b or a>b)) 
print("The value of a!=b or a<b is {}".format(a!=b or a<b)) 
print("The opposite of {}=={} is {}".format(a,b,not a==b)) 
print("The opposite of {}!={} is {}".format(a,b,not a!=b))
