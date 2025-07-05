def get_numbers():
    numbers = []
    for i in range(5):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    return numbers

def calculate_sum(numbers):
    return sum(numbers)

def main():
    print("Welcome to the 5-Number Addition Calculator!")
    numbers = get_numbers()
    total = calculate_sum(numbers)
    print(f"The sum of the numbers is: {total}")

if __name__ == "__main__":
    main()