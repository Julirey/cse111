# File: test_wordcounter.py
# Author: Julio Reyes

import os
import pytest
import csv

from wordcounter import read_text, make_string_dict, sort_dict_by_highest_value, write_csv

def test_read_text():
    """Verify that the read_text function works correctly.
    Parameters: none
    Return: nothing
    """
    # Write a sample file with three lines
    filename = "lines.txt"
    lines = ["    first....", ",,,,,second;;;;", "??third*    "]
    with open(filename, "wt") as outfile:
        print(*lines, sep="\n", file=outfile)

    # Call read_file to read the sample file.
    read = read_text(filename)

    # Delete the lines.txt file.
    os.remove(filename)

    # Verify that read_file read the file correctly.
    assert read == ["first", "second", "third"]

def test_make_string_dict():
    """Verify that the make_string_dict function works correctly.
    Parameters: none
    Return: nothing
    """
    # Declare a sample list with multiple strings 
    strings_list = ["one", "two", "two", "three", "three", "three", "four"]

    # Call make_string_dict to process the sample list and create a dictionary.
    word_dict = make_string_dict(strings_list)

    # Verify that make_string_dict makes the dictionary correctly.
    assert word_dict["one"] == 1
    assert word_dict["two"] == 2
    assert word_dict["three"] == 3
    assert word_dict["four"] == 1

def test_sort_dict_by_highest_value():
    """Verify that the sort_dict_by_highest_value function works correctly.
    Parameters: none
    Return: nothing
    """
    # Declare a sample dict 
    string_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 1,
        "five": 5,
    }

    # Call sort_dict_by_highest_value to sort the dictionary.
    string_dict_sorted = sort_dict_by_highest_value(string_dict)

    # Verify that sort_dict_by_highest_value makes the list of tuples correctly.
    assert string_dict_sorted[0] == ("five", 5)
    assert string_dict_sorted[1] == ("three", 3)
    assert string_dict_sorted[2] == ("two", 2)
    assert string_dict_sorted[3] == ("one", 1)
    assert string_dict_sorted[4] == ("four", 1)

def test_write_csv():
    """Verify that the write_csv function works correctly.
    Parameters: none
    Return: nothing
    """
    # Declare a sample list of tuples.
    tuple_list = [
        ("five", 5),
        ("three", 3),
        ("two", 2),
        ("one", 1),
        ("four", 1),
    ]

    # Set a name that the write_csv will use.
    filename = "words.txt"

    # Call write_csv to write the csv file.
    write_csv(filename, tuple_list)
    
    # Set the expected filename of the csv.
    expected_filename = "words.txt - Word Counter.csv"
    
    # Create an empty list.
    returned_list = []

    # Open the CSV file for reading.
    with open(expected_filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file, delimiter=";")

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the returned list.
            returned_list.append(tuple(row))

    # Delete the csv file.
    os.remove(expected_filename)       

    # Make sure that the numbers on the second column
    # are returned as intergers
    for i, (a, b) in enumerate(returned_list):
        new_b = int(b)
        returned_list[i] = (a, new_b)

    # Verify that write_csv writes the csv correctly.
    assert tuple_list == returned_list

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])