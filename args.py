# 1. Write a function that takes an unknown number of arguments and returns their sum.

def unknown_number(*number):
    return sum(number)
print(unknown_number(2, 7, 3, 1, 5))



# 2. Write a function that takes two arguments, the first being a string and the second being an
# unknown number of integers. The function should return a new string where the integers have 
# been added to the original string.

def string_integer(string, *numbers):
    results = string + "".join(str(num1)for num1 in numbers)
    return results
results= string_integer("I love clarah", 10, 20, 30) 
print(results)  
    
    

# 3. Write a function that takes an unknown number of keyword arguments and returns a dictionary
# where the keys are the argument names and the values are the argument values.

def key_values(**names):
    return names
result2 = key_values(name="esther", title = "mother", age = 70,)
print(result2)


# 4. Write a function that takes a function and an unknown number of arguments, and returns the
# result of calling the function with the arguments.

def return_result(num1, num2):
    return num1 + num2
answer2 = args_number(return_result, 45, 23)
print(answer2)

def mul_result(w, x, y):
    return w*x*y
answer2 = args_number(mul_result, 12, 32, 20)
print(answer2)


# 5. Write a function that takes a list of integers and an unknown number of keyword arguments.
# The function should return a new list where each integer in the original list has been 
# multiplied by the value of the corresponding keyword argument.

def multiply_by_value(list, **integers):
    result3 = []
    for x in list in enumerate(list):
        keys = "arg{}".format(x+1)
        if keys in integers:
            result3.append(list * integers[keys])
        else:
            result3.append(list)    
result3 = multiply_by_value([12, 54, 23, 22], arg1 = 5, arg3 = 8)
print(result3)


# 6. Write a function that takes a list of integers and an unknown number of additional integers 
# as arguments. The function should return the index of the first occurrence of the sum of the 
# list and the additional integers

def index_first_occurence(nums, *number):
    target_sum = sum(nums) + sum(number)
    this_sum = 0
    for x, num in enumerate(nums):
        this_sum += num
        if this_sum == target_sum:
            return x
    return -1
nums = [4, 6, 7, 9]
index = index_first_occurence(nums,6, 7)
print(index)



# 7. Write a function that takes an unknown number of keyword arguments, each with a string value.
# The function should concatenate all the strings and return the resulting string.

def concatenate_strings(**string):
    result4 = ""
    for number, strg in string.items():
        if isinstance(strg, str):
            result4 += strg
    return result4
result4 = concatenate_strings(x = "my", b = "mother")
print(result4)        
