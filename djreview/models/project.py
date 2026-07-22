from pathlib import Path

from djreview.models.app import DjangoApp


class ProjectMap:
    """
    Represents a complete map of a Django project.

    This object is used by the review engine
    to understand project structure.
    """

    def __init__(
        self,
        name: str,
        root: Path,
    ) -> None:

        self.name = name
        self.root = root

        self.python_files: list[Path] = []

        self.settings_file: Path | None = None
        self.root_url_file: Path | None = None

        self.apps: list[DjangoApp] = []

    def add_app(self, app: DjangoApp) -> None:
        """
        Add discovered Django application.
        """

        self.apps.append(app)