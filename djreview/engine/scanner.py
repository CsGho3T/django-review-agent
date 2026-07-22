from pathlib import Path

from djreview.workspace.workspace import Workspace


class Scanner:
    """
    Scans a Django project workspace.

    Responsible for discovering project files
    and collecting structural information.
    """

    def scan(self, workspace: Workspace) -> Workspace:
        """
        Scan workspace and collect information.

        Args:
            workspace:
                Loaded project workspace.

        Returns:
            Updated workspace.
        """

        self._find_python_files(workspace)

        self._find_django_files(workspace)

        return workspace

    def _find_python_files(
        self,
        workspace: Workspace
    ) -> None:
        """
        Find all Python files in project.
        """

        excluded_dirs = {
            ".venv",
            "venv",
            "env",
            "__pycache__",
            ".git",
            "node_modules",
        }

        workspace.python_files = [
            file
            for file in workspace.root.rglob("*.py")
            if not any(
                part in excluded_dirs
                for part in file.parts
            )
        ]

    def _find_django_files(
        self,
        workspace: Workspace
    ) -> None:
        """
        Find important Django files.
        """

        for file in workspace.python_files:

            if file.name == "settings.py":
                workspace.settings_file = file

            elif file.name in {"urls.py", "url.py", "routes.py"}:
                workspace.url_files.append(file)
                if (
                        workspace.settings_file
                        and file.parent == workspace.settings_file.parent
                ):
                    workspace.root_url_file = file