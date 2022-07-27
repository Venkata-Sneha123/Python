rows=int(input("Enter the number of rows: "))
print(rows,end="\n\n")
print("The pattern is :")
for i in range(rows,0,-1):
    for j in range(0,i):
        print(i,end=" ")
    print("\n")    


# output: 
#Enter the number of rows: 5
#5

#The pattern is :
#5 5 5 5 5 

#4 4 4 4 

#3 3 3 

#2 2 

#1

