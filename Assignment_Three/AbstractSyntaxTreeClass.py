from Assignment_Three import NodeClass

class AbstractSyntaxTree:
    """This is the base class for the Abstract Syntax Tree."""

    def __init__(self):
        """
        This is the constructor for the Abstract Syntax Tree.  We start by initializing a
        root_node variable which will be referenced in the beginning as we start to build our tree.
        """
        self.tree = []
        self.variable_dictionary = {}
        self.root_node = None
        self.current_node = None
        self.iter_node = None

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
            self.iter_node = self.root_node
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

    def __iter__(self):
        """
        This initializes the iterator to be set to the AbstractSyntaxTree class itself.
        :return: self
        :rtype: enumerate
        """
        return self

    def __next__(self):
        """
        This iterates through each of the nodes in the 'AbstractSyntaxTree'. It returns the first
        node that was added followed by the second, third and so forth until there are none left to
        be iterated upon.
        :return:
        """
        self.iter_data = []
        if self.iter_node == None:
            raise StopIteration
        elif self.iter_node.left_child == None:
            self.iter_data.append(self.iter_node.node_data)
            self.iter_data.append(self.iter_node.right_child.node_data)
            self.iter_node = None
            return self.iter_data
        self.iter_data.append(self.iter_node.node_data)
        self.iter_data.append(self.iter_node.right_child.node_data)
        self.iter_node = self.iter_node.left_child
        return self.iter_data