# Restaurant Billing System

A simple console-based restaurant billing application built in Python, created as a B.Tech Semester 1 mini project.

## Features

- Displays a categorized restaurant menu (Starters, Main Course, Beverages, Desserts)
- Lets the customer select items by number and enter quantity
- Calculates subtotal, 5% tax, and 2% service charge
- Prints a formatted final bill to the screen
- Saves a copy of the bill as a `.txt` file
- Supports generating multiple bills in one session

## Requirements

- Python 3.x (no external libraries needed)

## How to Run

1. Make sure Python is installed on your system.
2. Open a terminal in the project folder.
3. Run the program:
   ```
   python restaurant_billing_system.py
   ```
4. Enter the customer's name when prompted.
5. Enter the item number from the menu to add it to the order.
6. Enter the quantity for that item.
7. Enter `0` when you are done ordering to generate the bill.
8. The bill will be displayed on screen and saved as `bill_<customer_name>.txt` in the same folder.

## Project Structure

```
restaurant_billing_system.py   # Main program file
README.md                      # This file
```

## Concepts Demonstrated

- Dictionaries (menu storage)
- Functions and modular code design
- Loops and conditional statements
- Exception handling (`try`/`except`)
- String formatting
- File handling (writing the bill to a text file)
- The `if __name__ == "__main__":` execution guard

## Possible Future Improvements

- Add discount codes or membership offers
- Add a graphical user interface (Tkinter)
- Store menu and orders in a database instead of a dictionary
- Add multiple table/order tracking for a full restaurant setup

## Author

Yug Chauhan — B.Tech Semester 1

