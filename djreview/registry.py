from djreview.rules.base_rule import BaseRule
from djreview.rules.security_rule import DebugModeRule


class RuleRegistry:
    """
    Provides all enabled review rules.
    """

    @staticmethod
    def get_rules() -> list[BaseRule]:
        """
        Return active rules.
        """

        return [
            DebugModeRule(),
        ]