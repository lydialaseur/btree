from btreeindex import BTreeIndex
from btreenode import BTreeNode
import os

# os.chdir('./stories')

table_dir = 'stories'
col = 'AUTHOR'
p = 3

idx = BTreeIndex('stories',col,3)
idx.create()
