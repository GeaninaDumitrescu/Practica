
price=1000000
is_good_credit= True
if is_good_credit:
    downpayment=0.1 *price
else:
    downpayment=0.2*price
print(f"down payment: ${downpayment}")