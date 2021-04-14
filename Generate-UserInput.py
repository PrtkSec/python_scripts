#!/usr/bin/env

#request user for input
user_input = input("Enter String:")
user_input2 = int(input("Enter number:"))

#remove spaces
user_input = user_input.replace(" ","")

#generate the input string * the int value
result = user_input * user_input2

#print the input length
print (result)