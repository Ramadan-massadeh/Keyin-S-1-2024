# Program for the St.John's Marina & Yacht Club
# Author Ramadan Masadekh
# Date Sep 28, 2024



# define program constants

EVEN_NUM_SITE=80.00
ODD_NUM_SITE=120.00
ELTERNATE_COST=5.00
WEEKLY_CLEANINIG_CHARGE=50.00
VIDEO_SUR_CHARGE=35.00
HST_RATE=.15
STANDARD_MEMBER=75.00
EXECUTIVE_MEMBER=150.00
PROCESSING_FEE=59.99
CANCEL_FEE=.60

# Gather user information
print()

print("            Welcome to Marina & Yacht Club                ")
print()
Date=input("Please Input current date (YYYY-MM-DD) :       ")
SiteNumber=int(input("Please enter site number (1-100) :             " ))

MemberName=input("Please Enter Member Name :                     ")
StreetAdd=input("Please Enter your street adress :              " )
City=input("Please Enter your City :                       " )
Province=input("Please Enter your Province :                   " ).upper()
PostalCode=input("Please Enter your PostalCode :                 " ).upper()
PhoneNumber=input("Please Enter your Phone Number :               " )
CellNumber=input("Please Enter your Cell Number :                " )


MemberType=input("Please Enter the membership type (S or E) :    ").upper()
if MemberType=="S":
    MemberType="Standard"
else:
    MemberType="Executive"


AlternateMembers=int(input("The number of alternate members :              "))

WeeklySiteCl=input("Please Enter Y or N if you Need Weekly site cleaning service :  " ).upper()
if WeeklySiteCl=="Y":
    WeeklySiteCl="Yes"
else:
    WeeklySiteCl="No"


VideoSurveillance=input("Please Enter Y or N if you video surveillance service :         ").upper()
if VideoSurveillance=="Y":
    VideoSurveillance="Yes"
else:
    VideoSurveillance="No"

print()

# Generate program results through calculations.

# Determine the site charge based on site number

if SiteNumber %2==0:
    SiteCost=EVEN_NUM_SITE
else:
    SiteCost=ODD_NUM_SITE


# Calculate the alternate member charge
Alternate_Member_Charge = AlternateMembers * ELTERNATE_COST

# Add these two numbers to get the site charges.
Total_Site_Charge=Alternate_Member_Charge + SiteCost

# weekly site cleaning
WeeklyCharge=0
if WeeklySiteCl=="Yes":
    WeeklyCharge+=WEEKLY_CLEANINIG_CHARGE

# video surveillance
VideoCharge=0
if VideoSurveillance=="Yes":
    VideoCharge+=VIDEO_SUR_CHARGE

# the  extra charges is Add these together 

ExtraCharge=WeeklyCharge+VideoCharge


# The subtotal is the site charge plus the extra charges

SubTotal=Total_Site_Charge + ExtraCharge

# Taxes are calculated at 15% on subtotal, and the total monthly charge is the subtotal plus the taxes

Hst=SubTotal * HST_RATE

# The total monthly charge is the subtotal plus the taxes
Total_Monthly_Charge=SubTotal + Hst

# monthly dues are calculated  for standard members executive members

if MemberType =="Standard":
    MonthlyDue=STANDARD_MEMBER
else:
    MonthlyDue=EXECUTIVE_MEMBER


# The total monthly charge and the monthly dues are added together to give the Total Monthly Fees

Total_Monthly_Fees=Total_Monthly_Charge + MonthlyDue

# The total Yearly Fees by multiplying the total monthly fees by 12

Total_Yearly_Fees= Total_Monthly_Fees * 12

# The monthly payment is the Total yearly fees, plus a processing fee divided by 12

MonthlyPayment=(Total_Yearly_Fees + PROCESSING_FEE )/ 12

# Cancellation fee

Total_Year_Charge=Total_Site_Charge*12
CancellationFee=Total_Year_Charge* CANCEL_FEE


# Output: Display the results


print()
print(f"----------------------------------------")
print()
print(f"    St. John’s Marina & Yacht Club    ")
print(f"         Yearly Member Receipt        ")
print()
print(f"----------------------------------------")
print()
print(f'Client Name and Address:              ')
print()
print(f'{MemberName:<10s}')
print(f'{StreetAdd:<10s}')
print(f'{City:<10s},{Province:<2s} {PostalCode:<6s}')
print()
print(f'Phone:{PhoneNumber:<10s} (H)')
print(f'      {CellNumber:<10s} (C)')
print()

print(f'Site #: {SiteNumber:<2d} Member type:{MemberType:<10s}')
print()
print(f'Alternate members:                 {AlternateMembers:<2d}')
print(f'Weekly site cleaning:              {WeeklySiteCl:<3s}')
print(f'Video surveillance:                {VideoSurveillance:<3s}')
print()

Tot_Site_ChargeDsp = "${:,.2f}".format(Total_Site_Charge)
print(f'Site charges:                    {Tot_Site_ChargeDsp:<4s}')
Extr_Charge="${:.2f}".format(ExtraCharge)
print(f'Extra charges:                    {Extr_Charge:<4s}')
print(f'                               ---------')
print()
Sub_Total="${:.2f}".format(SubTotal)
print(f'Subtotal:                        {Sub_Total:<4s}')
Tax="${:.2f}".format(Hst)
print(f'Sales tax (HST):                  {Tax:<4s}')
print()
print(f'                               ---------')

TotMonthlyCharge="${:.2f}".format(Total_Monthly_Charge)
print(f'Total monthly charges:           {TotMonthlyCharge:<4s}')
Monthly_dues="${:.2f}".format(MonthlyDue)
print(f'Monthly dues:                     {Monthly_dues:<4s}')
print()
print(f'                               ---------')


TotMonthlyFees="${:.2f}".format(Total_Monthly_Fees)
print(f'Total monthly fees:             {TotMonthlyFees:<4s}')

TotYearFees="${:.2f}".format(Total_Yearly_Fees)
print(f'Total yearly fees:             {TotYearFees:<4s}')
print()
print(f'                               ---------')


Monthly_payment="${:.2f}".format(MonthlyPayment)
print(f'Monthly payment:                 {Monthly_payment:<4s}')
print()


print(f"----------------------------------------")
print()

print(f"Issued: {Date}")
print(f"HST Reg No: 549-33-5849-4720-9885")
print()

Cancellation_Fee="${:.2f}".format(CancellationFee)
print(f'Cancellation fee:                {Cancellation_Fee:<4s}')

print()


print(f"----------------------------------------")
'''

print("Cancle " , CancellationFee)
'''
