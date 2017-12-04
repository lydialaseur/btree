from btreeindex import BTreeIndex
from btreenode import BTreeNode
import os

os.chdir('/usr/share/databases/FanFiction/')

table_dir = 'stories'
col = 'AUTHOR'
p = 3


idx = BTreeIndex('stories',col,3)
num_insertions, num_levels = idx.create()


# print the first first 2 levels of the tree
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
