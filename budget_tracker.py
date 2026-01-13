# Student Budget Tracker
# Author: Qhayiya Zintle Lalapi
# A simple Python program to help NSFAS-funded students manage monthly expenses.

def budget_tracker():
    print("=== Student Budget Tracker ===")
    
    # Input allowance
    allowance = float(input("Enter your monthly NSFAS allowance (R): "))
    
    # Input expenses
    transport = float(input("Enter your monthly transport cost (R): "))
    food = float(input("Enter your monthly food cost (R): "))
    toiletries = float(input("Enter your monthly toiletries cost (R): "))
    accommodation = float(input("Enter your monthly accommodation shortfall (R): "))
    
    # Calculate total expenses
    total_expenses = transport + food + toiletries + accommodation
    
    # Calculate balance
    balance = allowance - total_expenses
    
    # ANSI escape codes for bold text
    BOLD = "\033[1m"
    RESET = "\033[0m"
    
    # Display summary
    print("\n=== Monthly Summary ===")
    print(f"Allowance: R{allowance:.2f}")
    print(f"Total Expenses: R{total_expenses:.2f}")
    print(f"Remaining Balance: R{balance:.2f}")
    
    # Feedback with bold personality markers
    if balance > 0:
        print(f"{BOLD}:){RESET} You have money left for savings or extras!")
    elif balance == 0:
        print(f"{BOLD}!{RESET} Your allowance is just enough to cover expenses.")
    else:
        print(f"{BOLD}:( {RESET} Your expenses exceed your allowance. Consider adjusting your budget.")

# Run the tracker
budget_tracker()
