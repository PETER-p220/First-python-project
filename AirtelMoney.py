print("Dial *149*99# to get the menu")
choice=input("Dial:")
print("Dear customer Choose what help can we provide to you!!")

print('select operation.')
print('0.salio')
print('1.Ofa yako')
print('2.SMS')
print('3.Mitandao yote')
print('4.Airtel-Airtel')
print('5.Internet')
print('6.Combo')
print('7.HBB/Router/MIFI')
print('8.Bila kikomo')
print('9.Kuzuru(Roaming)/Kimataifa')
print('10.Rusha salio')
print('11.Matumizi bila Bando')
choice=int(input("Enter your choice 1/2/3/4/5/6/7/8/9/10/11:"))
if choice==0:
    print('1.Salio')
    print('2.change Language')
    print('3.salio Upige mwingi')
    choice=int(input('Enter your choice 1/2/3:'))
    if choice==1:
        print('1.Salio:Tshs 0')
        print('2.DENI:Tshs 0')
    elif choice==2:
        print('Language Changed Successifully.Preferred Language Will be Active from next Login.')
    elif choice==3:
        print('Huna Salio la upige mwingi Bonasi')
    else:
        print('Invalid Request')
elif choice==1:
    print('1.UNI Ofa')
    print('2.Data zaidi-Mpya')
    print('3.SMS Ofa')
    print('4.Kopa BANDO')
    choice=int(input('Enter your choice 1/2/3/4:'))
    if choice==1:
        print('1.Sh 500=Dak 100 Saa 24 BIGI')
        print('2.Sh 500=Dak 60 Saa 24')
        print('3.Sh 1000=Dak 130+300 SMS Siku 7')
        print('4.Sh 1000=Dak 300 Siku 7 BIGI')
        print('5.Sh 1000=Dak 40+MB 350 Siku 7')
        print('6.ZAIDI/DATA')
        choice=int(input('Enter your choice 1/2/3/4/5/6:'))
        if choice==1:
            print('Pata Dak 90(Airtel-Airtel),Dak 10(Mitandao yote) na SMS 25@Sh 500.Nunua Kupitia.')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice=int(input('Enter your choice 1/2:'))
            if choice==1:
                print('Umepokea Dak 90(Airtel-Airtel),Dak 10(Mitandao yote) na SMS 25')
            elif choice==2:
                num=int(input('Ingiza namba ya siri:'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                print('Invalid Request')
        elif choice==2:
            print('Pata Dak 60(Mitandao yote) na SMS 25@Saa 24@Sh 500.Nunua Kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice=int(input('Enter your choice 1/2:'))
            if choice==1:
                print('Umepokea Dak Dak 60(Mitandao yote) na SMS 25')
            elif choice==2:
                num=int(input('Ingiza namba ya siri:'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice==3:
            print('Pata Dak 130(Mitandao yote) na SMS 300@Siku 7@Sh 1000.Nunua Kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice=int(input('Enter your choice 1/2:'))
            if choice==1:
                print('Umepokea Dak Dak 130(Mitandao yote) na SMS 300')
            elif choice==2:
                num=int(input('Ingiza namba ya siri:'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice==4:
            print('Pata Dak 260(Airtel-Airtel),Dak 40(Mitandao yote) na SMS 30@Siku 7@Sh 1000.Nunua Kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice=int(input('Enter your choice 1/2:'))
            if choice==1:
                print('Umepokea Dak 260(Airtel-Airtel),Dak Dak 400(Mitandao yote) na SMS 30')
            elif choice==2:
                num=int(input('Ingiza namba ya siri:'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice==5:
                print('Pata Dak 40(Mitandao yote),MB 350@ na SMS 10@Siku 7@Sh 1000.Nunua Kupitia')
                print('1.Muda wa Maongezi')
                print('2.Airtel Money')
                choice=int(input('Enter your choice 1/2:'))
                if choice==1:
                    print('Umepokea Dak 400(Mitandao yote),MB 350 na SMS 30')
                elif choice==2:
                    num=int(input('Ingiza namba ya siri:'))
                    print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                else:
                    print('Invalid Request')
        elif choice==6:
                print('1.Sh 1500=Dak 70+MB 500 Siku 7')
                print('2.Sh 1500=Dak 10+MB 700 Siku 7')
                print('3.Sh 2000=Dak 55+MB 800 Siku 7')
                print('4.Sh 2100=GB 1 Siku 7')
                choice=int(input('Enter your choice 1/2/3/4:'))
                if choice==1:
                    print('Pata MB 500+Dak 70@Siku 7.Nunua kupitia')
                    print('1.Muda wa Maongezi')
                    print('2.Airtel Money')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice==1:
                        print('Umepokea Dak 70(Mitandao yote) na MB 500')
                    elif choice == 2:
                        num=int('Ingiza namba ya siri:')
                        print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                    else:
                        print('Invalid Request')
                elif choice==2:
                    print('Pata MB 700+Dak 10(Mitandao yote)@Siku 7@Sh 1500.Nunua kupitia')
                    print('1.Muda wa Maongezi')
                    print('2.Airtel Money')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice==1:
                        print('Umepokea Dak 10(Mitandao yote) na MB 700')
                    elif choice == 2:
                        num=int(input('Ingiza namba ya siri:'))
                        print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                    else:
                        print('Invalid Request')
                elif choice==3:
                    print('Pata MB 800+Dak 55(Mitandao yote)@Siku 7@Sh 2000.Nunua kupitia')
                    print('1.Muda wa Maongezi')
                    print('2.Airtel Money')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('Umepokea Dak 55(Mitandao yote) na MB 800')
                    elif choice == 2:
                        num = int('Ingiza namba ya siri:')
                        print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                    else:
                        print('Invalid Request')
                elif choice==4:
                    print('Pata GB 1@Siku 7@Sh 2100.Nunua kupitia')
                    print('1.Muda wa Maongezi')
                    print('2.Airtel Money')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('Umepokea GB 1@Siku 7')
                    elif choice == 2:
                        num = int(input('Ingiza namba ya siri:'))
                        print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                    else:
                        print('Invalid Request')
    elif choice==2:
        print('1.Sh 500=MB 245 Saa 24')
        print('2.Sh 1000=MB 490 Siku 7')
        print('3.Sh 1500=MB 700+Dak 10 Siku 7')
        print('4.Sh 2000=MB 985 Siku')
        print('5.Sh 2100=GB 1 Siku 7')
        print('6.Sh 3000=GB 1.4 Siku 14')
        choice=int(input('Enter your choice 1/2/3/4/5/6:'))
        if choice==1:
            print('Pata MB 245@Saa 24@Sh 500.Nunua Kupitia.')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea MB 245@Saa 24@Sh 500')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice==2:
            print('Pata MB 490@Siku 7@Sh 1000.Nunua Kupitia.')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea MB 490@Siku 7@Sh 1000')
            elif choice == 2:
                num = int('Ingiza namba ya siri')
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice==3:
            print('Pata MB 700,Dak 10(Mitandao yote) na SMS 10@Siku 7@Sh 1500.Nunua Kupitia.')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea MB 700,Dak 10(Mitandao yote) na SMS 10@Siku 7@Sh 1500')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri:'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice==4:
            print('Pata MB 985@Siku 3@Sh 2000.Nunua Kupitia.')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea MB 985@Siku 3@Sh 2000.')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice==5:
            print('Pata GB 1@Siku 7@Sh 2100.Nunua kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea GB 1@Siku 7')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice==6:
            print('Pata GB 1.4@Siku 14@Sh 3000.Nunua kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea GB 1.4@Siku 14@Sh 3000')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
    elif choice==3:
        print('Chagua Bando')
        print('1.Sh 200=SMS 200 Saa 24')
        print('2.Sh 500=SMS 1000 Siku 7')
        print('3.Sh 1000=SMS 10000 Siku 30')
        print('4.Mnunulie Rafiki')
        print('5.Salio')
        choice=int(input('Enter your choice 1/2/3/4/5:'))
        if choice==1:
            print('Pata SMS 200@Saa 24.Nunua Kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea SMS 200@Saa 24@Sh 200')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice==2:
            print('Pata SMS 1000@Siku 7.Nunua Kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea SMS 1000@Siku 7@Sh 500')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice==3:
            print('Pata SMS 10000@Siku 30.Nunua Kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea SMS 10000@Siku 30@Sh 1000')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice==4:
            print('Andika Namba ya Simu ya unayemnunulia kifurushi')
            num=int(input('Enter the number:'))
            print('Umefanikiwa kumnunulia kifurushi mteja mwenye namba [num]')
        elif choice==5:
            print('1.Salio:Tshs 0')
            print('2.DENI:Tshs 0')
    elif choice==4:
        print('Selection operation:')
        print('0.Lipa Mkopo')
        print('1.Kopa Salio')
        print('2.OFA Yako')
        print('3.SMS')
        print('4.Mitandao Yote')
        print('5.Airtel-Airtel')
        print('6.Internet')
        print('7.Angalia Salio')
        print('8.Masharti')
        print('9.English')
        choice=int(input('Enter your choice 0/1/2/3/4/5/6/7/8/9:'))
        if choice==0:
            print('Mpendwa Mteja Umefanikiwa Kulipa Deni lako ulilokuwa unadaiwa.')
            print('Sasa unaweza kutumia huduma zetu popote ulipo.')
        elif choice==1:
            print('1.Kopa Sh 2000')
            print('2.Kopa Sh 1500')
            print('3.Kopa Sh 1000')
            print('4.Kopa Sh 500')
            print('5.Kopa Sh 200')
            print('6.Kopa Sh 100')
            choice=int(input('Enter your choice 1/2/3/4/5/6: '))
            if choice==1:
                print('Ndugu Mteja umepatiwa salio la Sh 2000.Utakatwa Sh 2300 Pindi utakapoongeza salio')
            elif choice==2:
                print('Ndugu Mteja umepatiwa salio la Sh 1500.Utakatwa Sh 1725 Pindi utakapoongeza salio')
            elif choice==3:
                print('Ndugu Mteja umepatiwa salio la Sh 1000.Utakatwa Sh 1150 Pindi utakapoongeza salio')
            elif choice==4:
                print('Ndugu Mteja umepatiwa salio la Sh 500.Utakatwa Sh 575 Pindi utakapoongeza salio')
            elif choice==5:
                print('Ndugu Mteja umepatiwa salio la Sh 200.Utakatwa Sh 230 Pindi utakapoongeza salio')
            elif choice==6:
                print('Ndugu Mteja umepatiwa salio la Sh 100.Utakatwa Sh 115 Pindi utakapoongeza salio')
            else:
                print('Invalid Request')
        elif choice==2:
            print('Kopa Ofa yako')
            print('1.UNI Ofa')
            print('2.Data Zaidi-Mpya')
            choice=int(input('Enter your choice 1/2: '))
            if choice==1:
                print('Kopa Ofa yako:UNI Ofa')
                print('1.Sh 2000=Dk 55+MB 800 Siku 7')
                print('2.Sh 1500=Dk 70+MB 500 Siku 7')
                print('3.Sh 1500=Dk 10+MB 700 Siku 7')
                print('4.Sh 1000=Dk 300 Siku 7')
                print('5.Sh 1000=Dk 130 Siku 7')
                print('6.Sh 1000=Dk 40+MB 350 Siku 7')
                print('7.Sh 500=Dk 60 Saa 24')
                choice=int(input('Enter your choice 1/2/3/4/5/6/7: '))
                if choice==1:
                    print('Pata Dk 55 & MB 800@Sh 2000 Siku 7')
                    print('Utakatwa Sh 2300 pindi utakapoongeza salio')
                elif choice==2:
                    print('Pata Dk 70 & MB 500@Sh 1500 Siku 7')
                    print('Utakatwa Sh 1775 pindi utakapoongeza salio')
                elif choice==3:
                    print('Pata Dk 10 & MB 700@Sh 1500 Siku 7')
                    print('Utakatwa Sh 1775 pindi utakapoongeza salio')
                elif choice==4:
                    print('Pata Dk 300@Sh 1000 Siku 7')
                    print('Utakatwa Sh 1150 pindi utakapoongeza salio')
                elif choice==5:
                    print('Pata Dk 130@Sh 1000 Siku 7')
                    print('Utakatwa Sh 1150 pindi utakapoongeza salio')
                elif choice==6:
                    print('Pata Dk 40+MB 350@Sh 1000 Siku 7')
                    print('Utakatwa Sh 1150 pindi utakapoongeza salio')
                elif choice==7:
                    print('Pata Dk 60@Sh 500 Saa 24')
                    print('Utakatwa Sh 615 pindi utakapoongeza salio')
                else:
                    print('Invalid Request')
elif choice==2:
    print('Chagua Bando')
    print('1.Sh 200=SMS 200 Saa 24')
    print('2.Sh 500=SMS 1000 Siku 7')
    print('3.Sh 1000=SMS 10000 Siku 30')
    print('4.Mnunulie Rafiki')
    print('5.Salio')
    choice = int(input('Enter your choice 1/2/3/4/5:'))
    if choice == 1:
        print('Pata SMS 200@Saa 24.Nunua Kupitia')
        print('1.Muda wa Maongezi')
        print('2.Airtel Money')
        choice = int(input('Enter your choice 1/2:'))
        if choice == 1:
            print('Umepokea SMS 200@Saa 24@Sh 200')
        elif choice == 2:
            num = int(input('Ingiza namba ya siri'))
            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
        else:
            print('Invalid Request')
    elif choice == 2:
        print('Pata SMS 1000@Siku 7.Nunua Kupitia')
        print('1.Muda wa Maongezi')
        print('2.Airtel Money')
        choice = int(input('Enter your choice 1/2:'))
        if choice == 1:
            print('Umepokea SMS 1000@Siku 7@Sh 500')
        elif choice == 2:
            num = int(input('Ingiza namba ya siri'))
            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
        else:
            print('Invalid Request')
    elif choice == 3:
        print('Pata SMS 10000@Siku 30.Nunua Kupitia')
        print('1.Muda wa Maongezi')
        print('2.Airtel Money')
        choice = int(input('Enter your choice 1/2:'))
        if choice == 1:
            print('Umepokea SMS 10000@Siku 30@Sh 1000')
        elif choice == 2:
            num = int(input('Ingiza namba ya siri'))
            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
        else:
            print('Invalid Request')
    elif choice == 4:
        print('Andika Namba ya Simu ya unayemnunulia kifurushi')
        num = int(input('Enter the number:'))
        print('Umefanikiwa kumnunulia kifurushi mteja mwenye namba [num]')
    elif choice == 5:
        print('1.Salio:Tshs 0')
        print('2.DENI:Tshs 0')
elif choice==3:
    print('1.Sh 500=Dak 30 Saa 24')
    print('2.Sh 1000=Dak 150 Siku 2')
    print('3.Sh 1500=Dak 150 Siku 7')
    print('4.Wiki')
    print('5.Mwezi')
    print('6.Mnunulie Rafiki')
    print('7.Salio')
    choice=int(input('Enter your choice 1/2/3/4/5/6/7: '))
    if choice==1:
        print('Pata Dk 30 Kwa Sh 500 saa 24.Nunua kupitia.')
        print('1.Airtime')
        print('2.Airtel Money')
        choice=int(input('Enter your choice 1/2: '))
        if choice==1:
            print('Umepokea Dk 30@Sh 500@Saa 24')
        elif choice==2:
            num=int(input('Enter your serial number: '))
            print('Subiri kidogo tukuhudumie.')
    elif choice==2:
        print('Pata Dk 150 Kwa Sh 1000 siku 2.Nunua kupitia.')
        print('1.Airtime')
        print('2.Airtel Money')
        choice = int(input('Enter your choice 1/2: '))
        if choice == 1:
            print('Umepokea Dk 150@Sh 1000@Siku 2')
        elif choice == 2:
            num = int(input('Enter your serial number: '))
            print('Subiri kidogo tukuhudumie.')
    elif choice==3:
        print('Pata Dk 150 Kwa Sh 1500 siku 7.Nunua kupitia.')
        print('1.Airtime')
        print('2.Airtel Money')
        choice = int(input('Enter your choice 1/2: '))
        if choice == 1:
            print('Umepokea Dk 150@Sh 1500@Siku 7')
        elif choice == 2:
            num = int(input('Enter your serial number: '))
            print('Subiri kidogo tukuhudumie.')
    elif choice==4:
        print('1.Tsh 1500=Dk 150 Siku 7')
        print('2.Tsh 2500=Dk 300 Siku 7')
        print('3.Tsh 5000=Dk 400 Siku 30')
        choice=int(input('Enter your choice 1/2/3: '))
        if choice==1:
            print('Pata Dk 150 Kwa Sh 1500 siku 7.Nunua kupitia.')
            print('1.Airtime')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2: '))
            if choice == 1:
                print('Umepokea Dk 150@Sh 1500@Siku 7')
            elif choice == 2:
                num = int(input('Enter your serial number: '))
                print('Subiri kidogo tukuhudumie.')
        elif choice==2:
            print('Pata Dk 300 Kwa Sh 2500 siku 7.Nunua kupitia.')
            print('1.Airtime')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2: '))
            if choice == 1:
                print('Umepokea Dk 300@Sh 2500@Siku 7')
            elif choice == 2:
                num = int(input('Enter your serial number: '))
                print('Subiri kidogo tukuhudumie.')
        elif choice==3:
            print('Pata Dk 400 Kwa Sh 5000 siku 7.Nunua kupitia.')
            print('1.Airtime')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2: '))
            if choice == 1:
                print('Umepokea Dk 400@Sh 5000@Siku 7')
            elif choice == 2:
                num = int(input('Enter your serial number: '))
                print('Subiri kidogo tukuhudumie.')
        else:
            print('Invalid Request')
    elif choice==5:
        print('1.Tsh 5000=Dk 400 Siku 30')
        print('2.Tsh10000=Dk 1200 Siku 30')
        choice=int(input('Enter your choice 1/2: '))
        if choice==1:
            print('Pata Dk 400 Kwa Sh 5000 siku 30.Nunua kupitia.')
            print('1.Airtime')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2: '))
            if choice == 1:
                print('Umepokea Dk 400@Sh 5000@Siku 30')
            elif choice == 2:
                num = int(input('Enter your serial number: '))
                print('Subiri kidogo tukuhudumie.')
        elif choice==2:
            print('Pata Dk 1200 Kwa Sh 10000 siku 30.Nunua kupitia.')
            print('1.Airtime')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2: '))
            if choice == 1:
                print('Umepokea Dk 1200@Sh 10000@Siku 30')
            elif choice == 2:
                num = int(input('Enter your serial number: '))
                print('Subiri kidogo tukuhudumie.')
        else:
            print('Invalid Request')
    elif choice==6:
        print('Tafadhali Andika namba ya mteja unayemnunulia yatosha,ikianza na 0******')
        num=int(input('Enter your number: '))
        print('Ombi lako limefanikiwa.Endelea kutumia huduma zetu.')
    elif choice==7:
        print('Salio: 0.00')
        print('DENI: Tsh 0.00')
    else:
        print('Oops Invalid Request')
elif choice==4:
    print('1.Sh 500=Dak 100 Saa 24')
    print('2.sh 1000=Dak 300 Siku 2')
    print('3.Sh 1500=Dak 300 Siku 7')
    print('4.Sh 5000=Dak 1200 Siku 30')
    print('5.Mnunulie Rafiki')
    choice=int(input('Enter your choice 1/2/3/4/5: '))
    if choice==1:
        print('Pata Dk 100 Kwa Sh 500 saa 24.Nunua kupitia.')
        print('1.Airtime')
        print('2.Airtel Money')
        choice = int(input('Enter your choice 1/2: '))
        if choice == 1:
            print('Umepokea Dk 100@Sh 500@Saa 24')
        elif choice == 2:
            num = int(input('Enter your serial number: '))
            print('Subiri kidogo tukuhudumie.')
        else:
            print('Invalid Request')
    elif choice==2:
        print('Pata Dk 300 Kwa Sh 1000 siku 2.Nunua kupitia.')
        print('1.Airtime')
        print('2.Airtel Money')
        choice = int(input('Enter your choice 1/2: '))
        if choice == 1:
            print('Umepokea Dk 300@Sh 1000@Siku 2')
        elif choice == 2:
            num = int(input('Enter your serial number: '))
            print('Subiri kidogo tukuhudumie.')
        else:
            print('Invalid Request')
    elif choice==3:
        print('Pata Dk 300 Kwa Sh 1500 siku 7.Nunua kupitia.')
        print('1.Airtime')
        print('2.Airtel Money')
        choice = int(input('Enter your choice 1/2: '))
        if choice == 1:
            print('Umepokea Dk 300@Sh 1500@Siku 7')
        elif choice == 2:
            num = int(input('Enter your serial number: '))
            print('Subiri kidogo tukuhudumie.')
        else:
            print('Invalid Request')
    elif choice==4:
        print('Pata Dk 1200 Kwa Sh 5000 siku 30.Nunua kupitia.')
        print('1.Airtime')
        print('2.Airtel Money')
        choice = int(input('Enter your choice 1/2: '))
        if choice == 1:
            print('Umepokea Dk 1200@Sh 5000@Siku 30')
        elif choice == 2:
            num = int(input('Enter your serial number: '))
            print('Subiri kidogo tukuhudumie.')
        else:
            print('Invalid Request')
    elif choice==5:
        print('Tafadhali Andika namba ya mteja unayemnunulia yatosha,ikianza na 0******')
        num = int(input('Enter your number: '))
        print('Ombi lako limefanikiwa.Endelea kutumia huduma zetu.')
    else:
        print('Invalid Request')
elif choice==5:
    print('0.Mpangilio wa Internet')
    print('1.OFA Yako/SMATIKA')
    print('2.Boresha Laini')
    print('3.Siku')
    print('4.Wiki')
    print('5.Mwezi')
    print('6.Bando za MIFI')
    print('7.Mnunulie Rafiki')
    print('8.Rusha MB')
    print('9.Peruzi kwa Muda wa Maongezi')
    choice=int(input('Enter your choice 0/1/2/3/4/5/6/7/8/9: '))
    if choice==0:
        print('Ombi lako linashughulikiwa utapokea mpangilio wa Internet hivi punde.............')
    elif choice == 1:
        print('1.Sh 500=MB 245 Saa 24')
        print('2.Sh 1000=MB 490 Siku 7')
        print('3.Sh 1500=MB 700+Dak 10 Siku 7')
        print('4.Sh 2000=MB 985 Siku 7')
        print('5.Sh 2100=GB 1 Siku 7')
        print('6.Sh 3000=GB 1.4 Siku 14')
        choice = int(input('Enter your choice 1/2/3/4/5/6:'))
        if choice == 1:
            print('Pata MB 245@Saa 24@Sh 500.Nunua Kupitia.')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea MB 245@Saa 24@Sh 500')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice == 2:
            print('Pata MB 490@Siku 7@Sh 1000.Nunua Kupitia.')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea MB 490@Siku 7@Sh 1000')
            elif choice == 2:
                num = int('Ingiza namba ya siri')
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice == 3:
            print('Pata MB 700,Dak 10(Mitandao yote) na SMS 10@Siku 7@Sh 1500.Nunua Kupitia.')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea MB 700,Dak 10(Mitandao yote) na SMS 10@Siku 7@Sh 1500')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri:'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice == 4:
            print('Pata MB 985@Siku 7@Sh 2000.Nunua Kupitia.')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea MB 985@Siku 3@Sh 2000.')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice == 5:
            print('Pata GB 1@Siku 7@Sh 2100.Nunua kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea GB 1@Siku 7')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice == 6:
            print('Pata GB 1.4@Siku 14@Sh 3000.Nunua kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea GB 1.4@Siku 14@Sh 3000')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
    elif choice==2:
        print('1.4G Capability Check')
        print('WELCOME! Your device and SIM Card are 4G capable.Dial *149*99# select 5 SMATIKA Yatosha Internet to subscribe and Enjoy the fastest Internet speed')
    elif choice==3:
        print('1.Sh 500=MB 245 Saa 24')
        print('2.Sh 1000=MB 490 Siku 7')
        print('3.Sh 1500=MB 700+Dak 10 Siku 7')
        print('4.Sh 2000=MB 950 Siku 7')
        print('5.Sh 2100=GB 1 Siku 7')
        print('6.Sh 3000=GB 1.4 Siku 14')
        choice = int(input('Enter your choice 1/2/3/4/5/6:'))
        if choice == 1:
            print('Pata MB 245@Saa 24@Sh 500.Nunua Kupitia.')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea MB 245@Saa 24@Sh 500')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice == 2:
            print('Pata MB 490@Siku 7@Sh 1000.Nunua Kupitia.')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea MB 490@Siku 7@Sh 1000')
            elif choice == 2:
                num = int('Ingiza namba ya siri')
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice == 3:
            print('Pata MB 700,Dak 10(Mitandao yote) na SMS 10@Siku 7@Sh 1500.Nunua Kupitia.')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea MB 700,Dak 10(Mitandao yote) na SMS 10@Siku 7@Sh 1500')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri:'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice == 4:
            print('Pata MB 950@Siku 7@Sh 2000.Nunua Kupitia.')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea MB 950@Siku 3@Sh 2000.')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice == 5:
            print('Pata GB 1@Siku 7@Sh 2100.Nunua kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea GB 1@Siku 7')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice == 6:
            print('Pata GB 1.4@Siku 14@Sh 3000.Nunua kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea GB 1.4@Siku 14@Sh 3000')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
    elif choice==4:
        print('1.Tsh 2000=MB 950 Siku 7')
        print('2.Tsh 2100=GB 1 Siku 7')
        print('3.Tsh 3000=GB 1.4 Siku 7')
        print('4.Tsh 5000=GB 2.4 Siku 7')
        print('5.Tsh 20000=GB 9.5 Siku 30')
        choice=int(input('Enter your choice 1/2/3/4/5: '))
        if choice==1:
            print('Pata MB 950@Siku 7@Sh 2000.Nunua Kupitia.')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea MB 950@Siku 3@Sh 2000.')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice==2:
            print('Pata GB 1@Siku 7@Sh 2100.Nunua kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea GB 1@Siku 7')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice==3:
            print('Pata GB 1.4@Siku 7@Sh 3000.Nunua kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea GB 1.4@Siku 7@Sh 3000')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice==4:
            print('Pata GB 2.4@Siku 7@Sh 5000.Nunua kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea GB 2.4@Siku 7@Sh 3000')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice==5:
            print('Pata GB 9.5@Siku 30@Sh 20000.Nunua kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea GB 9.5@Siku 30@Sh 20000')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        else:
            print('Invalid Choice')
    elif choice==5:
        print('1.Tsh 10000=GB 4.5 Siku 30')
        print('2.Tsh 20000=GB 9.5 Siku 30')
        print('3.Tsh 30000=GB 14.4 Siku 30')
        print('4.Tsh 50000=GB 24 Siku 60')
        print('5.Tsh 100000=GB 48 Siku 60')
        choice=int(input('Enter your choice 1/2/3/4/5: '))
        if choice==1:
            print('Pata GB 4.5@Siku 30@Sh 10000.Nunua kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea GB 4.5@Siku 30@Sh 10000')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice==2:
            print('Pata GB 9.5@Siku 30@Sh 20000.Nunua kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea GB 9.5@Siku 30@Sh 20000')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice==3:
            print('Pata GB 14.4@Siku 30@Sh 30000.Nunua kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea GB 14.4@Siku 30@Sh 30000')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice==4:
            print('Pata GB 24@Siku 60@Sh 50000.Nunua kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea GB 24@Siku 60@Sh 50000')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice==5:
            print('Pata GB 48@Siku 60@Sh 100000.Nunua kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea GB 48@Siku 60@Sh 100000')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        else:
            print('Invalid Request')
    elif choice==6:
        print('1.Tsh 2000=MB 985 Siku 3')
        print('2.Tsh 3000=GB 1.4 Siku 7')
        print('3.Tsh 5000=GB 2.4 Siku 7')
        print('4.Tsh 10000=GB 4.5 Siku 30')
        print('5.Tsh 20000=GB 9.5 Siku 30')
        print('6.Tsh 30000=GB 14.4 Siku 30')
        print('7.Tsh 50000=GB 24 Siku 60')
        print('8.Tsh 100000=GB 48 Siku 60')
        choice=int(input('Enter your choice 1/2/3/4/5/6/7/8: '))
        if choice==1:
            print('Pata MB 985@Siku 3@Sh 2000.Nunua kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea MB 985@Siku 3@Sh 2000')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice==2:
            print('Pata GB 1.4@Siku 7@Sh 3000.Nunua kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea GB 1.4@Siku 7@Sh 3000')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice==3:
            print('Pata GB 2.4@Siku 7@Sh 5000.Nunua kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea GB 2.4@Siku 7@Sh 5000')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice==4:
            print('Pata GB 4.5@Siku 30@Sh 10000.Nunua kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea GB 4.5@Siku 30@Sh 10000')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice==5:
            print('Pata GB 9.5@Siku 30@Sh 20000.Nunua kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea GB 9.5@Siku 30@Sh 20000')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice==6:
            print('Pata GB 14.4@Siku 30@Sh 30000.Nunua kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea GB 14.4@Siku 30@Sh 30000')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice==7:
            print('Pata GB 24@Siku 60@Sh 50000.Nunua kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea GB 24@Siku 60@Sh 50000')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        elif choice==8:
            print('Pata GB 48@Siku 60@Sh 100000.Nunua kupitia')
            print('1.Muda wa Maongezi')
            print('2.Airtel Money')
            choice = int(input('Enter your choice 1/2:'))
            if choice == 1:
                print('Umepokea GB 48@Siku 60@Sh 100000')
            elif choice == 2:
                num = int(input('Ingiza namba ya siri'))
                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
            else:
                print('Invalid Request')
        else:
            print('Invalid Request')
    elif choice==7:
        print('Tafadhali Andika namba ya mteja unayemnunulia yatosha,ikianza na 0******')
        num = int(input('Enter your number: '))
        print('Ombi lako limefanikiwa.Endelea kutumia huduma zetu.')
    elif choice==8:
        print('Tafadhali Andika namba ya mteja unayemnunulia Data,ikianza na 0******')
        num = int(input('Enter your number: '))
        print('Ombi lako limefanikiwa.Endelea kutumia huduma zetu.')
    elif choice==9:
        print('Umechagua kuperuzi kwa kutumia muda wa maongezi.Kusitisha piga *149*99# kisha chagua 5 Internet kisha chagua 10')
    else:
        print('Invalid Request')
elif choice==6:
    print('1.Sh 1000=Dak 40+MB 350 Saa 24')
    print('2.Sh 2000=Dak 55+MB 800 Siku 7')
    print('3.Sh 10000=Dak 400+GB 3.5 Siku 30')
    print('4.Sh 20000=Dak 500+GB 8 Siku 30')
    print('5.Mnunulie Rafiki')
    choice=int(input('Enter your choice 1/2/3/4/5: '))
    if choice==1:
        print('Pata Dak 40 & MB 350.Nunua Kupitia')
        print('1.Muda wa Maongezi')
        print('2.Airtel Money')
        choice = int(input('Enter your choice 1/2:'))
        if choice == 1:
            print('Umepokea Dak 40 & MB 350@Sh 1000@Saa 24')
        elif choice == 2:
            num = int(input('Ingiza namba ya siri'))
            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
        else:
            print('Invalid Request')
    elif choice==2:
        print('Pata Dak 55 & MB 800.Nunua Kupitia')
        print('1.Muda wa Maongezi')
        print('2.Airtel Money')
        choice = int(input('Enter your choice 1/2:'))
        if choice == 1:
            print('Umepokea Dak 55 & MB 800@Sh 2000@siku 7')
        elif choice == 2:
            num = int(input('Ingiza namba ya siri'))
            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
        else:
            print('Invalid Request')
    elif choice==3:
        print('Pata Dak 400 & GB 3.5.Nunua Kupitia')
        print('1.Muda wa Maongezi')
        print('2.Airtel Money')
        choice = int(input('Enter your choice 1/2:'))
        if choice == 1:
            print('Umepokea Dak 400 & GB 3.5@Sh 10000@Siku 30')
        elif choice == 2:
            num = int(input('Ingiza namba ya siri'))
            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
        else:
            print('Invalid Request')
    elif choice==4:
        print('Pata Dak 500 & GB 8.Nunua Kupitia')
        print('1.Muda wa Maongezi')
        print('2.Airtel Money')
        choice = int(input('Enter your choice 1/2:'))
        if choice == 1:
            print('Umepokea Dak 500 & GB 8@Sh 10000@Siku 30')
        elif choice == 2:
            num = int(input('Ingiza namba ya siri'))
            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
        else:
            print('Invalid Request')
    elif choice==5:
        print('Tafadhali Andika namba ya mteja unayemnunulia kifurushi kisicho na mwisho wa matumizi,ikianza na 0***')
        num=int(input('Enter the number: '))
        print('Ndugu mteja umeafanikiwa kumnunulia kifurushi rafiki yako.')
    else:
        print('Invalid Request')
elif choice==7:
    print('1.Nunua Bando')
    print('2.Salio la Bando')
    choice=int(input('Enter your choice 1/2: '))
    if choice==1:
        print('Andika namba ya HBB unayonunulia kifurushi cha Internet ikianza na 0***')
        num=int(input('Enter the number: '))
        print('Ndugu mteja ombi lako linashuhulikiwa.')
    elif choice==2:
        print('Weka namba ya simu unayotaka kuangalia salio ikianza na 0***')
        num=int(input('Enter the number: '))
        print('Salio: 0.00')
elif choice==8:
    print('Vifurushi Visivyo na Mwisho wa Muda wa Matumizi')
    print('1.sh 1000=Dak 30+SMS 50+MB 10')
    print('2.Sh 2000=Dak 20+MB 900')
    print('3.Mnunulie Rafiki')
    choice=int(input('Enter your choice 1/2/3: '))
    if choice==1:
        print('Pata Dak 30,MB 10 & SMS 50.Nunua Kupitia')
        print('1.Muda wa Maongezi')
        print('2.Airtel Money')
        choice = int(input('Enter your choice 1/2:'))
        if choice == 1:
            print('Umepokea Dak 30,MB 10 & SMS 50@Sh 1000')
        elif choice == 2:
            num = int(input('Ingiza namba ya siri'))
            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
        else:
            print('Invalid Request')
    elif choice==2:
        print('Pata Dak 20,MB 900.Nunua Kupitia')
        print('1.Muda wa Maongezi')
        print('2.Airtel Money')
        choice = int(input('Enter your choice 1/2:'))
        if choice == 1:
            print('Umepokea Dak 20,MB 90@Sh 2000')
        elif choice == 2:
            num = int(input('Ingiza namba ya siri'))
            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
        else:
            print('Invalid Request')
    elif choice==3:
        print('Tafadhali Andika namba ya mteja unayemnunulia kifurushi kisicho na mwisho wa matumizi,ikianza na 0***')
        num=int(input('Enter the number: '))
        print('Ndugu mteja umeafanikiwa kumnunulia kifurushi rafiki yako.')
elif choice==9:
    print('1.Kuzuru(Roaming)')
    print('2.Kimataifa')
    choice=int(input('Enter your choice 1/2:'))
    if choice==1:
        print('1.Wezesha/Sitisha kuzuru')
        print('2.Safari Bando-Kuzuru(Roaming)')
        choice=int(input('Enter your choice 1/2:'))
        if choice==1:
            print('1.Wezesha Roaming')
            print('2.Sitisha Roaming')
            print('3.Taarifa')
            choice=int(input('Enter your choice 1/2/3:'))
            if choice==1:
                print('Mpendwa Mteja umekwisha wezesha huduma ya kuzuru(Roaming).Endelea kufurahia huduma ya vifurushi vya kuzuru Internet kutoka Airtel.')
            elif choice==2:
                print('Habari Umesitisha huduma za kutumia mtandao wa nchi nyingine,kuwezesha,Piga *149*99#>Kuzuru(Roaming)>Wezesha Kuzuru au piga +255784105400 ukiwa nje ya nchi.')
            elif choice==3:
                print('Huduma hii inakuwezesha kusitisha kuzuru(Roaming) kwa kutounganishwa na mitandao mingine isipokuwa Airtel Tanzania.')
            else:
                print('Invalid Request')
        elif choice==2:
            print('CHAGUA KIFURUSHI')
            print('1.Bando za One Airtel')
            print('2.Bando Nje ya Airtel')
            print('3.Bando za Internet 1 Nje ya Airtel')
            print('4.Bando za Internet 2 Nje ya Airtel')
            choice=int(input('Enter your choice 1/2/3/4:'))
            if choice==1:
                print('CHAGUA KIFURUSHI')
                print('1.Siku/Siku 3')
                print('2.Wiki')
                print('3.Siku 14')
                print('4.Nchi za One Airtel')
                print('5.Salio')
                choice=int(input('Enter your choice 1/2/3/4/5:'))
                if choice==1:
                    print('1.5000Tsh=500MB Siku 1')
                    print('2.10000Tsh=1229MB Siku 3')
                    print('3.10000Tsh=10Dak+75MB Siku 3')
                    choice=int(input('Enter your choice 1/2/3:'))
                    if choice==1:
                        print('Pata 500MB za Internet kwa Sh 5000 kwa Siku 1.Nunua kupitia.')
                        print('1.Muda wa Maongezi')
                        print('2.Airtel Money')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('Umepokea MB 500@Sh 5000@Siku 1.')
                        elif choice == 2:
                            num = int(input('Ingiza namba ya siri'))
                            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                        else:
                            print('Invalid Request')
                    elif choice==2:
                        print('Pata 1229MB za Internet kwa Sh 10000 kwa Siku 3.Nunua kupitia.')
                        print('1.Muda wa Maongezi')
                        print('2.Airtel Money')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('Umepokea MB 1229@Sh 10000@Siku 3.')
                        elif choice == 2:
                            num = int(input('Ingiza namba ya siri'))
                            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                        else:
                            print('Invalid Request')
                    elif choice==3:
                        print('Pata Dak 10@75MB za Internet kwa Sh 10000 kwa Siku 3.Nunua kupitia.')
                        print('1.Muda wa Maongezi')
                        print('2.Airtel Money')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('Umepokea MB 75@Dak 10@Sh 10000@Siku 3.')
                        elif choice == 2:
                            num = int(input('Ingiza namba ya siri'))
                            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                        else:
                            print('Invalid Request')
                elif choice==2:
                    print('1.15000Tsh=2GB Siku 7')
                    print('2.25000Tsh=25Dak+250MB Siku 7')
                    choice=int(input('Enter your choice 1/2:'))
                    if choice==1:
                        print('Pata 2GB za Internet kwa Sh 15000 kwa Siku 7.Nunua kupitia.')
                        print('1.Muda wa Maongezi')
                        print('2.Airtel Money')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('Umepokea 2GB@Sh 15000@Siku 7.')
                        elif choice == 2:
                            num = int(input('Ingiza namba ya siri:'))
                            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                        else:
                            print('Invalid Request')
                    elif choice==2:
                        print('Pata Dak 25+250MB za Internet kwa Sh 25000 kwa Siku 7.Nunua kupitia.')
                        print('1.Muda wa Maongezi')
                        print('2.Airtel Money')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('Umepokea 250MB na Dak 25@Sh 25000@Siku 7.')
                        elif choice == 2:
                            num = int(input('Ingiza namba ya siri:'))
                            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                        else:
                            print('Invalid Request')
                elif choice==3:
                    print('1.30000Tsh=5GB Siku 14')
                    print('2.40000Tsh=45Dak+500MB Siku 14')
                    choice=int(input('Enter your choice 1/2:'))
                    if choice==1:
                        print('Pata 5GB za Internet kwa Sh 30000 kwa Siku 14.Nunua kupitia.')
                        print('1.Muda wa Maongezi')
                        print('2.Airtel Money')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('Umepokea 5GB@Sh 30000@Siku 14.')
                        elif choice == 2:
                            num = int(input('Ingiza namba ya siri:'))
                            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                        else:
                            print('Invalid Request')
                    elif choice==2:
                        print('Pata Dak 45+500MB za Internet kwa Sh 40000 kwa Siku 14.Nunua kupitia.')
                        print('1.Muda wa Maongezi')
                        print('2.Airtel Money')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('Umepokea 45Dak na MB 500@Sh 40000@Siku 14.')
                        elif choice == 2:
                            num = int(input('Ingiza namba ya siri:'))
                            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                        else:
                            print('Invalid Request')
                elif choice==4:
                    print('Congo B,DRC,Gabon,Ghana,Kenya,Madagascar,Malawi,Niger,Nigeria,Rwanda,Seychelles,Chad,Uganda,Zambia,India na Mauritius')
                elif choice==5:
                    print('1.Salio:Tshs 0')
                    print('2.DENI:Tshs 0')
            elif choice==2:
                print('CHAGUA KIFURUSHI')
                print('1.Tsh 10000=10Dak Siku 7')
                print('2.Tsh 25000=Dak 12+250MB Siku 3')
                print('3.Tsh 50000=Dak 15+200MB Siku 7')
                print('4.Nchi Husika')
                print('5.Salio')
                choice=int(input('Enter your choice 1/2/3/4/5:'))
                if choice==1:
                    print('Pata Dak 10 kwa Tsh 10000 Siku 7.Nunua kupitia.')
                    print('1.Muda wa Maongezi')
                    print('2.Airtel Money')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('Umepokea Dak 10@Tsh 10000@Siku 7.')
                    elif choice == 2:
                        num = int(input('Ingiza namba ya siri:'))
                        print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                    else:
                        print('Invalid Request')
                elif choice==2:
                    print('Pata Dak 12+250MB za Internet kwa Sh 25000 kwa Siku 3.Nunua kupitia.')
                    print('1.Muda wa Maongezi')
                    print('2.Airtel Money')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('Umepokea 12Dak na MB 250@Sh 25000@Siku 3.')
                    elif choice == 2:
                        num = int(input('Ingiza namba ya siri:'))
                        print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                    else:
                        print('Invalid Request')
                elif choice==3:
                    print('Pata Dak 15+200MB za Internet kwa Sh 50000 kwa Siku 7.Nunua kupitia.')
                    print('1.Muda wa Maongezi')
                    print('2.Airtel Money')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('Umepokea 15Dak na MB 200@Sh 50000@Siku 7.')
                    elif choice == 2:
                        num = int(input('Ingiza namba ya siri:'))
                        print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                    else:
                        print('Invalid Request')
                elif choice==4:
                    print('1.AFRIKA')
                    print('2.MAREKANI & CANADA')
                    print('3.ULAYA')
                    print('4.MASHARIKI YA KATI & ASIA')
                    print('5.OCENIA')
                    choice=int(input('Enter your choice 1/2/3/4/5:'))
                    if choice==1:
                        print('Botswana,Congo B,Congo DRC,Egypt,Gabon,Ghana,Kenya,Madagascar,Malawi,Mauritius,Mozambique,Niger,Nigeria,Rwanda,South Africa,Swaziland,Chad,Uganda,Zambia')
                    elif choice==2:
                        print('Marekani na Canada')
                    elif choice==3:
                        print('Denmark,France,Germany,Greece,Italy,Netherlands,Norway,Romania,Russia,Spain,Sweden,UK')
                    elif choice==4:
                        print('China,Bangladesh,India,Israel,Oman,Pakistan,Qatar,Saudi Arabia,SriLanka,Turkey,UAE')
                    elif choice==5:
                        print('New Zealand')
                    else:
                        print('Invalid Request')
                elif choice==5:
                    print('1.Salio:Tshs 0')
                    print('2.DENI:Tshs 0')
                else:
                    print('Invalid Request')
            elif choice==3:
                print('1.40000Tsh=1GB Siku 3')
                print('2.75000=2GB Siku 7')
                print('3.200000=5GB Siku 14')
                print('4.Nchi Husika')
                choice=int(input('Enter your choice 1/2/3/4:'))
                if choice==1:
                    print('Pata GB 1 za Internet kwa Sh 40000 kwa Siku 3.Nunua kupitia.')
                    print('1.Muda wa Maongezi')
                    print('2.Airtel Money')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('Umepokea GB 1@Sh 40000@Siku 3.')
                    elif choice == 2:
                        num = int(input('Ingiza namba ya siri:'))
                        print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                    else:
                        print('Invalid Request')
                elif choice==2:
                    print('Pata GB 2 za Internet kwa Sh 75000 kwa Siku 7.Nunua kupitia.')
                    print('1.Muda wa Maongezi')
                    print('2.Airtel Money')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('Umepokea GB 2@Sh 75000@Siku 7.')
                    elif choice == 2:
                        num = int(input('Ingiza namba ya siri:'))
                        print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                    else:
                        print('Invalid Request')
                elif choice==3:
                    print('Pata GB 5 za Internet kwa Sh 200000 kwa Siku 14.Nunua kupitia.')
                    print('1.Muda wa Maongezi')
                    print('2.Airtel Money')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('Umepokea GB 5@Sh 200000@Siku 14.')
                    elif choice == 2:
                        num = int(input('Ingiza namba ya siri:'))
                        print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                    else:
                        print('Invalid Request')
                elif choice==4:
                    print('1.AFRIKA')
                    print('2.MAREKANI & CANADA')
                    print('3.ULAYA')
                    print('4.MASHARIKI YA KATI & ASIA')
                    print('5.OCENIA')
                    choice = int(input('Enter your choice 1/2/3/4/5:'))
                    if choice == 1:
                        print('Botswana(MTN),Cameroun(Orange),Egypt(Orange),Ghana(Airtel,TIGO),Mali(Orange),Mauritius(Emtel),Mozambique(Vodacom),Senegal(Orange),Swaziland(MTN),South Africa(MTN,Vodacom)')
                    elif choice == 2:
                        print('USA(T-Mobile) & Canada(Bell,Telus)')
                    elif choice == 3:
                        print('Belgium(Base,Orange),Switzerland(Swisscom),Denmark(Telenor,TDC),France(Orange,SFR),Germany(T-Mobile,Vodafone),Greece(Cosmote),Italy(Vodafone,Tim),Netherlands(Vodafone,KPN),Norway(Telenor),Romania(Vodafone,Orange),Russia(Vimplelcom),Spain(Vodafone,Telefonica),Sweden(Telenor),UK(Vodafone,Telefonica)')

                    elif choice == 4:
                        print('India(Airtel),Israel(Orange,Pelephone,Cellcom),Pakistan(Mobilink,Telenor),Qatar(Qtel),Saudi Arabia(Zain),SriLanka(Airtel),Turkey(Vodafone),UAE(Etisalat)')
                    elif choice == 5:
                        print('New Zealand(China Mobile)')
                    else:
                        print('Invalid Request')
            elif choice==4:
                print('1.35000Tsh=200MB Siku 3')
                print('2.90000Tsh=512MB Siku 7')
                print('3.175000Tsh=GB 1 Siku 14')
                print('4.Nchi Husika')
                choice=int(input('Enter your Choice 1/2/3/4:'))
                if choice==1:
                    print('Pata 200MB za Internet kwa Sh 35000 kwa Siku 3.Nunua kupitia.')
                    print('1.Muda wa Maongezi')
                    print('2.Airtel Money')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('Umepokea 200MB@Sh 35000@Siku 3.')
                    elif choice == 2:
                        num = int(input('Ingiza namba ya siri:'))
                        print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                    else:
                        print('Invalid Request')
                elif choice==2:
                    print('Pata 512MB za Internet kwa Sh 90000 kwa Siku 7.Nunua kupitia.')
                    print('1.Muda wa Maongezi')
                    print('2.Airtel Money')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('Umepokea 512MB@Sh 90000@Siku 3.')
                    elif choice == 2:
                        num = int(input('Ingiza namba ya siri:'))
                        print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                    else:
                        print('Invalid Request')
                elif choice==3:
                    print('Pata GB 1 za Internet kwa Sh 175000 kwa Siku 14.Nunua kupitia.')
                    print('1.Muda wa Maongezi')
                    print('2.Airtel Money')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('Umepokea GB 1@Sh 175000@Siku 14.')
                    elif choice == 2:
                        num = int(input('Ingiza namba ya siri:'))
                        print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                    else:
                        print('Invalid Request')
                elif choice==4:
                    print('1.AFRICA')
                    print('2.MAREKANI')
                    print('3.MASHARIKI YA KATI & ASIA')
                    choice=int(input('Enter your choice 1/2/3:'))
                    if choice==1:
                        print('South Africa(Cell C)')
                    elif choice==2:
                        print("AT & T")
                    elif choice==3:
                        print('Oman(OmanTel),UAE(dU),Turkey(Turkcel)')
                    else:
                        print('Invalid Request')
    elif choice==2:
        print('CHOOSE BUNDLES')
        print('1.International Bundles')
        print('2.Safari Roaming Bundles')
        choice=int(input('Enter your Choice 1/2:'))
        if choice==1:
            print('CHOOSE BUNDLES')
            print('1.Daily')
            print('2.Weekly')
            print('3.Monthly')
            choice=int(input('Enter your choice 1/2/3:'))
            if choice==1:
                print('CHOOSE BUNDLES')
                print('1.INDIA')
                print('2.CHINA')
                print('3.USA & CANADA')
                print("4.EAST AFRICA")
                print('5.SOUTHERN AFRICA')
                print('6.MIDDLE EAST')
                print('7.EUROPE')
                choice=int(input('Enter your choice 1/2/3/4/5/6/7:'))
                if choice==1:
                    print('1.Get 1200 Seconds for TZS 1000/= to call India')
                    print('2.Balance')
                    choice=int(input('Enter your choice 1/2:'))
                    if choice==1:
                        print('1.Airtime')
                        print('2.Airtel Money')
                        choice=int(input('Enter your choice 1/2:'))
                        if choice==1:
                            print('You  Rerceived 1200sec for TZS 1000/= to call for India')
                        elif choice==2:
                            num = int(input('Ingiza namba ya siri:'))
                            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                        else:
                            print('Invalid Request')
                    elif choice==2:
                        print('Dear customer your Balance is 1200sec')
                    else:
                        print('Invalid Request')
                elif choice==2:
                    print('1.Get 1200 Seconds for TZS 1000/= to call China')
                    print('2.Balance')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('1.Airtime')
                        print('2.Airtel Money')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('You  Rerceived 1200sec for TZS 1000/= to call for China')
                        elif choice==2:
                            num = int(input('Ingiza namba ya siri:'))
                            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                        else:
                            print('Invalid Request')
                    elif choice == 2:
                        print('Dear customer your Balance is 1200sec')
                    else:
                        print('Invalid Request')
                elif choice==3:
                    print('1.Get 1200 Seconds for TZS 1000/= to call USA & CANADA')
                    print('2.Balance')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('1.Airtime')
                        print('2.Airtel Money')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('You  Rerceived 1200sec for TZS 1000/= to call for USA & CANADA')
                        elif choice==2:
                            num = int(input('Ingiza namba ya siri:'))
                            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                        else:
                            print('Invalid Request')
                    elif choice == 2:
                        print('Dear customer your Balance is 1200sec')
                    else:
                        print('Invalid Request')
                elif choice==4:
                    print('1.Get 180 Seconds for TZS 2500/= to call Kenya,Uganda,Rwanda for 1 day')
                    print('2.Balance')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('1.Airtime')
                        print('2.Airtel Money')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('You  Rerceived 180sec for TZS 2500/= to call for Kenya,Uganda,Rwanda for 1 day  ')
                        elif choice==2:
                            num = int(input('Ingiza namba ya siri:'))
                            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                        else:
                            print('Invalid Request')
                    elif choice == 2:
                        print('Dear customer your Balance is 1200sec')
                    else:
                        print('Invalid Request')
                elif choice==5:
                    print('1.Get 300 Seconds for TZS 3000/= to call Africa Kusini for 1 day')
                    print('2.Balance')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('1.Airtime')
                        print('2.Airtel Money')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('You  Rerceived 300sec for TZS 3000/= to call for Africa Kusini for 1 day  ')
                        elif choice==2:
                            num = int(input('Ingiza namba ya siri:'))
                            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                        else:
                            print('Invalid Request')
                    elif choice == 2:
                        print('Dear customer your Balance is 1200sec')
                    else:
                        print('Invalid Request')
                elif choice==6:
                    print('1.OMAN')
                    print('2.UAE,Saudi Arabia,Yemen,Lebanon,Pakistan & Qatar')
                    choice=int(input('Enter your choice 1/2:'))
                    if choice==1:
                        print('1.Get 180 Seconds for TZS 2500/= to call Oman for 1 day')
                        print('2.Balance')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('1.Airtime')
                            print('2.Airtel Money')
                            choice = int(input('Enter your choice 1/2:'))
                            if choice == 1:
                                print('You  Rerceived 180sec for TZS 2500/= to call for Oman for 1 day  ')
                            elif choice==2:
                                num = int(input('Ingiza namba ya siri:'))
                                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                            else:
                                print('Invalid Request')
                        elif choice == 2:
                            print('Dear customer your Balance is 1200sec')
                        else:
                            print('Invalid Request')
                    elif choice==2:
                        print('1.Get 300 Seconds for TZS 2500/= to call UAE,Saudi Arabia,Yemen,Lebanon,Pakistan & Qatar for 1 day')
                        print('2.Balance')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('1.Airtime')
                            print('2.Airtel Money')
                            choice = int(input('Enter your choice 1/2:'))
                            if choice == 1:
                                print('You  Rerceived 300sec for TZS 2500/= to call for UAE,Saudi Arabia,Yemen,Lebanon,Pakistan & Qatar for 1 day  ')
                            elif choice==2:
                                num = int(input('Ingiza namba ya siri:'))
                                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                            else:
                                print('Invalid Request')
                        elif choice == 2:
                            print('Dear customer your Balance is 1200sec')
                        else:
                            print('Invalid Request')
                elif choice==7:
                    print('1.Get 240 Seconds for TZS 2500/= to call UK,Italy & Germany for 1 day')
                    print('2.Balance')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('1.Airtime')
                        print('2.Airtel Money')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print(
                                'You  Rerceived 240sec for TZS 2500/= to call for UK,Italy & Germany  for 1 day  ')
                        elif choice==2:
                            num = int(input('Ingiza namba ya siri:'))
                            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                        else:
                            print('Invalid Request')
                    elif choice == 2:
                        print('Dear customer your Balance is 1200sec')
                    else:
                        print('Invalid Request')
                else:
                    print('Invalid Request')
            elif choice==2:
                print('CHOOSE BUNDLES')
                print('1.INDIA')
                print('2.CHINA')
                print('3.USA & CANADA')
                print("4.EAST AFRICA")
                print('5.SOUTHERN AFRICA')
                print('6.MIDDLE EAST')
                print('7.EUROPE')
                choice=int(input('Enter your choice 1/2/3/4/5/6/7:'))
                if choice==1:
                    print('1.Get 6000 Seconds for TZS 5000/= to call India')
                    print('2.Balance')
                    choice=int(input('Enter your choice 1/2:'))
                    if choice==1:
                        print('1.Airtime')
                        print('2.Airtel Money')
                        choice=int(input('Enter your choice 1/2:'))
                        if choice==1:
                            print('You  Rerceived 6000sec for TZS 5000/= to call for India')
                        elif choice==2:
                            num = int(input('Ingiza namba ya siri:'))
                            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                        else:
                            print('Invalid Request')
                    elif choice==2:
                        print('Dear customer your Balance is 1200sec')
                    else:
                        print('Invalid Request')
                elif choice==2:
                    print('1.Get 6000 Seconds for TZS 5000/= to call China')
                    print('2.Balance')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('1.Airtime')
                        print('2.Airtel Money')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('You  Rerceived 6000sec for TZS 5000/= to call for China')
                        elif choice==2:
                            num = int(input('Ingiza namba ya siri:'))
                            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                        else:
                            print('Invalid Request')
                    elif choice == 2:
                        print('Dear customer your Balance is 1200sec')
                    else:
                        print('Invalid Request')
                elif choice==3:
                    print('1.Get 6000 Seconds for TZS 5000/= to call USA & CANADA')
                    print('2.Balance')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('1.Airtime')
                        print('2.Airtel Money')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('You  Rerceived 6000sec for TZS 5000/= to call for USA & CANADA')
                        elif choice==2:
                            num = int(input('Ingiza namba ya siri:'))
                            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                        else:
                            print('Invalid Request')
                    elif choice == 2:
                        print('Dear customer your Balance is 1200sec')
                    else:
                        print('Invalid Request')
                elif choice==4:
                    print('1.Get 360 Seconds for TZS 5000/= to call Kenya,Uganda,Rwanda for 1 day')
                    print('2.Balance')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('1.Airtime')
                        print('2.Airtel Money')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('You  Rerceived 360sec for TZS 5000/= to call for Kenya,Uganda,Rwanda for 1 day  ')
                        elif choice==2:
                            num = int(input('Ingiza namba ya siri:'))
                            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                        else:
                            print('Invalid Request')
                    elif choice == 2:
                        print('Dear customer your Balance is 1200sec')
                    else:
                        print('Invalid Request')
                elif choice==5:
                    print('1.SOUTH AFRICA')
                    print('2.ZAMBIA')
                    print('3.MALAWI & DRC')
                    choice=int(input('Enter your choice 1/2/3:'))
                    if choice==1:
                        print('1.Get 600 Seconds for TZS 6000/= to call Africa Kusini for 1 day')
                        print('2.Balance')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('1.Airtime')
                            print('2.Airtel Money')
                            choice = int(input('Enter your choice 1/2:'))
                            if choice == 1:
                                print('You  Rerceived 300sec for TZS 3000/= to call for Africa Kusini for 1 day  ')
                            elif choice==2:
                                num = int(input('Ingiza namba ya siri:'))
                                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                            else:
                                print('Invalid Request')
                        elif choice == 2:
                                print('Dear customer your Balance is 1200sec')
                        else:
                                print('Invalid Request')
                elif choice==6:
                    print('1.OMAN')
                    print('2.UAE,Saudi Arabia,Yemen,Lebanon,Pakistan & Qatar')
                    choice=int(input('Enter your choice 1/2:'))
                    if choice==1:
                        print('1.Get 180 Seconds for TZS 2500/= to call Oman for 1 day')
                        print('2.Balance')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('1.Airtime')
                            print('2.Airtel Money')
                            choice = int(input('Enter your choice 1/2:'))
                            if choice == 1:
                                print('You  Rerceived 180sec for TZS 2500/= to call for Oman for 1 day  ')
                            elif choice==2:
                                num = int(input('Ingiza namba ya siri:'))
                                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                            else:
                                print('Invalid Request')
                        elif choice == 2:
                            print('Dear customer your Balance is 1200sec')
                        else:
                            print('Invalid Request')
                    elif choice==2:
                        print('1.Get 300 Seconds for TZS 2500/= to call UAE,Saudi Arabia,Yemen,Lebanon,Pakistan & Qatar for 1 day')
                        print('2.Balance')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('1.Airtime')
                            print('2.Airtel Money')
                            choice = int(input('Enter your choice 1/2:'))
                            if choice == 1:
                                print('You  Rerceived 300sec for TZS 2500/= to call for UAE,Saudi Arabia,Yemen,Lebanon,Pakistan & Qatar for 1 day  ')
                            elif choice==2:
                                num = int(input('Ingiza namba ya siri:'))
                                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                            else:
                                print('Invalid Request')
                        elif choice == 2:
                            print('Dear customer your Balance is 1200sec')
                        else:
                            print('Invalid Request')
                elif choice==7:
                    print('1.Get 240 Seconds for TZS 2500/= to call UK,Italy & Germany for 1 day')
                    print('2.Balance')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('1.Airtime')
                        print('2.Airtel Money')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print(
                                'You  Rerceived 240sec for TZS 2500/= to call for UK,Italy & Germany  for 1 day  ')
                        elif choice==2:
                            num = int(input('Ingiza namba ya siri:'))
                            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                        else:
                            print('Invalid Request')
                    elif choice == 2:
                        print('Dear customer your Balance is 1200sec')
                    else:
                        print('Invalid Request')
                else:
                    print('Invalid Request')
            elif choice == 3:
                print('CHOOSE BUNDLES')
                print('1.INDIA')
                print('2.CHINA')
                print('3.USA & CANADA')
                print("4.EAST AFRICA")
                print('5.SOUTHERN AFRICA')
                print('6.MIDDLE EAST')
                print('7.EUROPE')
                choice = int(input('Enter your choice 1/2/3/4/5/6/7:'))
                if choice == 1:
                    print('1.Get 18000 Seconds for TZS 15000/= to call India')
                    print('2.Balance')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('1.Airtime')
                        print('2.Airtel Money')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('You  Rerceived 18000sec for TZS 15000/= to call for India')
                        elif choice == 2:
                            num = int(input('Ingiza namba ya siri:'))
                            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                        else:
                            print('Invalid Request')
                    elif choice == 2:
                        print('Dear customer your Balance is 1200sec')
                    else:
                        print('Invalid Request')
                elif choice == 2:
                    print('1.Get 18000 Seconds for TZS 15000/= to call China')
                    print('2.Balance')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('1.Airtime')
                        print('2.Airtel Money')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('You  Rerceived 18000sec for TZS 15000/= to call for China')
                        elif choice == 2:
                            num = int(input('Ingiza namba ya siri:'))
                            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                        else:
                            print('Invalid Request')
                    elif choice == 2:
                        print('Dear customer your Balance is 1200sec')
                    else:
                        print('Invalid Request')
                elif choice == 3:
                    print('1.Get 18000 Seconds for TZS 15000/= to call USA & CANADA')
                    print('2.Balance')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('1.Airtime')
                        print('2.Airtel Money')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('You  Rerceived 18000sec for TZS 15000/= to call for USA & CANADA')
                        elif choice == 2:
                            num = int(input('Ingiza namba ya siri:'))
                            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                        else:
                            print('Invalid Request')
                    elif choice == 2:
                        print('Dear customer your Balance is 1200sec')
                    else:
                        print('Invalid Request')
                elif choice == 4:
                    print('1.Get 1080 Seconds for TZS 15000/= to call Kenya,Uganda,Rwanda for 1 month')
                    print('2.Balance')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('1.Airtime')
                        print('2.Airtel Money')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('You  Rerceived 1080sec for TZS 15000/= to call for Kenya,Uganda,Rwanda for 1 month ')
                        elif choice == 2:
                            num = int(input('Ingiza namba ya siri:'))
                            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                        else:
                            print('Invalid Request')
                    elif choice == 2:
                        print('Dear customer your Balance is 1200sec')
                    else:
                        print('Invalid Request')
                elif choice == 5:
                    print('1.SOUTH AFRICA')
                    print('2.ZAMBIA')
                    print('3.MALAWI & DRC')
                    choice = int(input('Enter your choice 1/2/3:'))
                    if choice == 1:
                        print('1.Get 1500 Seconds for TZS 15000/= to call Africa Kusini for 30 days')
                        print('2.Balance')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('1.Airtime')
                            print('2.Airtel Money')
                            choice = int(input('Enter your choice 1/2:'))
                            if choice == 1:
                                print('You  Rerceived 1500sec for TZS 15000/= to call for Africa Kusini for 30 days  ')
                            elif choice == 2:
                                num = int(input('Ingiza namba ya siri:'))
                                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                            else:
                                print('Invalid Request')
                        elif choice == 2:
                            print('Dear customer your Balance is 1200sec')
                        else:
                            print('Invalid Request')
                elif choice == 6:
                    print('1.OMAN')
                    print('2.UAE,Saudi Arabia,Yemen,Lebanon,Pakistan & Qatar')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('1.Get 1080 Seconds for TZS 15000/= to call Oman for 30days')
                        print('2.Balance')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('1.Airtime')
                            print('2.Airtel Money')
                            choice = int(input('Enter your choice 1/2:'))
                            if choice == 1:
                                print('You  Rerceived 180sec for TZS 15000/= to call for Oman for 30 days  ')
                            elif choice == 2:
                                num = int(input('Ingiza namba ya siri:'))
                                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                            else:
                                print('Invalid Request')
                        elif choice == 2:
                            print('Dear customer your Balance is 1200sec')
                        else:
                            print('Invalid Request')
                    elif choice == 2:
                        print('1.Get 1800 Seconds for TZS 15000/= to call UAE,Saudi Arabia,Yemen,Lebanon,Pakistan & Qatar for 30 days')
                        print('2.Balance')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('1.Airtime')
                            print('2.Airtel Money')
                            choice = int(input('Enter your choice 1/2:'))
                            if choice == 1:
                                print(
                                    'You  Received 1800sec for TZS 15000/= to call for UAE,Saudi Arabia,Yemen,Lebanon,Pakistan & Qatar for 30days  ')
                            elif choice == 2:
                                num = int(input('Ingiza namba ya siri:'))
                                print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                            else:
                                print('Invalid Request')
                        elif choice == 2:
                            print('Dear customer your Balance is 1200sec')
                        else:
                            print('Invalid Request')
                    else:
                        print('Invalid Request')
                elif choice == 7:
                    print('1.Get 1440 Seconds for TZS 15000/= to call UK,Italy & Germany for 30days')
                    print('2.Balance')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('1.Airtime')
                        print('2.Airtel Money')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print(
                                'You  Rerceived 1440sec for TZS 15000/= to call for UK,Italy & Germany  for 30days  ')
                        elif choice == 2:
                            num = int(input('Ingiza namba ya siri:'))
                            print('Mpendwa Mteja Subiri kidogo Tukuhudumie')
                        else:
                            print('Invalid Request')
                    elif choice == 2:
                        print('Dear customer your Balance is 1200sec')
                    else:
                        print('Invalid Request')
                else:
                    print('Invalid Request')
        elif choice==2:
            print('1.One Airtel Bando')
            print('2.Global Bundles')
            print('3.Global Data Bundles')
            print('4.Other Global Data Bundles')
            choice=int(input('Enter your choice 1/2/3/4:'))
            if choice==1:
                print('CHOOSE BUNDLE')
                print('1.Daily/3 days')
                print('2.Weekly')
                print('3.14 days')
                print('4.One Airtel Countries')
                print('5.Balance')
                choice=int(input('Enter your choice 1/2/3/4/5:'))
                if choice==1:
                    print('1.Tsh 5000=500MB 1 day')
                    print('2.Tsh 10000=1229MB 3 days')
                    print('3.Tsh 10000=10Min+75MB 3 days')
                    choice=int(input('Enter your choice 1/2/3:'))
                    if choice==1:
                        print('Get 500MB for Tsh 5000 for 1 day')
                        print('1.Airtime')
                        print('2.Airtel Money')
                        choice=int(input('Enter your choice 1/2:'))
                        if choice==1:
                            print('You received 500MB for Tsh 5000@1 day')
                        elif choice==2:
                            num=int(input('Enter your serial number'))
                            print('You have successifuly pay for Bundle')
                        else:
                            print('Invalid Request')
                    elif choice==2:
                        print('Get 1229MB for Tsh 10000 for 3 days')
                        print('1.Airtime')
                        print('2.Airtel Money')
                        choice=int(input('Enter your choice 1/2:'))
                        if choice==1:
                            print('You received 1229MB for Tsh 10000@3days')
                        elif choice==2:
                            num=int(input('Enter your serial number'))
                            print('You have successifuly pay for Bundle')
                        else:
                            print('Invalid Request')
                    elif choice==3:
                        print('Get 10Min+75MB for Tsh 10000 for 3 days')
                        print('1.Airtime')
                        print('2.Airtel Money')
                        choice=int(input('Enter your choice 1/2:'))
                        if choice==1:
                            print('You received 10Min+75MB for Tsh 10000@3 days')
                        elif choice==2:
                            num=int(input('Enter your serial number'))
                            print('You have successifuly pay for Bundle')
                        else:
                            print('Invalid Request')
                elif choice==2:
                    print('1.Tsh 15000=2GB 7 days')
                    print('2.Tsh 25000=25Min+250MB 7 days')
                    choice=int(input('Enter your choice 1/2:'))
                    if choice==1:
                        print('Get 2GB for Tsh 15000 for 7 days')
                        print('1.Airtime')
                        print('2.Airtel Money')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('You received 2GB for Tsh 15000@7 days')
                        elif choice == 2:
                            num = int(input('Enter your serial number'))
                            print('You have successifuly pay for Bundle')
                        else:
                            print('Invalid Request')
                    elif choice==2:
                        print('Get 25Min+250MB for Tsh 25000 for 7 days')
                        print('1.Airtime')
                        print('2.Airtel Money')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('You received 25Min+250MB for Tsh 25000@7 days')
                        elif choice == 2:
                            num = int(input('Enter your serial number'))
                            print('You have successifuly pay for Bundle')
                        else:
                            print('Invalid Request')
                    else:
                        print('Invalid Request')
                elif choice==3:
                    print('1.Tsh 30000=5GB 14 days')
                    print('2.Tsh 40000=45Min+500MB 14 days')
                    choice=int(input('Enter your choice 1/2:'))
                    if choice==1:
                        print('Get 5GB for Tsh 30000 for 14 days')
                        print('1.Airtime')
                        print('2.Airtel Money')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('You received 5GB for Tsh 30000@14 days')
                        elif choice == 2:
                            num = int(input('Enter your serial number'))
                            print('You have successifuly pay for Bundle')
                        else:
                            print('Invalid Request')
                    elif choice==2:
                        print('Get 45Min+500MB for Tsh 40000 for 14 days')
                        print('1.Airtime')
                        print('2.Airtel Money')
                        choice = int(input('Enter your choice 1/2:'))
                        if choice == 1:
                            print('You received 45Min+500MB for Tsh 40000@14 days')
                        elif choice == 2:
                            num = int(input('Enter your serial number'))
                            print('You have successifuly pay for Bundle')
                        else:
                            print('Invalid Request')
                elif choice==4:
                    print('Congo B,DRC,Gabon,Ghana,Kenya,Madagascar,Malawi,Niger,Nigeria,Rwanda,Seychelles,Tchad,Uganda,Zambia and India')
                elif choice==5:
                    print('1.Salio:Tshs 0')
                    print('2.DENI:Tshs 0')
                else:
                    print('Invalid Request')
            elif choice==2:
                print('CHOOSE BUNDLE')
                print('1.Tsh 10000=10Min 7 days')
                print('2.Tsh 25000=12Min & 250MB 3 days')
                print('3.Tsh 50000=15Min & 200MB 7 days')
                print('4.Destinations')
                print('5.Balance')
                choice=int(input('Enter your choice 1/2/3/4/5:'))
                if choice==1:
                    print('Get 10Min for Tsh 10000 for 7 days')
                    print('1.Airtime')
                    print('2.Airtel Money')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('You received 10Min for Tsh 10000@7 days')
                    elif choice == 2:
                        num = int(input('Enter your serial number'))
                        print('You have successifuly pay for Bundle')
                    else:
                        print('Invalid Request')
                elif choice==2:
                    print('Get 12Min+250MB for Tsh 25000 for 3 days')
                    print('1.Airtime')
                    print('2.Airtel Money')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('You received 12Min & 250MB for Tsh 25000@3 days')
                    elif choice == 2:
                        num = int(input('Enter your serial number'))
                        print('You have successifuly pay for Bundle')
                    else:
                        print('Invalid Request')
                elif choice==3:
                    print('Get 15Min + 200MB for Tsh 50000 for 7 days')
                    print('1.Airtime')
                    print('2.Airtel Money')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('You received 15Min & 200MB for Tsh 50000@7 days')
                    elif choice == 2:
                        num = int(input('Enter your serial number'))
                        print('You have successifuly pay for Bundle')
                    else:
                        print('Invalid Request')
                elif choice==4:
                    print('1.AFRIKA')
                    print('2.US & CANADA')
                    print('3.ULAYA')
                    print('4.MASHARIKI YA KATI & ASIA')
                    print('5.OCENIA')
                    choice = int(input('Enter your choice 1/2/3/4/5:'))
                    if choice==1:
                        print('Botswana,Congo B,Congo DRC,Egypt,Gabon,Ghana,Kenya,Madagascar,Malawi,Mauritius,Mozambique,Niger,Nigeria,Rwanda,South Africa,Swaziland,Chad,Uganda,Zambia')
                    elif choice==2:
                        print('US & Canada')
                    elif choice==3:
                        print('Denmark,France,Germany,Greece,Italy,Netherlands,Norway,Romania,Russia,Spain,Sweden,UK')
                    elif choice==4:
                        print('China,Bangladesh,India,Israel,Oman,Pakistan,Qatar,Saudi Arabia,SriLanka,Turkey,UAE')
                    elif choice==5:
                        print('New Zealand')
                elif choice==5:
                    print('1.Salio:Tshs 0')
                    print('2.DENI:Tshs 0')
                else:
                    print('Invalid Request')
            elif choice==3:
                print('CHOOSE BUNDLES')
                print('1.Tsh 40000=1GB 3 days')
                print('2.Tsh 75000=2GB 7 days')
                print('3.Tsh 200000=5GB 14 days')
                print('4.Destinations')
                choice=int(input('Enter your choice 1/2/3/4: '))
                if choice==1:
                    print('Get 1GB for Tsh 40000 for 3 days')
                    print('1.Airtime')
                    print('2.Airtel Money')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('You received 1GB for Tsh 40000@3 days')
                    elif choice == 2:
                        num = int(input('Enter your serial number'))
                        print('You have successifuly pay for Bundle')
                    else:
                        print('Invalid Request')
                elif choice==2:
                    print('Get 2GB for Tsh 75000 for 7 days')
                    print('1.Airtime')
                    print('2.Airtel Money')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('You received 2GB for Tsh 75000@7 days')
                    elif choice == 2:
                        num = int(input('Enter your serial number'))
                        print('You have successifuly pay for Bundle')
                    else:
                        print('Invalid Request')
                elif choice==3:
                    print('Get 5GB for Tsh 200000 for 14 days')
                    print('1.Airtime')
                    print('2.Airtel Money')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('You received 5GB for Tsh 200000@14 days')
                    elif choice == 2:
                        num = int(input('Enter your serial number'))
                        print('You have successifuly pay for Bundle')
                    else:
                        print('Invalid Request')
                elif choice==4:
                    print('1.AFRIKA')
                    print('2.US & CANADA')
                    print('3.ULAYA')
                    print('4.MASHARIKI YA KATI & ASIA')
                    print('5.CHINA')
                    choice = int(input('Enter your choice 1/2/3/4/5:'))
                    if choice==1:
                        print('Botswana(MTN),Cameroon(Orange),Egypt(Orange),Ghana(Airtel,TIGO),Mali(Orange),Mozambique(Vodacom),Mauritius(Emtel),Senegal(Orange),Swaziland(MTN),South Africa(MTN,Vodacom)')
                    elif choice==2:
                        print('USA(T-Mobile) & Canada(Bell,Telus)')
                    elif choice==3:
                        print('Belgium(Base,Orange),Switzerland(Swisscom),Denmark(Telenor,TDC),France(Orange,SFR),Germany(T-Mobile,Vodafone),Greece(Cosmote),Italy(Vodafone,Tim),Netherlands(Vodafone,KPN),Norway(Telenor),Romania(Vodafone,Orange),Russia(Vimlelcom),Spain(Vodafone,Telefonica),Sweden(Telenor),UK(Vodafone,Telefonica)')
                    elif choice==4:
                        print('India(Airtel),Israel(Orange,Pelephone,Cellcom),Pakistan(Mobilink,Telenor),Qatar(Qtel),Saudi Arabia(Zain),SriLanka(Airtel),Turkey(Vodafone),UAE(Etisalat)')
                    elif choice==5:
                        print('China Mobile')
                    else:
                        print('Invalid Request')
            elif choice==4:
                print('CHOOSE BUNDLES')
                print('1.Tsh 35000=200MB 3 days')
                print('2.Tsh 90000=512MB 7 days')
                print('3.Tsh 175000=1GB 14 days')
                print('4.Destinations')
                choice=int(input('Enter your choice 1/2/3/4: '))
                if choice==1:
                    print('Get 200MB for Tsh 35000 for 3 days')
                    print('1.Airtime')
                    print('2.Airtel Money')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('You received 200MB for Tsh 35000@3 days')
                    elif choice == 2:
                        num = int(input('Enter your serial number'))
                        print('You have successifuly pay for Bundle')
                    else:
                        print('Invalid Request')
                elif choice==2:
                    print('Get 512MB for Tsh 90000 for 7 days')
                    print('1.Airtime')
                    print('2.Airtel Money')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('You received 512MB for Tsh 90000@7 days')
                    elif choice == 2:
                        num = int(input('Enter your serial number'))
                        print('You have successifuly pay for Bundle')
                    else:
                        print('Invalid Request')
                elif choice==3:
                    print('Get 1GB for Tsh 175000 for 14 days')
                    print('1.Airtime')
                    print('2.Airtel Money')
                    choice = int(input('Enter your choice 1/2:'))
                    if choice == 1:
                        print('You received 1GB for Tsh 175000@14 days')
                    elif choice == 2:
                        num = int(input('Enter your serial number'))
                        print('You have successifuly pay for Bundle')
                    else:
                        print('Invalid Request')
                elif choice==4:
                    print('1.AFRIKA')
                    print('2.US')
                    print('3.MASHARIKI YA KATI & ASIA')
                    choice = int(input('Enter your choice 1/2/3/4/5:'))
                    if choice == 1:
                        print('South Africa(Cell C)')
                    elif choice==2:
                        print('AT & T')
                    elif choice==3:
                        print('Oman(Oman Tel),UAE(dU),Turkey(Turkcel)')
                    else:
                        print('Invalid Request')
                else:
                    print('Invalid Request')
elif choice==10:
    print('Tafadhali Andika Namba ya Mteja,ikianzia na 0*********')
    num=int(input('Enter the number:'))
    print('Umefanikiwa kurusha salio kwenda kwa mteja mwingine')
elif choice==11:
    print('1.ANZISHA Matumizi kwa Muda wa Maongezi')
    print('2.SITISHA Matumizi kwa Muda wa Maongezi')
    choice=int(input('Enter your choice 1/2:'))
    if choice==1:
        print('Umechagua Kuperuzi kwa kutumia Muda wa maongezi.Kusitisha piga *149*99# kisha chagua 5 Internet kisha chagua 10.')
    elif choice==2:


        print('Ndugu Mteja Umefanikiwa kuzuia matumizi kupitia kwenye salio.')
    else:
        print('Invalid Request')
else:
    print('Invalid Request')
import webbrowser
print(webbrowser.open('https://Airtel.co.tz'))