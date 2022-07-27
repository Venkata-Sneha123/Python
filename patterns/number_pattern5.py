rows=int(input("Enter the number of rows: "))
print(rows,end="\n\n")
print("The pattern is :")
for i in range(rows,0,-1):
    for j in range(rows,i-1,-1):
        print(i,end=" ")
    print("\n")  



#output:
#Enter the number of rows: 5
#5

#The pattern is :
#5 

#4 4 

#3 3 3 

#2 2 2 2 

#1 1 1 1 1     

