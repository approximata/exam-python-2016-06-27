# Create a function that takes a filename and a string as parameter,
# it should write the string to the file 3 times
# example: when called with "tree.txt" and "apple",
# it should write "appleappleapple" to the file "tree.txt".
# the function should not raise an error on any output problem, for example
# denied permission
def write_stringemulti_to_file(string, filename):
    fw = open(filename, 'w')
    fw.write(string * 3)
    fw.close()


write_stringemulti_to_file('valamiteljesenmas','sample.txt')
