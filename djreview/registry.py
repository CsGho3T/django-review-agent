from djreview.rules.base_rule import BaseRule
from djreview.rules.security.registry import (
    SecurityRuleRegistry,
)


class RuleRegistry:
    """
    Register every enabled review rule.
    """

    @staticmethod
    def get_rules() -> list[BaseRule]:

        rules: list[BaseRule] = []

        rules.extend(
            SecurityRuleRegistry.get_rules()
        )

        return rules