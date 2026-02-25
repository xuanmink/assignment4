def sum_of_list(numbers_list):
    total= 0
    for num in numbers_list:
     total+=num
    return total
if __name__ == "__main__":
 my_list = [10, 25, 5, 20]
 result = sum_of_list(my_list)
 print(f"The list is: {my_list}")
 print(f"The sum is: {result}")