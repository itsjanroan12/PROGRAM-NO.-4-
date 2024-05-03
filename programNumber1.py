#Creator Information: 
#Name: Abad, Jan Roan D.
#Section: BSCpE 1-2
#Date: April 30, 2024
#Faculty: Prof. Danilo Madigalejos
#Program Description: "a Python program that reads a text file named numbers.txt that contains 20 integers. The program will create two other text file; the first text file will be named even.txt that will contains all even numbers extracted from the numbers.txt. The second text file will be named odd.txt that will contains all odd numbers extracted from the numbers.txt.git git "
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