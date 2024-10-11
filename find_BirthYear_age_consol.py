import datetime
    
while True:
    # ضع الكود الخاص بك هنا

        try:
            print("------------------------------")
            import datetime
            dt = datetime.datetime.now()
            Birth_Year=int(input("Enter your Birth year OR \n Your Age :"))
            this_year = dt.strftime('%Y')
            age = int(this_year)- Birth_Year
            print("It's  : ",age)
            print("------------------------------")
        except:
            print('')
            print("------- Error Entry ---------")
            print("---Most be int number entry--- ")

    
            #print("تنفيذ الكود")
    
        # شرط للخروج من الحلقة إذا لزم الأمر
        user_input = input("هل تريد إعادة تشغيل الكود؟ : \n y = نعم  \n or Enter any key for Exit ")
        #print("y = نعم | n = لا")        
        if user_input.lower() != "y":
            print("------- good bay ---------")
            break
            



