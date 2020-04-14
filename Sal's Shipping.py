def ground_shipping(weight):
  if weight <= 2 :
    price_per_pound = 1.50
  elif weight <= 6 :
    price_per_pound = 3.00
  elif weight <= 10 :
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75
  cost = 20 + (weight * price_per_pound)
  return cost

cost_pr_ground_shipping = 125.00

def dron_shipping(weight):
  if weight <= 2:
    price_per_pounds = 4.50
  elif weight <= 6:
    price_per_pounds = 9.00
  elif weight <= 10:
    price_per_pounds = 12.00
  else:
    price_per_pounds = 14.25
  cost = weight*price_per_pounds
  return cost


def cheapset_shipping(weight):
  ground = ground_shipping(weight)
  dron = dron_shipping(weight)
  premuim = cost_pr_ground_shipping
  if ground < dron and ground < premuim:
    cost = ground
    return "You should ship using ground shipping, it will cost " + str(ground) + "$"
  elif dron < ground and dron < premuim:
    cost = dron
    return "You should ship using dron shipping, it will cost " + str(dron) + "$"
  else:
    cost = premuim
    return "You should ship using ground shipping, it will cost " + str(premuim) + "$"

print(cheapset_shipping(4.8)) 





