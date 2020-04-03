num1 = int(input("Enter first number::"))
num2 = int(input("Enter second number::"))
if  num2 > num1:
    temp = num2
    num2 = num1
    num1 = temp




def recursive_multiplication(num1 , num2):
    if num2 == 0:
        return 0
    return num1 + recursive_multiplication(num1 ,num2-1)


answer = recursive_multiplication(num1 , num2)
print(answer)