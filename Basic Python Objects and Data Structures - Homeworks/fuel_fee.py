#Program that Calculates Fuel Fee

#Get information about how much the vehicle has burned per kilometer and how many kilometers it has traveled

burned_per_km = float(input("How much does your car burn per kilometer? "))
km = int(input("How many kilometers did you travel? "))

#Calculate total fee

total_fee = burned_per_km * km
print("Total fee you will pay: ", total_fee)