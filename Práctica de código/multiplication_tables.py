def multiplication_tables(number):
    i = 1
    while i <= 10:
        result = number * i
        print(f"{number} x {i} = {result}")
        i+=1

number = int(input("Type a number: "))
print(multiplication_tables(number))


