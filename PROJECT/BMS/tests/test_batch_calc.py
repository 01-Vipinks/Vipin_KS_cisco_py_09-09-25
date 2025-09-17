"""
Tests for batch calculation functions in Banking Management System.
"""

import pytest

@pytest.fixture
def sample_accounts():
    """
    Fixture providing sample account data for tests.
    """
    return [
        {'id': 1, 'name': 'A1', 'balance': 100.0, 'number': '111'},
        {'id': 2, 'name': 'A2', 'balance': 200.0, 'number': '222'},
        {'id': 3, 'name': 'A3', 'balance': 300.0, 'number': '333'},
        {'id': 4, 'name': 'A4', 'balance': 400.0, 'number': '444'},
    ]

def test_batch_total_balance_thread(sample_accounts):
    """
    Test batch_total_balance_thread returns correct total.
    """
    from app.batch_calc import batch_total_balance_thread

    total = batch_total_balance_thread(sample_accounts, batch_size=2)
    assert total == 1000.0

@pytest.mark.asyncio
async def test_batch_total_balance_async(sample_accounts):
    """
    Test batch_total_balance_async returns correct total.
    """
    from app.batch_calc import batch_total_balance_async

    total = await batch_total_balance_async(sample_accounts, batch_size=2)
    assert total == 1000.0

class DummyResponse:
    """
    Dummy response class used for mocking requests in tests.
    """
    status_code = 200
    text = """
        <html>
        <table id="interest-rates">
            <tr><th>Product</th><th>Rate</th><th>Tenure</th></tr>
            <tr><td>FD</td><td>5%</td><td>1 year</td></tr>
            <tr><td>Savings</td><td>3.5%</td><td>None</td></tr>
        </table>
        </html>
        """

def test_scrape_interest_rates(monkeypatch):
    """
    Test scrape_interest_rates returns expected data using monkeypatching.
    """
    import requests
    from app.scrapper import scrape_interest_rates

    def mock_get(*args, **kwargs):
        """Mocked requests.get returning DummyResponse."""
        return DummyResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    rates = scrape_interest_rates("dummy-url", pages=1)
    assert len(rates) == 2
    assert rates[0]['product'] == 'FD'
    assert rates[1]['rate'] == '3.5%'
