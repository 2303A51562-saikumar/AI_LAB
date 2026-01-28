def get_discount_rate(num_items, subtotal):
    """Determine discount rate based on quantity and amount"""
    quantity_discount = 0
    amount_discount = 0
    
    # Quantity-based discount
    if num_items >= 50:
        quantity_discount = 0.15
    elif num_items >= 20:
        quantity_discount = 0.10
    elif num_items >= 10:
        quantity_discount = 0.05
    
    # Amount-based discount
    if subtotal >= 1000:
        amount_discount = 0.10
    elif subtotal >= 500:
        amount_discount = 0.05
    
    # Return the maximum applicable discount
    return max(quantity_discount, amount_discount)


def calculate_bill(customer_name, num_items, price_per_item):
    """Calculate total bill with discounts based on quantity and amount, plus tax"""
    
    subtotal = num_items * price_per_item
    discount_rate = get_discount_rate(num_items, subtotal)
    discount_amount = subtotal * discount_rate
    discounted_amount = subtotal - discount_amount
    tax_amount = discounted_amount * 0.10
    final_bill = discounted_amount + tax_amount
    
    print("\n" + "="*40)
    print(f"{'BILLING SYSTEM':^40}")
    print("="*40)
    print(f"Customer Name: {customer_name}")
    print(f"Number of Items: {num_items}")
    print(f"Price per Item: ${price_per_item:.2f}")
    print("-"*40)
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount ({discount_rate*100:.0f}%): -${discount_amount:.2f}")
    print(f"After Discount: ${discounted_amount:.2f}")
    print(f"Tax (10%): ${tax_amount:.2f}")
    print("-"*40)
    print(f"Final Bill Amount: ${final_bill:.2f}")
    print("="*40 + "\n")
    
    return final_bill


while True:
    customer_name = input("Enter customer name (or 'exit' to stop): ")
    if customer_name.lower() == 'exit':
        break
    num_items = int(input("Enter number of items: "))
    price_per_item = float(input("Enter price per item: "))
    calculate_bill(customer_name, num_items, price_per_item)
