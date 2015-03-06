# http://www.feyrer.de/g4u/#imgcreate

Image deployment

    Boot the CD or floppy to the shell prompt again, see above.

    Whole harddisk:
    Type "slurpdisk your.ftp.server.com filename.gz". This will log into the FTP server's "install" account, verify the password, then retrieve the image, uncompress it and write it back to /dev/rwd0d.

    If you want to restore to a SCSI disk, add the disk's name to the slurpdisk command line, e.g. "slurpdisk your.ftp.server.com filename.gz sd0".

    See above if you want to use an account name other than "install".
    One partition:
    Use "slurppart your.ftp.server.com filename.gz wd0e" or whatever values you passed to uploadpart. Please note that the partition information is taken from your MBR, which is expected to be the same as before image creation - expect surprises if you change something between image creation and deployment. In case of inevitable changes, check the start sector and size values given by "parts". For an image that includes the MBR, do a full backup with "uploaddisk".

    Reboot the machine (type "reboot" or press reset button), and see if your machine comes up as expected - it should! 


    4.1 Preparations
        Using the g4u floppy images:
            Download the floppy images, g4u-2.5-1.fs g4u-2.5-2.fs and g4u-2.5-3.fs or g4u-2.5.fs.zip, which contains these files.
            If you downloaded the g4u-2.5.fs.zip file, unpack it to get g4u-2.5-1.fs, g4u-2.5-2.fs and g4u-2.5-2.fs
            Write the two images to two seperate floppy disk. Under Unix, a simple "cat g4u-2.5-1.fs >/dev/diskette" (and same for -2.fs) will do. Make yourself familiar with the name of your floppy device, some common ones are:

                NetBSD: /dev/fd0a
                Solaris: /dev/diskette
                Linux: /dev/fd0 

            There are also similar devices for USB sticks, but you need to grab the g4u.fs from the ISO to put there:

                NetBSD: /dev/sd0d
                Linux: /dev/sd0 

            If you're using Microsoft Windows or DOS, use rawrite.exe. There's also a Windows-based program available called rawr32.zip. 
        Using the g4u CDROM ISO image:
            Download the CDROM ISO image, g4u-2.5.iso or g4u-2.5.iso.zip
            If you downloaded the g4u-2.5.iso.zip file, unpack it to get g4u-2.5.iso
            Please consult your CDROM writing software (Nero, DiskJuggler, WinOnCD, cdrecord, ...) 's manual on how to write the g4u.iso file to a CDROM. Note that the image is bootable. 

        On a FTP server of your choice, create an user-account called "install", and protect it with some password. Make sure the 'install' user can login via ftp (/etc/shells...)

        If you want to use a different account, you can specify "login@server" for slurpdisk, uploaddisk etc..
        Make sure you have a working DHCP server that hands out IP addresses and other data needed to access the FTP server from your workstation (name server, netmask, default gateway). Else you will have to set the IP-number manually.. 

    4.2 Image creation
        Boot the CD or floppy on the machine you want to clone. See it read the kernel from disk, then print out all the devices found in the machine. It will do DHCP next, asking for an IP number - be sure you have DHCP configured properly! At the end you'll get a text description of possible commands, and a shell prompt.

        Whole harddisk:
        Type "uploaddisk your.ftp.server.com filename.gz" to read out the machine's harddisk (rwd0d), and put it into the "install" account of your FTP server under the given filename. The disk image is compressed (with gzip -9), so maybe use a ".gz" file suffix. You don't have to, though. Before putting the file on the FTP server, the "install" account's password is requested.

        If you want to clone your second IDE disk, add it's name on the uploaddisk command line: "uploaddisk your.ftp.server.com filename.gz wd1". Similarly, if you use SCSI instead of IDE disks, use "uploaddisk your.ftp.server.com filename.gz sd0".

        If you want to use a different account name than "install", use "account@your.ftp.server.com" for both uploaddisk and slurpdisk.

        One partition only:
        Get an overview of disks recognized by g4u by typing "disks", a list of partitions on a certain disk is available via "parts disk", where disk is one of the disks printed by "parts", e.g. wd0, wd1, sd0, etc. Partitions are numbered with letters starting from 'a', where partitions a-d are usually predefined, with your partitions starting at 'e'. Partitions here are BSD-partitions, which have little in common with DOS MBR partitions. To specify a partition, use something like "wd0e" or "sd0f": "uploadpart your.ftp.server.com filename.gz wd0e". Run "uploadpart" without arguments for more examples.

        Wait until you're back at the shell prompt (ignore the errors :-). Depending on your network, CPU, harddisk hardware and contents, image creation can take several hours!
        You can switch off the machine now. Type "halt" or simply press reset/power button - there are no filesystems mounted so no harm will result.
        Check that your FTP server's "install" account now has the image file. 

    4.3 Image deployment
        Boot the CD or floppy to the shell prompt again, see above.

        Whole harddisk:
        Type "slurpdisk your.ftp.server.com filename.gz". This will log into the FTP server's "install" account, verify the password, then retrieve the image, uncompress it and write it back to /dev/rwd0d.

        If you want to restore to a SCSI disk, add the disk's name to the slurpdisk command line, e.g. "slurpdisk your.ftp.server.com filename.gz sd0".

        See above if you want to use an account name other than "install".
        One partition:
        Use "slurppart your.ftp.server.com filename.gz wd0e" or whatever values you passed to uploadpart. Please note that the partition information is taken from your MBR, which is expected to be the same as before image creation - expect surprises if you change something between image creation and deployment. In case of inevitable changes, check the start sector and size values given by "parts". For an image that includes the MBR, do a full backup with "uploaddisk".

        Reboot the machine (type "reboot" or press reset button), and see if your machine comes up as expected - it should! 

    4.4 Copying a disk locally
        If you just want to copy one local disk to another one with no network & server involved, the "copydisk" command is what you want. E.g. to copy the first IDE disk to the second IDE disk, use "copydisk wd0 wd1", to do the same for SCSI disks run "copydisk sd0 sd1".

        Beware! All data on the target disk will be erased!

        A list of disks as found during system startup can be found using the "disks" command.

    4.5 Copying a partition locally
        If you want to only copy one local partition to another local partition (similar to what 'uploadpart' and 'slurppart' do, just without the network and FTP in between), this can be done with the 'copypart' command. It takes two partition names as arguments, and copies the contents of one partition to the other. As an example if you found you want to copy your first local partition 'wd0e' to the second one 'wd0f', run:

        copypart wd0e wd0f

        A list of disks can be found using the 'disk' command, to list all the partitions on a disk use the 'parts' command. Partitions have the form of "wd0d", "w1e", "sd1f".

        Be aware that the partitions to copy should have identical size (down to the sector), else funny things will happen. When copying a 'big' partition into a 'small' one, g4u won't thrash the data behind the 'small' partition, but of course the copy is not complete either. Take special note that that case could happen when you restore a copy made that way, and which went fine when you first copied your small working partition to your big backup partition! 




################

# GZIP=1 uploaddisk your.ftp.server.com filename.gz
