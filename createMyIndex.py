from btreeindex import BTreeIndex
from btreenode import BTreeNode
import os

# os.chdir('./stories')

table_dir = 'stories'
col = 'AUTHOR'
p = 3


idx = BTreeIndex('stories',col,3)
idx.create()

#print(idx.root.keys)


#print tree at current state
# print('Number of levels: {}'.format(level_counter))
# print('------------------------ROOT------------------------')
# print(self.root)
# print('Keys in root: {0}'.format(self.root.keys))
# print('Children of root: {0}'.format(self.root.children))
# print('Parent of root: {0}'.format(self.root.parent))
#
# for l in range(level_counter+1):
#     if l == 1:
#         print('------------------LEVEL 1------------------')
#         for c in range(1,len(self.root.children)+1):
#             print('------------------CHILD {0}------------------'.format(c))
#             print('Keys in child: {0}'.format(self.root.children[c-1].keys))
#             print('Children of child: {0}'.format(self.root.children[c-1].children))
#             print('Parent of child: {0}'.format(self.root.children[c-1].parent))
#
#             print('\n')
#     if l == 2:
#         print('------------------LEVEL 2------------------')
#         for c in range(1,len(self.root.children)+1):
#             gc = 1
#             for grandchild in self.root.children[c-1].children:
#                 print('------------------GRANDCHILD {0} OF CHILD {1}------------------'.format(gc,c))
#                 print('Keys in child: {0}'.format(grandchild.keys))
#                 print('Children of child: {0}'.format(grandchild.children))
#                 print('Parent of child: {0}'.format(grandchild.parent))
#                 print(grandchild)
#                 gc += 1
#         print('\n\n\n')

# root = 'NULL_AUTHOR'
# c1_1 = 'ChosenHorcrux'
# c1_2 = 'Khgirl08'
# c2 = 'Shagman'
# gc1_c1 = 'AnteaterFang'
# gc2_c1 = "Devils'kin"
# gc3_c1 = 'Mikler22'
# gc1_c2 = 'PrimaVeraDream'
# gc2_c2_1 = 'fragonknight01'
# gc2_c2_2 = 'runobody2'
#
# #check root is between children
# if root > c1_1 and root > c1_2 and root < c2 and c1_1 < c1_2:
#     print('Root is good!')
#
# #check that child 1 is between it's grandchildren
# if c1_1 > gc1_c1 and c1_1 < gc2_c1 and c1_2 > gc2_c1 and c1_2 < gc3_c1:
#     print('Child 1 of root is good!')
#     if gc1_c1 < gc2_c1 and gc2_c1 < gc3_c1:
#         print('Child 1 Grandchildren are good!')
#
#
# #check that child 2 is between it's grandchildren
# if c2 > gc1_c2 and c2 < gc2_c2_1 and c2 < gc2_c2_2:
#     print('Child 2 of root is good!')
#     if  gc2_c2_1 < gc2_c2_2:
#         print('Child 2 Grandchildren are good!')


n = 613653
s = 0
level = 0
while s < n:
    s += 2 * 3**level
    level += 1
print(level)
