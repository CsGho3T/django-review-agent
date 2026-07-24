import ast
from pathlib import Path


class PythonParser:
    """
    Parse Python source files into AST.
    """

    def parse(
        self,
        file: Path,
    ) -> ast.AST:
        """
        Parse Python file and return AST tree.
        """

        source = file.read_text(
            encoding="utf-8"
        )

        return ast.parse(source)