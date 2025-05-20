# You will be given the number n. After that, you'll receive different strings n times. Your task is to check if the
# given strings are pure, meaning that they do NOT consist of any of the characters: comma ",", period ".",
# or underscore "_":
# · If a string is pure, print "{string} is pure."
# · Otherwise, print "{string} is not pure!"


number_of_strings = int(input())

for strings in range(number_of_strings):
    string = input()

    if "," in string or "." in string or "_" in string:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")
