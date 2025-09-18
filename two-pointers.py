"""


    1. Valid Palindrome

        Description: 
            Given a string s, return true if it is a palindrome, considering only alphanumeric characters and ignoring cases.
        Example:
            Input: "A man, a plan, a canal: Panama"
            Output: true



    2. Squares of a Sorted Array

        Description: 
            Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
        Example:
            Input: [-4,-1,0,3,10]
            Output: [0,1,9,16,100]



    3. Remove Duplicates from Sorted Array

        Description: 
            Given a sorted array nums, remove the duplicates in-place such that each element appears only once and return the new length.
        Example:
            Input: [1,1,2]
            Output: 2 (array becomes [1,2,_])


"""

def is_palindrome(s:str) -> bool:
    """ 
    1. Valid Palindrome

        Description: 
            Given a string s, return true if it is a palindrome, considering only alphanumeric characters and ignoring cases.
        Examples:
            1:
                Input: "race a car"
                Output: False
            2:
                Input: " "
                Output: False
            3:
                Input: "No lemon, no melon"
                Output: True

    """
    if len(s) <= 1:
        return False
    s = s.lower() # This is to account for case differences
    left, right = 0, len(s) - 1 # assign the left to the beginning of the list and right to the end

    while left < right: # Continue to run until the two pointers cross:
        if s[left] == s[right]: # if equal
            left +=1
            right -=1
        elif not s[right].isalnum() or s[right] == " ": # if the right pointer is not an alphanumeric char or is a space
            right -=1
        elif not s[left].isalnum() or s[left] == " ": # if the left pointer is not an alphanumeric char or is a space
            left +=1
        elif s[left] != s[right]: # if all the previous conditions are met and these are just two alphanumeric chars that and not equal, terminate and return false
            return False
    return True


def squares_of_sorted_array(arr: list) -> list:
    """
    2. Squares of a Sorted Array

        Description: 
            Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
        
    """
    for i in range(len(arr)): # double all the input
        arr[i] *= arr[i]

    left, right = 0, len(arr)-1
    new_list = []

    while left <= right: # add the the new_list from biggest to smallest until the pointers cross
        if arr[right] > arr[left]:
            new_list.insert(0, arr[right])
            right -=1
        else:
            new_list.insert(0, arr[left])
            left +=1

    return new_list


def remove_dupes(arr: list) -> tuple:
    """
    3. Remove Duplicates from Sorted Array

        Description: 
            Given a sorted array nums, remove the duplicates in-place such that each element appears only once and return the new length.
        Example:
            Input: [1,1,2]
            Output: 2 (array becomes [1,2,_])
    """
    left, right = 0, 1
    new_list = []

    while right != len(arr): # only append to the list when you come across a pair that dont match
        if arr[left] != arr[right]:
            new_list.append(arr[left])
        if right == len(arr)-1:
            if arr[left] != arr[right]:
                new_list.append(arr[right])
        left +=1
        right +=1

    if len(new_list) == 0: # to solve for every index being the same value
        new_list.append(arr[0])

    return (len(new_list), new_list)


def array_palindrome(arr: list) -> bool:
    left, right = 0, len(arr) -1
    while left < right:
        if arr[left] == arr[right]:
            left +=1
            right -=1
        elif arr[left] != arr[right]:
            return False
    return True
    
def run_tests(test_info: tuple) -> None:

    functions = {
        "pally": is_palindrome,
        "sorted_squares": squares_of_sorted_array, 
        "remove_dupes": remove_dupes,
        "array_pally": array_palindrome
    }

    tests, func_name = test_info[0], test_info[1]
    func = functions[func_name]

    for i in range(3):
        print(func(tests[i]))
        

# Tests
all_tests = [
    (["race a car", " ", "No lemon, no melon"], "pally"),
    ([[-7,-3,2,3,11], [0,2], [-5,-4,-1,0,3]], "sorted_squares"),
    ([[0,0,1,1,1,2,2,3,3,4], [1,2,3], [1,1,1,1]], "remove_dupes"),
    ([[1, 2, 3, 3, 2, 1], [1, 3, 2, 3, 4], ['a', 'b', 'c', 'b', 'a']], "array_pally")
]

for tests in all_tests:
    run_tests(tests)
