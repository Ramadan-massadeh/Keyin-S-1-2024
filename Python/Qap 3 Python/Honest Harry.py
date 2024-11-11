# Description: Project 3 – Python
# Author: Ramadan Masadekh
# Date(s): Oct 12,2024


# Define required libraries.
import datetime


# Define program constants.
STANDARD_RATE_FEE=75.00
HIGH_RATE_FEE=165.00
TRANSFER_FEE_RATE=.01
TRANSFER_ADDEITIONAL_FEE_RATE=.016
HST_RATE=.15
FINANCING_FEE=39.99
CUR_DATE=datetime.datetime.now()


# Define program functions.



# Main program starts here.
FtimePay=CUR_DATE + datetime.timedelta(days=30)
FtimePayD=FtimePay.strftime("%d-%b-%y")
InvDate=datetime.datetime.strftime(CUR_DATE,"%B %d, %Y")
InvDate2=datetime.datetime.strftime(CUR_DATE,"%d-%b-%y")


while True:
    allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'")
  
    # Gather user inputs.
    print()
    print()
    while True:
        FirstName=input("Enter the First name (END to Quit): ").title()

        if FirstName =="":
            print()
            print("   Data Entry Error - The first name must be entered ...")
            print()
        elif  set(FirstName).issubset(allowed_char) == False:
            print()
            print("First Name contains invalid characters. Please re-enter.")
            print()
        else:
            break

        
    if FirstName.upper()=="END":
        break


    while True:
        LastName=input("Enter the last name: ").title()

        if LastName=="":
            print()
            print("   Data Entry Error - The Last name must be entered ...")
            print()
        elif set(LastName).issubset(allowed_char)== False:
            print()
            print("Last Name contains invalid characters. Please re-enter.")
            print()
        else :
            break

    allowed_char=set("1234567890")
    while True:
            PhoneNum=input("Enter the phone numbet XXXXXXXXXX: ")

            if PhoneNum=="":
                print()
                print("   Data Entry Error - The Phone number must be entered ...")
                print()
            elif set(PhoneNum).issubset(allowed_char) == False:
                print()
                print("   Data Entry Error - The Phone number contains invalid characters. Please re-enter.")
                print()
            elif len(PhoneNum)!=10:
                print()
                print("   Data Entry Error - The Phone number must be 10 digit ...")
                print()
            else:
                break

    allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'") 
    allowed_char2 = set("1234567890")     
    while True:
        PlateNum=input("Enter the plate number XXX999: ").upper()
        PlateChar=PlateNum[0:3]
        PlateDigit=PlateNum[3:]

        if PlateNum == "":
             print()
             print("   Data Entry Error - The Plate number must be entered ...")
             print()
        elif len(PlateNum) !=6:
             print()
             print("   Data Entry Error - The Plate number must be  XXX999 ...")
             print()
        elif set(PlateChar).issubset(allowed_char) == False:
             print()
             print("   Data Entry Error - The Plate number must be start first 3 index as a char  XXX999 ...")
             print()
        elif set(PlateDigit).issubset(allowed_char2) == False:
             print()
             print("   Data Entry Error - The Plate number must be end the last 3 index as a digit  XXX999 ...")
             print()
        else:
            break
    while True:
        Car_Make = input("Enter The Car's Make: ").title()
        if Car_Make == "":
            print("Error - Car Make Must Be Entered")
        else:
            break

    while True:
        Car_Model = input("Enter The Car's Model: ").title()
        if Car_Model == "":
            print("Error - Vehicle's Model Must Be Entered: ")
        else:
            break
    
    while True:
        Car_Year = input("Enter The Vehicle's Year: ")
        if Car_Year == "":
            print("Error - Vehicle's Year Must Be Entered: ")
        else:
            break


    while True:
        try:
            SellPrice=float(input("Enter the sellig price: "))

        except:
            print()
            print(" The Car Price  invalid - Enter car price  must be valide number:")
            print()
        else:
            if SellPrice>50000.00:
                print()
                print(" The Car Price  invalid - car price  must be under 50000.00:")
                print()
            else:
                break


    while True:
        try:
         AmmTrade=float(input("Enter the Ammount trade: "))

        except:
            print()
            print(" The Ammount Trade  invalid - Enter the Ammount trade must be valide number:")
            print()
        else:
            if AmmTrade >= SellPrice:
                print()
                print(" The Ammount Trade  invalid - Ammount Trade  must be under Selling price:")
                print()
            else:
                break


    while True:
        SalePerson = input("Enter The Sales Person Name: ")
        if SalePerson == "":
            print("Error - Sale Person Name Must Be Entered: ")
        else:
            break

        


    # Perform required calculations.

    # The price after trade

    PriceAfter= SellPrice - AmmTrade

    # The licence fee

    if SellPrice <= 15000.00:
        LicenceFee=STANDARD_RATE_FEE
    else:
        LicenceFee=HIGH_RATE_FEE
    
    # The transfer fee 1% of the selling price - if the selling price is
    # more than $20,000.00, an additional 1.6% luxury tax is calculated on the selling price and added to the transfer fee. 
    TransFee= SellPrice * TRANSFER_FEE_RATE
    if SellPrice > 20000.00:
        TransFee=(TRANSFER_ADDEITIONAL_FEE_RATE* SellPrice) + TransFee

    # The Subtotal is the Price after trade plus the License Fee plus the Transfer Fee. 

    SubTotal= PriceAfter + LicenceFee + TransFee

    # Taxes (HST) are calculated at 15% on the Subtotal. 

    Hst= SubTotal * HST_RATE

    # The total sales price is the subtotal plus the HST.

    TotalSales = SubTotal + Hst
        
    ReceiptId=(FirstName[0:2] + "-" + PlateDigit + "-" + PhoneNum[6:])
    
    
    
    print()
    print()
    print()




    # Display results

    print(f"         1         2         3         4         5         6         7")
    print(f"123456789012345678901234567890123456789012345678901234567890123456789012345678")
    print()
    
    
    print(f'Honest Harry Car Sales                          Invoice Date: {InvDate :<14s}')
    print(f'Used Car Sale and Receipt                       Receipt No:        {ReceiptId:11s}')
    print()

    SellPriceDsp="${:,.2f}".format(SellPrice)
    AmmTradeDsp="${:,.2f}".format(AmmTrade)
    print(f'                                          Sale price:               {SellPriceDsp:<10}')
    print(f'Sold to:                                  Trade Allowance:          {AmmTradeDsp:<10}')
    print(f"                                          ------------------------------------")

    CusName=(FirstName[0]+". "+LastName)
    PhoneNumDsp=f"({PhoneNum[:3]}) {PhoneNum[3:6]}-{PhoneNum[6:]}"
    PriceAfterDsp="${:,.2f}".format(PriceAfter)
    LicenceFeeDsp="${:,.2f}".format(LicenceFee)
    TransFeeDsp="${:,.2f}".format(TransFee)

    print(f"     {CusName}                          Price after Trade:        {PriceAfterDsp:<10}")
    print(f"      {PhoneNumDsp}                      License Fee:              {LicenceFeeDsp:<10}")
    print(f'                                          Transfer Fee:             {TransFeeDsp:<10}')
    print(f"                                          ------------------------------------")

    SubTotaldsp="${:,.2f}".format(SubTotal)
    HstDsp="${:,.2f}".format(Hst)
    TotalSalesDsp="${:,.2f}".format(TotalSales)
    
    print(f'Car Details:                              Subtotal:                 {SubTotaldsp:<10}')
    print(f'                                          Hst:                      {HstDsp:<10}')
    print(f"    {Car_Year} {Car_Make:<12s} {Car_Model:<12s}        ------------------------------------")
    print(f'                                          Total Sale price:         {TotalSalesDsp:<10}')
    print()

    print("---------------------------------------------------------------------------")
    print()


    print(f"                                   Financing     Total        Monthly")
    print(f"     # Years    # Payments            Fee        Price        Payment")
    print("     -------------------------------------------------------------------")
    
    for years in range(1 , 5):
        NumOfMonth=years*12
        FinFeeTot=FINANCING_FEE *years
        TotPriceFin=float( TotalSales )+ FinFeeTot
        MontPayment=TotPriceFin / NumOfMonth

        FinFeeTotDsp="${:,.2f}".format(FinFeeTot)
        TotPriceFinDsp="${:,.2f}".format(TotPriceFin)
        MontPaymentDsp="${:,.2f}".format(MontPayment)
        print(f"         {years:<4}        {NumOfMonth:<2}            {FinFeeTotDsp:<7}     {TotPriceFinDsp:<10}    {MontPaymentDsp:<10}  ")
    print("     -------------------------------------------------------------------")
    print(f'     Invoice date: {InvDate2}          First payment date: {FtimePayD}')
    print()
    print("---------------------------------------------------------------------------")
    print(f"                   Best Used Cars At The Best Prices!                     ")
    print()
    print()

    
    
    
    # Write the values to a data file for storage.





# Any housekeeping duties at the end of the program.