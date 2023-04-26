#-----------------------------
#External_Files.py
#Sedric Asuncion
#-----------------------------

## ----- Questions ----- ##
# What are the benefits of external files for your program?
#
# Data Persistence: Able to access the data as it's saved on a file that exists outside of the code 
# Seperation of Concerens: Seperating the data from the program makes the code easier to read
# Sharing Data: Able to share data between programs and other people
#
# I'm thinking of this project as a 'concept', so my answers are also conceptual. The way it is right now,
# using external files doesn't matter much, but if scaled larger, it would be easier to maintain. I used append
# so I can add data to the file without having to rewrite the entire file.
#
# External Files are being used in the code as I'm creating a .txt file with my first function,
# appending onto that file for the second function, and then printing the file
# on the third function.

## ----- Thoughts on Code ----- ##
# I could have just wrote everything using 'write' mode in opening the file, but I added
# 'append' mode to the mix, for more practice on it, and future practical use I might have

## ----- Functions ----- ##
def inputs():
    #Prompts user to enter name of file and basic Character information
    Player = input("Create Character Name: ")
    Race = input('Create Character Race: ')
    Job = input('Create Character Job: ')
    Level = 0

    #Returns Character Name, Race, Job, and Level
    return Player, Race, Job, Level

def file_create():
    #Calls the inputs function to get the values of the prompts 
    #What we only need read is the Player value
    Player, Race, Job, Level = inputs()

    #Creates the file and writes the placeholders for the values
    with open(f"{Player}_Data.txt", 'w') as crt:
        crt.write('User: ')
        crt.write('\nRace: ')
        crt.write('\nJob: ')
        crt.write('\nLevel: ')
        crt.close()
    #Returns the values, we need those in next functions
    return Player, Race, Job, Level

def file_append():
    #Calls the inputs function to get the values of the prompts
    #I don't recall inputs function, because it'll prompt again
    Player, Race, Job, Level = file_create()

    #Appends the values to the file on their rightful placeholders
    with open(f"{Player}_Data.txt", 'r+') as app:
        lines = app.readlines()
        lines[0] = lines[0].strip() + f' {Player}\n'
        lines[1] = lines[1].strip() + f' {Race}\n'
        lines[2] = lines[2].strip() + f' {Job}\n'
        lines[3] = lines[3].strip() + f' {Level}\n'
        app.seek(0)
        app.writelines(lines)
        app.close()

    #Returns the file_name value
    x = Player
    return x

def file_read():
    Player = file_append()

    #Reads and prints file and values
    with open(f"{Player}_Data.txt", 'r') as rd:
        print(rd.read())
        rd.close()
        

## ----- Main Code ----- ##
file_read()