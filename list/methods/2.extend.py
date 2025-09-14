'''

2.extend(iterable): it is used  to add new iterable objet to end of the list and it will return none

if we call list1.extend(list2) then at the end of the list1  list2 is added and method will return none that means list1 will be updated

which are iterable objects in python?
    1.string
    2.list
    3.set
    4.tuple
    5.dictionary (key,value)
'''


list_one=[8,7,9,3,5,6,9,6,3,1]
list_two=['shubham','siom','pune']

list_one.extend(list_two)
# in above method call list_one will be updated that means list_one will be now combination of list_one and list_two 
# [8,7,9,3,5,6,9,6,3,1,'shubham','siom','pune']

for x in list_one:
    print(x)


#  without using any inbuilt method extend operation

def add_list(list1,list2):
    new_len=len(list1)+len(list2)
    new_list=[0]*(new_len)
    for x in range(len(list1)):
        new_list[x]=list1[x]
    y=len(list1)
    for x in range(len(list2)):
        new_list[y]=list2[x]
        y+=1
    return new_list

l1=[1,2,3,4,5,6]
l2=[7,8,9,10,11,12]
l3=add_list(l1,l2)
print(l3)
