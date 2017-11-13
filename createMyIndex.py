from btreeindex import BTreeIndex
from btreenode import BTreeNode
import os

# os.chdir('./stories')

table_dir = 'stories'
col = 'AUTHOR'
p = 3

idx = BTreeIndex('stories',col,3)
idx.create()

root = 'Mikler22'
c1 = "Devils'kin"
c2 = 'Shagman'
gc1_c1_1 = 'AnteaterFang'
gc1_c1_2 = 'ChosenHorcrux'
gc2_c1 = 'Khgirl08'
gc1_c2_1 = 'PrimaVeraDream'
gc1_c2_2 = 'SeriouslySnape17'
gc2_c2_1 = 'fragonknight01'
gc2_c2_2 = 'runobody2'

#check root is between children
if root > c1 and root < c2:
    print('Root is good!')

#check that child 1 is between it's grandchildren
if c1 > gc1_c1_1 and c1 > gc1_c1_2 and c1 < gc2_c1:
    print('Child 1 of root is good!')
    if gc1_c1_1 < gc1_c1_2:
        print('Child 1 Grandchildren are good!')


#check that child 2 is between it's grandchildren
if c2 > gc1_c2_1 and c2 > gc1_c2_2 and c2 < gc2_c2_1 and c2 < gc2_c2_2:
    print('Child 2 of root is good!')
    if gc1_c2_1 < gc1_c2_2 and gc2_c2_1 < gc2_c2_2:
        print('Child 2 Grandchildren are good!')
