import os
import banner

def download():
    while True:
        os.system("clear")
        banner.wm_aker()
        default_dir = ("~/Documents/")
        vm_folder = input("Set the dir of your vm (not need to add ~/Documents/): ")
#    wget = os.system("wget " + mirror + " -P " +default_dir +vm_folder)
        distro = input('''
Now select one of the supported iso's
[1]Arch linux
[2]Debian
Your iso: ''')
        if distro == "1":
            os.system("clear")
            banner.wm_aker()
            arch_mirror = input('''
Now select one of the supported mirror's
[1]Brazil
[2]Worldwide
Your option: ''')
            if arch_mirror == "1":
                mirror = "http://br.mirror.archlinux-br.org/iso/2021.07.01/archlinux-2021.07.01-x86_64.iso"
                try:
                    os.system("wget " + mirror + " -P " +default_dir +vm_folder)
                    break
                except:
                    print("Something is wrong!")
            elif arch_mirror == "2":
                mirror = "http://mirrors.evowise.com/archlinux/iso/2021.07.01/archlinux-2021.07.01-x86_64.iso"
                try:
                    os.system("wget " + mirror + " -P " +default_dir +vm_folder)
                    break
                except:
                   print("something is wrong!")
        elif distro == "2":
            mirror = "https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-10.10.0-amd64-netinst.iso"
            try:
                os.system("wget " + mirror + " -P " +default_dir +vm_folder)
                break
            except:
                print("something is wrong!")
                
#main = download()
    
