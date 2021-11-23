''' Write a program to 
find all pairs of an integer array whose sum is equal to a given number? '''

def match_sum_pairs(arr, n, sum):
    count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1
    return count
 
arr = [2,3,5,6,8,2,4,7,9,6]
n = len(arr)
sum = 7
print(f"Count of pairs is, {match_sum_pairs(arr, n, sum)}")