from djreview.workspace.loader import WorkspaceLoader


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

    if workspace.manage_py:
        print(f"Manage  : {workspace.manage_py}")


if __name__ == "__main__":
    main()