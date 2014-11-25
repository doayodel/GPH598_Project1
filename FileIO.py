'''
Created on Nov 20, 2014

@author: Bumsub
'''

The function 'openFile' can open csv, txt, dbf and shp files

# 'seek' finds the first row and 'append' adds subsequent rows
# 'outputArray' returns a list data type

def openFile(connectionString, mode='r'):
        point = pysal.pysal.core.FileIO.FileIO.open(connectionString, mode='r')  # @UndefinedVariable
        point.seek(0)
        outputArray = []
        for i in point:
            outputArray.append(i)
        return outputArray
