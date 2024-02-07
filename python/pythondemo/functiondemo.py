def my_function():
    a=1+2+1
    print(a)
    if a==3:
        print("A is three")

        x="using split method  "
        for x1 in x:
            print(x1)
        x=x.split(" ")
        for x2 in x:
            print(x2)
    elif a>3:
        print("a is greater than")
        z="This value is greater than 3"
        for z1 in z:
            print(z1)
        z=z.split(" ")
    y=input("enter the value").split()
    print(y)
my_function() 