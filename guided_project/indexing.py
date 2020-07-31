records = [
    ("Tim", "Texas"),
    ("Adam", "Florida"),
    ("Austin", "Florida"),
    ("Kai", "South Carolina"),
    ("Jud", "Pheobus"),
    ("Eric", "Utah"),
    ("Mandi", "Virginia"),
    ("Emma", "Florida"),
    ("Anna", "Texas"),
    ("Andrew", "Utah"),
    ("Leo", "New York"),
    ("James", "New York"),
    
    ]

# UNDERSTAND
# given a list of records, build an index
# so we can quickly find everyone in a given space

# PLAN
# Iterate through the tuples in our list
# Build a dictionary as we go
# us states as key, and names as values

# if state isn't in the dictionary, add it as a key
# value: [name1. name2, etc...]
# 
# possible value data strucutre: list, set, nested hash table 

def build_index(records):
    index = {}
    # iterate through the list
    # for each pair, check if the sate is in the dictionary
    # if so, append the name to the list
    # if not, add the key and list (with name in it)
    for name, state in records:
        if state in index:
            index[state].append(name)
        else:
            index[state] = []
            index[state].append(name)
    return index

idx = build_index(records)
print(idx["New York"])