import os
import banner

def create_dir():
    os.system("clear")
    banner.wm_aker()
    default_dir = ("~/Documents/")
    vm_folder = input("Set the name of the folder that contain your vm's you can try something like (vm/): ")
    vm_name = input("Set the vm name, try something like (your_name+the_distrubution/): ")
    try:
        os.system("mkdir "+ default_dir + vm_folder + vm_name)
        print("dir created successfully!")
        os.system("clear")
    except:
        print("something is wrong! please check your settings")

#CreateDir = create_dir()
