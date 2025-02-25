import random as rnd
from colorama import Fore,Style,Back
from pyperclip import copy
from bs4 import BeautifulSoup as bs
import requests
import json
from datetime import datetime
import pytz
from pathlib import Path
import os
import webbrowser as wb

class Main: # This class includes essential functions will be used in apps
    def printg(x): # Basically this function returns the green text.e
        return print(Fore.GREEN+x+Style.RESET_ALL)

    def true_false_dialog(message): # This functions returns the terminal based input function where only '1' or '2' is correct answer.
                var = input(message)
                while var != "1" and var != "2":
                    print(Fore.RED + "Geçersiz cevap. Lütfen tekrar giriniz!"+ Style.RESET_ALL)
                    var = input(message)
        
                return var
    def input_dialog(input_message,error_message): # This functions returns the terminal based input function where every answer is correct except empty.
        while True:
            var = input(input_message)
            if var == "":
                print(f"{Style.BRIGHT}{Fore.RED}{error_message}{Style.RESET_ALL}")
                pass
            else:
                return var
    def choice_dialog(input_message,error_message,condition): # This function is final form of the older functions ^^
            while True:
                var = input(input_message)
                if eval(condition):
                    print(f"{Style.BRIGHT}{Fore.RED}{error_message}{Style.RESET_ALL}")
                    pass
                else:
                    return var
    def str_range(start,end): # This function basically done same thing with series, but list element's variable type is 'str' not 'int'.
        range_list = list()
        while start<end:
            range_list.append(str(start))
            start+=1
        return range_list
class Passgen: # Password Generator App's Class
    
    # Character Variant Lists
    special_chars = ["~","`","!","@","#","$","%","^","&","*","(",")","_","-","+","=","}","[","{","]","|","\\",":",";","'","<",",",">",".","?","/"]
    tr_alphabet = ["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]
    tr_alphabet_capital = ["A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z"]
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    
    # The main dialog function
    def dialog():
        Main.printg("Koray.PASS Şifre Oluşturma Aracı - sürüm 1.0")
        
        while True: # This while loop prevents the ValueError.
            try:
                char_count = int(input(f"{Fore.BLUE}1. {Style.RESET_ALL}Lütfen kaç haneli bir şifre istediğinizi yazınız (Max. 255): "))
            except ValueError:
                print(Fore.RED + "Geçersiz karakter, lütfen tekrar deneyiniz..."+ Style.RESET_ALL)
                continue
            break
        
        while char_count > 255:
            print(Fore.RED + "Geçersiz karakter, lütfen tekrar deneyiniz..."+ Style.RESET_ALL)
            char_count = input(f"{Fore.BLUE}1. {Style.RESET_ALL}Lütfen kaç haneli bir şifre istediğinizi yazınız: ")
        
        # Detailed configuration option given for advanced users.
        print(Fore.CYAN + "(OPSİYONEL)"+ Style.RESET_ALL +"\nŞifrenin karakter içeriğini özelleştirmek istiyor musunuz?\nEvet der iseniz şifredeki büyük harf, sayı gibi karakterlerin olup olmayacağını belirleyebilirsiniz. Aksi takdirde varsayılan olarak bütün karakterler açık olacaktır.\n")
        detailed_option = input("1) Evet\n2) Hayır: ")
        while detailed_option !="1" and detailed_option !="2":
            print("Hatalı giriş. Lütfen tekrar deneyiniz.")
            detailed_option = input("1) Evet\n2)Hayır\n")
        if detailed_option == "1":
            return Passgen.detailed_pass_dialog(char_count)
        else:
            return Passgen.generate_pass("1","1","1",char_count)
    def detailed_pass_dialog(char_count):
        
        # Automated this "1" or "2" sequence with single function.
        capital_include = Main.true_false_dialog(f"{Fore.BLUE}2. {Style.RESET_ALL}Şifre büyük harfli karakterler içersin mi?\n1) Evet\n2) Hayır: ")
        special_include = Main.true_false_dialog(f"{Fore.BLUE}3. {Style.RESET_ALL}Şifre özel karakter içersin mi?\n1) Evet\n2) Hayır: ")
        number_include = Main.true_false_dialog(f"{Fore.BLUE}4. {Style.RESET_ALL}Şifre sayı içersin mi?\n1) Evet\n2) Hayır: ")
        
        return Passgen.generate_pass(capital_include,special_include,number_include,char_count)
    
    # This function is the core of the password generator, it creates password based on "random" library.
    
    def generate_pass(capital,special,numb,char_count): 
        char_variants = {"normal":"1","capital":capital,"special":special,"numb":numb} # Firstly, it gets the status of all variants.
        
        for variant in list(char_variants.keys()):
            if char_variants[variant] == "2":
                del char_variants[variant] # Deletes unnecessary variants.

        variant_count = len(char_variants.keys()) # To assign count, gets the number of necessary variants.
        generate_count = dict()
        variant_keylist = list(char_variants.keys())
        
        for variant_name in variant_keylist: # And with this (not so complex) loop, every variant has own random count.
            if variant_name == variant_keylist[-1]:
                generate_count[variant_name] = char_count
            else:
                generate_count[variant_name] = rnd.randint(1,char_count-variant_count+variant_keylist.index(variant_name)) # This part is critical to prevent out of range errors.
                char_count = char_count - generate_count[variant_name]
                
        generated_pass = list() # This list collects the random picked characters.
        def rand_list_pick(listpick,count): # This function picks the random items with desired count, and returns the list of it.
                return_list = []
                for picked in range(1,count+1):
                    return_list.append(listpick[(rnd.randint(0,len(listpick)-1))])
                return return_list
                    
        for variant_name in list(generate_count.keys()): # This part can be more modular. But with only 4 variable, it works as expected.
            range_count = generate_count[variant_name]
            def add_pass_chars_to_list(passlib,range_count):
                return generated_pass.extend((rand_list_pick(eval(f"Passgen.{passlib}"),range_count)))
            
            if variant_name == "normal":
                add_pass_chars_to_list('tr_alphabet',range_count)
            elif variant_name == "capital":
                add_pass_chars_to_list('tr_alphabet_capital',range_count)
            elif variant_name == "special":
                add_pass_chars_to_list('special_chars',range_count)
            elif variant_name == "numb":
                add_pass_chars_to_list('numbers',range_count)   
                
        rnd.shuffle(generated_pass) # Shuffles with 'random' library
        pass_text = ''.join(generated_pass) # Getting the string from list.
        copy(pass_text)          
        print(f"{Fore.CYAN}Oluşturulan Şifreniz:{Style.RESET_ALL}\n{pass_text}{Fore.BLACK}\t(Panoya Kaydedildi. CTRL+V kullanarak yapıştırabilirsiniz.){Style.RESET_ALL}")
        another_dialog = Main.true_false_dialog(f"\n{Style.BRIGHT}Bir şifre daha oluşturmak ister misiniz?{Style.RESET_ALL}\n1) Evet\n2) Hayır: ")
        if another_dialog == "1":
            return Passgen.dialog()
        else:
            return
class Weather: # Weather API App's Class
    def dialog():
        Main.printg("Koray.WEATHER Hava Durumu Aracı - sürüm 1.0")
        print(f"\n{Style.BRIGHT}Lütfen hava durumunu öğrenmek istediğiniz şehir veya ilçeyi giriniz: (Çıkmak için 'çıkış'){Style.RESET_ALL}")
        place = input()
        while True: # The while loop for getting non-empty input.
            if place == "":
                print("İl-İlçe bölümü boş bırakılamaz. Lütfen tekrar giriniz.")
                print(f"\n{Style.BRIGHT}Lütfen hava durumunu öğrenmek istediğiniz şehir veya ilçeyi giriniz:{Style.RESET_ALL}")
                place = input()
            elif place == 'çıkış':
                return
            else:
                break
        Weather.getWeather(place)
    def getWeather(place): # API Function
        
        # This function takes 2 api requests.
        # First to get lat-lon for desired place.
        # Other for getting Weather Datas from this lat lon cordinates.
        
        url_geo_loc = f"http://api.openweathermap.org/geo/1.0/direct?q={place}&lang=tr&limit=1&appid=0e51ac6541608d1b8d4ad81d227dd12d" # Geographic Lat-Lon Request
        response = requests.get(url_geo_loc)
        if response.status_code == 200:
            if response.text.strip("[]") == "":
                print("Geçersiz Konum girdiniz lütfen tekrar deneyiniz")
                return exit()
            geo_data  = json.loads(response.text.strip("[]"))
            lat_lon = (geo_data['lat'], geo_data['lon']) #Getting lat and lon from it.
            url_weather = f"https://api.openweathermap.org/data/2.5/weather?lat={lat_lon[0]}&lon={lat_lon[1]}&units=metric&lang=tr&appid=0e51ac6541608d1b8d4ad81d227dd12d" # Main Weather API
            response_weather = requests.get(url_weather)
            if response_weather.status_code == 200:
                weather_data = json.loads(response_weather.text.strip("[]")) # Turns Json into dictionary.
                def date_get(api_dict): # Automaticly converts timestamps to human time GMT+3 for better visualization.
                    return str(datetime.fromtimestamp(api_dict, tz=pytz.timezone("Europe/Istanbul")))[11:-6]
                def blank():
                    return (Back.BLACK + "")
                # This print section is all about getting specific key to get 'desired' data -- and with colorama, getting better visualization.
                print(f"{Back.CYAN}Gösterilen Lokasyon:{Back.GREEN}{weather_data['name']+", "+ weather_data['sys']['country']}{Style.RESET_ALL}\n")
                print(f"{Back.BLUE}Hava Durumu:{Back.BLACK}{Fore.GREEN} {weather_data['weather'][0]['description']}{Style.RESET_ALL}\n{Back.MAGENTA}Sıcaklık:{Style.RESET_ALL}{Back.BLACK}{Style.BRIGHT} {weather_data['main']['temp']} C°{Style.RESET_ALL}\n{Back.MAGENTA}Hissedilen:{Style.RESET_ALL}{Back.BLACK}{Style.BRIGHT} {weather_data['main']['feels_like']} C°{Style.RESET_ALL}\n")
                print(f"{Back.RED}Güneş Doğuş:{Back.BLACK}{Fore.WHITE} {date_get(weather_data['sys']['sunrise'])}\n{Back.RED}Güneş Batış:{Back.BLACK}{Fore.WHITE} {date_get(weather_data['sys']['sunset'])}{Style.RESET_ALL}")
                print(f"{Style.NORMAL}\n(Son Güncellenme Tarihi: {date_get(weather_data['dt'])}){Style.RESET_ALL}")
                
                answer = Main.true_false_dialog(f"\n{Style.BRIGHT}* Başka bir sorgu yapmak ister misiniz?\n{Style.RESET_ALL}(1- Evet / 2- Hayır): ")
                if answer == "1":
                    return Weather.dialog()
                elif answer== "2":
                    return
            else:
                 print("Hata:", response.status_code)
                 return
        else:
            print("Hata:", response.status_code)
            return
class Note: # Classic Note App Class
    def dialog():
        Main.printg(f"{Style.NORMAL}\nKoray.NOTES Not Defteri Aracı - sürüm 1.0\n")
        print(f"{Style.BRIGHT}{Fore.YELLOW}>> İşlem Menüsü\n{Style.RESET_ALL}{Style.BRIGHT}{Fore.CYAN}1.{Style.RESET_ALL} Notları Listele\n{Style.BRIGHT}{Fore.CYAN}2.{Style.RESET_ALL} Not Oluştur\n{Style.BRIGHT}{Fore.CYAN}3.{Style.RESET_ALL} Not Görüntüle\n{Style.BRIGHT}{Fore.CYAN}4.{Style.RESET_ALL} Not Sil\n{Style.BRIGHT}{Fore.CYAN}5.{Style.RESET_ALL} Çıkış")
        choice = Main.choice_dialog("Lütfen bir işlem seçiniz: ","Geçersiz işlem, lütfen geçerli bir işlem seçiniz.","var not in ('1', '2', '3', '4', '5')")
        print()
        if choice == '1':
            Note.listNote()
        elif choice == '2':
            Note.createNote()
        elif choice == '3':
            Note.viewNote()
        elif choice == '4':
            Note.deleteNote()
        elif choice == "5":
            return 
        return Note.dialog()
        
    def list_files_with_extension(directory, extension): # This function simply lists the target folder's files which has desired extensions.
        return [f.name for f in Path(directory).glob(f'*.{extension}')]
    note_list = list_files_with_extension("notes","txt")
    def refresh_list(): # After all list add and delete operation, we need to refresh this data.
        Note.note_list = Note.list_files_with_extension("notes","txt")
        return
    def createNote():
        create_note_list = list()
        first_line = True
        while True: # This while loop basicly makes taking notes easier with getting down row.
            if first_line == True:
                note_line = input(f"{Style.RESET_ALL}{Back.BLUE}Lütfen notunuzu giriniz:{Style.RESET_ALL} (Satır atlamak için ENTER kullanın; boş satır, not bitti demektir.)\n")
                first_line = False
                if note_line == "":
                    break
                create_note_list.append(note_line)
            else:
                note_line = input("")
                if note_line == "":
                    break
                create_note_list.append(note_line)
        note_text = "\n".join(create_note_list)
        note_name = Main.input_dialog(f"{Back.BLUE}Lütfen notunuza bir isim veriniz:{Style.RESET_ALL} ","İsim boş olamaz!")
        if note_name[-4:] == ".txt": # This unique fix is important for accesibility. If even user doesn't type the full file name, program understands this situation and adds .txt to it.
            note_name = note_name[:-4]
        try: # The basic error handling.
            with open("notes/"+note_name+".txt","w",encoding='UTF-8') as created_note: #*** The only important part in here is UTF-8 because of the turkish language.
                created_note.writelines(note_text)
                Note.refresh_list()
                print(f"{Fore.GREEN}{Style.BRIGHT}{note_name}.txt başarı ile oluşturuldu.{Style.RESET_ALL}")
                return
        except Exception:
            print(f"{Fore.RED}{Style.BRIGHT}Not oluşturulurken bir sorun oluştu, lütfen tekrar deneyiniz.{Style.RESET_ALL}")
            return
    def listNote():
        print(f"{Back.RED}{Fore.WHITE}{Style.BRIGHT}'notes' klasörü içinde oluşturduğun notların listesi{Style.RESET_ALL}")
        for note in Note.note_list:
            print(f"{Style.BRIGHT}* {note}")
        return
    def viewNote():
        file_name = Main.input_dialog(f"{Style.BRIGHT}{Back.GREEN}Lütfen görüntülenecek notun ismini giriniz:{Style.RESET_ALL} ","İsim kısmı boş bırakılamaz!")
        if file_name[-4:] == ".txt": #***
            file_name = file_name[:-4]
        if file_name+".txt" in Note.note_list:        
            try: # Another basic error handling.
                with open("notes/"+file_name+".txt","r",encoding='UTF-8') as viewed_note: # UTF-8 is also important for reading.
                    print(f"\n{Style.RESET_ALL}{Back.CYAN}{file_name}.txt - {Style.BRIGHT}[Okuma Modu]{Style.RESET_ALL}")
                    for note_line in viewed_note:
                        print(note_line.strip())
                    return print()
            except Exception:
                return print(f"{Fore.RED}{Style.BRIGHT}Not okunurken bir sorun oluştu, lütfen tekrar deneyiniz.{Style.RESET_ALL}")
        else:
            return print(f"{Fore.RED}{Style.BRIGHT}Dosya bulunamadı. Lütfen tekrar deneyiniz.{Style.RESET_ALL}\n")
    def deleteNote():
        file_name = Main.input_dialog(f"{Style.BRIGHT}{Back.RED}Lütfen silinecek notun ismini giriniz:{Style.RESET_ALL} ","İsim kısmı boş bırakılamaz!")
        if file_name[-4:] == ".txt": #***
            file_name = file_name[:-4]
        if file_name+".txt" in Note.note_list:
            try:
                os.remove("notes/"+file_name+".txt") # Calls remove function from 'os' library to remove desired .txt file.
                Note.refresh_list()
                print(f"{Fore.GREEN}{Style.BRIGHT}{file_name}.txt başarı ile silindi.{Style.RESET_ALL}")
            except Exception:
                return print(f"{Fore.RED}{Style.BRIGHT}Not silinirken bir sorun oluştu, lütfen tekrar deneyiniz.{Style.RESET_ALL}")
        else:
            return print(f"{Fore.RED}{Style.BRIGHT}Dosya bulunamadı. Lütfen tekrar deneyiniz.{Style.RESET_ALL}\n")

class News: # News Preview App Class
    source_dict = { # This is list of News Sources, user can easily be able to updated this list with just typing new functions' parameters
        "Mynet Haber":"News.getNews('Mynet Haber','https://haber.mynet.com/','h3','card-text-title py-2 px-3',ex_arg='news_title.pop(-1)')",
        "Hürriyet":"News.getNews('Hürriyet','https://www.hurriyet.com.tr/','a','box__content box-lg-3__content')",
        "Sözcü":"News.getNews('Sözcü','https://www.sozcu.com.tr/','a','news-card-footer',limit=20)",
        "HaberTürk":"News.getNews('HaberTürk','https://www.haberturk.com','a','block gtm-tracker',start=14,limit=34)",
        "NTV Haber":"News.getNews('NTV Haber','https://www.ntv.com.tr/','a','card-text-link',start=16,limit=36,ex_arg='news_title.pop(2)')"
        }
        
    def dialog(): # Classic dialog side.
        Main.printg("Koray.NEWS Haber Önizleme Aracı - sürüm 1.0")
        print(f"\n{Style.BRIGHT}Mevcut Haber Kaynakları:{Style.RESET_ALL}")
        for source in News.source_dict.keys():
            print(f"{Style.BRIGHT}{Fore.YELLOW}{list(News.source_dict.keys()).index(source)+1}. {Fore.WHITE}{source}{Style.RESET_ALL}")
        choice = Main.choice_dialog(f"{Style.BRIGHT}{Fore.BLUE}Lütfen başlıklarını önizlemek istediğiniz haber kaynağını seçiniz:{Fore.WHITE} (çıkmak için 'çıkış'){Style.RESET_ALL}\n",'Hatalı seçim. Lütfen tekrar deneyiniz.','var not in ("1","2","3","4","5","çıkış")')
        if choice == 'çıkış':
            return
        return exec(News.source_dict[list(News.source_dict.keys())[(int(choice)-1)]]) # This exec specificly finds the desired key's value from its' index.
    
    def getNews(name,url,title_element,title_class,ex_arg=None,start=0,limit=None): # Modular API Request-base News Preview Function
        response = requests.get(url)
        if response.status_code == 200:
            html_site =response.text # Function basicly gets the content of page as text with 'requests' lib.
            soup = bs(html_site, "lxml") # Makes it Bs4 understand and parse.
            news_title = soup.find_all(title_element,class_=title_class) # With using 'bs4', finds the specific 'class' and specific 'element' combo to get news article's title.
            not_repeated_list = []
            for title in news_title: # This loop removes repeating elements.
                if title in not_repeated_list:
                    continue
                else:
                    not_repeated_list.append(title)
                    
            news_title = not_repeated_list
            if ex_arg != None: # With external argument, user can easily modify some things in list with executing giving code.
                exec(ex_arg)
            for title in news_title: # This loop removes empty-stringed elements.
                if title.text.strip() == '' or title.text == '' or title.text.strip() == ' ':
                    news_title.remove(title)
            if limit != None: # User can easily define the limit with 'limit' and 'start' arguments.
                news_title = news_title[start:limit+1]
            print(f"{Back.RED}{Fore.WHITE}{Style.BRIGHT}Kaynak:{Back.CYAN}{name}{Style.RESET_ALL}\n")
            for title in news_title: # This for loop prints the items of returned element list.
                print(f"{Style.BRIGHT}{Fore.CYAN}{str(news_title.index(title))}.{Style.RESET_ALL} {title.text.strip()}") 
                
            count_of_titles = len(news_title) # This variable will be usable in the eval() function, thats why defined.
    
            choice = Main.choice_dialog(f"{Style.BRIGHT}Lütfen açmak için bir haber seçiniz: (çıkmak için 'çıkış')\n","Geçersiz haber ID'si!",f"var not in (Main.str_range(0,{count_of_titles})+['çıkış'])")
            if choice == 'çıkış':
                return News.dialog()
            else:
                if title_element == 'a': # This if condition actually is about our target 'title_element'. If we haven't any element to reach sub-element like 'a' but have an 'a' directly; we basically get the text of it. Otherwise our code block in this sequence visibly changes.
                    if news_title[int(choice)].get('href')[:3] != "htt": # Some websites uses relative-links, other uses direct-links. Thats why this sequence in here, makes every link 'direct'.
                        choice_link = url + news_title[int(choice)].get('href')
                    else:
                        choice_link = news_title[int(choice)].get('href')
                    print(f"'{Fore.GREEN}{news_title[int(choice)].text.strip()}' isimli haber tarayıcıda açılıyor...{Style.RESET_ALL}")
                    wb.open(choice_link) # Basicly open the link.
                    another = Main.true_false_dialog('Aynı kaynakta başka bir habere bakmak ister misiniz?: (1- Evet / 2- Hayır)\n')
                    if another == '1':
                        return News.getNews(name,url,title_element,title_class,ex_arg,start,limit)
                    else:
                        return News.dialog()
                else:
                    if news_title[int(choice)].find('a').get('href')[:3] != "htt":
                        choice_link = url + news_title[int(choice)].find('a').get('href')
                    else:
                        choice_link = news_title[int(choice)].find('a').get('href')
                    print(f"'{Fore.GREEN}{news_title[int(choice)].text.strip()}' isimli haber tarayıcıda açılıyor...{Style.RESET_ALL}")
                    wb.open(choice_link)
                    another = Main.true_false_dialog('Aynı kaynakta başka bir habere bakmak ister misiniz?: (1- Evet / 2- Hayır)\n')
                    if another == '1':
                        return News.getNews(name,url,title_element,title_class,ex_arg,start,limit)
                    else:
                        return News.dialog()
        else:
            print(f"{Fore.RED}Sunucu ile bağlantı kurulamadı.{Style.RESET_ALL}")
            return News.dialog()