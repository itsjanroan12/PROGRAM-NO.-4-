#Creator Information: 
#Name: Abad, Jan Roan D.
#Section: BSCpE 1-2
#Date: April 30, 2024
#Faculty: Prof. Danilo Madigalejos
#Program Description: "A method in python that will create two separate text files after reading the source text file named integers.txt that contains 20 integers. The first output file will be named double.txt containing the square of all even integers found in integers.txt and the second file will be named triple.txt containing the cube of all odd numbers found in the integers.txt."
def process_integers(input_file):
    # Open the source file for reading
    with open(input_file, 'r') as f:
        integers = f.readlines()

    # Process integers and create lists of squares and cubes
    even_squares = [int(num) ** 2 for num in integers if int(num) % 2 == 0]
    odd_cubes = [int(num) ** 3 for num in integers if int(num) % 2 != 0]

    # Write results to output files
    with open('double.txt', 'w') as f:
        f.write('\n'.join(map(str, even_squares)))

        
    with open('triple.txt', 'w') as f:
        f.write('\n'.join(map(str, odd_cubes)))

# Call the method with the input file name
process_integers('integers.txt')