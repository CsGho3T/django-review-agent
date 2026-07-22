from djreview.workspace.loader import WorkspaceLoader


def main() -> None:
    loader = WorkspaceLoader()

    workspace = loader.load(
        input("Project path: ")
    )

    print()
    print("Project Loaded")
    print("----------------------")
    print(f"Name   : {workspace.name}")
    print(f"Root   : {workspace.path}")
    print(f"Exists : {workspace.exists}")


if __name__ == "__main__":
    main()