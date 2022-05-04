
def binary_search(numbers, target_value):
    left_index = 0
    right_index = len(numbers)-1
    step_count = 0
    while right_index >= left_index:
        step_count += 1
        mid_index = (right_index + left_index) // 2
        print("left: ", left_index, ", right: ", right_index, ", mid: ", mid_index, sep="")
        if numbers[mid_index] == target_value:
            return mid_index
        if numbers[mid_index] < target_value:
            left_index = mid_index +1
        if numbers[mid_index] > target_value:
            right_index = mid_index -1
        if right_index < (left_index):
            return -1
        

 	

numbers = [7, 13, 18, 54, 61, 78, 93]
print(binary_search(numbers, 61))