from heapq import heappush, heappop

# Read Text file from user
print('-----------------read file------------------------')
s = (input("Please enter The Text File"))
with open(s) as file:
    data = file.read()
# print(data)
arr = list(data)
for i in arr:
    if i == " " and  "\n":
        arr.remove(i)
# print(arr)
# define the lists
count1 = []
count = []
test = []
c = 0
# calculate frequency
for j in range(len(arr)):
    c = 0
    for i in range(len(arr)):
        if arr[j] == arr[i]:
            c = c + 1
    count1.append(c)

# to get the frequency
for i in range(len(arr)):
    if arr[i] not in test:
        count.append(count1[i])
        test.append(arr[i])
print("--------------the Frequency Table for Characters--------------------")
this_dict = {}
for i in range(len(test)):
    this_dict.update({test[i]: count[i]})
print(this_dict)
# sorted the data
print("-----------------sorted the frequency table------------------")
sort = sorted(this_dict, key=this_dict.get)
sort1 = sorted(count)
dict_sort = {}
for i in range(len(count)):
    dict_sort.update({sort[i]: sort1[i]})
print(dict_sort)
# make the huffman tree
print('--------------------build tree--------------------------------')
heap = [[sort1, [sort, '']] for sort, sort1 in dict_sort.items()]
# heapify(heap)
print(heap)
while len(heap) > 1:

    left = heappop(heap)
    print('left = ', left)
    right = heappop(heap)
    print('right =', right)
    for i in left[1:]:
        i[1] = '0' + i[1]
    print("left add one = ", left)
    for i in right[1:]:
        i[1] = '1' + i[1]
    print('right add one =', right)
    print('')
    heappush(heap, [right[0] + left[0]] + right[1:] + left[1:])
huffman_list = right[1:] + left[1:]
print(huffman_list)

# C:\Users\lap store\Desktop\test\tese.txt

