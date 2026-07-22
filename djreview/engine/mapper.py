from djreview.models.project import ProjectMap
from djreview.workspace.workspace import Workspace


class ProjectMapper:
    """
    Convert Workspace data into a ProjectMap.
    """

    def build(
        self,
        workspace: Workspace,
    ) -> ProjectMap:

        project_map = ProjectMap(
            name=workspace.name,
            root=workspace.root,
        )

        project_map.settings_file = (
            workspace.settings_file
        )

        project_map.root_url_file = (
            workspace.root_url_file
        )
        project_map.python_files = workspace.python_files

        for app in workspace.apps:
            project_map.add_app(app)

        return project_map