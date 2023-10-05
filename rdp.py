import os

print("Идет установка...")

os.system("wget https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb")

os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")

os.system("wget https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64&lang=en-US")

os.system("sudo apt install ./chrome-remote-desktop_current_amd64.deb")

os.system("sudo apt install ./google-chrome-stable_current_amd64.deb")

os.system("cd ~/Downloads")

os.system("clear")

print("Подождите, распакуем файлы...")

os.system("tar xjf firefox-*.tar.bz2")

os.system("clear")

print("Установка...")

os.system("sudo mv firefox /opt")

os.system("sudo ln -s /opt/firefox/firefox /usr/local/bin/firefox")

os.system("sudo wget https://raw.githubusercontent.com/mozilla/sumo-kb/main/install-firefox-linux/firefox.desktop -P /usr/local/share/applications")

os.system("""
sudo DEBIAN_FRONTEND=noninteractive \
    apt install --assume-yes xfce4 desktop-base dbus-x11 xscreensaver""")
    
with open("file.txt", "r") as file:
    os.system(f"file.read()")
    
os.system("sudo systemctl disable lightdm.service")

text = input("Зайдите на сайт https://remotedesktop.google.com/headless, потом нажмите Начать, потом нажмите Далее, потом нажмите Авторизовать, скопируйте, где Debian Linux и вставьте сюда: ")

with open("file1.txt", "w") as file1:
	file1.write("text")
	
with open("file1.txt", "r") as file2:
	os.system(f"{file2.read()}")
	
os.system("clear")

print("Успешно установлено!")
