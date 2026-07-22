from djreview.models.project import ProjectMap
from djreview.models.finding import Finding
from djreview.rules.base_rule import BaseRule


class ReviewEngine:
    """
    Execute review rules on a Django project.
    """

    def __init__(
        self,
        rules: list[BaseRule],
    ) -> None:
        self.rules = rules

    def review(
        self,
        project: ProjectMap,
    ) -> list[Finding]:
        """
        Run all rules and collect findings.
        """

        findings: list[Finding] = []

        for rule in self.rules:
            findings.extend(
                rule.check(project)
            )

        return findings