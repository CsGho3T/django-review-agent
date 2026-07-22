from pathlib import Path
from djreview.models.project import ProjectMap
from djreview.rules.base_rule import BaseRule
from djreview.models.finding import (
    Finding,
    Severity,
    Category,
)

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

        content = project.settings_file.read_text(
            encoding="utf-8"
        )

        if "DEBUG = True" in content:
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