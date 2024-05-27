
            if arr [row1][col1]> arr[row2][col2]:
                arr[row1][col1], arr[row2][col2] = arr[row2][col2], arr[row1][col1]

def search_element(arr,element): 
    found = False 
    for i in range(len(arr)):
        for j in range (len(arr[i])):
            if arr[i][j]== element:
                print (f"Element found at position: row = {i}, column = {j} ")
                found = True
                return 
    if not found:
        print("Element not found in the given array.")

arr = [
    [9, 2, 3], [4, 5, 6], [7, 8, 1]
]

print(arr)
bubble_sort_2nd(arr)
print(arr)

search = int (input("Enter the element to search: "))
search_element(arr, search)