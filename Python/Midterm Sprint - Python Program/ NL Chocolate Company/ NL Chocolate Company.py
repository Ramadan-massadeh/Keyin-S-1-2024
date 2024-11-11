def NLchocoCom():

    # Description: Midterm Sprint - Python Program - Project 1 - NL Chocolate Company
    # Author: Ramadan Masadekh
    # Date(s): Oct 20 , 2024


    # Define required libraries.
    import datetime


    # Define program constants.
    DAILY_RATE=85.00
    RATE_PER_KILOMETER=.17
    RATE_PER_DAY=65.00
    BOUNS_NUM_OF_DAYS_RATE=100.00
    BOUNS_KILO_RATE=0.04
    BOUNS_EXECUTIVE_RATE=45.00
    BOUNS_DEC_RATE=50.00
    HST_RATE=0.15




    # Define program functions.



    # Main program starts here.
    while True:
        allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'")
        
        
        # Gather user inputs.
        print()
        print()

        # the employee number (must be entered and be 5 characters)
        while True:
            EmpNumber= input("Enter the employee number (must be entered and be 5 characters):")

            if EmpNumber =="":
                print()
                print("   Data Entry Error - The Employee number must be entered ...")
                print()
            elif set(EmpNumber).issubset(allowed_char) == False:
                print()
                print("   Data Entry Error - The Employee number must be characters ...")
                print()
            elif len(EmpNumber)!=5:
                print()
                print("   Data Entry Error - The Employee number must be 5 characters ...")
                print()
            else:
                break
        
        # Employee first name (must be entered – adjust to title case)
        while True:
            EmpFirstName= input("Enter the First Name: ").title()

            if EmpNumber =="":
                print()
                print("   Data Entry Error - The Employee First Name must be entered ...")
                print()
            else:
                break
            
        # last name (must be entered – adjust to title case)

        while True:
            EmpLastName= input("Enter the Last Name: ").title()

            if EmpLastName =="":
                print()
                print("   Data Entry Error - The Employee Last Name must be entered ...")
                print()
            else:
                break
            
        
        #  location of the trip

        while True:
            Location= input ("Enter the location of the trip: ")

            if Location =="":
                print()
                print("   Data Entry Error - The Location must be entered ...")
                print()
            else :
             break
        
        # start date (Must be entered and valid)
        

        while True:
            try:
                TripStart = input("Enter The Employee Trip Start Date: (YYYY-MM-DD) ")
                TripStart = datetime.datetime.strptime(TripStart,"%Y-%m-%d")
            except:
                print("Data Entry Error - Start Date Is Invaild")
            else:
               
                    break
        # End date (Must be entered and after the start date by no more than 7 days)
        while True:
            try:
                TripEnd = input("Enter The Employee Trip End Date: (YYYY-MM-DD) ")
                TripEnd= datetime.datetime.strptime(TripEnd,"%Y-%m-%d")
                TreipEndPlus7=TripStart + datetime.timedelta(days=7)
            except:
                print("Data Entry Error - End Date Is Invaild")
            else:
                if TripEnd > TreipEndPlus7:
                    print("   Data Entry Error - The trip cannot exceed 7 days. ...")
            
                else:
                    break

    
        
        # if they used their own car, or if a car was rented (Must be entered and must be the letters O or R only). Adjust to upper case)
        while True:
        
            CarUsed=input ("Enter The Car used or if a car was rented:  (O or R ) ").upper()

            if CarUsed =="":
                print()
                print("   Data Entry Error - The Car used must be entered ...")
                print()
            elif CarUsed != "O" and CarUsed !="R":
                print()
                print("   Data Entry Error - The Car used must be (O or R) ...")
                print()
            else:
                break
            
            # the total kilometers traveled (Must be entered and cannot exceed 2000) - only enter the kilometers if the employee used their own car

        while True:
    
         KiloTraveled=0
         try:
                if CarUsed=="O":
                 KiloTraveled = int(input ("Enter the total kilometers traveled: "))
                else:
                 break
            
            
         except:
                print()
                print(" The kilometers traveled  invalid - The kilometers must be valide number:")
                print()
         else:
            if KiloTraveled>2000:
                print()
                print("   Data Entry Error - The kilometers cannot exceed 2000 ...")
                print()
            else:
             break
        
        #  the claim type as standard or executive (S/E) (Must be S or E – adjust to uppercase).

        while True:
            ClaimType=input("Enter the claim type as standard or executive: (S/E) ").upper()

            if ClaimType=="":
                    print()
                    print("   Data Entry Error - The claim type must be entered ...")
                    print()
            elif ClaimType !="S" and ClaimType !="E":
                    print()
                    print("   Data Entry Error - The claim type must be (S or E) ...")
                    print()
            else:
                break
            
            
        

            
                
                





        


        # Perform required calculations.

        # Calculate the number of days based on the start and end dates

        NumOfDayes=( TripEnd - TripStart ).days

        # Calculate the per diem amount by multiplying the total days by a daily rate 

        PerDAmount= NumOfDayes * DAILY_RATE

        # The mileage amount is calculated using a rate of .17 per kilometer if the salesperson used their car, or a rate of $65.00 per day is the salesperson rented a car.
        
        if CarUsed=="O":
            MileageAmount=KiloTraveled * RATE_PER_KILOMETER
        else:
            MileageAmount=NumOfDayes * RATE_PER_DAY

        # The bonus is calculated

        Amtbonus = 0 
        if NumOfDayes > 3:
                Amtbonus += BOUNS_NUM_OF_DAYS_RATE

        if KiloTraveled > 1000 and CarUsed == 'O':
                Amtbonus += BOUNS_KILO_RATE * KiloTraveled

        if ClaimType == "E": 
                Amtbonus += BOUNS_EXECUTIVE_RATE * NumOfDayes
        
        

        if TripStart.month == 12 and TripStart.day in range(15, 23):
            Amtbonus+=BOUNS_DEC_RATE
        
        
        # The Claim Amount is calculated as the per diem amount , the mileage amount, and the bonus.

        ClaimAmmount= PerDAmount + MileageAmount + Amtbonus
        
    # The HST is calculated on the Claim Amount using a rate of 15%.

        Hst = ClaimAmmount * HST_RATE
        
    
    # The Claim Total is the Claim Amount plus the HST.

        ClaimTotal = ClaimAmmount + Hst



        # Display results
        print()
        print(f"          NL Chocolate Company")
        print(f"------------------------------------------")
        print(f"Employee #:           {EmpNumber:<5s}")
        print(f"First Name:           {EmpFirstName:<10s}")
        print(f"Last Name:            {EmpLastName:<10s}")
        print(f"------------------------------------------")
        print(f"Trip Details")
        print(f"------------------------------------------")
        print(f"Trip Location:        {Location:<8s}")
        TripStartdsp= TripStart.strftime("%Y-%m-%d")
        TripEnddsp= TripEnd.strftime("%Y-%m-%d")
        print(f"Trip Start-Date:      {TripStartdsp:<10s}")
        print(f"Trip End-Date:        {TripEnddsp:<10s}")
        print(f"Number Of Days:       {NumOfDayes:<2}")
        print(f"Transportation Type:  {CarUsed:<6s}")
        print(f"Claim Type:           {ClaimType:<10s}")
        print(f"Total Kilometers:     {KiloTraveled:<4}")
        print(f"------------------------------------------")
        print(f"Invoice Summary")
        print(f"------------------------------------------")
        MilageAmountDsp = "${:,.2f}".format(MileageAmount)
        print(f"Mile Amount:          {MilageAmountDsp:<10}")
        AmtbonusDsp = "${:,.2f}".format(Amtbonus)
        print(f"Bonus:                {AmtbonusDsp:<4}")
        ClaimAmountDsp = "${:,.2f}".format(ClaimAmmount)
        print(f"Claim Amount:         {ClaimAmountDsp:<8}")
        SalesTaxDsp = "${:,.2f}".format(Hst)
        print(f"HST Amount:           {SalesTaxDsp:<8}")
        ClaimTotalDsp = "${:,.2f}".format(ClaimTotal)
        print(f"Total Claim Amount:   {ClaimTotalDsp:<8}")
        print(f"------------------------------------------")

        print()
        print()

        Continue = input(" Any Further Data Entry's ?? (END to quit): ").upper()         
        if Continue == "END":
            break


    


def InterQue():
     #Desc: A common program used at interviews for programming position is the FizzBiss problem.
    #Author:Ramadan masadekh
    #Date:October 22nd, 2024
    def fizz_buzz(n):
        result = []

        for i in range(1, n + 1):

            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")

            elif i % 3 == 0:
                result.append("Fizz")

            elif i % 5 == 0:
                result.append("Buzz")
            else: 
                result.append(str(i))
        
        return result

    n = 100

    result = fizz_buzz(n)

    print(result)

def StringAndDates():
    #Desc:Calculates years of service, years until retirement,days until next birthday, Employee ID, Username, and Password
    #Author:Brandon Pike
    #Date:October 22nd, 2024
    
    from datetime import datetime
    
    # Employee details
    first_name = "John"
    last_name = "Doe"
    phone_number = "123-456-7890"
    current_date = datetime.now()
    start_date = datetime(2020, 5, 15)  # Example start date
    birthdate = datetime(1990, 8, 25)  # Example birthdate
    
    # Calculate years of service
    years_of_service = current_date.year - start_date.year
    if (current_date.month, current_date.day) < (start_date.month, start_date.day):
        years_of_service -= 1
    
    # Calculate years until retirement
    retirement_age = 65
    retirement_year = birthdate.year + retirement_age
    years_until_retirement = retirement_year - current_date.year
    
    # Calculate days until next birthday
    next_birthday = birthdate.replace(year=current_date.year)
    if next_birthday < current_date:
        next_birthday = next_birthday.replace(year=current_date.year + 1)
    days_until_birthday = (next_birthday - current_date).days
    
    # Generate Employee ID
    employee_id = first_name[:3].lower() + last_name.lower() + phone_number[-4:]
    
    # Generate Username
    username = first_name[0].lower() + last_name.lower() + str(birthdate.year)
    
    # Generate Password
    password = last_name.lower() + str(birthdate.year) + "!@#"
    
    # Print results
    print("Employee ID:", employee_id)
    print("Username:", username)
    print("Password:", password)
    print("Years of Service:", years_of_service)
    print("Years until Retirement:", years_until_retirement)
    print("Days until Next Birthday:", days_until_birthday)
    
    
    #Desc: This does various calculations for SD13 Company
    #Author:Brandon Pike
    #Date:October 23rd, 2024
    
    from datetime import datetime, timedelta
    
    def calculate_maintenance_dates(purchase_date):
        basic_cleaning_date = purchase_date + timedelta(days=10)
        tube_fluid_check_date = purchase_date + timedelta(weeks=3)
        major_inspection_date = purchase_date + timedelta(weeks=26)  # 6 months
        return basic_cleaning_date, tube_fluid_check_date, major_inspection_date
    
    def calculate_amortization(cost):
        salvage_value = cost * 0.10
        useful_life_months = 15 * 12  # 15 years
        amortization = (cost - salvage_value) / useful_life_months
        return amortization, salvage_value
    
    def main():
        print("SD13 Company Maintenance Schedule")
    
        # Get user input for cost
        while True:
            try:
                cost = float(input("Enter the cost of the equipment: $"))
                if cost <= 0:
                    raise ValueError("Cost must be positive.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid number.")
    
        # Get user input for purchase date
        while True:
            try:
                purchase_date_str = input("Enter the purchase date (YYYY-MM-DD): ")
                purchase_date = datetime.strptime(purchase_date_str, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
    
        # Calculate maintenance dates
        basic_cleaning_date, tube_fluid_check_date, major_inspection_date = calculate_maintenance_dates(purchase_date)
    
        # Calculate amortization
        amortization, salvage_value = calculate_amortization(cost)
    
        # Display results
        print("\n--- Maintenance Schedule ---")
        print(f"Purchase Date: {purchase_date.strftime('%Y-%m-%d')}")
        print(f"Basic Cleaning Date: {basic_cleaning_date.strftime('%Y-%m-%d')}")
        print(f"Tube and Fluid Check Date: {tube_fluid_check_date.strftime('%Y-%m-%d')}")
        print(f"Major Inspection Date: {major_inspection_date.strftime('%Y-%m-%d')}")
    
        print("\n--- Amortization Details ---")
        print(f"Cost: ${cost:.2f}")
        print(f"Salvage Value (10%): ${salvage_value:.2f}")
        print(f"Monthly Amortization: ${amortization:.2f}")
    

def bb():
    #Desc: This does various calculations for SD13 Company
#Author:Brandon Pike
#Date:October 23rd, 2024

    from datetime import datetime, timedelta

    def calculate_maintenance_dates(purchase_date):
        basic_cleaning_date = purchase_date + timedelta(days=10)
        tube_fluid_check_date = purchase_date + timedelta(weeks=3)
        major_inspection_date = purchase_date + timedelta(weeks=26)  # 6 months
        return basic_cleaning_date, tube_fluid_check_date, major_inspection_date

    def calculate_amortization(cost):
        salvage_value = cost * 0.10
        useful_life_months = 15 * 12  # 15 years
        amortization = (cost - salvage_value) / useful_life_months
        return amortization, salvage_value

    def main():
        print("SD13 Company Maintenance Schedule")

        # Get user input for cost
        while True:
            try:
                cost = float(input("Enter the cost of the equipment: $"))
                if cost <= 0:
                    raise ValueError("Cost must be positive.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid number.")

        # Get user input for purchase date
        while True:
            try:
                purchase_date_str = input("Enter the purchase date (YYYY-MM-DD): ")
                purchase_date = datetime.strptime(purchase_date_str, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

        # Calculate maintenance dates
        basic_cleaning_date, tube_fluid_check_date, major_inspection_date = calculate_maintenance_dates(purchase_date)

        # Calculate amortization
        amortization, salvage_value = calculate_amortization(cost)

        # Display results
        print("\n--- Maintenance Schedule ---")
        print(f"Purchase Date: {purchase_date.strftime('%Y-%m-%d')}")
        print(f"Basic Cleaning Date: {basic_cleaning_date.strftime('%Y-%m-%d')}")
        print(f"Tube and Fluid Check Date: {tube_fluid_check_date.strftime('%Y-%m-%d')}")
        print(f"Major Inspection Date: {major_inspection_date.strftime('%Y-%m-%d')}")

        print("\n--- Amortization Details ---")
        print(f"Cost: ${cost:.2f}")
        print(f"Salvage Value (10%): ${salvage_value:.2f}")
        print(f"Monthly Amortization: ${amortization:.2f}")
      
    if __name__ == "__main__":
        main() 

def OldNew():
    
    # Program For a Game of Rock, Paper, Scissors
    
    import random

    options = ("Rock", "Paper", "Scissors")
    running = True

    while running:

        player = None
        computer = random.choice(options)
        print()
        while player not in options: 
            player = input("Enter A Choice (Rock, Paper or Scissors): ").title()

        print(f"Player: {player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("It's A Tie!")
        elif player == "Rock" and computer == "Scissors":
            print("You Win! ")
        elif player == "Paper" and computer == "Rock":
            print("You Win")
        elif player == "Scissors" and computer == "Paper":
            print("You Win! ")
        else:
            print("You Lose!")

        if not input("Play Again? (y/n): ").lower() == "y":
            running = False

    print("Thanks For Playing!")   

 


 




    # Display the user menu
while True:
    print()
    print(" Python Programs - Main Menu")
    print()
    print("1. NL Chocolate Company: ")
    print("2. Fun Interview Questions: ")
    print("3. Cool Stuff With Strings And Dates: ")
    print("4. A Little Bit Of Everything: ")
    print("5. Something old, Something New: ")
    print("6. Quit: ")
    print()

    while True:
        try:
            Choice= int (input("Enter choice (1 - 6): "))
        except:
            print()
            print("Data Entry Error -  must be a valid number between 1 and 3.")
            print()
        else:
            if Choice <1 or Choice >6:
                print()
                print("Data Entry Error -  must be a valid number between 1 and 3.")
                print()
            else:
                break
    if Choice==1:
        NLchocoCom()
    elif Choice==2:
        InterQue()
    elif Choice==3:
        StringAndDates()
    elif Choice==4:
        bb()
    elif Choice==5:
        OldNew()

    else:
        break

print()
print()
print("....................Good Bye ................")
