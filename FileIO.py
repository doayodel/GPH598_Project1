'''
Created on Nov 20, 2014

@author: Bumsub
'''

import pysal

def openFile(connectionString, mode='r'):
    shp = pysal.pysal.core.FileIO.FileIO.open(connectionString, mode='r')  # @UndefinedVariable
    shp.seek(0)
    
@author: Kailai 

import pysal
shp = pysal.open('E:/PUP598 geocomputation/Cities.shp')
print len(shp)

import pysal
dbf = pysal.open('E:/PUP598 geocomputation/Cities.dbf')
print len(dbf)

import pysal
csv = pysal.open('E:/PUP598 geocomputation/Cities.csv')
print len (csv)
