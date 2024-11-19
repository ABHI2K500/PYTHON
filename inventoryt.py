inventory=[
    ("laptop",5,100000),
    ("mouse",10,200)
]
for item in inventory:
    item_name,num_of_items,amount=item
    total=num_of_items*amount
    print(total)