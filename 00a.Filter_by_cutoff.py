# Written by: Nguyet Nguyen and Vinh Ngo on 10/09/2020
# Script used filter out normalized data by cut-off

# STEM1      STEM2       LOOP1       LOOP2       TERTIARY     NATIVE      NON-NATIVE      RMSD        RG    Project(string) run clone time

usage = "\nUsage:python scalar-normalizer.py [normalized_list] [CutOff Time in ps] [Output]\n"

import sys
import numpy as np 

if (len(sys.argv) == 4):

    # Arrays to be normalized 
    stem1_array = []
    stem2_array = []
    loop1_array = []
    loop2_array = []
    tertiary_array = []
    native_array = []
    nonnative_array = []
    RMSD_array = []
    Rg_array = []
    project_array = []
    run_array = []
    clone_array = []
    time_array = []
    normalized_list = sys.argv[1]
    filename = open(normalized_list, "r")


    for line in filename:
        column = line.split()
        stem1_array.append(column[0]) 
        stem2_array.append(column[1])
        loop1_array.append(column[2])
        loop2_array.append(column[3])
        tertiary_array.append(column[4])
        native_array.append(column[5])
        nonnative_array.append(column[6])
        RMSD_array.append(column[7])
        Rg_array.append(column[8])
        project_array.append(column[9])
        run_array.append(column[10])
        clone_array.append(column[11])
        time_array.append(column[12])
        
    #Declaring elements as arrays 
    stem1_array = np.array(stem1_array).astype(np.float)
    stem2_array = np.array(stem2_array).astype(np.float)
    loop1_array = np.array(loop1_array).astype(np.float)
    loop2_array = np.array(loop2_array).astype(np.float)
    tertiary_array = np.array(tertiary_array).astype(np.float)
    native_array = np.array(native_array).astype(np.float)
    nonnative_array = np.array(nonnative_array).astype(np.float)
    RMSD_array = np.array(RMSD_array).astype(np.float)
    Rg_array = np.array(Rg_array).astype(np.float)
    project_array = np.array(project_array).astype(str)
    run_array = np.array(run_array).astype(np.float)
    clone_array = np.array(clone_array).astype(np.float)
    time_array = np.array(time_array).astype(np.int)


  # Filter with time cutoff
    time_cutoff = int(sys.argv[2])


    # Getting the user's input so it can output the file
    output_name = sys.argv[3]
    output_file = open(output_name, "w")
    

    # Loop in order to write back to the Output file

    for i in range(len(time_array)):
        if time_array[i] >= time_cutoff:
            line_to_write = str(stem1_array[i]) + '\t'  + str(stem2_array[i]) + "\t" + str(loop1_array[i]) + "\t" + str(loop2_array[i]) + "\t" + str(tertiary_array[i]) +  "\t" + str(nonnative_array[i]) + "\t" + str(RMSD_array[i]) + "\t" + str(Rg_array[i]) + "\t" + str(project_array[i]) + "\t" + str(run_array[i]) + "\t" + str(clone_array[i]) + "\t" + str(time_array[i]) + "\n"
            output_file.write(line_to_write)
 # Closing out the files to read and write from so it doesn't lock
    output_file.close()
    filename.close()

else:
    print(usage)
    sys.exit()   


        