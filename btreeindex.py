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
        for page in list(os.walk(self.table_dir))[0][1]:
            num_recs_current_page = len(list(os.walk('{0}/{1}'.format(self.table_dir,page)))[0][2])
            total_num_rec += num_recs_current_page


        level_counter = 0
        insert_counter = 0
        for i in range(1, total_num_rec+1):
            ptr = '{0}/{1}/{2}'.format(self.table_dir,i//1000,i%1000)
            record = list(csv.reader(open(ptr),delimiter=','))[0]
            key_val = record[self.colnum]
            key = "{0}".format(key_val)
            print('Current Key: {0}'.format(key))
            #if key is null for current record, skip to next record
            if key == '':
                continue

            key_ptr = (key,ptr)
            # print('Key - pointer pair: {0}'.format(key_ptr))

            current_node = self.root

            if current_node.parent != None:
                print('Error, root has a parent!')
                input()

            # return_val = current_node.insertDown(key_ptr)
            # print('Return_value: {0}'.format(return_val))
            current_node.insertDown(key_ptr)
            insert_counter += 1
            #if new root was created, reset the root

            # if return_val != None:
            #     level_counter += 1
            #     self.root = return_val
            #     print('Level Up!')

            if current_node.parent != None:
                print('Level Up!')
                level_counter += 1
                self.root = current_node.parent

            # print('------------------Printing from btreeindex------------------')
            # print('Key - pointer pair: {0}'.format(key_ptr))
            # print('P for current node: {0}'.format(current_node.p))
            # print('Q for current node: {0}'.format(current_node.q))
            # print('Keys for current node: {0}'.format(current_node.keys))
            # print('Children for current node: {0}'.format(current_node.children))
            # print('Parent for current node: {0}'.format(current_node.parent))
            # input()

            #print tree at current state
            print('Number of levels: {}'.format(level_counter))
            print('------------------------ROOT------------------------')
            print(self.root)
            print('Keys in root: {0}'.format(self.root.keys))
            print('Children of root: {0}'.format(self.root.children))
            print('Parent of root: {0}'.format(self.root.parent))

            for l in range(level_counter+1):
                if l == 1:
                    print('------------------LEVEL 1------------------')
                    for c in range(1,len(self.root.children)+1):
                        print('------------------CHILD {0}------------------'.format(c))
                        print('Keys in child: {0}'.format(self.root.children[c-1].keys))
                        print('Children of child: {0}'.format(self.root.children[c-1].children))
                        print('Parent of child: {0}'.format(self.root.children[c-1].parent))

                        print('\n')
                if l == 2:
                    print('------------------LEVEL 2------------------')
                    for c in range(1,len(self.root.children)+1):
                        gc = 1
                        for grandchild in self.root.children[c-1].children:
                            print('------------------GRANDCHILD {0} OF CHILD {1}------------------'.format(gc,c))
                            print('Keys in child: {0}'.format(grandchild.keys))
                            print('Children of child: {0}'.format(grandchild.children))
                            print('Parent of child: {0}'.format(grandchild.parent))
                            print(grandchild)
                            gc += 1
                    print('\n\n\n')

            if insert_counter == 10:
                break
