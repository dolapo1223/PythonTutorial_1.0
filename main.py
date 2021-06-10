calculation_to_units = 24
name_of_units = "hours"

########write funtion to calculate different hours
def days_to_units():
  print(f"20 days are {20 * calculation_to_units} {name_of_units}")
  print("All good")

days_to_units()

#########funtion parameters

def days_to_units(number_of_days):
  print(f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_units}")
  print("All good")

#calling function
days_to_units(40)
days_to_units(20)
days_to_units(30)

## Entering multiple parameters
'''def days_to_units(number_of_days , customer_message):
  print(f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_units}")
  print(customer_message)


days_to_units(34 , "This is awesome")
days_to_units(76, "This is super great")
'''

#inputing values

def days_to_units(number_of_days):
  print(f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_units}")

input("Hey user, enter the number of days\n")

