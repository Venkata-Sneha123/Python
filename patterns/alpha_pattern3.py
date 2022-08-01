rows=int(input("Enter the number of rows: "))
print(rows,end="\n\n")
ch=97
print("The pattern is :")
for i in range(1,rows+1):
    for j in range(rows,i-1,-1):
        print(chr(ch),end=" ")
        ch=ch+1  
    print("\n")   

#output:
#Enter the number of rows: 5
#5

#The pattern is :
#a b c d e 

#f g h i 

#j k l 

#m n 

#o    

