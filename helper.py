
from classes import Transaction
import json

def read_transactions_from_file(filename):
    """
    Read transactions from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        list: A list of Transaction objects.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    
    transactions = []
    for transaction_data in data.values():
        transaction = Transaction(**transaction_data)
        transactions.append(transaction)
    
    return transactions


def combine_transactions(transactions):
    """
    Combines a list of transactions based on their merchant codes.

    Args:
        transactions (list): A list of transaction objects.

    Returns:
        dict: A dictionary where the keys are merchant codes and the values are dictionaries
              containing the combined amount in cents for each merchant code.
    """
    combined_transactions = {}
    for transaction in transactions:
        merchant_code = transaction.merchant_code

        if merchant_code in combined_transactions:
            combined_transactions[merchant_code]['amount_cents'] += transaction.amount_cents
        else:
            combined_transactions[merchant_code] = {
                'amount_cents': transaction.amount_cents
            }
    return combined_transactions