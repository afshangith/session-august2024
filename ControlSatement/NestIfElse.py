age = int(input("please enter age :"))
weight = int(input("please enter weight in KG:"))

if age >= 18:

    if weight > 45:
        print ("He is eligible for blood donation")

    else:
        print("Weight is less than 45 so person is not eligible for blood donation")

else:
    print("Age is less than 18 so person is not eligible for blood donation")

