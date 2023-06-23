string = "Hello, World!"

string[0:5]  # Output: "Hello"
string[7:]  # Output: "World!"
string[:5]  # Output: "Hello"
string[7:12]  # Output: "World"
string[::2]  # Output: "HloWrd"

string[-6:-1]  # Output: "World"
string[-7:]  # Output: "World!"
string[:-7]  # Output: "Hello"
string[-12:-7]  # Output: "Hello"
string[::-1]  # Output: "!dlroW ,olleH"

string[1:10:2]  # Output: "el,Wr"
string[::3]  # Output: "Hl r!"
string[5:0:-1]  # Output: ",olle"
string[-1:-12:-2]  # Output: "!lo,Wle"

copy = string[:]  # Creates a copy of the string

modified_string = string[:6] + "Python"  # Output: "Hello, Python!"