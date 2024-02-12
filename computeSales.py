import argparse
import json
import time
import os


def compute_total_cost(price_data, sales_data):
    start_time = time.time()  # Start time for execution
    total_cost = 0
    for sale in sales_data:
        product_name = sale['Product']
        quantity = sale['Quantity']
        product_price = next((product['price'] for product in price_data if product['title'] == product_name), 0)
        sale_total = product_price * quantity
        total_cost += sale_total
    end_time = time.time()  # End time for execution
    execution_time = end_time - start_time  # Calculate execution time
    return total_cost, execution_time


def main():
    parser = argparse.ArgumentParser(description='Process product price information and sales records.')
    parser.add_argument('price_file', nargs='?', default='./TC1/TC1.ProductList.json',
                        help='Path to the JSON file containing product price information (default: ./TC1/TC1.ProductList.json)')
    parser.add_argument('sales_file', nargs='?', default='./TC1/TC1.Sales.json',
                        help='Path to the JSON file containing sales records (default: ./TC1/TC1.Sales.json)')
    args = parser.parse_args()

    try:
        # Read and parse JSON files
        with open(args.price_file, 'r') as price_file:
            price_data = json.load(price_file)
        with open(args.sales_file, 'r') as sales_file:
            sales_data = json.load(sales_file)

        # Compute total cost for all sales and measure execution time
        total_cost, execution_time = compute_total_cost(price_data, sales_data)

        # Print total cost and execution time for all sales
        print(f'\nTotal cost for all sales: ${total_cost}')
        print(f'Execution time: {execution_time:.2f} seconds')

        # Write results to SalesResults.txt file
        with open('SalesResults.txt', 'w') as results_file:
            results_file.write('Sales Results:\n')
            for sale in sales_data:
                product_name = sale['Product']
                quantity = sale['Quantity']
                product_price = next((product['price'] for product in price_data if product['title'] == product_name), 0)
                sale_total = product_price * quantity
                results_file.write(f'Product: {product_name}, Quantity: {quantity}, Total Cost: ${sale_total}\n')
            results_file.write(f'Total cost for all sales: ${total_cost}\n')
            results_file.write(f'Execution time: {execution_time:.2f} seconds')

    except json.JSONDecodeError as e:
        print(f'Error parsing JSON file: {e}')
    except FileNotFoundError as e:
        print(f'File not found: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')


if __name__ == "__main__":
    main()
