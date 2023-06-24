"""
Write program that calculates total price for someone's movie tickets.  Tickets are $11 each.  Ask user to enter the number of tickets they want, then print out the total price. Ignore tax.

Extra: For orders of 20 or more tickets at once, tickets are discounted to $7 each.
"""
ticket_price = 0
num_tickets = input("Movie Theatre A: Number of tickets:")
num_tickets = int(num_tickets)

#Applying Discount
  #Movie Theatre A 
if num_tickets >= 20:
  ticket_price = 7
else:
  ticket_price = 11

total_cost = (num_tickets * ticket_price)
print("Movie Theatre A: Your total is $" + str(total_cost) + ".")

'''
Write code that makes the discount applicable, but in groupings of five tickets at a time, such that every collective 5 tickets is discounted to $7, but the remaining are originally priced.
'''

ticket_price = 11
discounted_ticket_price = 7
num_tickets = input("Movie Theatre B: Number of tickets:")
num_tickets = int(num_tickets)

#Applying Discount
  #Movie Theatre B

num_discounted_tickets = int(num_tickets / 5) * 5
num_nonDiscounted_tickets = num_tickets % 5


if num_tickets >= 5 :
  total_cost = (ticket_price * num_nonDiscounted_tickets) + (discounted_ticket_price * num_discounted_tickets)
  print("Movie Theatre B: Your total is $" + str(total_cost) + ".")
else:
  total_cost = ticket_price * num_tickets
  print("Movie Theatre B: Your total is $" + str(total_cost) + ".")

print("Movie Theatre B: Your total is $" + str(total_cost) + ".")
