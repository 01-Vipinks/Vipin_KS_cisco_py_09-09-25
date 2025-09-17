"""
Batch calculation utilities for Banking Management System.

Provides thread-based and asyncio-based batch total balance calculations.
"""

import asyncio
from concurrent.futures import ThreadPoolExecutor

def _batch_sum(accounts_batch):
    """Helper to sum balance of accounts in a batch."""
    return sum(account['balance'] for account in accounts_batch)

def batch_total_balance_thread(accounts, batch_size=10):
    """
    Calculate total balance by splitting accounts into batches using ThreadPoolExecutor.

    Args:
        accounts (list of dict): list of account dicts with 'balance' key.
        batch_size (int): number of accounts per batch.

    Returns:
        float: total balance sum.
    """
    batches = [accounts[i:i+batch_size] for i in range(0, len(accounts), batch_size)]
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(_batch_sum, batches))
    return sum(results)

async def _async_batch_sum(accounts_batch):
    """Async helper to sum balances."""
    # Simulate async operation if needed (e.g., DB or IO call)
    total = sum(account['balance'] for account in accounts_batch)
    await asyncio.sleep(0)  # yield control
    return total

async def batch_total_balance_async(accounts, batch_size=10):
    """
    Asyncio coroutine to calculate total balance in batches.

    Args:
        accounts (list of dict): list of account dicts with 'balance'.
        batch_size (int): batch size.

    Returns:
        float: total balance sum.
    """
    batches = [accounts[i:i+batch_size] for i in range(0, len(accounts), batch_size)]
    tasks = [_async_batch_sum(batch) for batch in batches]
    results = await asyncio.gather(*tasks)
    return sum(results)

async def main():
    """Example main function demonstrating batch calculations."""
    example_accounts = [
        {'id': 1, 'name': 'Acct 1', 'balance': 100},
        {'id': 2, 'name': 'Acct 2', 'balance': 200},
        {'id': 3, 'name': 'Acct 3', 'balance': 300},
    ]
    # Threaded batch sum
    total_balance_thread = batch_total_balance_thread(example_accounts, batch_size=2)
    print(f"Total balance (threaded): {total_balance_thread}")
    # Async batch sum
    total_balance_async = await batch_total_balance_async(example_accounts, batch_size=2)
    print(f"Total balance (async): {total_balance_async}")

if __name__ == "__main__":
    asyncio.run(main())
