def compute_average(numbers):
    return sum(numbers) / len(numbers)

def main():
    numbers = []
    while True:
        try:
            user_input = input("Enter a number (or 'done' to finish): ")
            if user_input.lower() == 'done':
                break
            numbers.append(float(user_input))
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done' to finish.")
    
    if numbers:
        average = compute_average(numbers)
        print(f"The average of the numbers is: {average}")
    else:
        print("No numbers were entered.")

if __name__ == "__main__":
    main()
