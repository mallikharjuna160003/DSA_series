class TreeNode:
    def __init__(self,data,designation):
        self.data = data
        self.designation = designation
        self.children=[]
        self.parent=None
    def add_node(self,child):
        child.parent=self
        self.children.append(child)
    def get_level(self):
        count = 0
        p = self.parent
        while p:
            count+=1
            p = p.parent
        return count
    def print_names(self):
        space = " "*self.get_level()*3 
        prefix = space+"|__" if self.parent else ""
        print(prefix+
              self.data)
        if self.children:
            for child in self.children:
                child.print_names()
    def print_designation(self):
        space = " "*self.get_level()*3 
        prefix = space+"|__" if self.parent else ""
        print(prefix+
              self.designation)
        if self.children:
            for child in self.children:
                child.print_designation()
    def print_nodes(self):
        space = " "*self.get_level()*3 
        prefix = space+"|__" if self.parent else ""
        print(prefix+self.data+
              ("({})").format(self.designation))
        if self.children:
            for child in self.children:
                child.print_nodes()
    
                
def build_tree():
    ceo = TreeNode("Nilupul","CEO")
    
    cto = TreeNode("Chinmay","CTO")
    hrhead = TreeNode("Gels","HR Head")
    
    Infrahead = TreeNode("Vishwa","Infrastructure Head")
    Cloudmanager = TreeNode("Dhaval","Cloud Manager")
    Appmanager = TreeNode("Abhijit","App Manager")
    apphead = TreeNode("Amir","Application head")
    RecruitManager = TreeNode("Peter","Recruitment Manager")
    PolicyManager = TreeNode("Waqas","Policy Manager")
    hrhead.add_node(RecruitManager)
    hrhead.add_node(PolicyManager)
    Infrahead.add_node(Cloudmanager)
    Infrahead.add_node(Appmanager)
    cto.add_node(Infrahead)
    cto.add_node(apphead)
    ceo.add_node(cto)
    ceo.add_node(hrhead)
        
    return ceo
    
                

if __name__ == "__main__":
    
    root = build_tree()
    root.print_names()
    root.print_designation()
    root.print_nodes()
