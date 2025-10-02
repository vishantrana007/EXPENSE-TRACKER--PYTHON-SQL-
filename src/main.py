"""
main.py
Entry point for Expense Tracker CLI
Fully professional, menu-driven CLI version
"""

from db import create_table
from expense_manager import (
    add_expense,
    get_all_expenses,
    update_expense,
    delete_expense,
    get_monthly_summary,
    get_category_report,
    view_spending_insights
)

def show_menu():
    """
    Displays the main menu of the Expense Tracker CLI.
    """
    print("\n=============================")
    print("   EXPENSE TRACKER - MENU")
    print("=============================")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Monthly Summary")
    print("6. Category-wise Report")
    print("7. View Spending Insights")
    print("8. Exit")
    print("=============================")

def main():
    """
    Main loop for the CLI.
    Handles user input, validation, and calls the appropriate functions.
    """
    # -----------------------------
    # Step 1: Initialize Database
    # -----------------------------
    print("Initializing Expense Tracker Database...")
    create_table()
    print("Database & Table setup complete ✅")

    # -----------------------------
    # Step 2: Menu Loop
    # -----------------------------
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        # -----------------------------
        # Option 1: Add Expense
        # -----------------------------
        if choice == "1":
            print("\n--- Add New Expense ---")
            date = input("Enter date (YYYY-MM-DD): ").strip()
            category = input("Enter category (Food/Travel/Bills/Shopping/Others): ").strip()
            description = input("Enter description: ").strip()

            # Validate numeric amount
            while True:
                try:
                    amount = float(input("Enter amount: ").strip())
                    break
                except ValueError:
                    print("Invalid amount! Please enter a numeric value.")

            # Insert into database
            add_expense(date, category, description, amount)
            print(f"✅ Expense recorded: {date}, {category}, {description}, {amount}")

        # -----------------------------
        # Option 2: View Expense
        # -----------------------------
        elif choice == "2":
            print("\n--- All Recorded Expenses ---")
            expenses = get_all_expenses()
            if not expenses:
                print("No expenses recorded yet.")
            else:
                print(f"{'ID':<5}{'Date':<12}{'Category':<15}{'Description':<25}{'Amount':<10}")
                print("-" * 70)
                for exp in expenses:
                    exp_id, date, category, description, amount = exp
                    print(f"{exp_id:<5}{date:<12}{category:<15}{description:<25}{amount:<10}")

        # -----------------------------
        # Option 3: Update Expense
        # -----------------------------
        elif choice == "3":
            print("\n--- Update Expense ---")
            try:
                exp_id = int(input("Enter Expense ID to update: ").strip())
                new_date = input("Enter new date (YYYY-MM-DD): ").strip()
                new_category = input("Enter new category (Food/Travel/Bills/Shopping/Others): ").strip()
                new_description = input("Enter new description: ").strip()
                while True:
                    try:
                        new_amount = float(input("Enter new amount: ").strip())
                        break
                    except ValueError:
                        print("Invalid amount! Please enter a numeric value.")

                update_expense(exp_id, new_date, new_category, new_description, new_amount)
                print(f"✅ Expense ID {exp_id} updated successfully.")
            except ValueError:
                print("Invalid ID! Please enter a numeric value.")

        # -----------------------------
        # Option 4: Delete Expense
        # -----------------------------
        elif choice == "4":
            print("\n--- Delete Expense ---")
            try:
                exp_id = int(input("Enter Expense ID to delete: ").strip())
                delete_expense(exp_id)
                print(f"✅ Expense ID {exp_id} deleted successfully.")
            except ValueError:
                print("Invalid ID! Please enter a numeric value.")

        # -----------------------------
        # Option 5: Monthly Summary
        # -----------------------------
        elif choice == "5":
            print("\n--- Monthly Summary ---")
            summary = get_monthly_summary()
            if not summary:
                print("No data available for monthly summary.")
            else:
                print(f"{'Month':<10}{'Total Amount':<15}")
                print("-" * 30)
                for month, total in summary:
                    print(f"{month:<10}{total:<15}")

        # -----------------------------
        # Option 6: Category-wise Report
        # -----------------------------
        elif choice == "6":
            print("\n--- Category-wise Report ---")
            report = get_category_report()
            if not report:
                print("No data available for category-wise report.")
            else:
                print(f"{'Category':<15}{'Total Amount':<15}")
                print("-" * 30)
                for category, total in report:
                    print(f"{category:<15}{total:<15}")

        # -----------------------------
        # Option 7: View Spending Insights
        # -----------------------------
        elif choice == "7":
            print("\n--- Spending Insights ---")
            insights = view_spending_insights()
            if not insights:
                print("No insights available yet.")
            else:
                for line in insights:
                    print(f"- {line}")

        # -----------------------------
        # Option 8: Exit
        # -----------------------------
        elif choice == "8":
            print("Exiting Expense Tracker. Goodbye!")
            break

        # -----------------------------
        # Invalid Input
        # -----------------------------
        else:
            print("Invalid choice! Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
