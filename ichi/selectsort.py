# Problem Statement
# You are given N pairs of integers. Each pair contains two values (a, b).
# Your task is to sort the pairs using Selection Sort based on the following rules:

# Sorting Criteria
# Sort pairs in ascending order of the first element.
# If the first elements are equal, then sort based on the second element in ascending order.
# Input Format
# First line contains an integer N — number of pairs.

# Next N lines each contain two integers a and b.

# Output Format
# Print sorted pairs (one per line)
n = int(input("Enter no of pairs: "))
pairs = []
for i in range(n):
    a, b = map(int, input("Enter a and b: ").split())
    pairs.append((a, b))
    
print("Pairs: ", pairs)
print("Sorted Pairs: ", sorted(pairs))
    