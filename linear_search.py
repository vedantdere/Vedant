number_of_elements = int(input("Enter how many elements u want::"))
num_list = []
for i in range(1,number_of_elements+1):
    numbers = int(input("Enter elements ::"))
    num_list.append(numbers)
target = int(input("Enter your target::"))



def insetion(num_list , target):
    for i in range(number_of_elements):
        if num_list[i] == target:
            print(num_list[i])
            break
    else :
        print("Not found")


insetion(num_list , target)






