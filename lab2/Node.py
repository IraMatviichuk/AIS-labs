class Node:
    def __init__(self, state, parent, operator, depth):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.depth = depth

    def get_state(self):
        return self.state

    def get_moves(self):
        return self.operator

    def path_from_start(self):
        state_list = []
        moves_list = []
        curr_node = self
        while curr_node.get_moves() is not None:
            state_list.append(curr_node.get_state())
            moves_list.append(curr_node.get_moves())
            curr_node = curr_node.parent
        moves_list.reverse()
        state_list.reverse()
        for state in state_list:
            state.display_board()
            print()
        return moves_list

    @staticmethod
    def create_node(state, parent, operator, depth):
        return Node(state, parent, operator, depth)

    @staticmethod
    def expand_node(node):
        expanded_nodes = []
        expanded_nodes.append(
            Node.create_node(node.state.move_up(), node, "up", node.depth + 1)
        )
        expanded_nodes.append(
            Node.create_node(node.state.move_down(), node, "down", node.depth + 1)
        )
        expanded_nodes.append(
            Node.create_node(node.state.move_left(), node, "left", node.depth + 1)
        )
        expanded_nodes.append(
            Node.create_node(node.state.move_right(), node, "right", node.depth + 1)
        )
        expanded_nodes = [node for node in expanded_nodes if node.state != None]

        return expanded_nodes
