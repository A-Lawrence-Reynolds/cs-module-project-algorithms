'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

def sliding_window_max(nums, k):
    # Your code here
        if nums == []:
            return []
        ans,tmp = [], []
        for i in range(0, k):
            while tmp != [] and nums[i] > nums[tmp[-1]]:
                tmp.pop()
            tmp.append(i)
        for i in range(k, len(nums)):
            ans.append(nums[tmp[0]])
            while tmp != [] and nums[i] > nums[tmp[-1]]:
                tmp.pop()
            tmp.append(i)
            while tmp != [] and tmp[0] <= i-k:
                tmp.pop(0)
        ans.append(nums[tmp[0]])
        return ans
       
if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
