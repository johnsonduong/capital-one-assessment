"""
Each rule contains a 'points' value and a 'requirements' dictionary.
The 'requirements' dictionary specifies the conditions that need to be met for the rule to be applied.
"""
RULES = [
    {
        'points': 500,
        'requirements': {
            'sportcheck': 75,
            'tim_hortons': 25,
            'subway': 25
        }
    },
    {
        'points': 300,
        'requirements': {
            'sportcheck': 75,
            'tim_hortons': 25
        }
    },
    {
        'points': 200,
        'requirements': {
            'sportcheck': 75
        }
    },
    {
        'points': 150,
        'requirements': {
            'sportcheck': 25,
            'tim_hortons': 10,
            'subway': 10
        }
    },
    {
        'points': 75,
        'requirements': {
            'sportcheck': 25,
            'tim_hortons': 10
        }
    },
    {
        'points': 75,
        'requirements': {
            'sportcheck': 20
        }
    },
    {
        'points': 1,
        'requirements': {
            'all': 1            # Assuming `all` is not a code for an existing merchant
        }
    }
]