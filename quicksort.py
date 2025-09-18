def quicksort(arr: list) -> list:
    pivot = len(arr) -1
    i = -1 # if arr[j] < arr[pivot], i +=1 and swap arr[i] and arr[j]
    j = 0 # if arr[j] > arr[pivot], j +=1 until you get to the pivot
    temp = None

    if len(arr) == 1:
        return arr

    while j != pivot:
        if arr[j] < arr[pivot]:
            i+=1
            temp=arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        j+=1
    
    temp = arr[pivot]
    arr[pivot] = arr[i+1]
    arr[i+1] = temp
    pivot = i+1

    return arr
    # Once you reach the pivot, you will increment i one more time and the swap arr[i] and arr[pivot]
    # Now partition the arr into halves and then recursively do this with each half. 
    # NOTE: you are getting the values to the left and the right of the pivot. You wont grab the pivot itself.


test_cases = [
    [8,2,4,7,1,3,9,6,5], 
    [5,0,2,6,9,3,1,8], 
    [2,7,9,3,5,6,0,1]
]

for test in test_cases:
    print(quicksort(test))