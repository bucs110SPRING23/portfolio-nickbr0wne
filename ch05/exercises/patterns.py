def startriangle():
    rows=int(input("Amount of rows: "))
    for i in range(1, rows+1):
        print("*"*i)
startriangle()

def reversestartriangle():
    rows=int(input("Amount of rows: "))
    for i in range(rows, 0, -1):
        print("*"*i)
reversestartriangle()
