import time

ordered_list = []
for number in range(10):
    ordered_list.append(number)
print(ordered_list)

user_value = input("Now enter your number: ")
time.sleep(1)
print("Now we're going to see if your number belongs to the list...")
time.sleep(1)
for number2 in ordered_list:
    if number2 == int(user_value):
        print("Yes, it's a match!")
