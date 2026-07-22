from pathlib import Path


class Workspace:
    """
    Represents a Django project loaded into the review engine.

    This object stores metadata and paths used during
    the review lifecycle.
    """

    def __init__(self, root: Path) -> None:
        self.root = root

    @property
    def name(self) -> str:
        """
        Return project directory name.
        """
        return self.root.name

    @property
    def exists(self) -> bool:
        """
        Check whether project directory exists.
        """
        return self.root.exists()

    @property
    def path(self) -> str:
        """
        Return absolute project path.
        """
        return str(self.root)