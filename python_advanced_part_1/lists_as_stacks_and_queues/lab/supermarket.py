customers = input()
customers_list = []
while customers != 'End':

    if customers == 'Paid':
        for c in customers_list:
            print(c)

        customers_list = []
    else:
        customers_list.append(customers)

    customers = input()

print(f"{len(customers_list)} people remaining.")
