inputStr = input("enter a string : ")
count = 0
whitespaces = 0
for c in inputStr:
    if(c == ' ' or c == '\t' or c == '\n'):
        whitespaces = whitespaces + 1
    
    count = count + 1
print(f"the length of string is : {count}")
print(f"the length of the string without whitespaces is : {count - whitespaces}")
print(f"len function output : {len(inputStr)}")
