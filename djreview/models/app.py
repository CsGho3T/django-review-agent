from pathlib import Path


class DjangoApp:
    """
    Represents a Django application
    discovered inside a project.
    """

    def __init__(
        self,
        name: str,
        path: Path,
    ) -> None:

        self.name = name
        self.path = path

        self.models_file: Path | None = None
        self.views_file: Path | None = None
        self.urls_file: Path | None = None
        self.admin_file: Path | None = None

        self.migrations_path: Path | None = None

    def __repr__(self) -> str:
        return f"DjangoApp(name={self.name})"