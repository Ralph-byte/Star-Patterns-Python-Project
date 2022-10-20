
num = int(input("Enter number of rows: "))

rows=1
for i in range(0, num):
    for j in range(0, rows):
        print("*", end="")
    rows=rows+2
    print()    