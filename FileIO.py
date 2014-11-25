'''
Created on Nov 20, 2014

@author: Bumsub
'''

import pysal

def openFile(connectionString, mode='r'):
        point = pysal.pysal.core.FileIO.FileIO.open(connectionString, mode='r')  # @UndefinedVariable
        point.seek(0)
        outputArray = []
        for i in point:
            outputArray.append(i)
        return outputArray
