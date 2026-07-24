from pathlib import Path
from djreview.models.project import ProjectMap
from djreview.rules.base_rule import BaseRule
from djreview.models.finding import (
    Finding,
    Severity,
    Category,
)
from djreview.engine.parser import PythonParser
import ast