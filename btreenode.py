class BTreeNode(object) :
    '''Object represents a node in a b-tree that can have p children and q = p-1
    key-value, data pointer pairs, without being overfull.  self.children is a list
    of references to self's children nodes. self.keys is a list of (key,ptr) tuples
    that are contained in the node. self.children[0] references all nodes less than
    self.keys[0], self.children[1] references all nodes less than self.keys[1] or
    greater than or equal to self.keys[0], and so on.  The number of children will
    always be 1 greater than the number of keys. self.parent refers to the parent node
    of self. if self is the root node, self.parent equal None.
    '''

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

    def insertDown(self, key_ptr) :

        '''Searches for the leaf node to insert a new key-pointer pair into, and does the insertion.
        No return value.'''

        # if this node is a leaf, insert the pair (key, pointer) tuple
        if self.isLeaf():

            #if node is empty, just insert key_ptr
            if self.q == 0:
                self.keys.append(key_ptr)
                self.q += 1
            #if node has other keys
            else:
                #loop through keys to find right position
                for i in range(self.q+1):
                    # if i less than number of keys
                    if i < self.q:
                        #and if key value is greater than or equal to value of key at index i in node, continue loop
                        if key_ptr[0] >= self.keys[i][0]:
                            continue
                        #if key value is less than key at index i in self, insert the key_ptr tuple before it
                        else:
                            self.keys.insert(i,key_ptr)
                            self.q += 1
                            break
                    # i == q+1 > q, value in key_ptr is greater than or equal to all other keys, so append it to the end of self.keys
                    else:
                        self.keys.append(key_ptr)
                        self.q += 1

            # if after insertion this node is overfull:
            if self.isOverfull():

                # if this node is root (and leaf!), call insertRoot()
                    if self.getParent() == None:
                        self.insertRoot()
                # if this node is not root
                    # call splitNode to push middle value up and create new sibling to hold right-most keys
                    else:
                        self.splitNode()

        # if this node has children, insert the key-ptr pair into the correct child and recurse
        else:
            #loop through all keys to locate correct child
            for i in range(self.q+1):
                # if i less than total number of keys in node
                if i < self.q:
                    # and if key value is greater than or equal value of key already in node at index i, continue loop
                    if key_ptr[0] >= self.keys[i][0]:
                        continue
                    #if key value is less than key at index i in self, select the child at index i and insert key_ptr
                    else:
                        child = self.children[i]
                        child.insertDown(key_ptr)
                        break
                else: # i == q+1 > q, value in key_ptr is greater than or equal to all other keys, so pick the right most child, which is self.children[i]
                    child = self.children[i]
                    child.insertDown(key_ptr)


    def insertUp(self,key_ptr) :
        '''Inserts a key-pointer pair into parent of self.
        Typically called by an overfull child or sibling.
        Returns index where key-pointer was pair was inserted'''
        #get parent of self
        parent = self.getParent()

        #loop through keys to find right position
        for i in range(parent.q+1):
            # if i less than number of keys in parent and value in key_ptr greater than or equal to value in parent.keys[i], continue loop
            if i < parent.q:
                #if key value is greater than or equal to value of key already in node, continue loop
                if key_ptr[0] >= parent.keys[i][0]:
                    continue
                else:
                    #if key value is less than key in parent at index i, insert before it, save location of insert
                    parent.keys.insert(i,key_ptr)
                    parent.q += 1
                    loc = i
                    break
            else: # i == q+1 > q, value in key_ptr is greater than or equal to all other keys, so append it to the end of parent.keys
                parent.keys.append(key_ptr)
                parent.q += 1
                loc = i

        return loc

    def splitNode(self) :
        '''Called by a over-full node. Moves middle key-pointer pair up to
        parent and splits self into 2 half-full nodes. If parent is then over-full,
        recurse until a non-full parent or root is found.  If root is found,
        call insertRoot.  Returns nothing.'''

        # insert middle value of over-full self into parent, get parent after
        # insertion and the location of the insertion
        middle_key_ptr = self.keys[self.p//2]
        loc = self.insertUp(middle_key_ptr)

        # remove middle value from self
        self.keys.remove(middle_key_ptr)
        self.q -= 1

        # create new sibling, remove right-most key from self, add to sibling
        sibling = BTreeNode(self.p)
        rightmost_key_ptr = self.keys.pop()
        sibling.keys.append(rightmost_key_ptr)
        self.q -= 1
        sibling.q += 1

        #if self is not a leaf, i.e. has children, self keeps left half of children
        #and gives right half of children to sibling
        if not self.isLeaf():
            half = len(self.children)//2
            sibling.children = self.children[half:]
            self.children = self.children[:half]
        #else self is a leaf, thus has no children to split up


        parent = self.getParent()

        #make parent of self, the parent of the new sibling
        sibling.setParent(parent)

        #add sibling to children of self's parent, in correct location
        parent.children.insert(loc+1,sibling)

        #if parent is full
        if parent.isOverfull():
            #if parent is not root, recurse
            if parent.getParent() != None:
                parent.splitNode()
            #if parent is root, call insertRoot
            else:
                parent.insertRoot()

    def insertRoot(self):
        '''Called when this node is root and overfull, creates a new parent/root node and
        a sibling node to contain half the entries. Returns nothing.'''

        # create a new parent/root node and a new sibling node
        new_root = BTreeNode(self.p)
        sibling = BTreeNode(self.p)

        # make the new root the parent of this node and its sibling.
        sibling.setParent(new_root)
        self.setParent(new_root)

        # move this node's middle key-pointer pair into the parent, i.e. the new root
        middle_key_ptr = self.keys[self.p//2]
        self.insertUp(middle_key_ptr)

        # remove middle value from self
        self.keys.remove(middle_key_ptr)
        self.q -= 1

        # create new sibling, remove right-most key from self, add to sibling
        rightmost_key_ptr = self.keys.pop()
        sibling.keys.append(rightmost_key_ptr)
        self.q -= 1
        sibling.q += 1

        #if self is not a leaf, i.e. has children, self keeps left half of children
        #and gives right half of children to sibling
        if not self.isLeaf():
            half = len(self.children)//2
            sibling.children = self.children[half:]
            self.children = self.children[:half]
        #else self is a leaf, thus has no children to split up

        #assign self and sibling as children of the new root
        #new_root.children = [self,sibling]
        new_root.children.append(self)
        new_root.children.append(sibling)
