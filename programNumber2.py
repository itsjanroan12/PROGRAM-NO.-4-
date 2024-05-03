#Creator Information: 
#Name: Abad, Jan Roan D.
#Section: BSCpE 1-2
#Date: April 30, 2024
#Faculty: Prof. Danilo Madigalejos
#Program Description: " A Python program that read a file containing the name of 20 students together with their GWA. The program will outputs the name of the student who got the highest GWA (including the GWA)."
def main():
    # Open the file for reading
    with open("students.txt", "r") as file:
        lines = file.readlines()

    # Initialize variables to store the closest GWA to 1.00 and the corresponding student
    closest_to_1 = float('inf')
    top_student = ""

    # Loop through each line to find the student with the GWA closest to 1.00
    for line in lines:
        name, gwa = line.strip().split(",")
        gwa = float(gwa)
        if abs(gwa - 1.00) < abs(closest_to_1 - 1.00):
            closest_to_1 = gwa
            top_student = f"{name} (GWA: {gwa})"
            
    # Output the student with the GWA closest to 1.00
    print("Top Student:", top_student)

if __name__ == "__main__":
    main()