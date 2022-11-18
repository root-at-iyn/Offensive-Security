# Quick Reference on Using Frida

## Setup

- To get Frida working, you need to download the archive from GitHub and then extract the binary. 
- Once you have extracted the bin, copy the server to the device
- Make the server bin executable
- Start the server 

## Commands

### Copy the server to the device
adb push ./frida-server-$version-android-$arch /data/local/tmp/frida-server
        ^Change this to match the name of the binary you just extracted

### Enable root access to the device
adb root

### Make the server binary executable
adb shell "chmod 755 /data/local/tmp/frida-server"

### Start the server on your device
adb shell "/data/local/tmp/frida-server &"
