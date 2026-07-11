# WAP to calculate selling price of book based on cost price and discount.
cp_book = float(input('enter the cost price of book: '))
dis_per = float(input('enter the discount in percetange: '))

dis_amt = (cp_book * dis_per) / 100

sp = cp_book - dis_amt

print(f'the selling price of book is {sp}.')