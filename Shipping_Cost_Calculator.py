# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))
currency = input("Enter the currency (e.g., USD, EUR, GBP): ").upper()

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
# print(f"Shipping Cost: {shipping_cost} USD")
print(f"Shipping Cost: {shipping_cost} {currency}")
