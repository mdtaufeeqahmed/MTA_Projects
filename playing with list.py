list=[4,5,6,7,8,9,7]
print(list)
list.append(2)      #adding element at last
print(list)
list.pop()           #removing the last element
print(list)
list.remove(8)      # removing selected element directly
print(list)
list=list+[8,5,3,10,5,9,6,7] # appending more elements at a time
print(list)
list.extend([58,49,21])        # appending more elements at a time
print(list)
list.insert(2,77)    #adding an element at a selected location(index)
print(list)
list.pop(1)          #removing the element at a selected location(index)
print(list)
list.sort()          #sorting in increasing order
print(list)
list1=list.copy()    #deep copy----the list1(new) will not get effected with the changes in the list(old)
print(list1)
print(min(list))
print(max(list))
print(list)
del list[2:10]       # deleting elements with index values from 2 to 10
print(list)
del list[ :7]        #deleting elements fron starting index to index 7
print(list)
print(list1)
list2=list1.copy()
list1.clear()       #clearing the list1
print(list1)
print(list2)
print(list2[6])      # selecting a particular element based on index from list2
print(list2.count)
print(list2.count(7))   # number of occurences of an element counted
print(list2.index)
print(list2.index(5))    #index of element in list
print(len(list2))     #length of list2
list2.extend([20,47,58,64])
print(list2)
list2.sort()
print(list2)
print(len(list2))
print(len(list2)//3)