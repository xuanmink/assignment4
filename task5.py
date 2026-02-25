def remove_odd_numbers(original_list):
    even_list= []
    for num in original_list:
     if num%2== 0:
       even_list.append(num)
    return even_list
if __name__ == "__main__":
 test_list = [1,2, 3 , 4, 5,6, 7, 8, 9,10]
 cut_down_list = remove_odd_numbers(test_list)
 print(f"Original list: {test_list}")
 print(f"Cut-down list: {cut_down_list}")