rows=int(input("Enter the number of rows: "))
print(rows,end="\n\n")
print("The pattern is :")
for i in range(1,rows+1):
    for j in range(rows,i-1,-1):
        print("*",end=" ")
    print("\n")    


# output:
#Enter the number of rows: 5
#5

#The pattern is :
#* * * * * 

#* * * * 

#* * * 

#* * 

#*

