'''
1.list.append(item): It is used to add item to the end of the list
'''
list_one=[8,7,9,3,5,6,9,6,3,1]
name='shubham'
list_one.append(name)
for x in list_one:
    print(x)

    
# without using inbuilt method how to append element at the end of the list
list_one=[8,7,9,3,5,6,9,6,3,1]
def add_end(list,data):
    new_list=[0]*(len(list)+1)
    for x in range(len(list)):
        new_list[x]=list[x]
    new_list[len(list)]=data
    return new_list

list_one=add_end(list_one,"Puri")
for x in list_one:
    print(x)