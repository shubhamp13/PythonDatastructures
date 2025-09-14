'''
 list.insert(i, x):
    1.Insert an item at a given position. 
    2.The first argument is the index of the element before which to insert, so a.
    3.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
'''

mobile_no=[8,7,9,3,5,6,9,6,3,1]
mobile_no.insert(0,9)
# insert(index,data)-?>this will insert an element at specified index in list
for num in mobile_no:
    print(num)

def insert_index(list,index,data):
    new_list=[0]*(len(list)+1)
    j=0
    for i in range(len(new_list)):
        if i==index:
            new_list[i]=data
        else:
            new_list[i]=list[j]
            j+=1

    return new_list


pin_code=[4,1,3,5,1,2]
print(pin_code)#[4,1,3,5,1,2]
new_pincode=insert_index(pin_code,1,18)#[4,18,1,3,5,1,2]
print(new_pincode)
    