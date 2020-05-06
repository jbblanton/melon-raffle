"""Randomly pick customer and print customer info"""

import random
from customers import Customer, get_customers_from_file

def pick_winner(customers):
    """Choose a random winner from the customers list"""

    chosen_customer = random.choice(customers)

    print(f"Tell {chosen_customer.name} at {chosen_customer.email} they've won!")

def run_raffle():
    """Run the raffle"""

    customers = get_customers_from_file("customers.txt")
    pick_winner(customers)

if __name__ == "__main__":
    run_raffle()

