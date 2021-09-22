#Prompt user for a weight variable
weight = input("Enter your weight amount in pounds ")
weight = float(weight)

#Define cost variables
cost_ground = ""
cost_ground_premium = 125.00
cost_drone = ""

#Ground shipping price
if weight <= 2:
  cost_ground = weight * 1.5 + 20

elif weight <= 6:
  cost_ground = weight * 3 + 20

elif weight <= 10:
  cost_ground = weight * 4 + 20

elif weight > 10:
  cost_ground = weight * 4.75 + 20

print("Ground Shipping cost $", cost_ground)

#Premium shipping cost
print("Ground Shipping Premium $", cost_ground_premium)

#Drone shipping price
if weight <= 2:
  cost_drone = weight * 4.5 

elif weight <= 6:
  cost_drone = weight * 9 

elif weight <= 10:
  cost_drone = weight * 12 

elif weight > 10:
  cost_drone = weight * 14.25 

print("Drone Shipping cost $", cost_drone)
