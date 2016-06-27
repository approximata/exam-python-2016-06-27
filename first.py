# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the orignal list
# It should raise an error if the parameter is not a list
# example: [1, 2, 3, 4, 5] should produce [2, 4]

def get_secound_elements(raw_list):
    if type(raw_list) != list:
        raise ValueError('Excepted a list')
    secound_elemets_list = []
    for i in range(1, len(raw_list), 2):
        print(i)
        secound_elemets_list.append(raw_list[i])
    return secound_elemets_list

testlist = [1, 2, 3, 5, 8, 90]

print(get_secound_elements(testlist))
