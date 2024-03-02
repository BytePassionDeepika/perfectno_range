def perfect_num(num):
    sum_of_divisors = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num

def print_perfect_numbers(start, end):
    print(f"Perfect numbers in the range {start} to {end}:")
    for num in range(start, end + 1):
        if perfect_num(num):
            print(num)

start = int(input("Enter the Start Range: "))
end = int(input("Enter the End Range: "))
print_perfect_numbers(start, end)
