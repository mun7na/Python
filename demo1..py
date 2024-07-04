def reverse_string(str):
    str1=""
    for i in str:
        str1=i+str1
    return str1

str="munna"
print("Orginal is ",str)
print("Reverse ",reverse_string(str))
