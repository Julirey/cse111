# File: wordcounter.py
# Author: Julio Reyes

# Summary: This program reads a block of text, counts the amount of times
# each word appears, and shows the result in a csv.  

# -Full version-

import csv

def main():
    try:
        textfile = input("What's the name of the file: ")
        print()

        word_list = read_text(textfile)
        number_of_words = len(word_list)

        word_dict = make_string_dict(word_list)
        number_of_words_unique = len(word_dict)

        word_tuple_list_sorted = sort_dict_by_highest_value(word_dict)
        most_used_word = word_tuple_list_sorted[0]

        write_csv(textfile, word_tuple_list_sorted)
        
        print(" - The csv file was written succesfully -")
        print()
        print("     -----Summary-----")
        print(f"The text file containted {number_of_words} words.")
        print(f"Of which {number_of_words_unique} were unique.")
        print(f"The most used word was '{most_used_word[0]}'.")
        print(f"With a number of {most_used_word[1]} appearances.")

    except FileNotFoundError as not_found_err:
        print(type(not_found_err).__name__, not_found_err, sep=": ")
        print(f"The file {textfile} doesn't exist.")
        print("Run the program again and enter the" \
                " name of an existing file.")

    except PermissionError as perm_err:
        print(type(perm_err).__name__, perm_err, sep=": ")
        print("You don't have permission to read or alter the file.")
        print("Run the program again and make sure to close any" \
                " instances of the file.")
    
    except UnicodeDecodeError as unic_err:
        print(type(unic_err).__name__, unic_err, sep=": ")
        print("The text file constains characters that the program can't recognize.")
        print("The program will not run until said characters of the text file are deleted.")


def read_text(filename):
    """Reads and returns the contents
    of a text file as a list of strings.
    """
    words = []

    with open(filename, "rt", encoding='utf-8') as infile:
        for line in infile:
            # Strip the extra space.
            clean_line = line.strip()

            # Split the string into a list of strings.
            lines = clean_line.split()

            # Strip the extra characters and append
            # each word to a different list.
            for word in lines:
                clean_word = word.strip(",;:().-?!'[]*+=<>“”")
                cleaner_word = clean_word.strip('"')
                if cleaner_word != '':
                    words.append(cleaner_word.lower())         

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