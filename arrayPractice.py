from array import *

# 1. Create an array and traverse

my_array = array('i',[1,2,3,4,5])

for i in my_array:
    print(i)
# 2.Access individual elements through indexes
print("step 2")
print(my_array[3])
# 3.Append any value to the array using append() method
print("step 3")
my_array.append(6)
print(my_array)
# 4. Insert value in an array using insert method
print("step 4")
my_array.insert(4, 11)
print(my_array)
# 5.Extend python array using extend() method
print("step 5")
my_array1 = array('i',[10,11,12])
my_array.extend(my_array1)
print(my_array)
# 6.Add items from list into arrays using fromList() method
print("step 6")
tempList =[21,22,23]
my_array.fromlist(tempList)
print(my_array)
# 7.remove any aray element using remove() method
print("step 7")
my_array.remove(11)
print(my_array)
# 8.remove last array method using pop() method
print("step 8")
my_array.pop()
print(my_array)
# 9.fetch any element through its index using index()  method
print("step 9")
print(my_array.index(21))
# 10.Reverse a python array using reverse method
print("step 10")
my_array.reverse()
print(my_array)
# 11.get array buffer information using buffer_info() method
print("step 11")
print(my_array.buffer_info())
# 12.check for number of occurrences of an element using count() method
print("Step 12")
my_array.append(11)
print(my_array.count(11))
print(my_array)
# 13.convert array to string using toString() method
print("Step 13")
strTemp = my_array.tostring()
print(strTemp)
ints = array('i')
ints.fromstring(strTemp)
print(ints)
# 14.Convert array to a python list with same elements using toList() method
print("step 14")
print(my_array.tolist())
# 15.Append a string to char array using fromString() method())
# 16.Slice elements from an array
print("step 16")
print(my_array[1:4])