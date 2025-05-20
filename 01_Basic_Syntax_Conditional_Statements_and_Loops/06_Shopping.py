# Write a program that reads an integer number representing a budget. On the following lines, it reads integer numbers
# representing the prices of each product you should buy until it receives the command "End".
# During the iterations, if there is not enough budget left to buy the next product, it prints "You went in overdraft!"
# and end the program.
# Otherwise, if you accomplished to buy all products before receiving "End", it prints "You bought everything needed."

#
# budget = int(input())
#
# while True:
#     command = input()
#     if command == "End":
#         print("You bought everything needed.")
#         break
#     else:
#         current_price = int(command)
#         budget -= current_price
#         if budget < 0:
#             print("You went in overdraft!")
#             break
# --------------------------
# budget = int(input())
#
# while True:
#     command = input()
#     if command == "End":
#         print("You bought everything needed.")
#         break
#
#     current_price = float(command)
#     budget -= current_price
#     if budget < 0:
#         print("You went in overdraft!")
#         break
# -----------------------------

# budget = int(input())
# total_price = 0
#
# while True:
#     command = input()
#     if command == "End":
#         print("You bought everything needed.")
#         break
#
#     current_price = float(command)
#     if total_price > budget - current_price:
#         print("You went in overdraft!")
#         break
#
#     total_price += current_price

budget = int(input())
command = input()
total_price = 0

while command != "End":
    current_price = int(command)
    total_price += current_price
    if total_price > budget:
        print("You went in overdraft!")
        break

    command = input()

if total_price <= budget:
    print("You bought everything needed.")




