import pandas as pd

from src.main import FinPrompt


def test_redact_pii_masks_digits():
    fp = FinPrompt()
    fp.data = pd.DataFrame({"account": ["1234-56", "AB12"], "amount": [10, 20]})
    fp._redact_pii()
    assert fp.data["account"].iloc[0] == "XXXX-XX"
    assert fp.data["account"].iloc[1] == "ABXX"


def test_generate_summary_contains_amount_and_count():
    fp = FinPrompt()
    fp.data = pd.DataFrame(
        {
            "account": ["1111"],
            "amount": [42.5],
            "date": ["2026-02-22"],
        }
    )
    summary = fp._generate_summary()
    assert "Total transactions: 1" in summary
    assert "Total amount" in summary
