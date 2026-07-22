from pathlib import Path
from djreview.models.app import DjangoApp
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

            is_app = self._is_django_app(item)

            if is_app:
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
    ) -> DjangoApp:
        """
        Create DjangoApp object.
        """

        app = DjangoApp(
            name=path.name,
            path=path,
        )

        for file in path.iterdir():

            if file.name == "models.py":
                app.models_file = file

            elif file.name == "views.py":
                app.views_file = file

            elif file.name in {"urls.py", "url.py"}:
                app.urls_file = file

            elif file.name == "admin.py":
                app.admin_file = file

            elif file.name == "migrations":
                app.migrations_path = file

        return app