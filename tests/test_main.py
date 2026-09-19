from pathlib import Path
import runpy
from unittest.mock import Mock

import app.calculator


MAIN = Path(__file__).resolve().parents[1] / "main.py"


def test_main_starts_calculator(monkeypatch):
    mock_calculator = Mock()
    monkeypatch.setattr(
        app.calculator,
        "calculator",
        mock_calculator,
    )

    runpy.run_path(str(MAIN), run_name="__main__")

    mock_calculator.assert_called_once_with()


def test_main_does_not_start_when_imported(monkeypatch):
    mock_calculator = Mock()
    monkeypatch.setattr(
        app.calculator,
        "calculator",
        mock_calculator,
    )

    runpy.run_path(
        str(MAIN),
        run_name="calculator_import_test",
    )

    mock_calculator.assert_not_called()