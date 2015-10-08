== Making a bootable OSX USB from dmg on Linux ==

Install dmg2img

sudo apt-get install dmg2img

Convert DMG image file to ISO file

dmg2img -v -i /path/to/image_file.dmg -o /path/to/image_file.iso

Copy ISO image to USB

sudo dd if=/path/to/image_file.iso of=/dev/sdb && sync

sdb is an example. In your case it might be different
Edit

You can do the conversion and actual writing in one pass, if you don't need the
.iso afterwards: it will take half the time as converting to .iso and THEN
writing to the USB device. Just do:

    sudo dmg2img -v -i /path/to/image_file.dmg -o /dev/sdb

    Again, sdb is an example. In your case it might be different.

