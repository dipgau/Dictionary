# This is a dictionary program where user gives input of a word he/she wants to search for and
#  in return, the program gives the meaning of the searched word

# importing in-built json function to work with json data for dictionary
import json
# importing get_close_matches method from difflib library
from difflib import get_close_matches

# opens and reads a data.json files which is inside data directory
data = json.load(open('data/data.json'))


# function to process the word enetered by user
def dictionary(word):
    # converts the entered string to lower case format
    word = word.lower()
    # checks if entered string is in data.json file
    if word in data:
        # if the string is in data.json file, it returns back the meaning
        return data[word]

    # if the entered word does not matches the content in data file, this function checks
    # if there is any close match and if the matches are more than one
    elif len(get_close_matches(word, data.keys(), n=2)) > 0:
        # print the two closest alternatives for users to tell if it was their desired search
        print('Do you want to search %s or %s instead?' % (get_close_matches(
            word, data.keys(), n=2)[0], get_close_matches(word, data.keys(), n=2)[1]))

        # if user wants to take the first alternative given by program, 1 is entered and for second, 2 is inputted
        value = input('Enter 1 for %s or 2 for %s or any button to exit: ' % (get_close_matches(
            word, data.keys(), n=2)[0], get_close_matches(word, data.keys(), n=2)[1]))

        # when user enters the value of 1, the function returns the first alternative
        if value == str(1):
            return data[get_close_matches(word, data.keys(), n=2)[0]]
        # when user enters the value of 2, second alternative is shown
        elif value == str(2):
            return data[get_close_matches(word, data.keys(), n=2)[1]]
        # if program does not see neither 1 nor 0, it returns the following statement
        else:
            return 'You did not enter neither 1 nor 0'

    # when comparing enetered string by user with data.json file, if program does not find any match or even
    # the word with close match, then it gives the following output
    else:
        return 'No such word exist. Please give a correct word'


# asks input from a user
word = input('Give a word: ')

# pass the input to the dictionary function
meanings = (dictionary(word))

# checks if the output type of function is list or not, if it is a list then performs for loop to print each output
if type(meanings) == list:
    for each in meanings:
        print(each)

# if the output is not list and is a string, it just prints the string
else:
    print(dictionary(word))
