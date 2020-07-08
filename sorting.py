my_list = []

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

my_list = [5, 3, 4, 2, 6, 8, 1, 9]

d = {
    'Austin': 12,
    'Michael': 24,
    'Troy': 35,
    'Jorge':99,
    'David':42
}

# turn into a list
for pair in d.items():
    print(pair)

print("USING SORTED METHOD: ", sorted(d.items()))

sorted_list_of_items = list(d.items())

def anon_function(pair):
    return pair[1]

sorted_list_of_items.sort(reverse=True, key=lambda pair: pair[1])
print("USING LAMBDA FUNCTION TO SORT", sorted_list_of_items)

#sorted_list_of_items.sort()
#print(sorted_list_of_items)
# for k, v in d.items():


