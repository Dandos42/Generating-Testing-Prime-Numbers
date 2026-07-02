# IMPORT KNIHOVEN
import  sys, random, logging, math

def BruteForce(generate_prime_number):   #metoda pro test prvočíselnosti přes Brute force
    if generate_prime_number < 2:  # Ošetření vstupu, aby byl větší než 2
        print("Číslo je menší než 2 tudíž nelze pokračovat v testování")
    i = 2
    x = generate_prime_number - 1
    if generate_prime_number % 5 == 0:
        print(generate_prime_number, "Nejedná se o prvočíslo ale o číslo složené")
    elif generate_prime_number % 2 == 0:
        print(generate_prime_number, "Nejedná se o prvočíslo ale o číslo složené")
    else:
        for i in range(2, generate_prime_number - 1):  # zjištění jestli se jedná o prvočíslo operací Brute Force
            if generate_prime_number % 5 == 0 | generate_prime_number % 2 ==0:
                print(generate_prime_number, "Nejedná se o prvočíslo ale o číslo složené")
            if generate_prime_number % i == 0:
                print(generate_prime_number, "Nejedná se o prvočíslo ale o číslo složené")
                break
            else:
                print(generate_prime_number, "= jedná se o prvočíslo")
                break
logging.basicConfig(level=logging.DEBUG, format ="{asctime} {levelname:<8} {message}", style='{', filename='logs.log', filemode='a')
#Úvodní slovo autorů
print("GENEROVÁNÍ PRVOČÍSEL")
print("")
print("Srdečně tě vítá Daneček, Matějíček a Daliborek")
print("Ahoj uživateli toto je náš program do předmětu Kryptografie!")
print("")

# DEKLARACE
It_is_number = False
steps: int = 0
MaxINTValue = sys.maxsize
pokracovani = "ano"
is_it_prime_number =0
is_it_prime_number_2 = 0


#menu pro výběr akce
while pokracovani == "ano":
    logging.debug('starting program')
    print("Vyberte jednu z požadovaných akcí:")
    print("1 - Vygenerování velkého čísla, a test prvočíselnosti vygenerovaného čísla")
    print("2 - Otestovaní zadáného prvočísla, čísla ze souboru a export výsledků do souboru")
    print("3 - Zadání čísla a následné vypsání všech prvočísel, které obsahuje")
    print("4 - Faktorizace složeného čísla")
    print("5 - Informace o projektu")
    zvol_operace = int(input("")) #vygenerování velkého čísla + test + export
    # --------------------------------------------------------------------------------------------------------------------------------------#
    if zvol_operace == 1:   # vygenerování velkého čísla + test + export
        logging.info('user chose operation number 1')
        random_cislo = random.randint(10000, MaxINTValue - 1000) #vygenerování velkého náhodného čísla
        generate_prime_number = random_cislo
        print("To je náhodné velké číslo:" + str(generate_prime_number))
        BruteForce(generate_prime_number)

#--------------------------------------------------------------------------------------------------------------------------------------#
    elif zvol_operace == 2: #otestování zadaného čísla
        logging.info('user chose operation number 2')
        while pokracovani == "ano":
            print("Otestování zadaného čísla") #výběrové menu pro operaci 2
            print("Vyberte jednu z požadovaných akcí:")
            print("1 - Chceš zadat číslo z konzole")
            print("2 - Chceš zadat číslo ze souboru")
            print("3 - Chceš exportovat výsledek do souboru")
            zvol_operace_2 = int(input(""))
            if (zvol_operace_2 == 1):                                                                                      #zadání čísla z konzole
                logging.info('user chose operation number 2-1')
                print("Číslo bude otestováno: metodou Brute Force, Lucas-Lehmerovým testem, Miler-Rabinovým testem")
                vstupni_cislo = input("Vložte číslo, které chcete otestovat: ")
                is_it_prime_number = int(vstupni_cislo)
                logging.info('user wrote number for the test')
                BruteForce(is_it_prime_number)
                #Lucas-Lehmerův test
                s = 4
                M = pow(2, is_it_prime_number) - 1
                for x in range(1, (is_it_prime_number - 2) + 1):
                    s = ((s * s) - 2) % M
                if is_it_prime_number % 2 ==0:
                    print(is_it_prime_number, "= Nejedná se o prvočíslo ale o číslo složené, [Lucas-Lehmerův test]")
                    break
                elif s == 0:
                    print(is_it_prime_number, "= jedná se o prvočíslo, [Lucas-Lehmerův test]")
                else:
                    print(is_it_prime_number, "= Nejedná se o prvočíslo ale o číslo složené, [Lucas-Lehmerův test]")


            elif (zvol_operace_2 == 2):                                                                                   #zadání čísla ze souboru
                logging.info('user chose operation number 2-2')
                print("import čísla ze souboru")
                # otevření souboru, s prvočíslem a jeho otestování
                with open("random_cislo.txt", "r", encoding="utf-8") as f: #název souboru, české kódování
                    for cislo_ze_souboru in f.readlines(): #přečtení souboru
                        print(cislo_ze_souboru.strip() + " - toto je číslo ze souboru") # Odstraníme prázdné řádky "\n" a vypíšeme číslo

                # otestování zda-li číslo v souboru je prvočíslo
                is_it_prime_number_2 = int(cislo_ze_souboru)
                BruteForce(is_it_prime_number_2)

            elif (zvol_operace_2 == 3):                                                                                   #export do souboru
                print("akce - export do souboru")  #funkce with automaticky uzavře soubor
                #zápis do souboru výsledky test
                with open("vysledky_test.txt", "w", encoding="utf-8") as f:
                    if is_it_prime_number == 0 and is_it_prime_number_2 == 0:
                        f.write(str(is_it_prime_number) + "\n")
                        f.write(str(is_it_prime_number_2) + "\n")
                    elif is_it_prime_number != 0 and is_it_prime_number_2 == 0:
                        f.write(str(is_it_prime_number) + "\n")  # pro úspěšný zápis do souboru musíme přeparsovat
                    elif is_it_prime_number == 0 and is_it_prime_number_2 != 0:
                        f.write(str(is_it_prime_number_2) + "\n")

                    f.write("Toto je konec našeho souboru ")
                print("všechny hodnoty byly úspěšně zapsány do souboru")
            else:
                print("Chybná volba!!!")
            # kontrola podmínky zda-li chceme pokračovat pokud ne tak se program ukončí
            pokracovat = input("Přejete si pokračovat v akci 2? = ano || chcete ukončit program = press any button: ")
            if (pokracovat != "ano"):
                break;
 # --------------------------------------------------------------------------------------------------------------------------------------#
    elif zvol_operace == 3:  # vypsání seznamu prvočísel + export
        logging.info('user chose operation number 2-3')
        with open("seznam_prvocisel.txt", 'w'):
            pass
        print("vypsání seznamu prvočísel po zadané číslo a jeho okamžitý export dou soboru ")
        number = int(input("Zadej cislo, pro vypsání seznamu prvočísel: "))  # vstup
        prime_number = number
        # Cyklus generuje a vypíše všechny prvočísla po zadané číslo:
        for j in range(1, prime_number):
            j += 1
            iteration = j
            divisor = 2  # dělíme číslem 2
            while iteration > 1:
                if iteration % divisor == 0:  # zjištění jestli zbytek po dělení je 0
                    iteration //= divisor  # Vydělení samotného čísla dělitelem pokud zbytek po dělení je 0
                    # Je počet kroků provedených dělení menší než 1
                    if steps < 1:
                        It_is_number = True  # Dané číslo je prvočíslem pokud platí podmínka
                    else:
                        It_is_number = False  # Dané číslo není prvočíslem
                    steps += 1  # zvětšení počtu kroků
                else:
                    divisor += 1  # Zbytek dělení není nulový, a tak zvětším dělitele o 1
            steps = 0  # vynulování kroků
            vysledne_cislo = divisor
            if It_is_number:
                print("Prvočíslo" + ": " + str(vysledne_cislo))  # vypání * prvočísel po dané číslo pod sebe
            # následný export čísel do souboru seznam_prvočísel
            with open("seznam_prvocisel.txt", "a", encoding="utf-8") as f:
                f.write(str(vysledne_cislo) + "\n")  # pro úspěšný zápis do souboru musíme přeparsovat

        print("všechny hodnoty byly úspěšně zapsány do souboru")
        logging.info('saved data into file')
    # --------------------------------------------------------------------------------------------------------------------------------------#
    elif zvol_operace == 4: #faktorizace čísel
        logging.info('user chose operation number 4')
        # Uživatel zadá číslo n program zjistí jestli se jedná o prvočíslo
        # pokud ano vypíše prvočíslo
        # pokud ne vypíše prvočísla, ze kterého se číslo skládá
        def FaktorizaceCisel(funkce_faktorizace):
            print("{} - rozklad na prvočísla:\t".format(funkce_faktorizace), end="")
            fakt_number = 2
            while funkce_faktorizace > 1:
                if funkce_faktorizace % fakt_number == 0:  # zjištění jestli zbytek po dělení je 0
                    print(fakt_number, end=" ") #pokud ano vypíšou prvočísla s mezerou
                    funkce_faktorizace //= fakt_number  # // jedná se o celočíselné dělení
                else:
                    fakt_number += 1
        print()  # vynechat řádek po vypsaných prvočíslech
        # výpis prvočísel z rozkladu k na prvočísla
        vypis_fakt_number = int(input("Zadejte jakékoliv číslo pokud se jedná o prvočíslo vypíše se || pokud se jedná o složenné číslo provede se faktorizace: "))
        FaktorizaceCisel(vypis_fakt_number)
    # --------------------------------------------------------------------------------------------------------------------------------------#
    elif zvol_operace == 5: #project info
        logging.info('user chose operation number 5')
        print()
        print("Název: Generování velkých prvočísel")
        print("Datum vytvoření: 25.10.2022")
        print("Autoři: Daniel Prachař, Dalibor Rada, Matěj Oszelda")
        print("Datum odevzdání: 4.11.2020")
        print("Předmět: Kryptografie ")
        print("Obor: Informační bezpečnost")
        print("Fakulta: Fakulta elektrotechniky a informačních technologí ")
    # --------------------------------------------------------------------------------------------------------------------------------------#



    # --------------------------------------------------------------------------------------------------------------------------------------#
    else:
        print("Chybná operace!!!")
        logging.warning('user tried to chose wrong operation!')
    print()
    #kontrola podmínky zda-li chceme pokračovat pokud ne tak se program ukončí
    pokracovat= input("Přejete si pokračovat v programu = ano || chcete ukončit program = press any button: ")
    if(pokracovat != "ano"):
        logging.info('user chose to continue using the program')
        break;
print()
logging.debug('program has ended')
print("Děkuji za použití našeho programu :D ")
print("S přáním hezkého dne Daneček, Dalibor a Matěj")