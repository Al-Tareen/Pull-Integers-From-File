def averageOfNumbers():
    
    quantity = 0.0
    avg = 0.0
    total = 0.0

    #Open the file
    infile = open(r'C:\Users\Al\OneDrive\Desktop\Main\Python\numbers.txt', 'r')

    #Read the file's contents
    contents = infile.read().strip().split()

    #Display the file's contents
    print(contents)

    #Read values from file and compute average
    for num in contents:
        amount = float(num)
        total += amount
        quantity = quantity + 1

    avg = total / len(contents)

    #Close the file
    infile.close()

    #Print the amount of integers in file and average
    print('There were ', quantity, ' numbers in the file.' )
    print(format(avg, ',.2f'),  'is your average')

averageOfNumbers()
