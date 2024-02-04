#Part 1 - Multiply all list items together.
#Choose a function that will multiply each in the list to the preceeding number.
def mul_list(LIST):
    result1 = 1
    for i in LIST:
        result1 = result1 * i
    return result1
    
part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
print(mul_list(part1))
print("The answer to question 1 is: ", mul_list(part1))
#In this section I had to figure out an alternative definition to the add to the loop shown in the tutorial.
#I found an example of a multiplication definition to use on a list 'mul_list(LIST)' 

###Part 2 - Add all list items together.
part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]
result2 = 0

for i in part2:
    result2 = 0 + i

print("The answer to question 2 is: ", result2)

###Part 3 - In the given list, only add together items which are even. 
# Use Modelo operation to determine if a number is even or odd.
part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21] 
result3 = 0

for i in part3:
    result3 = 0 + i

print("The answer to question 3 is: " result3)
