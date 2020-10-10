# Written by: Nguyet Nguyen and Vinh Ngo on 08/13/2020
# Script used normalized data prior to running Kmeans scripts

# PROJECT     RUN     CLONE      TIME     STEM1       STEM2       LOOP1       LOOP2       TERTIARY     NATIVE      NON-NATIVE      RMSD        RG

usage = "\nUsage:python scalar-normalizer.py [Summarized_list] [Output]\n"

import sys
import numpy as np 

if (len(sys.argv) == 3):

    # Normalizing function
    def normalize(my_list):
     maximum = float(max(my_list))
     minimum = float(min(my_list))
     diff = maximum - minimum
     for i in range(len(my_list)):
            normalized_value = (float(my_list[i]) - minimum) / diff * 100 
            my_list[i] = normalized_value
     return my_list

    # Arrays to be normalized 
    project_array = []
    run_array = []
    clone_array = []
    time_array = []
    stem1_array = []
    stem2_array = []
    loop1_array = []
    loop2_array = []
    tertiary_array = []
    native_array = []
    nonnative_array = []
    RMSD_array = []
    Rg_array = []

    summarized_list = sys.argv[1]
    filename = open(summarized_list, "r")


    for line in filename:
        column = line.split()
        project_array.append(column[0])
        run_array.append(column[1])
        clone_array.append(column[2])
        time_array.append(column[3])
        stem1_array.append(column[4]) 
        stem2_array.append(column[5])
        loop1_array.append(column[6])
        loop2_array.append(column[7])
        tertiary_array.append(column[8])
        native_array.append(column[9])
        nonnative_array.append(column[10])
        RMSD_array.append(column[11])
        Rg_array.append(column[12])
    
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

    # Calling the normalizing function and rounding it to 2 decimals
    stem1_array = np.round(normalize(stem1_array), decimals =2)
    stem2_array = np.round(normalize(stem2_array), decimals = 2)
    loop1_array = np.round(normalize(loop1_array), decimals = 2)
    loop2_array = np.round(normalize(loop2_array), decimals = 2)
    tertiary_array = np.round(normalize(tertiary_array), decimals = 2)
    native_array = np.round(normalize(native_array), decimals = 2)
    nonnative_array = np.round(normalize(nonnative_array), decimals =2)
    RMSD_array = np.round(normalize(RMSD_array), decimals= 2)
    Rg_array = np.round(normalize(Rg_array), decimals= 2)

    # Getting the user's input so it can output the file
    output_name = sys.argv[2]
    output_file = open(output_name, "w")

    # Loop in order to write back to the Output file
    for i in range(len(stem1_array)):

     # Building the line to write into Output_file
        # # @line_to_write = 'PROJ/R/C/F    0   0   0   12.3    12.3    11.3    ....

        # This line DOES include native contact. 
        # line_to_write =  str(stem1_array[i]) + "\t" + str(stem2_array[i]) + "\t" + str(loop1_array[i]) + "\t" + str(loop2_array[i]) + "\t" + str(tertiary_array[i]) + "\t" + str(native_array[i]) + "\t" + str(nonnative_array[i]) + "\t" + str(RMSD_array[i]) + "\t" + str(Rg_array[i]) + str(project_array[i]) + "\t" + str(run_array[i]) + "\t" + str(clone_array[i]) + "\t" + str(time_array[i]) + "\n"
        
        # This line DOES NOT include native contact...for clustering purposes.
        line_to_write =  str(stem1_array[i]) + "\t" + str(stem2_array[i]) + "\t" + str(loop1_array[i]) + "\t" + str(loop2_array[i]) + "\t" + str(tertiary_array[i]) +  "\t" + str(nonnative_array[i]) + "\t" + str(RMSD_array[i]) + "\t" + str(Rg_array[i]) + "\t" + str(project_array[i]) + "\t" + str(run_array[i]) + "\t" + str(clone_array[i]) + "\t" + str(time_array[i]) + "\n"

        # Writting to the file line by line
        output_file.write(line_to_write)

    # Closing out the files to read and write from so it doesn't lock
    output_file.close()
    filename.close()

else:
    print(usage)
    sys.exit()


        