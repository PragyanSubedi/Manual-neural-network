class Operation()
    def __init__(self,input_nodes=[]):
        self.input_nodes =input_nodes
        self.output_nodes = []

        for node in input_nodes:
            node.output_nodes.append(self)

    def compute(self):
        pass


class add(Operation):
    def __init__(self,x,y):
        super().__init__([x,y])

    def compute(self,x_var,y_var):
        self.inputs=[x_var,y_var]
        return x_var + y_var


class multiply(Operation):
    def __init__(self, x, y):
        super().__init__([x, y])

    def compute(self, x_var, y_var):
        self.inputs = [x_var, y_var]
        return x_var * y_var


class matmul(Operation):
    def __init__(self, x, y):
        super().__init__([x, y])

    def compute(self, x_var, y_var):
        self.inputs = [x_var, y_var]
        return x_var.dot(y_var)

class Placeholder():
    def __index__(self):
        self.output_nodes=[]
        _default_graph.placeholders.append(self)

        


