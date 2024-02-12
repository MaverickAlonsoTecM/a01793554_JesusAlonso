""" 
compute_Sales.py
"""
import argparse
import json
import time


def compute_total_cost(price_data, sales_data):
    """
        Compute the total cost for all sales and measure execution time.

        Args:
            price_data (list): List containing product price information.
            sales_data (list): List containing sales records.

        Returns:
            tuple: A tuple containing total cost and execution time.
    """
    start_time = time.time()  # Start time for execution
    total_cost = 0

    # Write results to SalesResults.txt file
    with open('SalesResults.txt', 'w', encoding='utf-8') as results_file:
        results_file.write('Sales Results:\n')

        for sale in sales_data:
            product_name = sale['Product']
            quantity = sale['Quantity']
            product_price = next((
                product['price']
                for product in price_data
                if product['title'] == product_name), 0)
            sale_total = product_price * quantity
            total_cost += sale_total

            end_time = time.time()  # End time for execution
            execution_time = end_time - start_time  # Calculate execution time

        results_file.write(f'Total cost for all sales: ${total_cost}\n')
        results_file.write(f'Execution time: {execution_time:.2f} seconds')
    return total_cost, execution_time


def main():
    """
    Process product price information and sales records.
    """
    parser = argparse.ArgumentParser(
        description='Process product price information and sales records.')
    parser.add_argument('price_file',
                        nargs='?',
                        default='./TC1/TC1.ProductList.json',
                        help='Path to the JSON file containing product price')
    parser.add_argument('sales_file',
                        nargs='?',
                        default='./TC1/TC1.Sales.json',
                        help='Path to the JSON file containing sales records')
    args = parser.parse_args()

    try:
        # Read and parse JSON files
        with open(args.price_file, 'r', encoding='utf-8') as price_file:
            price_data = json.load(price_file)
        with open(args.sales_file, 'r', encoding='utf-8') as sales_file:
            sales_data = json.load(sales_file)

        # Compute total cost for all sales and measure execution time
        total_cost, execution_time = compute_total_cost(price_data, sales_data)

        # Print total cost and execution time for all sales
        print(f'\nTotal cost for all sales: ${total_cost}')
        print(f'Execution time: {execution_time:.2f} seconds')

    except json.JSONDecodeError as e:
        print(f'Error parsing JSON file: {e}')
    except FileNotFoundError as e:
        print(f'File not found: {e}')


if __name__ == "__main__":
    main()
