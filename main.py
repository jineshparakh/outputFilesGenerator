"""
Written by: Jinesh Parakh

This is a script which is used to run C++ codes against input files and generate output files from them and store all the input files and output files in their respective folders
"""
#import necessary libraries or modules
import os
import glob
import sys
import shutil
from termcolor import colored, cprint #This module is just used for enhancing user experience

def returnNumberofInputFiles(): #function to return number of input.txt files in that folder
    noOfInputFiles=0
    
    for f in glob.glob("*"):
        if "input"  in f:
            noOfInputFiles+=1
    
    return noOfInputFiles

numFiles=returnNumberofInputFiles()
print("The total number of input files are: "+str(numFiles),end="\n\n")

print("Compiling Code........")
if os.system("g++ soln.cpp")!=0:    #Compiling the C++ code (soln.cpp)
    cprint('Compilation Error', 'red',attrs=['bold'])
    sys.exit()
cprint('Code successfully Compiled!!!!', 'green',attrs=['bold'])

for i in range(0,numFiles):
    print("Generating output against input"+str(i)+".txt file................")
    os.system("./a.out<input"+str(i)+".txt>output"+str(i)+".txt")
    print(" SUCCESS!!!!! output"+str(i)+".txt file successfuly generated from input"+str(i)+".txt file")
    print()
     #running the compiled C++ code and storing the outputs in the respective .txt files
    

cprint('All output files successfully Created!!!', 'green',attrs=['bold'])
print("\n\n")
print("Starting to move files into respective folders........\n\n")



#The next few lines will store all the input files in a folder called input and all the output files to a folder called output

inputFolderName="input"
outputFolderName="output"
initialDirectory=os.getcwd()
os.makedirs(os.path.join(initialDirectory,inputFolderName)) #make directory for the input files
os.makedirs(os.path.join(initialDirectory,outputFolderName)) #make directory for the input files
for f in glob.glob("*"):
    if "input" in f:
        print("Moving "+f+" to the input folder............")
        shutil.move(os.path.join(initialDirectory,f),os.path.join(initialDirectory,inputFolderName))
        print("Successfully moved "+f+" to the input folder!!!!")
        print()
    if "output" in f:
        print("Moving "+f+" to the output folder............")
        shutil.move(os.path.join(initialDirectory,f),os.path.join(initialDirectory,outputFolderName))
        print("Successfully moved "+f+" to the output folder!!!!")
        print()
        
cprint("Successfully moved all input and output files in their respective folders!!!", 'green',attrs=['bold'])




            

