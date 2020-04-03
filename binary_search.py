number_of_elements = int(input("Enter how many elements u want::"))
num_list = []
for i in range(1,number_of_elements+1):
    numbers = int(input("Enter elements ::"))
    num_list.append(numbers)
target = int(input("Enter your target::"))
num_list.sort()
print(num_list)



def binary_search(num_list , target):
    min = 0
    max = len(num_list)
    mid = (min+max)//2
    for i in range (number_of_elements):
        if mid < target:
            new_list = num_list[1:mid+1]
            if num_list[i] == target:
                print(num_list[i])
        elif mid> target:
            new_list = num_list[mid:max+1]
            if new_list[i] == target:
                print(new_list[i])
        elif mid == target:
            print(mid)
        else:
            print("Not found")





binary_search(num_list , target)


