# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 17:05:11 2020

@author: ajb22
"""
"""
#############################################################################
############### variables ###################################################
# data types: 
number = 2 # int
name_of_number = "three" # string
array_numbers = [1, 2, 3] # array of integers
array_names = ["one", "two", "three"] # array of strings


#############################################################################
############### functions ###################################################

# create a function that takes 2 numbers and adds them - print the result
def my_sum(a , b):
    c = a + b
    print(c)
    return c


jojo = my_sum(423, 2546)
    

#############################################################################
############### if statements ###############################################

# ways to compare things:
# equals ==
# not equals !=
# less than <
# greater than >
# less than equal <=
# greater than equal >=


# if number does not equal 3 then do blanky blank blank 
if number != 3:
    # whatever you wanna do here
    print("boo ya")
    print(number)
    if name_of_number == "two":
        print("poop")
else:
    print("evan is a poop for calling me a small brain")
    print("because Ally is a smol brain")


# conjunction 
# and - both statements have to be true
# or - just one of the statements have to be true 
    
if number == 2:
    print("dos!")

elif number == 1 or number == 3:
    print("uno o tres!")
    if number == 3:
        print("yo soy tres veces mas listo")
    else:
        print("regular smart")
else:
    print("no bueno")

# you can also look to see if a value is in array 
    
if number in array_numbers:
    print("look at dat array beaut")
    

    
#############################################################################
############### for loops ################################################### 

for animal in ["hamster", "doggy", "kitty", "shark"]:
    #print(animal)
    for num_animal in [6,3,7]:
        print(animal, " : ",num_animal)

print('##############################')        
for num_animal in [6,3,7]:
    for animal in ["hamster", "doggy", "kitty", "shark"]:
        print(num_animal, " : ",animal)
        # if animal == "shark" and num_animal == 3:
        #     print("win")
        # else:
        #     print("try again")

        
# create a function that takes in a number ex: 1000 and returns a string 1,000
# you will need to know how to reverse a string - which is string[::-1]

# combining strings 
#first_name = "ally"
#last_name = "beach"
#first_name + last_name 
#Out[25]: 'allybeach'

def learningForLoops(my_num):
    my_str = str(my_num)
    print(my_str)
    out_str = ""
    my_iter = 0
    # my_str = '1000'
    # my_char = '1' , '0', '0', '0'
    # how about if my_str = '0001'
    for my_char in my_str[::-1]:
        out_str = out_str +  my_char
        print(my_char)
        if my_iter < 2: 
            my_iter = my_iter + 1
        else: 
            
            out_str = out_str + ","
            
            #print("NEED TO ADD COMMA")
            my_iter = 0
    out_str = out_str[::-1]
    if out_str[0] == ',':
        out_str = out_str[1:]
    print(out_str)
learningForLoops(100000000) 

# fizz buzz

# will need modulus - in python it is '%'
# example 
# 15 % 3 = 0
# 16 % 3 = 1
def fizzBuzz(fizz_num):
    for buzz_num in range(1,fizz_num+1):
        check1 = buzz_num % 3
        check2 = buzz_num % 5
        if check1 == 0 and check2 != 0:
            print("Fizz")
        if check1 != 0 and check2 == 0:
            print("Buzz")
        if check1 == 0 and check2 == 0:
            print("Fizzbuzz")
        if check1 != 0 and check2 != 0:
            print(buzz_num)

fizzBuzz(15)
"""
# integer to ascii and ascii to integer 

def ascii_to_int(ascii):
    ascii_ans = ascii - 48
    print(ascii_ans)

ascii_to_int(52)


def int_to_ascii(int):
    int_ans = int + 48
    print(int_ans)

int_to_ascii(6)


# sorting





