import math

while True:
    a=input("Enter the measure of First side:")
    b=input("Enter the measure of Second side:")
    c=input("Enter the measure of Third side:")

    s=(int(a)+int(b)+int(c))/2

    print(f"The semiperimeter of the triangle is: {s}")

    e=s-int(a)
    f=s-int(b)
    g=s-int(c)

    h=(e*f*g)
    i=(s*h)

    x=math.sqrt(i)

    print(f"The area of the triangle is: {x}")

    user_input = input("Do you want to run again? Y/N: ")


    if user_input not in ["Y", "y"]:
        break
print("This code was made by Varthedev. Thank you for using this.")
