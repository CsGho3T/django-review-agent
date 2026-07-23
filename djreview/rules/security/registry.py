from djreview.rules.base_rule import BaseRule
from djreview.rules.security.debug_mode import DebugModeRule


class SecurityRuleRegistry:
    """
    Register all security rules.
    """

    @staticmethod
    def get_rules() -> list[BaseRule]:
        return [
            DebugModeRule(),
        ]