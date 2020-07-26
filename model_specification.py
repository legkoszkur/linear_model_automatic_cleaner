
from data_input import the_data


while True:
    y_endo = input("Pleace insetr your endogenic variable:")
    if y_endo in the_data.columns.values:
        print("You chosen endogenic", y_endo, "variable.")
        break
    else:
        print("Your input variable do not belongs to variables from file.")
        continue


while True:
  try:
     how_many_variables = int(input("How many egzogenic variables do you want to insert:"))
     if how_many_variables < len(the_data.columns) and how_many_variables > 0:
         break
     else:
         print("Number of variables should be between 1 and dataset variables amount.")
  except ValueError:
      print("Pleace insert intiger.")
      continue

zero_number = 0
x_egzo = []
while zero_number < how_many_variables:
    temporary_variable = input("Chose your exogenous variables(one at a time):")
    if temporary_variable != y_endo:
        if temporary_variable not in x_egzo:
            if temporary_variable in the_data.columns and temporary_variable:
                x_egzo.append(temporary_variable) 
                zero_number += 1
            else:
                print("Your input variable do not belongs to variables from file!")
        else:
            print("You can insert variable only one time!")
    else:
        print("Exogenous variable can not be the same as endogenous is!")

print("Your chosen variables. Endogenius:",y_endo,".Egzogenius:",x_egzo)
##########################################################################

