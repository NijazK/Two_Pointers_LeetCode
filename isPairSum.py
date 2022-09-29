# Python program for two pointers technique 
# Find if there is a pair [A0..N-1] with given sum

def isPairSum(A, N, X):
    
    # First pointer
    i = 0
    
    # Second pointer
    j = N - 1
    
    while (i < j):
        
        # If there is a match
        if (A[i] + A[j] == X):
            return True
        
        # If sum of elements at current
        # pointers is less, we move towards
        # higher values by doing i += 1
        elif (A[i] + A[j] < X):
            i += 1
            
        # If sum of elements at current
        # pointers is more, we move towards
        # lower values by doing j -= 1
        else:
            j -= 1
    return False

# Array declaration
arr = [2, 3, 5, 8, 9, 10, 11]

# value to search
val = 18

print(isPairSum(arr, len(arr), val))
