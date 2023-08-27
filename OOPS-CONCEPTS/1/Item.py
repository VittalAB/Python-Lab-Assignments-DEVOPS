class Item:

    def __init__(self, item_id, item_name, company_name, price) -> None:
        self.item_id = item_id
        self.item_name = item_name
        self.company_name = company_name
        self.price = price

    def display(self):
        ans = f'''Item Id:  {self.item_id}
Item Name:  {self.item_name}
Company Name: {self.company_name}
Price of Item: {self.price} Rs'''
        print(ans)