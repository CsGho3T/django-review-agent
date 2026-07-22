from pathlib import Path


class Workspace:
    """
    Represents a Django project loaded into the review engine.

    This object stores information about the project
    during the review lifecycle.
    """

    def __init__(self, root: Path) -> None:
        self.root = root
        self.python_files: list[Path] = []
        self.settings_file: Path | None = None
        self.url_files: list[Path] = []
        self.root_url_file: Path | None = None
        self.apps: list[dict] = []

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

    @property
    def manage_py(self) -> Path | None:
        """
        Return Django manage.py path if exists.
        """
        manage_file = self.root / "manage.py"

        if manage_file.exists():
            return manage_file

        return None

    @property
    def is_django_project(self) -> bool:
        """
        Check whether workspace is a Django project.

        A Django project must contain manage.py.
        """
        return self.manage_py is not None