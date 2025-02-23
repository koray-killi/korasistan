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


class Main: # This class includes essential functions will be used in apps
    def printg(x):
        return print(Fore.GREEN+x+Style.RESET_ALL)

    def true_false_dialog(message):
                var = input(message)
                while var != "1" and var != "2":
                    print(Fore.RED + "Geçersiz cevap. Lütfen tekrar giriniz!"+ Style.RESET_ALL)
                    var = input(message)
        
                return var
    def input_dialog(input_message,error_message):
        while True:
            var = input(input_message)
            if var == "":
                print(f"{Style.BRIGHT}{Fore.RED}{error_message}{Style.RESET_ALL}")
                pass
            else:
                return var
    def choice_dialog(input_message,error_message,condition):
            while True:
                var = input(input_message)
                if eval(condition):
                    print(f"{Style.BRIGHT}{Fore.RED}{error_message}{Style.RESET_ALL}")
                    pass
                else:
                    return var
    
class Passgen: # Password Generator App's Class
    
    # Character Variant Lists
    special_chars = ["~","`","!","@","#","$","%","^","&","*","(",")","_","-","+","=","}","[","{","]","|","\\",":",";","'","<",",",">",".","?","/"]
    tr_alphabet = ["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]
    tr_alphabet_capital = ["A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z"]
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    
    # The main dialog function
    def dialog():
        Main.printg("Koray.PASS Şifre Oluşturma Aracı - sürüm 0.1")
        
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
        another_dialog = Main.true_false_dialog("\nBir şifre daha oluşturmak ister misiniz?\n1) Evet\n2) Hayır: ")
        if another_dialog == "1":
            return Passgen.dialog()
        else:
            return
class Weather:
    def dialog():
        Main.printg("Koray.WEATHER Hava Durumu Aracı - sürüm 0.1")
        print(f"\n{Style.BRIGHT}Lütfen hava durumunu öğrenmek istediğiniz şehir veya ilçeyi giriniz: (Çıkmak için 'çıkış'){Style.RESET_ALL}")
        place = input()
        while True:
            if place == "":
                print("İl-İlçe bölümü boş bırakılamaz. Lütfen tekrar giriniz.")
                print(f"\n{Style.BRIGHT}Lütfen hava durumunu öğrenmek istediğiniz şehir veya ilçeyi giriniz:{Style.RESET_ALL}")
                place = input()
            elif place == 'çıkış':
                return
            else:
                break
        Weather.getWeather(place)
    def getWeather(place):
        
        url_geo_loc = f"http://api.openweathermap.org/geo/1.0/direct?q={place}&lang=tr&limit=1&appid=0e51ac6541608d1b8d4ad81d227dd12d"
        response = requests.get(url_geo_loc)
        if response.status_code == 200:
            if response.text.strip("[]") == "":
                print("Geçersiz Konum girdiniz lütfen tekrar deneyiniz")
                return exit()
            geo_data  = json.loads(response.text.strip("[]"))
            lat_lon = (geo_data['lat'], geo_data['lon'])
            url_weather = f"https://api.openweathermap.org/data/2.5/weather?lat={lat_lon[0]}&lon={lat_lon[1]}&units=metric&lang=tr&appid=0e51ac6541608d1b8d4ad81d227dd12d"
            response_weather = requests.get(url_weather)
            
            if response_weather.status_code == 200:
                weather_data = json.loads(response_weather.text.strip("[]"))
                
                def date_get(api_dict): # Automaticly converts timestamps to human time GMT+3.
                    return str(datetime.fromtimestamp(api_dict, tz=pytz.timezone("Europe/Istanbul")))[11:-6]
                def blank():
                    return (Back.BLACK + "")
                print(f"{Back.CYAN}Gösterilen Lokasyon:{Back.GREEN}{weather_data['name']+", "+ weather_data['sys']['country']}\n")
                print(f"{Back.BLUE}Hava Durumu:{Back.BLACK}{Fore.GREEN} {weather_data['weather'][0]['description']}{Style.RESET_ALL}\n{Back.YELLOW}Sıcaklık:{Back.BLACK} {Fore.BLUE}{weather_data['main']['temp']} C°{Style.RESET_ALL}\n{Back.YELLOW}Hissedilen:{Back.BLACK} {Fore.BLUE}{weather_data['main']['feels_like']} C°{Style.RESET_ALL}\n")
                print(f"{Back.RED}Güneş Doğuş:{Back.BLACK} {date_get(weather_data['sys']['sunrise'])}\n{Back.RED}Güneş Batış:{Back.BLACK} {date_get(weather_data['sys']['sunset'])}")
                print(f"{Fore.BLACK}\n(Son Güncellenme Tarihi: {date_get(weather_data['dt'])}){Style.RESET_ALL}")
                
                answer = Main.true_false_dialog(f"\n{Style.BRIGHT}* Başka bir sorgu yapmak ister misiniz?\n{Style.RESET_ALL}(1- Evet / 2- Hayır): ")
                if answer == "1":
                    return Weather.dialog()
                elif answer== "2":
                    return
            else:
                 print("Hata:", response.status_code)
        else:
            print("Hata:", response.status_code)
class Note:
    def dialog():
        Main.printg(f"{Style.NORMAL}\nKoray.NOTES Not Defteri Aracı - sürüm 0.1\n")
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
        
    def list_files_with_extension(directory, extension):
        return [f.name for f in Path(directory).glob(f'*.{extension}')]
    note_list = list_files_with_extension("notes","txt")
    def refresh_list():
        Note.note_list = Note.list_files_with_extension("notes","txt")
        return
    def createNote():
        create_note_list = list()
        first_line = True
        while True:
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
        if note_name[-4:] == ".txt":
            note_name = note_name[:-4]
        try:
            with open("notes/"+note_name+".txt","w",encoding='UTF-8') as created_note:
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
        if file_name[-4:] == ".txt":
            file_name = file_name[:-4]
        if file_name+".txt" in Note.note_list:        
            try:
                with open("notes/"+file_name+".txt","r") as viewed_note:
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
        if file_name[-4:] == ".txt":
            file_name = file_name[:-4]
        if file_name+".txt" in Note.note_list:
            try:
                os.remove("notes/"+file_name+".txt")
                Note.refresh_list()
                print(f"{Fore.GREEN}{Style.BRIGHT}{file_name}.txt başarı ile silindi.{Style.RESET_ALL}")
            except Exception:
                return print(f"{Fore.RED}{Style.BRIGHT}Not silinirken bir sorun oluştu, lütfen tekrar deneyiniz.{Style.RESET_ALL}")
        else:
            return print(f"{Fore.RED}{Style.BRIGHT}Dosya bulunamadı. Lütfen tekrar deneyiniz.{Style.RESET_ALL}\n")

Note.dialog()