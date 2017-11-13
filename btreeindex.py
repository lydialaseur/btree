#import btreenode.BTreeNode
from btreenode import BTreeNode
import csv

class BTreeIndex(object) :
    '''Represents a B-Tree index for a database table.

        The table is represented by a directory name dir,
        and the i-th record is contained in the file dir/j/k
        where j = i/1000 and k = i % 1000.

        The column names are contained in the file dir/header.'''

    def __init__(self, dir, column, p) :
        self.dir = dir
        self.column = column
        self.colnum = 0 # set this from dir/header and check it exists!
        self.p = p
        self.root = BTreeNode(p)

    def create(self):
        '''Creates a B-Tree index on the column.'''
        
        # for each i, insert the key of the i-th record and a record pointer into the index.
            # reset root if necessary

        # return the number of records indexed.
