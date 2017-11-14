from btreeindex import BTreeIndex
from btreenode import BTreeNode
import os

os.chdir('/usr/share/databases/FanFiction/')

table_dir = 'stories'
col = 'AUTHOR'
p = 3


idx = BTreeIndex('stories',col,3)
num_insertions, num_levels = idx.create()


#print tree after 10 insertions
print('Number of levels: {}'.format(num_levels))
print('-------------------------------ROOT--------------------------------')
# print(self.root)
print('Keys in root: {0}'.format(idx.root.keys))
# print('Children of root: {0}'.format(self.root.children))
# print('Parent of root: {0}'.format(self.root.parent))
print('\n\n')
for l in range(num_levels+1):
    if l == 1:
        print('------------------------------LEVEL 1------------------------------')
        for c in range(1,len(idx.root.children)+1):
            print('------------------------------CHILD {0}------------------------------'.format(c))
            print('Keys in child: {0}'.format(idx.root.children[c-1].keys))
            # print('Children of child: {0}'.format(idx.root.children[c-1].children))
            # print('Parent of child: {0}'.format(idx.root.children[c-1].parent))
            print('\n')
        print('\n')
    if l == 2:
        print('------------------------------LEVEL 2------------------------------')
        for c in range(1,len(idx.root.children)+1):
            gc = 1
            for grandchild in idx.root.children[c-1].children:
                print('----------------------GRANDCHILD {0} OF CHILD {1}----------------------'.format(gc,c))
                print('Keys in grandchild: {0}'.format(grandchild.keys))
                print('\n')
                # print('Children of child: {0}'.format(grandchild.children))
                # print('Parent of child: {0}'.format(grandchild.parent))
                # print(grandchild)
                gc += 1
        print('\n\n')


#check that tree structure is correct after first 10 records are inserted
# root = 'NULL_AUTHOR'
# child1_key1 = 'ChosenHorcrux'
# child1_key2 = 'Khgirl08'
# child2 = 'Shagman'
# grandchild1_child1 = 'AnteaterFang'
# grandchild2_child1 = "Devils'kin"
# grandchild3_child1 = 'Mikler22'
# grandchild1_child2 = 'PrimaVeraDream'
# grandchild2_child2_key1 = 'fragonknight01'
# grandchild2_child2_key2 = 'runobody2'
#
# #check root is between children
# if (root > child1_key1) and (root > child1_key2) and (root < child2) and (child1_key1 < child1_key2):
#     print('Root is good!')
#
# #check that child 1 is between it's grandchildren
# if (child1_key1 > grandchild1_child1) and (child1_key1 < grandchild2_child1) and (child1_key2 > grandchild2_child1) and (child1_key2 < grandchild3_child1):
#     print('Child 1 of root is good!')
#     if (grandchild1_child1 < grandchild2_child1) and (grandchild2_child1 < grandchild3_child1):
#         print('Child 1 Grandchildren are good!')
#
#
# #check that child 2 is between it's grandchildren
# if (child2 > grandchild1_child2) and (child2 < gc2_c2_1) and (child2 < grandchild2_child2_key2):
#     print('Child 2 of root is good!')
#     if  gc2_c2_1 < grandchild2_child2_key2:
#         print('Child 2 Grandchildren are good!')
