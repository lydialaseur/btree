from btreeindex import BTreeIndex
import os

os.chdir('./stories')


# get the range of i
# i = 0
# for page in list(os.walk('./'))[0][1]:
#     num_recs_current_page = len(list(os.walk('./{0}'.format(page)))[0][2])
#     i += num_recs_current_page

infile = open('header','r')
column = 'test'

# header = infile.read().strip().split(',').index(column)
header = infile.read().strip().split(',')
print(column in header)

infile.close()
