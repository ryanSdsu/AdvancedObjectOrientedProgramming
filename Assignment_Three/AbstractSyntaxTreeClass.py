from Assignment_Three import NodeClass

class AbstractSyntaxTree:
    """This is the base class for the Abstract Syntax Tree."""

    def __init__(self):
        """
        This is the constructor for the Abstract Syntax Tree.  We start by initializing a
        root_node variable which will be referenced in the beginning as we start to build our tree.
        """
        self.root_node = None

    def add_to_tree(self, node = NodeClass.Node):
        if self.root_node == None:
            self.root_node = node
            return
