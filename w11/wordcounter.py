# File: wordcounter.py
# Author: Julio Reyes

# Summary: This program reads a block of text, counts the amount of times
# each word appears, and shows the result in a csv.  

# -W11 version-

import csv

def main():

    textfile = input("What's the name of the file: ")

    word_list = read_text(textfile)

    word_dict = make_string_dict(word_list)

    word_tuple_list_sorted = sort_dict_by_highest_value(word_dict)

    write_csv(textfile, word_tuple_list_sorted)

def read_text(filename):
    """Reads and returns the contents
    of a text file as a list of strings.
    """
    words = []

    with open(filename, "rt") as infile:
        for line in infile:
            # Strip the extra space.
            clean_line = line.strip()

            # Split the string into a list of strings.
            lines = clean_line.split()

            # Strip the extra characters and append
            # each word to a different list.
            for word in lines:
                clean_word = word.strip(",;:().-?!")
                if clean_word != '':
                    words.append(clean_word.lower())         

    return words

def make_string_dict(list):
    """Converts a list of strings into a dictionary
    where the key is the string and the value is the amount of 
    times that string was repeated in the list
    """
    word_dict = {}

    # Go through each string in the list
    for item in list:
        
        # If the string is in the dictionary, 
        # add 1 to the value
        if item in word_dict: 
            word_dict[item] = word_dict[item] + 1

    	# If the string is NOT the dictionary, 
        # add it to the dictionary and set its
        # value to 1 
        else: 
            word_dict[item] = 1

    return word_dict 

def sort_dict_by_highest_value(dictionary):
    """ Sorts a dictionary and returns a list of tuples ordered
    by the second element from highest to lowest.
    """
    sorted_dict = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict

def write_csv(filename, tuple_list):
    """ Reads a list of tuples and writes in a csv file the 
    first value of each tuple on the first column and the second on the 
    second column.
    """
    with open(f"{filename} - Word Counter.csv", 'at') as infile:
     writer = csv.writer(infile, delimiter=';', lineterminator='\n')
     writer.writerows(tuple_list)

if __name__ == "__main__":
    main()