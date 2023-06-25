# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


import string
import random

if __name__ == '__main__':
    s1 = string.ascii_lowercase
    print(s1)
    s2 = string.ascii_uppercase
    print(s2)
    s3 = string.digits
    print(s3)
    s4 = string.punctuation
    print(s4)
    passlen = int(input("Enter password length : "))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    #print(s)

    # random.shuffle(s)
    # print(s)
    print("Your password is: ")
    # print("".join(s[0:passlen]))
    print("".join(random.sample(s, passlen)))

