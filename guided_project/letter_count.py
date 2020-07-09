# given a string
## return every letter with how many times it occurs in the string
# sort by how often they occur.

# iterate threw the string
# tally the count using the dictionary
# sort our dictionary by the value (i.e. the count of each letter)
def print_letter_count(s):
    tally = {}
    s = s.lower()
    for char in s:
        if char >= 'a' and char <= 'z':
            if char not in tally:
                tally[char] = 1
            else:
                tally[char] += 1

   #  print(sorted(tally.items(), key=lambda x: x[1], reverse=True))
    tally_list = list(tally.items())
    tally_list.sort(key=lambda x: x[1], reverse=True)

    for pair in tally_list:
        print(f"Count {pair[1]}, letter: {pair[0]}")

print_letter_count('bunny hop')
print_letter_count('The quick brown fox jumps over the lazy dog.')

