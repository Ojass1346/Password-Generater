import random

char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+`~[{]}:;'/.,<>\|"

num = int(input("How many passwords do you want-"))
len = int(input("How Long do you want your password to be-"))

for i in range(num):
    print()
    for j in range(len):
        print(random.choice(char),end='')