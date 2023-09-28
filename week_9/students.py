import csv


def read_dictionary(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    student_dictionary = {}

    with open(filename, "rt") as file:
        csv_file = csv.reader(file)

        next(csv_file)

        for row in csv_file:
            id_index = row[0]
            name_index = row[1]

            student_dictionary[id_index] = name_index

    return student_dictionary
  

def main():
    file_name = "students.csv"
    student_dictionary = read_dictionary(file_name)
    
    i_number = input("Please enter an I-Number (xxxxxxxxx): ")
    if i_number in student_dictionary:
      print("Student name:", student_dictionary[i_number])
    else:
      print("No such student")

if __name__ == "__main__":
    main()
