import asyncio
import pytest
from app.batch_calc import batch_total_balance_thread, batch_total_balance_async

@pytest.fixture
def sample_accounts():
    return [
        {'id': 1, 'name': 'A1', 'balance': 100.0, 'number': '111'},
        {'id': 2, 'name': 'A2', 'balance': 200.0, 'number': '222'},
        {'id': 3, 'name': 'A3', 'balance': 300.0, 'number': '333'},
        {'id': 4, 'name': 'A4', 'balance': 400.0, 'number': '444'},
    ]

def test_batch_total_balance_thread(sample_accounts):
    total = batch_total_balance_thread(sample_accounts, batch_size=2)
    assert total == 1000.0

@pytest.mark.asyncio
async def test_batch_total_balance_async(sample_accounts):
    total = await batch_total_balance_async(sample_accounts, batch_size=2)
    assert total == 1000.0
