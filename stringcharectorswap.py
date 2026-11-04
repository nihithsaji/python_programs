str1=input("Enter the first string : ")
str2=input("Enter the second string : ")
new_str1=str2[0]+str1[1:]
new_str2=str1[0]+str2[1:]
result=new_str1+" "+new_str2
print("swapped string is - ",result)
