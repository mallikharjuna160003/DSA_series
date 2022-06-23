class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_node(self, data):
        if data == self.data:
            return
        if self.data > data:
            # left insertion case
            if self.left:
                self.left.add_node(data)
            else:
                self.left = BSTNode(data)
        else:
            # right insertion case
            if self.right:
                self.right.add_node(data)
            else:
                self.right = BSTNode(data)
                
    def inorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.inorder_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.inorder_traversal()
        return elements

    def Bsearch(self,data):
        if self.data == data:
            return True
        elif data < self.data:
            if self.left:
                return self.left.Bsearch(data)
            else:
                return False
        elif data > self.data:
            if self.right:
                return self.right.Bsearch(data)
            else:
                return False
            
    def Fmin(self):
        
        if self.left == None:
            return self.data
        if self.left:
            return self.left.Fmin()
        
    def Fmax(self):
        
        if self.right == None:
            return self.data
        if self.right:
            return self.right.Fmax()
        
    
        
        


        
    

def build_tree(elements):
    root = BSTNode(elements[0])

    for i in range(1,len(elements)):
        root.add_node(elements[i])
        
    return root

if __name__ == "__main__":
    numbers = [17,4,1,20,9,18,34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.inorder_traversal())
    print(numbers_tree.Bsearch(10))
    print("min element",numbers_tree.Fmin())
    print("max element",numbers_tree.Fmax())
    
                        

























    

        
                                    
                
                
