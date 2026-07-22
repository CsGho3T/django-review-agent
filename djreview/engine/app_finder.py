from pathlib import Path

from djreview.workspace.workspace import Workspace


class AppFinder:
    """
    Discover Django applications inside a project.
    """

    def find(self, workspace: Workspace) -> Workspace:
        """
        Find Django apps and store information.
        """

        for item in workspace.root.iterdir():

            if not item.is_dir():
                continue

            if item.name.startswith("."):
                continue

            if self._is_django_app(item):
                workspace.apps.append(
                    self._analyze_app(item)
                )

        return workspace

    def _is_django_app(
        self,
        path: Path
    ) -> bool:
        """
        Check if directory looks like Django app.
        """

        required_files = {
            "models.py",
            "views.py",
        }

        files = {
            file.name
            for file in path.iterdir()
            if file.is_file()
        }

        return required_files.issubset(files)

    def _analyze_app(
        self,
        path: Path
    ) -> dict:
        """
        Collect app information.
        """

        return {
            "name": path.name,
            "path": path,
            "files": [
                file.name
                for file in path.iterdir()
                if file.is_file()
            ],
        }