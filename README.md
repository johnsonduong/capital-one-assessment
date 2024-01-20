# Credit Card Reward Points Systems

## Overview
This application calculates the maximum monthly reward points for credit card transactions, optimizing points based on user transactions and predefined rules.

## How to Use
- To run the rules engine: Execute `python3 rules_engine.py` in your terminal. This will utilize the main transaction data from `transactions/sample_transaction.json`.
- To test the rules engine: Execute `python3 test_rules_engine.py` to perform unit tests. The engine successfully passes all defined tests in the project manual.

## Components
- `rules.py`: Contains rules for calculation.
- `classes.py`: Defines `Transaction` and `Rule` class.
- `helper.py`: Functions for reading and combining transactions.
- `rules_engine.py`: Contains the main function for points calculation.

## Testing
Unit tests are included to ensure the accuracy and reliability of the calculations. Test cases cover various scenarios, including different sets of transactions and rules. These tests validate the functionality of the `calculate_max_points` function using predefined examples and expected results.

## Requirements
- Python environment.
