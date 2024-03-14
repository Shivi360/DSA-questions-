food_bill = float(input("enter the food bill:")) #only food bill
cgst = food_bill * 0.18
sgst = food_bill * 0.18
tip_bill = float(input('tip of yours')) /100 # Tip entered and converting it to decimal with float 
total_bill = food_bill * tip_bill #aclculation of tip 
total = total_bill + food_bill  + cgst + sgst  #total bill calculation 
print('__________________________________')
print('__________________________________')
print(f'food bill is :${food_bill}') #f we are addin because I added {}
print('\n')
print(f'your tip is added :${tip_bill}')
print('\n')
print(f'cgst is added 18%  :{cgst}')
print(f'sgst is added 18%  :{sgst}')
print('__________________________________')
print(f'The total bill: ${total}')
print('__________________________________')
print('__________________________________')
print('Thank You for visit')
#your regular food bill 