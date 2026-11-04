list1=["aravind","aparna"]
print("The orginal list :"+str(list1))
res=[ord(ele)for sub in list1 for ele in sub]
print("the ASCII list is :"+str(res))
