# Assignment 1 The Edsel Car Rental Company rents 
# Ramadan Masadekh
# Date : 14 SEP , 2024

# Constants

RENTS_PER_DAY =75.00 
RENTS_PER_KILOM=0.26
INSURANCE_PER_DAY=17.00
DISCOUNT_RENTAL_RATE=0.10
DISCOUNT_MILEAGE_RATE=0.25
HST_RATE=0.15

# User input.
print()
print("-----------  Welcome to Edsel Car Rental Company!  ----------")
print()
CustomerName=input("Enter the customer name:                                      ")
PhoneNumber=input("Enter the customer phone number:                              ")
NumberOfDay=int(input("Enter number of days the car was rented:                      "))
OdometerStart=int(input("Enter the odometer reading when the car was rented:           "))
OdometerEnd=int(input("Enter odometer reading when the car was returned:             "))


# Process

# Calculate the total kilometers travelled 

TotalKilometers= OdometerEnd - OdometerStart

# The rental cost

RentalCost= NumberOfDay * RENTS_PER_DAY

# The mileage cost

MileageCost= TotalKilometers * RENTS_PER_KILOM

# The insurance cost

InsuranceCost= NumberOfDay * INSURANCE_PER_DAY


# Offer a discount for any rentals during this winter

DiscountRental= RentalCost * DISCOUNT_RENTAL_RATE

DiscountMileage= MileageCost * DISCOUNT_MILEAGE_RATE

TotalDiscount= DiscountRental + DiscountMileage

# The total rental cost

TotalRental = RentalCost + MileageCost + InsuranceCost - TotalDiscount

Hst = TotalRental * HST_RATE

TotalInvoice = TotalRental +Hst

# Display the invoice for the customer.
print()
print("----------------------------------------------------------------------------------------------------------")
print()
print(f"Customer name:                                    {CustomerName}")
print(f"Customer phone number:                            {PhoneNumber}")
print(f"Number of days the car was rented:                {NumberOfDay}")
print(f"The odometer reading when the car was rented:     {OdometerStart}KM")
print(f"The odometer reading when the car was returned:   {OdometerEnd}KM")

print(f"The total kilometers travelled:                   {TotalKilometers}KM")
print(f"The rental cost is:                              ${RentalCost:.3f}")
print(f"The mileage cost is:                             ${MileageCost:.3f}")
print(f"The insurance cost is:                           ${InsuranceCost:.3f}")
print(f"The discount at 10% off the rental cost:         ${DiscountRental:.3f}")
print(f"The discount at 25% off the mileage cost:        ${DiscountMileage:.3f}")

print(f"The total discount is:                           ${TotalDiscount:.3f}")
print(f"Total Rental Cost (before HST):                  ${TotalRental:.3f}")
print(f"The HST (15%) is:                                ${Hst:.3f}")
print(f"The final invoice total is:                      ${TotalInvoice:.3f}")