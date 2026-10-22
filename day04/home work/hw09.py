#დავალება 10: მინი-მარკეტის სრული სალარო (მინი-პროექტი)
#შექმენი შემდეგი ცვლადები მომხმარებლის შეტანილი მონაცემებით (input-ით):
#• item_name (პროდუქტის სახელი - string)
#• price (ერთეულის ფასი - float)
#• quantity (რაოდენობა - int)
#გამოთვალე ჯამური ღირებულება (total_cost = price * quantity). შექმენი პირობა: თუ total_cost მეტია 50-ზე, მიანიჭე has_discount = True (სხვა შემთხვევაში False). გამოიტანე ეკრანზე სრული სავაჭრო ქვითარი: პროდუქტი, რაოდენობა, ჯამური ფასი და ფასდაკლების სტატუსი (True/False).
item_name=input("დაწერეთ ნივთის სახელი")
price=float(input("რა არის ფასი? "))
quality=int(input("რაოდენობა"))
total_cost=price*quality
has_discount=None
if total_cost >50:
    has_discount=True
else:    
    has_discount=False