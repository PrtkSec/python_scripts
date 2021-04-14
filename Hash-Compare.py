#!/usr/bin/env

#allow user to input two values
hash_1 = input("Enter 1st Hash Value:")
hash_2 = input("Enter 2nd Hash value:")

#remove the space character
user_input = hash_1.replace(" ","")
user_input = hash_2.replace(" ","")

#compare if statement
if (hash_1==hash_2):
    print("hash matched!")
else:
    print("hash NOT matched!")

