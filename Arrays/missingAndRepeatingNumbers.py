# https://www.codingninjas.com/codestudio/problems/873366?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website

def missingAndRepeating(arr, n):
    # Write your code here
    repeating = 1
    for i in range(n):
        t = abs(arr[i]) - 1
        if arr[t] < 0:
            repeating = t + 1
        else:
            arr[t] = -arr[t]

    for i in range(n):
        if arr[i] > 0:
            return [i + 1, repeating]

    pass
