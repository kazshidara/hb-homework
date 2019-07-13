


#list of new customers that weren't previously in the file
# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00


# # For each new customer, the previous SWE printed out the total amount new customer paid and how much the expected cost was 

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )

#To not waste time, we want to automatically repeat the above statement for each customer in the file.
#We want function to take in a text-file, parse/go through each line, strip('|'), and iterate through 
# each customer's line, calculate out expected_pay and compare to actually_paid 

# We have a couple of constant variables:
# expected_pay = melons_bought * melon_cost 
# if actually_paid doesnt match the expected_pay:
#     print statement "Customer_name paid _, expected was $_"

MELON_COST = 1.00

def print_payment_status(path):
    text_file = open(path)
    for line in text_file:
        order = line.split('|')
        customer_name = order[1]
        expected_pay = float(order[2]) * MELON_COST
        actually_paid = float(order[3])
        print(f"{customer_name} paid ${actually_paid:.2f}, expected",f"${expected_pay:.2f}") 
        #precisely tell function to use floats that only have 2 decimal points

        if expected_pay < actually_paid:
            print(f"{customer_name} has overpaid for their melons.")
        elif expected_pay > actually_paid:
            print(f"{customer_name} has underpaid for their melons.")
    text_file.close()

print_payment_status('customer-orders.txt')



