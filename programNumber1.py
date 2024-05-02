def main():
    # Open the file for reading
    with open("numbers.txt", "r") as file:
        numbers = file.readlines()

    # Convert strings to integers
    numbers = [int(num.strip()) for num in numbers]

    # Separate even and odd numbers
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]

    # Write even numbers to even.txt
    with open("even.txt", "w") as even_file:
        for num in even_numbers:
            even_file.write(str(num) + "\n")

    # Write odd numbers to odd.txt
    with open("odd.txt", "w") as odd_file:
        for num in odd_numbers:
            odd_file.write(str(num) + "\n")

if __name__ == "__main__":
    main()
