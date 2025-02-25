import applications as app
import speech_recognition as sr
from colorama import Fore, Back, Style

class Prefs:
    # Input / Output Functions for Preferances
    def getPrefs():
        prefslist = list()
        try:
            with open("prefs.ini", "r") as file:
                for i in file.readlines():
                    if i.strip() == "True":
                        prefslist.append(True)
                    elif i.strip() == "False":
                        prefslist.append(False)
                    else:
                        prefslist.append(i.strip())
            return prefslist
        except FileNotFoundError:
            return "Error"
    def importPrefs():
        preflist = Prefs.getPrefs()
        if preflist == "Error":
            return print("Seçim dosyaları bulunamadı, ana değerler yükleniyor.")
        else:
            Prefs.remember_input_preferance = preflist[0]
            Prefs.pref_input = preflist[1]
            return "Ayarlar Başarıyla Yüklendi."        
    def savePrefs():
        with open("prefs.ini","w") as file:
            file.write(str(Prefs.remember_input_preferance) + "\n")
            file.write(str(Prefs.pref_input) + "\n")
        print(Fore.CYAN + "BİLGİ: Başarıyla Kaydedildi, çıkış yapılıyor..." + Style.RESET_ALL)
        return exit()
    # Preferance Dialog Functions       
    def inputprefer(x):
        if x == False: # Controls if it is starting screen or not
             Prefs.remember_input_preferance = False
        if Prefs.remember_input_preferance == True:
            if Prefs.pref_input == "Microphone":
                return MainFuncs.cli_microphone()
            elif Prefs.pref_input == "Text":
                return MainFuncs.cli_text()  
        else:
            print(Fore.BLUE + "Hangi Şekilde girdi vermek istersiniz?\n1) Mikrofon\n2) Yazı\nçıkış) Çıkış Yap")
            choice = input(Fore.WHITE + "Lütfen bir sayı giriniz (1,2,çıkış): ")
            while choice != "1" and choice !="2" and choice != "çıkış":
                choice = input(Fore.RED + "Geçersiz değer lütfen tekrar deneyiniz (1,2,çıkış): " + Fore.GREEN)
            if choice == "çıkış":
                exit()
            print(Fore.BLUE + "Seçimin kaydedilmesini ister misiniz? (1- Evet / 2- Hayır)")
            choice2 = input("(1/2)?")
            while choice2 != "1" and choice2 !="2" and choice2 != "çıkış":
               choice2 = input(Fore.RED + "Geçersiz değer lütfen tekrar deneyiniz (1,2,çıkış): " + Fore.GREEN)  
            if choice2 == "çıkış":
                exit()
            Prefs.remember_input_preferance = True if choice2 == 1 else Prefs.remember_input_preferance == False
            if choice ==  "1":
                Prefs.pref_input = "Microphone"
                return MainFuncs.cli_microphone()
            if choice =="2":
                Prefs.pref_input = "Text"
                return MainFuncs.cli_text()  
    # Main Preferance Variables and Default Values
    remember_input_preferance = False
    pref_input = "Microphone"
class MainFuncs:
    def selectApp(input):
        if input in Apps.appdict.keys():
            return eval(Apps.appdict[input])
        else:
            print(Fore.LIGHTRED_EX + "Bilinmeyen Komut Lütfen tekrar deneyiniz." + Fore.LIGHTBLUE_EX)
            if Prefs.pref_input == "Microphone":
                return MainFuncs.cli_microphone()
            elif Prefs.pref_input == "Text":
                return MainFuncs.cli_text()
    
    def getInput():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print(Fore.BLACK+">> Dinleniyor🎧... Lütfen sesli bir komut söyleyiniz 🎤\n"+Style.RESET_ALL)
            audio = r.listen(source)
        try:
            return r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("Sesin anlaşılamadı lütfen tekrar konuş:")
            return MainFuncs.getInput()
        except sr.RequestError as e:
            print("Google API Hatası; {0}".format(e) + "lütfen internet bağlantınızı kontrol edin.")
            return MainFuncs.cli_microphone()
    def cli_start():
        # Essential Functions for starting
        Prefs.importPrefs()
        print(Style.RESET_ALL) # To reset style, actually basically not that important.
        print(Fore.GREEN +"~"*60 + Fore.CYAN)
        ascii_art = '''
  _                       _     _                __   ___  
 | |                     (_)   | |              /_ | / _ \ 
 | | _____  _ __ __ _ ___ _ ___| |_ __ _ _ __    | || | | |
 | |/ / _ \| '__/ _` / __| / __| __/ _` | '_ \   | || | | |
 |   < (_) | | | (_| \__ \ \__ \ || (_| | | | |  | || |_| |
 |_|\_\___/|_|  \__,_|___/_|___/\__\__,_|_| |_|  |_(_)___/ 
                                                           
                                                           '''
        print(ascii_art)
        print(Fore.GREEN +"~"*60)
        return Prefs.inputprefer(True)
    def cli_microphone():
        print(f"\n{Style.RESET_ALL}{Fore.GREEN}* Kabul edilebilir komutlar: {Apps.cmds}")
        input = MainFuncs.getInput()
        MainFuncs.selectApp(input)
    def cli_text():
        print(f"\nKabul edilebilir girdiler: {Apps.cmds}")
        u_input = input(Fore.BLACK+ ">> Lütfen girdi yazınız: "+ Style.RESET_ALL)
        while u_input== "":
            print(Fore.RED + "Unvalid value please try again." + Style.RESET_ALL)
            u_input = input("Please enter input: ")
        MainFuncs.selectApp(u_input)        
class Apps:
    # With this modular dictionary, you can easily add more functions just typing.
    appdict = {"not al":"Apps.note()", 
               "hava durumu":"Apps.weather()",
               "şifre oluştur": "Apps.passgen()",
               "haberler":"Apps.news()",
               "girdi değiştir":"Prefs.inputprefer(False)",
               "çıkış":"Prefs.savePrefs()"}
    
    # This list returns the keys but more readable.
    cmds = (Fore.LIGHTMAGENTA_EX + "")
    for i in appdict.keys():
        if i == list(appdict.keys())[-1]:
            cmds+=f"{i}"
        else:
            cmds+=f"{i}, "
    def note():
        app.Note.dialog()
        return Apps.another_action()
    def weather():
        app.Weather.dialog()
        return Apps.another_action()
    def passgen():
        app.Passgen.dialog()
        return Apps.another_action()
    def news():
        app.News.dialog()
        return Apps.another_action()

    def another_action():
        print(f"{Fore.YELLOW}\nBaşka bir işlem yapmak ister misiniz?")
        choice = input(f"(1. Evet / 2. Hayır): {Style.RESET_ALL}")
        while choice != "1" and choice != "2":
            print(Fore.RED + "Geçersiz seçim. Lütfen tekrar deneyiniz.." + Style.RESET_ALL)
            choice = input("(1-> Evet / 2-> Hayır): ")
        if choice == "1":
            return MainFuncs.cli_start()
        elif choice == "2":
            return Prefs.savePrefs()
# Trigger

MainFuncs.cli_start()
