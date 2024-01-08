def c_total(items):#func that receives the number of items to be purchased and the total amount to be paid per quantity of items
    total = 0
    for item in items:
        total += (item['quantity'] * item['price'])
    return total

def invoice(items, tax, discount):
    total = c_total(items)
    taxAmount = total * (tax / 100)
    discountedAmount = total * (discount / 100)
    grandTotal = total + taxAmount - discountedAmount
    
    print("\n===== Invoice =====")
    for item in items:
        print(f"{item['name']}: {item['quantity']} x ${item['price']:.2f} = ${item['quantity'] * item['price']:.2f}")
    
    print(f"\nTotal: ${total:.2f}")
    print(f"Tax ({tax}%): ${taxAmount:.2f}")
    print(f"Discount ({discount}%): ${discountedAmount:.2f}")
    print(f"Grand Total: ${grandTotal:.2f}")

#def main():
    items = []
    
    while True:
        name = input("Enter item name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: "))
        
        items.append({'name': name, 'quantity': quantity, 'price': price})
    
    tax_rate = float(input("Enter tax rate (%): "))
    discount = float(input("Enter discount (%): "))
    
    invoice(items, tax, discount)

# if __name__ == '__main__':
#     main()


## More ideas:
 # make the discount a choice kuburyo a seller ari we uhitamo if he/she gives the customer the discount or not
