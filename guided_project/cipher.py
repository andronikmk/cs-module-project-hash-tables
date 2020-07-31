# suppose you have a bunch of data, and you want to transform it
# you know what you want to trasnform it into.

# e.g. substituting one leter for another.
# write an encode function.

# need to change from one character to another
# map from one character to another
# use that to change an entire string

encode_table = {"A": "M",
"B": "N",
"C": "B",
"D": "V",
"E": "C",
"F": "X",
"G": "Z",
"H": "L",
"I": "K",
"J": "J",
"K": "H",
"L": "G",
"M": "F",
"N": "D",
"O": "S",
"P": "A",
"Q": "P",
"R": "O",
"S": "I",
"T": "U",
"U": "Y",
"V": "T",
"W": "R",
"X": "E",
"Y": "W",
"Z": "Q"}


def build_decode(encoding_table):
    for key, value in encode.items():
        decoded_table[value] = 

def encode(s):
    encoded_string = ""

    # iterate over a given string
    s = s.upper()
    for char in s:
    # for each char, look up its mapping
        if char.isspace():
            scrambled_character = encode_table[char]
            encoded_string += scrambled_character
    return encoded_string

print(encode("Hello, My name is Andronik Mkrtcyhev")) 