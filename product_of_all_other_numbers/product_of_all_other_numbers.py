'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    # Your code here
    right_multiply = [0] * len(arr)
    right_multiply[-1] = arr[-1]
    for i in range(1, len(arr)):
        right_multiply[len(arr)-i-1] = right_multiply[len(arr)-i] * arr[len(arr)-i-1]
    output = [0]*len(arr)
    prefix = 1
    current_index = 0
    while current_index < len(output)-1:
      output[current_index] = prefix * right_multiply[current_index+1]
      prefix *= arr[current_index]
      current_index += 1
    output[-1] = prefix
    return output
    


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
