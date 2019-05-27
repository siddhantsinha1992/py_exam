l1=[]

n=int(input("Enter the number of elements in the list"))

for i in range(0,n):
    l1.append(int(input("Enter element: ")))

print("The list is:")
print(l1)

print("The maximum number in list l1 is")
print(max(l1))