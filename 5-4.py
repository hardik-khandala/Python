# Sample customer data (you should replace this with your actual data)
customer_data = [
    {'customer_acc_no': 1, 'customer_name': 'Alice', 'product_no': 'P001', 'product_category': 'Bread', 'unit_price': 2.5},
    {'customer_acc_no': 2, 'customer_name': 'Bob', 'product_no': 'P002', 'product_category': 'Butter', 'unit_price': 1.0},
    {'customer_acc_no': 3, 'customer_name': 'Charlie', 'product_no': 'P001', 'product_category': 'Bread', 'unit_price': 2.5},
    {'customer_acc_no': 4, 'customer_name': 'David', 'product_no': 'P003', 'product_category': 'Milk', 'unit_price': 3.0},
    # Add more customer records as needed
]

# Extract customers who purchased Bread, Butter, and Milk
bread_buyers = set()
butter_buyers = set()
milk_buyers = set()

for record in customer_data:
    if record['product_category'] == 'Bread':
        bread_buyers.add(record['customer_acc_no'])
    elif record['product_category'] == 'Butter':
        butter_buyers.add(record['customer_acc_no'])
    elif record['product_category'] == 'Milk':
        milk_buyers.add(record['customer_acc_no'])

# How many customers have purchased bread?
num_customers_purchased_bread = len(bread_buyers)

# How many customers have purchased butter?
num_customers_purchased_butter = len(butter_buyers)

# How many customers have purchased bread and butter?
customers_purchased_both = bread_buyers.intersection(butter_buyers)
num_customers_purchased_both = len(customers_purchased_both)

# Who has purchased bread but not butter?
bread_not_butter = bread_buyers.difference(butter_buyers)

# Which customers have purchased bread, butter, and milk?
customers_purchased_all = bread_buyers.intersection(butter_buyers, milk_buyers)

# Print the name of the most valuable customers who have purchased all three items.
most_valuable_customers = []
max_total_price = 0.0

for customer_acc_no in customers_purchased_all:
    total_price = sum(record['unit_price'] for record in customer_data if record['customer_acc_no'] == customer_acc_no)
    if total_price > max_total_price:
        max_total_price = total_price
        most_valuable_customers = [record['customer_name'] for record in customer_data if record['customer_acc_no'] == customer_acc_no]

print("How many customers have purchased bread?", num_customers_purchased_bread)
print("How many customers have purchased butter?", num_customers_purchased_butter)
print("How many customers have purchased bread and butter?", num_customers_purchased_both)
print("Who has purchased bread but not butter?", bread_not_butter)
print("Which customers have purchased bread, butter, and milk?", customers_purchased_all)
print("The name of the most valuable customers who have purchased all three items:", most_valuable_customers)
