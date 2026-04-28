import matplotlib.pyplot as plt

def show_graph():
    data = {}

    try:
        with open("data.txt", "r") as file:
            for line in file:
                amount, category = line.strip().split(",")
                amount = float(amount)
                
                if category in data:
                    data[category] += amount
                else:
                    data[category] = amount

        # Prepare data for graph
        categories = list(data.keys())
        amounts = list(data.values())

        # Create pie chart
        plt.pie(amounts, labels=categories, autopct='%1.1f%%')
        plt.title("Expense Distribution")
        plt.show()

    except FileNotFoundError:
        print("No data to show.")
def add_expense(amount, category):
    with open("data.txt", "a") as file:
        file.write(f"{amount},{category}\n")


def view_expenses():
    try:
        with open("data.txt", "r") as file:
            for line in file:
                amount, category = line.strip().split(",")
                print(f"Amount: {amount} | Category: {category}")
    except FileNotFoundError:
        print("No expenses found.")


def total_expense():
    total = 0
    try:
        with open("data.txt", "r") as file:
            for line in file:
                amount, _ = line.strip().split(",")
                total += float(amount)
        print("Total Expense:", total)
    except FileNotFoundError:
        print("No data available.")