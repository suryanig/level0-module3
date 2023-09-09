for i in range (99, -1, -1):
    print(str(i)+ " bottles of beer on the wall, " + str(i)+ " bottles of beer. You take one down, pass it around, " + str(i-1) + " bottles of beer on the wall.")

if i == 1:
    print("1 bottle of beer on the wall. 1 bottle of beer. You take one down, pass it around, no more bottles of beer on the wall.")
elif i == 0:
    print("No more bottles of beer on the wall. No more bottles of beer. Go to the store, and buy some more, 99  bottles of beer on the wall." )
