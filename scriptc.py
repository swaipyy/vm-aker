import os

def create_script():
    home_dir =os.environ['HOME']
    path = (home_dir + "/.local/bin/")
    os.chdir(path)
    vm_path = input("enter the path of the vm: ")
    name = input("enter the name of the vm: ")
    ram = input("enter the amount of ram in mb: ")
    with open(name + '.sh', 'w') as f:
        f.writelines("#!/bin/sh\n" + "qemu-system-x86_64 -enable-kvm -m " + ram + "\n" + "-daemonize " + home_dir + "/Documents/" + vm_path + "disk.qcow2")
        f.close()
    os.system("chmod +x " + name + ".sh")

#main = create_script()

