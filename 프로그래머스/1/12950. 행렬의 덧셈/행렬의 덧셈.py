def solution(arr1, arr2):
    
    for row in range(len(arr1)):
        for col in range(len(arr1[0])):
            arr2[row][col] += arr1[row][col]
    
    return arr2
    