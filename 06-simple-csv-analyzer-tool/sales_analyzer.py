import csv
from collections import Counter, defaultdict


def log_result(line, file = None):
    print(line)
    if file:
        print(line, file = file)

def csv_analyzer(path: str) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))
        order_quantity = sum(int(row["quantity"]) for row in reader)
        total_revenue = sum(int(row["price"]) * int(row["quantity"]) for row in reader)
        customer_counts = Counter()
        for row in reader:
            customer_counts[row["customer_name"]] += int(row["quantity"])
        counted = Counter(row["product"] for row in reader)
        most_popular_product = counted.most_common(1)[0][0]
        revenue_by_customer = defaultdict(int)
        for row in reader:
            name = row["customer_name"]
            quantity = int(row["quantity"])
            price = int(row["price"])
            revenue = quantity * price
            revenue_by_customer[name] += revenue
        best_customer = max(revenue_by_customer.items(), key=lambda x: x[1])[0]

        with open("analyzed_sales.txt", "w", encoding="utf-8") as result:
            log_result(f"Total quantity of orders: {order_quantity}", result )
            log_result(f"Total revenue: {total_revenue}", result)
            log_result("Quantity of orders for each customer", result)
            for name, qty in customer_counts.items():
                log_result(f"{name}: {qty}", result)
            log_result(f"Most common product: {most_popular_product}", result)
            log_result(f"Top revenue-generating customer: {best_customer}", result)
if __name__ == "__main__":
    csv_analyzer("sales.csv")