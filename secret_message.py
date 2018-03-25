import os
import twilio

def rename_secret():
    file_list = os.listdir(r"E:\prank")
    print (file_list)
    old_dir = os.getcwd()
    os.chdir(r"E:\prank")

    #changing the file name using translate function

    for list_item in file_list:
        os.rename(list_item,list_item.translate(None,"0123456789"))
    
    os.chdir(old_dir)
    return

rename_secret()
