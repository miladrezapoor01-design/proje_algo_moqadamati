


import random
tedadbord_shoma=(0)
tedadbord_game=(0)
while True:
    menu_game=input("1.start 2.exit")
    
    match menu_game:
        case"1":
            

            menu_entekhabe_shoma=input("1.sang  2.kaqaz 3.qeychi")
            
            if menu_entekhabe_shoma not in ["1","2","3"] :
                print("adade vared shode sahih nist !!!!") 
                break 
            if menu_entekhabe_shoma == "1":
                print("entekhabe shoma: sang")
            if menu_entekhabe_shoma == "2":
                print("entekhabe shoma: kaqaz")
            if menu_entekhabe_shoma == "3":
                print("entekhabe shoma: qeychi")
                
            list_game=["sang","kaqaz","qeychi"]
            entekhab_game=random.choice(list_game)
            print("entekhabe game : ",entekhab_game)
                
            if entekhab_game=="sang" and menu_entekhabe_shoma =="1" :
                print("barabar")
            if entekhab_game=="sang" and menu_entekhabe_shoma == "2" :
                print("you win")
                tedadbord_shoma+=1
            if entekhab_game== "sang" and menu_entekhabe_shoma == "3":  
                print("you lost")
                tedadbord_game+=1

            
            
            if entekhab_game=="kaqaz" and menu_entekhabe_shoma =="1" :
                print("you lost")
                tedadbord_game+=1
            if entekhab_game=="kaqaz" and menu_entekhabe_shoma == "2" :
                print("barabar")
            if entekhab_game== "kaqaz" and menu_entekhabe_shoma == "3":  
                print("you win")
                tedadbord_shoma+=1

            if entekhab_game=="qeychi" and menu_entekhabe_shoma =="1" :
                print("you win")
                tedadbord_shoma+=1
            if entekhab_game=="qeychi" and menu_entekhabe_shoma == "2" :
                print("you lost")
                tedadbord_game+=1
            if entekhab_game== "qeychi" and menu_entekhabe_shoma == "3":  
                print("barabar")
        
            print("tedade borde shoma : ",tedadbord_shoma)
            print("tedade borde game : ",tedadbord_game)     
        case"2":
            break


                                      