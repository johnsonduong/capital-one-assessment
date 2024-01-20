from rules import RULES
from classes import Rule
from helper import read_transactions_from_file, combine_transactions

def calculate_max_points(transactions, rules):
    """
    Calculates the maximum points a user can earn from their transactions.

    Args:
        transactions (dict): A dictionary where the keys are merchant codes and the values are dictionaries
                             containing the combined amount in cents for each merchant code.
        rules (list): A list of rules.

    Returns:
        int: The maximum points the user can earn.
    """
    rules = [Rule(rule['points'], rule['requirements']) for rule in rules]
    transactions = combine_transactions(transactions)
    total_points = 0

    # Sort the rules array by largest points and lowest spend (for rules with same points) in the dictionary
    rules.sort(key=lambda rule: (-rule.points, sum(rule.requirements.values())))

    for rule in rules:
        if 'all' not in rule.requirements:
            # Check if all merchants in the rule's requirements are present in the transactions and meet the minimum spend required
            all_merchants_present = True
            for merchant in rule.requirements:
                if merchant not in transactions or transactions[merchant]['amount_cents'] / 100 < rule.requirements[merchant]:
                    all_merchants_present = False
                    break

            # If all merchants required for the rule to execute are present, calculate the points
            if all_merchants_present:
                # First loop calculates the limiting number of times the rule can be applied, specifically handles cases for multiple merchants in one rule
                num_applied = float('inf')
                for merchant in rule.requirements:
                    spend_amount = transactions[merchant]['amount_cents'] / 100  # Convert cents to dollars
                    num_applied = min(spend_amount // rule.requirements[merchant], num_applied)

                # Second loop updates the leftover amount that can be used for the next rule
                for merchant in rule.requirements:
                    amount_redeemed_for_points = num_applied * rule.requirements[merchant]  # In dollars
                    transactions[merchant]['amount_cents'] -= amount_redeemed_for_points * 100

                total_points += (num_applied) * rule.points
        else:
            # Apply the rule for all other purchases (including leftovers from the previous rules)
            total_spend_amount = sum(transaction['amount_cents'] for transaction in transactions.values()) / 100  # Convert cents to dollars
            points = (total_spend_amount // rule.requirements['all']) * rule.points
            total_points += points

    return total_points

if __name__ == "__main__":
    transactions = read_transactions_from_file('transactions/sample_transactions.json')
    total_points = calculate_max_points(transactions, RULES)

    # Debugging print statements
    # print(json.dumps(transactions, default=lambda x: x.__dict__, indent=4))
    # print(combined_transactions)

    print("The maximum number of points you earned this month are:", total_points)