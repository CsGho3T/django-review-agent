from abc import ABC, abstractmethod

from djreview.models.project import ProjectMap
from djreview.models.finding import Finding


class BaseRule(ABC):
    """
    Base class for all review rules.
    """

    name: str = "Base Rule"

    @abstractmethod
    def check(
        self,
        project: ProjectMap,
    ) -> list[Finding]:
        """
        Analyze project and return findings.
        """

        pass