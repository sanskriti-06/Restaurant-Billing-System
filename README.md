# **Restaurant Billing System**
## **Overview**
This project is a simple **Python-based Restaurant Billing System** that allows customers to:
- **View the menu** categorized by Snacks, Lunch, and Dinner
- **Select food items** and specify quantity
- **Automatically calculate the total bill**
- **Exit the system** once billing is complete

## **Prerequisites**
Ensure you have:
- **Python 3.x** installed

## **Installation & Execution**
1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-repo/restaurant-billing.git
   cd restaurant-billing
   ```
2. **Run the script**:
   ```sh
   python restaurant_billing.py
   ```

## **How It Works**
- The customer is shown a menu with categorized food items and their prices.
- They can **add items** to the order by specifying quantity.
- The total **bill is calculated dynamically** and displayed upon request.
- The customer can **continue ordering or exit the program**.

## **Menu Example**
### **Snacks**
- Tea → ₹80  
- Coffee → ₹180  
- Cookies → ₹120  

### **Lunch**
- Roti → ₹50  
- Dal → ₹250  
- Rice → ₹220  

### **Dinner**
- Paneer → ₹300  
- Pizza → ₹550  
- Noodles → ₹350  

## **Example Output**
```
WELCOME TO XYZ RESTAURANT
1. Menu
2. Bill
3. Exit
Select one of these: 1
Choose menu: Snacks
How many items do you want to add? 2
Select food you want to eat: Tea
Quantity: 2
Select food you want to eat: Cookies
Quantity: 1

Your bill is:
1. Tea*2 -> ₹160
2. Cookies*1 -> ₹120
Total = ₹280

Thank you for visiting!
```

## **Future Enhancements**
- **Integrate a database** to store past customer orders  
- **Implement a graphical user interface (GUI)** for better interaction  
- **Add discount features** and promo codes for special offers  

## **License**
This project is open-source and free to use. Contributions and improvements are welcome!
