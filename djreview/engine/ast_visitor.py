import ast


class ASTVisitor:
    """
    Helper class for traversing Python AST.
    """

    def __init__(
        self,
        tree: ast.AST,
    ) -> None:

        self.tree = tree

    def walk(self):
        """
        Iterate over all AST nodes.
        """

        return ast.walk(self.tree)

    def assignments(self):
        """
        Iterate over assignment nodes.
        """

        for node in ast.walk(self.tree):

            if isinstance(node, ast.Assign):
                yield node

    def find_assignment(
            self,
            name: str,
    ):
        """
        Find assignment by variable name.
        """

        for node in self.assignments():

            for target in node.targets:

                if (
                        isinstance(target, ast.Name)
                        and target.id == name
                ):
                    return node

        return None