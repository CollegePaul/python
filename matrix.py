#Function declaration, with 2 parameters, matrix a and matrix b
def matrixmultiplication (A, B):

    #get row and colum sizes
    Arows = len(A)
    Brows = len(B)
    Bcols = len(B[0])
    Acols = len(A[0])

    #check the matrix can be done
    if Acols != Brows:  #see line 26
        print("Not applicable")
        return
    
    #create the reuslting matrix filled with zeros 
    C = []
    for row in range(0,Bcols):
        newrow = []
        for col in range(0,Arows):
            newrow += [0]   
        C += [newrow] 
           
    #the nested for loops are used to loop over the rows and columns
    for i in range(Arows):  #the rows in A
        for j in range(Bcols):  #Column in B
                for k in range(Acols):  #the row in B , see line 11
                    #add to the result
                    #result[row][column] += A[row][column] * B[row][column]
                    #Because this is looping over the rows, this is adding results
                    C[i][j] += A[i][k] * B[k][j]
    
    #the funcion sends the answer back
    return C

#code to test rhe function  2x3   *  3x2 
#testing a 2x2 * 2x2 is not a good idea, as the rows and cols may be mixed up
#but because they are the same size you might not know.
#matrix example and walkthrough is at...
#https://www.mathsisfun.com/algebra/matrix-multiplying.html
m1 = [[1,2,3],
      [4,5,6]]

m2 = [[7,8],
      [9,10],
      [11,12]]

#store result from the function return
result = matrixmultiplication(m1,m2)

#loop over the rows in the resulting matrix to print by row
for row in result:
    print(row)


#Original problem source
#https://www.gla.ac.uk/media/Media_632422_smxx.pdf