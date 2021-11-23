'''Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.'''

def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
        
A = [1, 2, 3, 4, 5, 6]
reverseList(A, 0, 5)
print(f"Reversed list is {A}")
