'''
Created on Nov 20, 2014

@author: Bumsub
'''

import pysal

def openFile(connectionString, mode='r'):
    shp = pysal.pysal.core.FileIO.FileIO.open(connectionString, mode='r')  # @UndefinedVariable
    shp.seek(0)
    outputArray = []
    for i in shp:
        outputArray.append(i)
