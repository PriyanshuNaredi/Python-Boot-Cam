# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas

data = pandas.read_csv('Day-26/NATO-alphabet-start/Nato_alphabet.csv')
print(data.to_dict())

# TODO 1. Create a dictionary in this format:

dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate():
    word = input('Entre a word ').upper()
    try:
        output_list = [dict[letter] for letter in word]
    except KeyError:
        print("Only Alphabets Please")
        generate()
    else:
        print(output_list)
        
generate()