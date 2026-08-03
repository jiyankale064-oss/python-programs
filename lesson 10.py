string = '1889345'
print(string.isnumeric())

string = '\u00BD'
print(string.isnumeric())

input  : (string) = '123ayu456'
print(string.isnumeric())

####################################################################



string = 'Dev'
print(string.isalpha())


string = 'Sarga shala'
print(string.isalpha())



string = 'sarga1'
print(string.isalpha())
##################################################################



text = "Hello World"

result = text.endswith('Word')
print (result)

result = text.endswith('World')
print (result)

#################################################################

string = "How can a clam cram in a clean cream can?"


print(string.count("can"))