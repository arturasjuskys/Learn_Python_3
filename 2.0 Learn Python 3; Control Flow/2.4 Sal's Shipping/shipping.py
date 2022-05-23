# Ground Shipping
# 1. & 3.
weight = 41.5
cost = 0

# 2.
if weight <= 2:
  cost = weight * 1.50 + 20
  print('Ground Shipping: $' + str(cost))
elif weight >= 2 and weight <= 6:
  cost = weight * 3.00 + 20
  print('Ground Shipping: $' + str(cost))
elif weight >= 6 and weight <= 10:
  cost = weight * 4.00 + 20
  print('Ground Shipping: $' + str(cost))
else:
  cost = weight * 4.75 + 20
  print('Ground Shipping: $' + str(cost))

# Ground Shipping Premium
# 4.
cost_ground_premium = 125.00
# 5.
print('Ground Shipping Premium: $' + str(cost_ground_premium))

# Drone Shipping
# 6.
cost = 0
if weight <= 2:
  cost = weight * 4.50
  print('Drone Shipping: $' + str(cost))
elif weight >= 2 and weight <= 6:
  cost = weight * 9.00
  print('Drone Shipping: $' + str(cost))
elif weight >= 6 and weight <= 10:
  cost = weight * 12.00
  print('Drone Shipping: $' + str(cost))
else:
  cost = weight * 14.25
  print('Drone Shipping: $' + str(cost))
