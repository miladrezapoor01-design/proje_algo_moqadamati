list_film=[]
list_sans=[]
list_price=[]
list_sum_price=[]
while True:
    menu_sinema=input("1.film  2.sorathesab  3.hazine_belit 4.exit")
    
    
       
    match menu_sinema:
                

        case"1":
            menu_film=input("1.mumiyaei  2.super_man  3.batman  4.topgun  5.exit")
              
            match menu_film:
                case"1":
                        
                    tedad_belit_mumiyaei=int(input("tedad belit ra vared konid :"))
                    price_mumiyaei=tedad_belit_mumiyaei*(350000)
                    list_price.append(price_mumiyaei)
                    list_film.append("mumiyaei")
                    menu_sans_mumiyaei=input("1.14_16  2.16_18  3.18_20   4.20_22  5.exit")
                    match menu_sans_mumiyaei:
                        case"1":
                            list_sans.append("mumiyaei 14_16")
                        case"2":
                              list_sans.append("mumiyaei 16_18")
                        case"3":
                              list_sans.append("mumiyaei 18_20")
                        case"4":
                              list_sans.append("mumiyaei 20_22")
                        case"5":
                            break            

                case"2":
                   
                        tedad_belit_super_man=int(input("tedad belit ra vared konid :"))
                        price_super_man=tedad_belit_super_man*(250000)
                        list_price.append(price_super_man)
                        list_film.append("super_man")
                        menu_sans_super_man=input("1.14_16  2.16_18  3.18_20   4.20_22  5.exit")
                        match menu_sans_super_man:
                            case"1":
                                list_sans.append("super_man 14_16")
                            case"2":
                                list_sans.append("super_man 16_18")
                            case"3":
                                list_sans.append("super_man 18_20")
                            case"4":
                                list_sans.append("super_man 20_22")
                            case"5":
                                break            

                case"3":
                        tedad_belit_batman=int(input("tedad belit ra vared konid :"))
                        price_batman=tedad_belit_batman*(250000)
                        list_price.append(price_batman)
                        list_film.append("batman")
                        menu_sans_batman=input("1.14_16  2.16_18  3.18_20   4.20_22  5.exit")
                        match menu_sans_batman:
                            case"1":
                                list_sans.append("batman 14_16")
                            case"2":
                                list_sans.append("batman 16_18")
                            case"3":
                                list_sans.append("batman 18_20")
                            case"4":
                                list_sans.append("batman 20_22")
                            case"5":
                                break            
                        
                case"4":
                        tedad_belit_topgun=int(input("tedad belit ra vared konid :"))
                        price_topgun=tedad_belit_topgun*(350000)
                        list_price.append(price_topgun)
                        list_film.append("topgun")
                        menu_sans_topgun=input("1.14_16  2.16_18  3.18_20   4.20_22  5.exit")
                        match menu_sans_topgun:
                            case"1":
                                list_sans.append("topgun 14_16")
                            case"2":
                                list_sans.append("topgun 16_18")
                            case"3":
                                list_sans.append("topgun 18_20")
                            case"4":
                                list_sans.append("topgun 20_22")
                            case"5":
                                break            
                                                
                case"5":
                    break    
        case"2":
            mablaq_nahayi=sum(list_price)
            list_sum_price.append(mablaq_nahayi)
            print("film hay entekhabi : ",list_film)
            print("sans haye entekhabi :", list_sans)
            print("mablaqe pardakhti : ", list_sum_price)    
            break
        case"3":
            print("mumiyaei  350000   ,   super_man   250000 ,  batman    250000 , topgun    350000")
            break
        case"4":
            break
                        
                                                
                                                                        
