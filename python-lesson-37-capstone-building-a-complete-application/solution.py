import pytest
from ledger import Expense, Ledger

def test_add_expense():
    ledger = Ledger()
    ledger.add(Expense("Coffee", 4.5))
    assert ledger.total() == 4.5

def test_total_multiple():
    ledger = Ledger()
    ledger.add(Expense("Coffee", 4.5))
    ledger.add(Expense("Lunch", 12))
    assert ledger.total() == 16.5

def test_empty_ledger_total_is_zero():
    assert Ledger().total() == 0
