import json
from difflib import get_close_matches

data = json.load(open("Dictionary/data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes or N if no: " %get_close_matches(word, data.keys())[0])
        yn = yn.upper()
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist, please enter a valid word."
        else:
            "We didn't understand your entry."
    else:
        return "The word doesn't exist, please enter a valid word."

word = input("Enter a word: ")
word = word.lower()
output = translate(word)

if type(output) == list:
    for x in output:
        print(x)
else:
    print(output)