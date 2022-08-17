filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [files.rstrip("hp") for files in filenames ] 
newfilename = [files+"h" for files in newfilenames if files.endswith(".")]

common = [b for a in filenames for b in newfilenames if a == b]

newfilename2 = [files.replace(".hpp", ".h") for files in filenames]


print(newfilename2) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]