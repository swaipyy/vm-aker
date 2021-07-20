import os
import banner
import scriptc

def vm():
    os.system("clear")
    banner.wm_aker()
    vm_dir = input("Please set the wm dir: ")
    home_dir =os.environ['HOME']
    path = (home_dir + "/Documents/" + vm_dir)
    os.chdir(path)
    space = input("Enter in G the space of the virtual disk (example: 20G): ")
    os.system("qemu-img create -f qcow2 disk.qcow2 " + space)
    os.system("clear")
    banner.wm_aker()
    scriptc.create_script()
    vm_dir = input("Please set the wm dir: ")
    path = (home_dir + "/Documents/" + vm_dir)
    os.chdir(path)
    os.system("ls")
    iso = input("Enter the iso name: ")
    os.system("qemu-system-x86_64 -enable-kvm -m 1024 -cdrom " + iso +" -boot d disk.qcow2")

#main = wm()