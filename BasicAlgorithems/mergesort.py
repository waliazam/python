'''
Merge Sort for sorting books by title because of its efficiency with larger datasets.
Binary Search for finding a book by title because it's fast, 
provided the list of books is sorted.

Step 1: Define the Book Inventory

'''

# Define the book inventory
books = [
    {"title": "Python Programming", "author": "John Doe", "year": 2015},
    {"title": "Introduction to Algorithms", "author": "Thomas H. Cormen", "year": 2009},
    {"title": "Clean Code", "author": "Robert C. Martin", "year": 2008},
    {"title": "Design Patterns", "author": "Erich Gamma", "year": 1994},
    {"title": "The Pragmatic Programmer", "author": "Andrew Hunt", "year": 1999}
]

# Merge Sort Function
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i]['title'] < R[j]['title']:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Binary Search Function
def binary_search(arr, title):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]['title']

        if mid_val < title:
            low = mid + 1
        elif mid_val > title:
            high = mid - 1
        else:
            return arr[mid]
    return None

# Sort the books by title
merge_sort(books)

# Search for a specific book by its title
book_title = input("Enter the title of the book you're searching for: ")


found_book = binary_search(books, book_title)

if found_book:
    print(f"Book found: {found_book}")
else:
    print("Book not found.")
