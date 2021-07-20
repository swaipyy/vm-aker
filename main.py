import os
import dircreator
import isod
import stdiomask
import vmcreator
import scriptc
import banner

def main():
    banner.wm_aker()
    input("Welcome to vm-aker your vm maker assistant! press enter to continue: ")
    dircreator.create_dir()
    isod.download()
    vmcreator.vm()

main = main()

