from btreeindex import BTreeIndex
from btreenode import BTreeNode
import os

os.chdir('/usr/share/databases/FanFiction/')

table_dir = 'stories'
col = 'AUTHOR'
p = 3


idx = BTreeIndex('stories',col,3)
num_insertions, num_levels = idx.create()
