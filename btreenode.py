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
        self.q = 0
        self.childKeyPtrs = list() # contains tuples (child i, (key i, ptr i))
        self.rightChild = None
        self.parent = None

    def setRightChild(self, rightChild):
        self.rightChild = rightChild

    def getRightChild(self):
        return self.rightChild

    def setParent(self, node):
        self.parent = node

    def getParent(self):
        return self.parent

    def isOverfull(self) :
        return (q>=p)

    def isLeaf(self) :
        return (self.rightChild is None)

    def insertDown(self, keyPtr) :
        '''Searches for the leaf node to insert a new key-pointer pair into, and does the insertion.
        Returns None, or a reference to the new root if one is created.'''

        # if this node is a leaf, insert the pair (node ref, (key, pointer))
        if self.isLeaf():

            if self.q == 0: #if node is empty, just inset key_ptr
                self.childKeyPtrs = self.childKeyPtrs.append((None,keyPtr))
                self.q += 1
            else: #if node has other keys
                #loop through keys to find right position
                for i in range(q+1):

                    if keyPtr[0] > self.childKeyPtrs[i][1][0] and i < q:
                        continue
                    else:
                        self.childKeyPtrs = self.childKeyPtrs.insert(i,(None,keyPtr))
                        self.q += 1

            # if after insertion this node is overfull:
            if self.isOverfull():

                # if this node is root (and leaf!), call insertRoot()
                    if self.getParent() == None:
                        return self.insertRoot()
                # if this node is not root
                    # insert the rightmost key-pointer pair into this node's parent
                    #  with insertUp(None, key-ptr, rightChild)
                    #  and fix this node's references
                    else:
                        right_most_keyPtr = self.childKeyPtrs[-1][1]
                        return self.insertUp(None,right_most_keyPtr,self.getRightChild)

            else:
                return None


        # if this node has children, insert the key-ptr pair into the correct child and recurse
        else:
            #loop through all keys to locate correct child
            for i in range(q+1):
                if keyPtr[0] > self.childKeyPtrs[i][1][0] and i < q:
                    continue
                else:
                    if i > q:
                        child = self.getRightChild
                        child.insertDown(keyPtr)
                    else:
                        child = self.childKeyPtrs[i][0]
                        child.insertDown(keyPtr)

        return # None or return value of insertRoot, insertUp, or insertDown

    def insertUp(self, leftNode, keyPtr, rightNode) :
        '''Inserts a key-pointer pair into a node.
        Typically called by an overfull child or sibling.
        Returns None, or a reference to the new root if one is created.'''

        #This method isn't making any sense to me since it pushes the right-most
        #key-ptr pair up to the parent and not the middle key-ptr pair
        # insert the leftNode-keyPtr tuple into the list at the correct index

        # replace the child in the next list element, or the rightChild, with rightNode

        # if this node is overfull

            # if this node is not root, insert the rightmost key-pointer pair into this node's parent

            # if this node is root, call insertRoot()

        return # None or return value of insertRoot, insertUp, or insertDown

    def insertRoot(self):
        '''Called when this node is root and overfull, creates a new parent/root node and
        a sibling node to contain half the entries.
        Returns a reference to the new root.'''

        # create a new parent/root node and a new sibling node
        # set the return value
        new_root = BTreeNode(self.p)
        new_sibling = BTreeNode(self.p)

        # move this node's middle key-pointer pair into the parent
        #  with insertUp(self, key-ptr, sibling)
        #  and fix this node's references
        middle_keyptr = self.childKeyPtrs[self.p//2][1]
        self.insertUp(self,middle_keyptr,new_sibling)
        self.childKeyPtrs = self.childKeyPtrs[0]


        # give this node's right child to the sibling
        # give the right half of this node's child-key-pointer tuples to the sibling
        #  with calls to insertUp(child, key-ptr, None)
        #i


        # make the root the parent of this node and its sibling.
        new_sibling.setParent(new_root)
        self.setParent(new_root)

        return # reference to new root
