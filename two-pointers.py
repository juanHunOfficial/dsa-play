"""
EASY


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

=====================================================================================================================================


MEDIUM


    1. 3Sum

        Description: 
            Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j != k and nums[i] + nums[j] + nums[k] == 0.
        Example:
            Input: [-1,0,1,2,-1,-4]
            Output: [[-1,-1,2],[-1,0,1]]



    2. Container With Most Water

        Description: 
            You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container that holds the most water.
        Example:
            Input: [1,8,6,2,5,4,8,3,7]
            Output: 49



    3. Sort Colors (Dutch National Flag Problem)

        Description: 
            Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. Use integers 0, 1, and 2 to represent the colors.
        Example:
            Input: [2,0,2,1,1,0]
            Output: [0,0,1,1,2,2]

=====================================================================================================================================


HARD


    1. Trapping Rain Water

        Description: 
            Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
        Example:
            Input: [0,1,0,2,1,0,1,3,2,1,2,1]
            Output: 6



    2. Minimum Window Substring

        Description: 
            Given two strings s and t, return the minimum window in s which will contain all the characters in t. If no such window exists, return an empty string.
        Example:
            Input: s = "ADOBECODEBANC", t = "ABC"
            Output: "BANC"



    3. Longest Substring Without Repeating Characters

        Description: 
            Given a string s, find the length of the longest substring without repeating characters.
        Example:
            Input: "abcabcbb"
            Output: 3

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
    
def run_tests(test_info: tuple) -> None:

    functions = {
        "pally": is_palindrome,
        "sorted_squares": squares_of_sorted_array, 
        "remove_dupes": remove_dupes
    }

    tests, func_name = test_info[0], test_info[1]
    func = functions[func_name]

    for i in range(3):
        print(func(tests[i]))
        

# Tests
all_tests = [
    (["race a car", " ", "No lemon, no melon"], "pally"),
    ([[-7,-3,2,3,11], [0,2], [-5,-4,-1,0,3]], "sorted_squares"),
    ([[0,0,1,1,1,2,2,3,3,4], [1,2,3], [1,1,1,1]], "remove_dupes")
]

for tests in all_tests:
    run_tests(tests)
