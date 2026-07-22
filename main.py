from djreview.workspace.loader import WorkspaceLoader
from djreview.engine.scanner import Scanner
from djreview.engine.app_finder import AppFinder

def main() -> None:
    loader = WorkspaceLoader()

    workspace = loader.load(
        input("Project path: ")
    )

    print()

    print("Project Loaded")
    print("----------------------")
    print(f"Name    : {workspace.name}")
    print(f"Root    : {workspace.path}")
    print(f"Exists  : {workspace.exists}")
    print(f"Django  : {workspace.is_django_project}")

    scanner = Scanner()

    workspace = scanner.scan(workspace)

    print()
    print("Scan Result")
    print("----------------------")

    print(
        f"Python files: {len(workspace.python_files)}"
    )

    print(
        f"Settings: {workspace.settings_file}"
    )

    print(
        f"Root URL: {workspace.root_url_file}"
    )

    print()

    print("App URLs:")

    for url_file in workspace.url_files:
        if url_file != workspace.root_url_file:
            print(f"- {url_file}")

    finder = AppFinder()

    workspace = finder.find(workspace)

    print()

    print("Django Apps")
    print("----------------------")

    for app in workspace.apps:
        print(f"- {app.name}")



if __name__ == "__main__":
    main()