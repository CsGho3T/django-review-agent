from djreview.workspace.loader import WorkspaceLoader
from djreview.engine.scanner import Scanner
from djreview.engine.app_finder import AppFinder
from djreview.engine.mapper import ProjectMapper
from djreview.engine.reviewer import ReviewEngine
from djreview.registry import RuleRegistry

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

    print("Workspace Apps")
    print("----------------------")

    for app in workspace.apps:
        print(f"- {app.name}")
    mapper = ProjectMapper()

    project_map = mapper.build(workspace)

    print()

    print("Project Map")
    print("----------------------")

    print(f"Name: {project_map.name}")
    print(f"Apps: {len(project_map.apps)}")

    for app in project_map.apps:
        print(f"- {app.name}")

    review_engine = ReviewEngine(
        rules=RuleRegistry.get_rules()
    )

    findings = review_engine.review(
        project_map
    )

    print()

    print("Review Result")
    print("----------------------")

    for finding in findings:
        print(f"Title          : {finding.title}")
        print(f"Severity       : {finding.severity}")
        print(f"Category       : {finding.category}")
        print(f"Description    : {finding.description}")
        print(f"Recommendation : {finding.recommendation}")
        print(f"File           : {finding.file}")

        if finding.line:
            print(f"Line           : {finding.line}")

        print("----------------------")

if __name__ == "__main__":
    main()