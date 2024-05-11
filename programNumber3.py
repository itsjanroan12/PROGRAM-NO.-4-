#Creator Information: 
#Name: Abad, Jan Roan D.
#Section: BSCpE 1-2
#Date: April 30, 2024
#Faculty: Prof. Danilo Madigalejos
#Program Description: "a method in python to write multiple line of text contents into a text file mylife.txt. See sample output"
def write_to_file(file_name, lines):
    with open (file_name, 'w') as file:
        for line in lines:
            file.write(line + '\n')

#The example usage:
lines = [
"In life's journey, twists and turns",
"Each chapter teaches, each lesson I discern",
"Grateful for every moment's sway",
"This is but the dawl of my way",

"With each stop, new adventures unfold",
"In this tale of life, yet to be told",
"Here's to the journey, here's to the flight",
"May many more adventures light up the night!",
]

write_to_file("mylife.txt",lines)