try:
    import datetime
    dt = datetime.datetime.now()
    Birth_Year=int(input("Enter your Birth year OR \n Your Age :"))
    this_year = dt.strftime('%Y')
    age = int(this_year)- Birth_Year
    print("It's  : ",age)
except:
    print('')
    print("------- Error Entry ---------")
    print("------------------------------")
    print("---Most be int number entry--- ")



