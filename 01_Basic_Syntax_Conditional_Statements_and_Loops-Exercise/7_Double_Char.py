# You will be given strings until you receive the command "End". For each string given, you should print a string in
# which each character (case-sensitive) is repeated twice. Note that if you receive the string "SoftUni", you should
# NOT print it!

# string = ""
#
# while string != "End":
#     string = input()
#     if string == "End":
#         break
#     if string == "SoftUni":
#         continue
#     for i in range(len(string)):
#         print(string[i]+string[i],end="")
#
#     print()

# ALTERNATIVELY:

current_string = input()

while current_string != "End":
    if current_string != "SoftUni":
        new_string = ""
        for character in current_string:
            new_string += character * 2
        print(new_string)
    current_string = input()



