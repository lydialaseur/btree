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

        #get the total number of records to insert
        total_num_rec = 0
        for page in list(os.walk(self.table_dir))[0][1]:
            num_recs_current_page = len(list(os.walk('{0}/{1}'.format(self.table_dir,page)))[0][2])
            total_num_rec += num_recs_current_page

        level_counter = 0
        insert_counter = 0

        #for each record in the "table"
        for i in range(1, total_num_rec+1):
            #set pointer as path to record
            ptr = '{0}/{1}/{2}'.format(self.table_dir,i//1000,i%1000)
            #set key as the value at specified column
            record = list(csv.reader(open(ptr),delimiter=','))[0]
            key = record[self.colnum]

            #if key is an empty string, i.e. if key is null, set key to more readable value
            if key == '':
                key = 'NULL_{0}'.format(self.column)

            key_ptr = (key,ptr)

            current_node = self.root

            current_node.insertDown(key_ptr)
            insert_counter += 1

            #if root before insert now has a parent, reset the root as the parent, and increment the level counter
            if current_node.parent != None:
                # print('Level Up!')
                level_counter += 1
                self.root = current_node.parent

            #print progress
             if (insert_counter%100000) == 0:
                print('{0} insertions complete'.format(insert_counter))
                print('Current level of tree is {0} \n'.format(level_counter))

        return(insert_counter,level_counter)
