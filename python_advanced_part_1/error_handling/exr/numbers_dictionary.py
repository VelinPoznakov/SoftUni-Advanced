numbers_dictionary = {}

line = input()

while line != "Search":  # adding to the dictionary
    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number  # make key value pair with line and number
    except ValueError:
        print("The variable number must be an integer")

    line = input()  # get the next line of input

line = input()

while line != "Remove":  # searching in the dictionary
    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")

    line = input()

line = input()

while line != "End":
    searched = line
    try:
        numbers_dictionary.pop(line)
    except KeyError:
        print("Number does not exist in dictionary")

    line = input()


print(numbers_dictionary)
