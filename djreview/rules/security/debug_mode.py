import ast
from djreview.engine.parser import PythonParser
from djreview.models.finding import (
    Finding,
    Severity,
    Category,
)
from djreview.models.project import ProjectMap
from djreview.rules.base_rule import BaseRule



class DebugModeRule(BaseRule):
    """
    Check if Django DEBUG mode is enabled.
    """

    name = "Debug Mode Check"

    def check(
        self,
        project: ProjectMap,
    ) -> list[Finding]:

        findings: list[Finding] = []

        if not project.settings_file:
            return findings
        parser = PythonParser()

        tree = parser.parse(
            project.settings_file
        )


        for node in ast.walk(tree):

            if not isinstance(node, ast.Assign):
                continue

            for target in node.targets:

                if (
                        isinstance(target, ast.Name)
                        and target.id == "DEBUG"
                ):

                    if (
                            isinstance(node.value, ast.Constant)
                            and node.value.value is True
                    ):

                        findings.append(
                            Finding(
                                title="Debug mode enabled",

                                description=(
                                    "Django DEBUG is enabled. "
                                    "This can expose sensitive information."
                                ),

                                recommendation=(
                                    "Set DEBUG=False in production."
                                ),

                                severity=Severity.HIGH,

                                category=Category.SECURITY,

                                file=project.settings_file,
                            )
                        )

        return findings