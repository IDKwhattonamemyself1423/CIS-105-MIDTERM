a = int(input("type 1st number "))
b = int(input("type 2nd number "))
c = int(input("type 3rd number "))
d = int(input("type 4th number "))
e = int(input("type 5th number "))
f = int(input("type 6th number "))

numbers = [a, b, c, d, e, f]

def sum_of_evens(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

print(sum_of_evens(numbers))