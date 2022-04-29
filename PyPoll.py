# The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3.The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote. 
#----------------------------------------------------------------------------------------------------------***
# # Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'
# # # Open the election results and read the file
# with open(file_to_load) as election_data:

#       # To do: perform analysis.
#       print(election_data)
# # Close the file.
# election_data.close()

#---------------------------------------------------------------------------------------------------------***
# # Open the election results and read the file
# import csv
# import os
# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#       # Print the file object.
#        print(election_data)

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")

# #----Adding Hello World to election analysis___
# #Create a filename variable to a direct or indirect path to the file.
# file_to_save= os.path.join("analysis", "election_analysis.txt")

# # #Use the open statement to open the file as a text file.
# # outfile =open (file_to_save, "w")
# # #Write some data to the file.
# # outfile.write("Hello World")
# # Create a filename variable to a direct or indirect path to the file
# with open(file_to_save, "w") as txt_file:

#     # Write some data to the file.
#    # txt_file.write("Hello World")
# #Close the file
# #outfile.close()
# #-------------will add 3 counties-------------------------------------------------------------------
# # Write three counties to the file.
#       # txt_file.write("Arapahoe, ")
#       # txt_file.write("Denver, ")
#       # txt_file.write("Jefferson, ")
#       #txt_file.write("Arapahoe, Denver, Jefferson")
#       # print each name in a new line
#       txt_file.write("Counties in the Election\n------------------------------\nArapahoe\nDenver\nJefferson")

#---------------------------------------3.4.4 Read the Election Files-------------------------------------------------------------------

# Add our dependencies.
import csv
import os

#Assign a variable to load a file from a path.
file_to_load=os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path.
file_to_save=os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data:

      #To do: read and analyze the data here.
            # Read the file object with the reader function.
            file_reader=csv.reader(election_data)
            # Print each row in the CSV file.
            #for row in file_reader:
                  #print(row)
            headers=next(file_reader)
            print(headers)