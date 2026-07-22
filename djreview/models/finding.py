from pathlib import Path
from dataclasses import dataclass
from enum import Enum


class Severity(str, Enum):
    """
    Finding severity levels.
    """

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

    def __str__(self) -> str:
        return self.value


class Category(str, Enum):
    """
    Finding categories.
    """

    SECURITY = "SECURITY"
    PERFORMANCE = "PERFORMANCE"
    STYLE = "STYLE"
    BUG = "BUG"

    def __str__(self) -> str:
        return self.value

@dataclass
class Finding:
    """
    Represents a detected issue during project review.
    """

    title: str
    description: str
    recommendation: str
    severity: Severity
    category: Category
    file: Path | None = None
    line: int | None = None