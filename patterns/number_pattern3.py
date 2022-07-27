rows=int(input("Enter the number of rows: "))
print(rows,end="\n\n")
print("The pattern is :")
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")    


# output: 
#Enter the number of rows: 5
#5

#The pattern is :
#1 

#1 2 

#1 2 3 

#1 2 3 4 

#1 2 3 4 5

