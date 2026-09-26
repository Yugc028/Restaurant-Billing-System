"""
Restaurant Billing System
--------------------------
 
Concepts used: dictionaries, functions, loops, conditionals,
string formatting, and basic file handling.
"""
 
import datetime
 
# ---------------------------------------------------------
# MENU DATA
# Each category is a dictionary of {item_name: price}
# ---------------------------------------------------------
menu = {
    "Starters": {
        "Veg Spring Roll": 120,
        "Paneer Tikka": 180,
        "Chicken Wings": 220
    },
    "Main Course": {
        "Veg Biryani": 160,
        "Chicken Biryani": 220,
        "Paneer Butter Masala": 200,
        "Dal Makhani": 150
    },
    "Beverages": {
        "Cold Drink": 40,
        "Fresh Lime Soda": 60,
        "Masala Chai": 30
    },
    "Desserts": {
        "Gulab Jamun": 70,
        "Ice Cream": 80
    }
}
 
TAX_RATE = 0.05          # 5% GST
SERVICE_CHARGE_RATE = 0.02   # 2% service charge
  
def display_menu():
#   Prints the full menu with item numbers for easy ordering.
    print("\n===== RESTAURANT MENU =====")
    item_number = 1
    item_map = {}  # maps number -> (item_name, price)
 
    for category, items in menu.items():
        print(f"\n-- {category} --")
        for item, price in items.items():
            print(f"{item_number}. {item} - Rs.{price}")
            item_map[item_number] = (item, price)
            item_number += 1
 
    return item_map
 
def take_order(item_map):
#    Takes customer's order and returns a list of ordered items.
    order = []
    print("\nEnter item number to add to order. Enter 0 to finish ordering.")
 
    while True:
        try:
            choice = int(input("Item number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
 
        if choice == 0:
            break
        elif choice in item_map:
            qty = int(input("Quantity: "))
            item_name, price = item_map[choice]
            order.append({"name": item_name, "price": price, "qty": qty})
            print(f"Added {qty} x {item_name} to order.")
        else:
            print("Invalid item number. Try again.")
 
    return order
  
def generate_bill(order, customer_name):
#   Calculates totals and prints/saves the final bill.
    if not order:
        print("\nNo items ordered. Bill not generated.")
        return
 
    print("\n========== BILL ==========")
    print(f"Customer: {customer_name}")
    print(f"Date: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    print("-" * 40)
    print(f"{'Item':<20}{'Qty':<6}{'Price':<8}{'Total':<8}")
    print("-" * 40)
 
    subtotal = 0
    bill_lines = []
 
    for entry in order:
        line_total = entry["price"] * entry["qty"]
        subtotal += line_total
        line = f"{entry['name']:<20}{entry['qty']:<6}{entry['price']:<8}{line_total:<8}"
        print(line)
        bill_lines.append(line)
 
    tax = subtotal * TAX_RATE
    service_charge = subtotal * SERVICE_CHARGE_RATE
    grand_total = subtotal + tax + service_charge
 
    print("-" * 40)
    print(f"Subtotal:        Rs.{subtotal:.2f}")
    print(f"Tax (5%):        Rs.{tax:.2f}")
    print(f"Service Charge:  Rs.{service_charge:.2f}")
    print(f"Grand Total:     Rs.{grand_total:.2f}")
    print("=" * 40)
 
    save_bill_to_file(customer_name, bill_lines, subtotal, tax, service_charge, grand_total)
  
def save_bill_to_file(customer_name, bill_lines, subtotal, tax, service_charge, grand_total):
#   Saves the bill details to a text file.
    filename = f"bill_{customer_name.replace(' ', '_')}.txt"
    with open(filename, "w") as f:
        f.write("========== BILL ==========\n")
        f.write(f"Customer: {customer_name}\n")
        f.write(f"Date: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
        f.write("-" * 40 + "\n")
        for line in bill_lines:
            f.write(line + "\n")
        f.write("-" * 40 + "\n")
        f.write(f"Subtotal:        Rs.{subtotal:.2f}\n")
        f.write(f"Tax (5%):        Rs.{tax:.2f}\n")
        f.write(f"Service Charge:  Rs.{service_charge:.2f}\n")
        f.write(f"Grand Total:     Rs.{grand_total:.2f}\n")
        f.write("=" * 40 + "\n")
 
    print(f"\nBill saved to file: {filename}")
 
def main():
    print("Welcome to the Restaurant Billing System")
    customer_name = input("Enter customer name: ")
 
    while True:
        item_map = display_menu()
        order = take_order(item_map)
        generate_bill(order, customer_name)
 
        again = input("\nStart a new bill? (y/n): ").strip().lower()
        if again != "y":
            print("Thank you! Have a great day.")
            break
 
if __name__ == "__main__":
    main()

