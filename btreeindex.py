#import btreenode.BTreeNode
from btreenode import BTreeNode
import csv
import os

class BTreeIndex(object) :
    '''Represents a B-Tree index for a database table.

        The table is represented by a directory name dir,
        and the i-th record is contained in the file dir/j/k
        where j = i/1000 and k = i % 1000.

        The column names are contained in the file dir/header.'''

    def __init__(self, table_dir, column, p) :
        self.table_dir = table_dir
        self.column = column

        infile = open('{}/header'.format(table_dir),'r')
        header = infile.read().strip().split(',')
        if column in header:
            self.colnum = header.index(column) # set this from dir/header and check it exists!
        else:
            print('Column named {} does not exist!'.format(column))
        infile.close()
        self.p = p
        self.root = BTreeNode(p)

    def create(self):
        '''Creates a B-Tree index on the column.'''

        # for each i, insert the key of the i-th record and a record pointer into the index.
            # reset root if necessary

        # return the number of records indexed.


        #get the range of i
        total_num_rec = 0
        for page in list(os.walk(table_dir))[0][1]:
            num_recs_current_page = len(list(os.walk('{0}/{1}'.format(table_dir,page)))[0][2])
            total_num_rec += num_recs_current_page


        for i in range(1, total_num_rec+1):
            ptr = '{0}/{1}/{2}'.format(self.table_dir,i//1000,i%1000)
            infile = open(ptr)
            key = infile.read().strip().split(',')[self.colnum]
            infile.close()

            key_ptr = (key,ptr)
            current_node = self.root
            current_node.insertDown(key_ptr)
