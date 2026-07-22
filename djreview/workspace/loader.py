from pathlib import Path

from djreview.workspace.workspace import Workspace


class WorkspaceLoader:
    """
    Load a Django project into a Workspace object.
    """

    def load(self, project_path: str) -> Workspace:
        """
        Load project workspace.

        Args:
            project_path:
                Path to project root.

        Returns:
            Workspace instance.
        """

        root = Path(project_path).resolve()

        if not root.exists():
            raise FileNotFoundError(
                f"Project not found: {root}"
            )

        if not root.is_dir():
            raise NotADirectoryError(
                f"{root} is not a directory."
            )

        return Workspace(root)