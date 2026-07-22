from pathlib import Path


class Finding:
    """
    Represents a single issue found during review.
    """

    def __init__(
        self,
        title: str,
        severity: str,
        message: str,
        file: Path | None = None,
    ) -> None:

        self.title = title
        self.severity = severity
        self.message = message
        self.file = file

    def __repr__(self) -> str:
        return (
            f"Finding("
            f"title={self.title}, "
            f"severity={self.severity}"
            f")"
        )