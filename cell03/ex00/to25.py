input = int(input("Enter a number less than 25\n"))

if input > 25:
    print("Error")
else:
    while input <= 25:
        print(f"Inside the loop, my variable is {input}")
        input += 1
