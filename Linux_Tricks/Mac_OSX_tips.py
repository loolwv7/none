= Mac OSX =
== How to create OSX bootable usb on Linux ==
{{{
dmg2img -v -i /path/to/MacOSX_image_file.dmg -o /path/to/image_file.iso
dd if=/path/to/MacOSX_image_file.iso of=/dev/sdb && sync
}}}
OR make it direct.
{{{
dmg2img -v -i /path/to/image_file.dmg -o /dev/sdb
}}}


== How to Clean Install OS X Yosemite on Your Mac ==
http://www.ibtimes.co.uk/how-clean-install-os-x-yosemite-via-bootable-usb-flash-drive-1470625

Step 1: Ensure the bootable USB flash drive is plugged into your Mac and
restart the computer. As soon as the start-up chime plays, press the Option key
(Alt).

Step 2: Choose the USB drive on the start-up drive selection screen and hit
Enter/Return on the keyboard.

Step 3: Wait until the Yosemite installer appears on screen. This could take a
few seconds or minutes.

Step 4: Click on Disk Utility and then hit Continue.

Step 5: Click on Macintosh HD from the left hand-side pane and then hit Erase
tab on the top-right portion of the window. Leave all the settings at their
default values and then hit Erase button at the bottom right. This will wipe
all files stored on your startup hard drive.

Step 6: When the erasing process is complete, return to the first screen where
you selected Disk Utility. Now click on Install OS X and then hit Continue.

Step 7: Choose the Macintosh HD partition you erased in step 5 and then click
Install.

If you have followed all the steps correctly, your computer should now boot
right into the newly installed operating system, OS X Yosemite, and you could
cherish its stunning new UI.

==  Triple boot Linux, Windows and Mac using Grub2 ==
http://www.tuxtrix.com/2014/03/triple-boot-linux-windows-and-mac-using.html

 Edit /etc/grub.d/40_custom using your favourite text editor and paste in the
 following

 menuentry "MacOS X 10.8" {
          insmod hfsplus
          set root=(hd0,msdos8) #change X to the Mac SL
          partition
          multiboot /boot
}





== Reference ==

http://www.macbreaker.com/2012/02/how-to-update-mac-os-x-lion-on-your-pc.html

http://superuser.com/questions/505821/making-a-bootable-osx-usb-from-dmg-on-linux

http://www.hackintosh.com/#hackintosh_tutorials1
