rows=int(input("Enter the number of rows: "))
print(rows,end="\n\n")

print("The pattern is :")
for i in range(1,rows+1):
    ch=97
    for j in range(1,i+1):
        print(chr(ch),end=" ")
        ch=ch+1  
    print("\n") 

#output:
#Enter the number of rows: 5
#5

#The pattern is :
#a 

#a b 

#a b c 

#a b c d 

#a b c d e 

