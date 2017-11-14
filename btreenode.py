class BTreeNode(object) :
    '''represents a node in a B-tree, containing q < p references to child nodes
        and a key-pointer pair between each pair of references:

        ... | child i | key i, ptr i | child i+1 | key i+1, ptr i+1 | ...

        In the picture,

            child node ref i refers to the root of a tree of nodes whose keys are <= key i
            child node ref i+1 refers to the root of a tree of nodes whose keys are > key i and <= key i+1
            key i is the value of a data column,
            ptr i is an integer or string representing the location of a data record

        Note: This Python implementation uses references to nodes instead of pointers to nodes.
        In a leaf node each node reference is None.'''

    def __init__(self, p) :
        self.p = p
        self.q = 0 #the number of keys in a node, if q >= p, node is overfull
        self.children = [] #contains references to children, if length(self.children) > p, node is overfull
        self.keys = [] #contains tuples (key,data pointer), if length == p, node is overfull
        self.parent = None

    def setParent(self, node):
        self.parent = node

    def getParent(self):
        return self.parent

    def isOverfull(self) :
        return (self.q >= self.p)

    def isLeaf(self) :
        return (len(self.children) == 0)

    def insertDown(self, keyPtr) :

        '''Searches for the leaf node to insert a new key-pointer pair into, and does the insertion.
        No return value.'''

        # if this node is a leaf, insert the pair (node ref, (key, pointer))
        if self.isLeaf():

            if self.q == 0: #if node is empty, just insert key_ptr
                self.keys.append(keyPtr)
                self.q += 1
            else: #if node has other keys
                #loop through keys to find right position
                for i in range(self.q+1):
                    # if i less than number of keys and value in keyPtr greater than or equal to value in keys[i], continue loop
                    if i < self.q:
                        if keyPtr[0] >= self.keys[i][0]: #if key value is greater than or equal to value of key already in node
                            continue
                        else:
                            self.keys.insert(i,keyPtr)
                            self.q += 1
                            break
                    else: # i == q+1 > q, value in keyPtr is greater than or equal to all other keys, so append it to the end of self.keys
                        self.keys.append(keyPtr)
                        self.q += 1

            # if after insertion this node is overfull:
            if self.isOverfull():

                # if this node is root (and leaf!), call insertRoot()
                    if self.getParent() == None:
                        self.insertRoot()
                # if this node is not root
                    # call splitNode to push middle value up and create new sibling to hold right-most key
                    else:
                        self.splitNode()

        # if this node has children, insert the key-ptr pair into the correct child and recurse
        else:
            #loop through all keys to locate correct child
            for i in range(self.q+1):
                # if i less than number of keys and value in keyPtr greater than value in keys[i], continue loop
                if i < self.q:
                    if keyPtr[0] >= self.keys[i][0]: #if key value is greater than or equal value of key already in node
                        continue
                    else:
                        child = self.children[i]
                        child.insertDown(keyPtr)
                        break
                else: # i == q+1 > q, value in keyPtr is greater than or equal to all other keys, so pick the right most child, which is self.children[i]
                    child = self.children[i]
                    child.insertDown(keyPtr)


    def insertUp(self,keyPtr) :
        '''Inserts a key-pointer pair into parent of self.
        Typically called by an overfull child or sibling.
        Returns index where key-pointer was pair was inserted'''

        parent = self.getParent()
        #loop through keys to find right position
        for i in range(parent.q+1):
            # if i less than number of keys in parent and value in keyPtr greater than or equal to value in parent.keys[i], continue loop
            if i < parent.q:
                if keyPtr[0] >= parent.keys[i][0]: #if key value is greater than or equal to value of key already in node
                    continue
                else:
                    parent.keys.insert(i,keyPtr)
                    parent.q += 1
                    loc = i
                    break
            else: # i == q+1 > q, value in keyPtr is greater than or equal to all other keys, so append it to the end of self.keys
                parent.keys.append(keyPtr)
                parent.q += 1
                loc = i

        return loc

    def splitNode(self) :
        '''Called by a over-full node. Moves middle key-pointer pair up to
        parent and splits self into 2 half-full nodes. If parent is then over-full,
        recurse until a non-full parent or root is found.  If root is found,
        call insertRoot.  Returns None, or a reference to new root if one
        is created '''

        # insert middle value of over-full self into parent, get parent after
        # insertion and the location of the insertion
        middle_keyptr = self.keys[self.p//2]
        loc = self.insertUp(middle_keyptr)

        # remove middle value from self
        self.keys.remove(middle_keyptr)
        self.q -= 1
        # create new sibling, remove right-most key from self, add to sibling
        sibling = BTreeNode(self.p)
        rightmost_keyptr = self.keys.pop()
        sibling.keys.append(rightmost_keyptr)
        self.q -= 1
        sibling.q += 1
        #if self is not a leaf, i.e. has children, self keeps left half of children
        #and gives right half of children to sibling
        if not self.isLeaf():
            #check that number of children is p+1
            if len(self.children) != (self.p + 1):
                print('Error in splitNode(). Number of children,{0}, does not equal p+1,{1}.'.format(len(self.children),self.p+1))
                input()
            else:
                half = len(self.children)//2
                sibling.children = self.children[half:]
                self.children = self.children[:half]
        #self is a leaf, thus has no children to split up

        parent = self.getParent()
        #make parent of self, the parent of the new sibling
        sibling.setParent(parent)
        #add sibling to children of self's parent, in correct location
        parent.children.insert(loc+1,sibling)

        #if parent is full
        if parent.isOverfull():
            #if parent is not root, recurse
            if parent.getParent() != None:
                # print('RECURSING splitNode')
                parent.splitNode()
            else: #if parent is root, call insertRoot
                parent.insertRoot()

    def insertRoot(self):
        '''Called when this node is root and overfull, creates a new parent/root node and
        a sibling node to contain half the entries.
        Returns a reference to the new root.'''

        # create a new parent/root node and a new sibling node
        # set the return value
        new_root = BTreeNode(self.p)
        sibling = BTreeNode(self.p)

        # make the new root the parent of this node and its sibling.
        sibling.setParent(new_root)
        self.setParent(new_root)

        # move this node's middle key-pointer pair into the parent, i.e. the new root
        middle_keyptr = self.keys[self.p//2]
        self.insertUp(middle_keyptr)

        # remove middle value from self
        self.keys.remove(middle_keyptr)
        self.q -= 1
        # create new sibling, remove right-most key from self, add to sibling
        rightmost_keyptr = self.keys.pop()
        sibling.keys.append(rightmost_keyptr)
        self.q -= 1
        sibling.q += 1

        #if self is not a leaf, i.e. has children, self keeps left half of children
        #and gives right half of children to sibling
        if not self.isLeaf():
            #check that number of children is p+1
            if len(self.children) != (self.p + 1):
                print('Error in insertRoot(). Number of children,{0}, does not equal p+1,{1}.'.format(len(self.children),self.p+1))
                input()
            else:
                half = len(self.children)//2
                sibling.children = self.children[half:]
                self.children = self.children[:half]
        #self is a leaf, thus has no children to split up

        #assign self and sibling as children of the new root
        #new_root.children = [self,sibling]
        new_root.children.append(self)
        new_root.children.append(sibling)
