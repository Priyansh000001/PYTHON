import numpy as np 

# Unique() ---> It will create an array in which it will remove duplicate values an
# it will return 3 arrays :
# arr ---> Unique elements of array
# return_index = True ----> Indexing of Unique element
# return_counts = True ---> Frequency of each unique element.

a = np.array([1,2,3,1,1,1,1,4,5,4,4,4,4, 4, 4, 6, 71])
print(a)

b= np.unique(a, return_index = True , return_counts = True)
print(b)

# linspace() ----› It will return an array in which elements will be same gap in a given range.
# syntax : np.linspace(min_num , max_num , total_numbers)

a = np.linspace(1,2,5)
print(a)

# Horizontal And Vertical Stacking ---->
# Horizontal Stacking ---› It will add 2 or more arrays in horizontally .
a = np.arange (1,5)
print(a)

b = np.arange(5,9)
print(b)

c = np.arange(9,13)
print(c)

np.hstack((a,b,c))

np.vstack((a,b,c))
