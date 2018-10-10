from Assignment_Three import NodeClass

class AbstractSyntaxTree:
    """This is the base class for the Abstract Syntax Tree."""

    def __init__(self):
        """
        This is the constructor for the Abstract Syntax Tree.  We start by initializing a
        root_node variable which will be referenced in the beginning as we start to build our tree.
        """
        self.root_node = None
        self.current_node = None

    def add_to_tree(self, node = NodeClass.Node):
        """
        This add_to_tree definition works specifically for 'nodes' which contains a list of 2 different
        elements as its 'node_data'. It assumes that the first element is the operation while the second
        is the value.
        :param node: a node which contains a list of two elements in its 'node_data' variable
        :return:
        """
        if self.root_node == None:
            self.root_node = NodeClass.Node(node.node_data[0])
            self.root_node.right_child = NodeClass.Node(node.node_data[1])
            return
        else:
            self.current_node = self.root_node

            if self.current_node.left_child == None:
                self.current_node.left_child = NodeClass.Node(node.node_data[0])
                self.current_node.left_child.right_child = NodeClass.Node(node.node_data[1])
                return

            while (self.current_node.left_child != None):
                self.current_node = self.current_node.left_child

            self.current_node.left_child = NodeClass.Node(node.node_data[0])
            self.current_node.left_child.right_child = NodeClass.Node(node.node_data[1])

