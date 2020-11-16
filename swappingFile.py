def SwapFileData():
    data1 = input("Enter your file name :  ")
    data2 = input("Enter your file name :  ")
    
    file1 = open(data1,'r')
    data_a = file1.read()
    file1.close()
       
    file2 = open(data2, 'r')
    data_b = file2.read()
    file2.close()

    file3 = open(data1,"w")
    file3.write(data_b)
    file3.close()

    file4 = open(data2,"w")
    file4.write(data_a)
    file4.close()

SwapFileData()
    
    
