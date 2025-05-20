# You will be given two strings. Transform the first string into the second one, letter by letter, starting
# from the first one. After each interaction, print the resulting string only if it is unique.
# Note: the strings will have the same length.

first_string = input()
second_string = input()

# last_printed_string = first_string
# for character_index in range(len(first_string)):
#     left_part = second_string[:character_index + 1] # in left part we're taking numbers from the second string
#     right_part = first_string[character_index + 1:] # in right part we're taking numbers from the first string
#     new_string = left_part + right_part
#     if new_string != last_printed_string:
#         print(new_string)

for character_index in range(len(first_string)):
    left_part = second_string[:character_index + 1] # in left part we're taking numbers from the second string
    right_part = first_string[character_index + 1:] # in right part we're taking numbers from the first string
    new_string = left_part + right_part
    if first_string[character_index] != second_string[character_index]:
        print(new_string)

# See this for better understanding!
# my_string = "ilovecoding"
# character_index = 5
# left_part = second_string[:character_index + 1]
# print(left_part)
