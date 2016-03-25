= LUKFS =
== benchmark it ==
cryptsetup benchmark 

== Create cryptographic device mapper device in LUKS encryption mode ==
# cryptsetup --verbose --hash sha512 --iter-time 5000 --use-random luksFormat /dev/sdb3

WARNING!
========
This will overwrite data on /dev/sdb3 irrevocably.

Are you sure? (Type uppercase yes): YES
Enter passphrase: 
    Verify passphrase: 
        device-mapper: remove ioctl on temporary-cryptsetup-2361 failed: Device
        or resource busy
        Command successful.

# cryptsetup status test
# cryptsetup close test

== Verify the results of your handiwork ==
{{{
# cryptsetup luksDump /dev/sdb3 
LUKS header information for /dev/sdb3

Version:        1
Cipher name:    aes
Cipher mode:    xts-plain64
Hash spec:      sha1
Payload offset: 4096
MK bits:        256
MK digest:      45 ec 34 04 6f 81 c4 8c aa e1 3c d9 99 0c fd 92 c7 d0 eb d9 
MK salt:        9a 56 93 8c 04 cf 4d b7 2d 01 14 b8 a8 ff 4a d8 
                e7 81 03 51 79 96 1a 28 dc 66 44 5f 29 c1 1a 60 
MK iterations:  21125
UUID:           e84fc348-8b36-41b6-86d3-f4ff18410f48

Key Slot 0: ENABLED
        Iterations:             84993
        Salt:                   95 eb 99 ee 53 94 8f 4d 9f 97 47 e4 4e 69 6d d0 
                                0b b1 92 b6 a1 11 51 0d 29 89 a2 92 20 84 d0 f8 
        Key material offset:    8
        AF stripes:             4000
Key Slot 1: DISABLED
Key Slot 2: DISABLED
Key Slot 3: DISABLED
Key Slot 4: DISABLED
Key Slot 5: DISABLED
Key Slot 6: DISABLED
Key Slot 7: DISABLED
}}}

== Create a device we can map to ==
# cryptsetup luksOpen /dev/sdb3 test   (( Old options ))
OR
# cryptsetup open --type luks /dev/sdb3 test

== Format with your filesystem of choice ==
{{{
# mkfs.ext4 -m 0 /dev/mapper/test 
mke2fs 1.42.12 (29-Aug-2014)
Creating filesystem with 8257196 4k blocks and 2064384 inodes
Filesystem UUID: 62b629f7-8b13-4726-8789-e1f9584830ec
Superblock backups stored on blocks: 
        32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208, 
        4096000, 7962624

Allocating group tables: done                            
Writing inode tables: done                            
Creating journal (32768 blocks): done
Writing superblocks and filesystem accounting information: done 
}}}

== Mounting it! ==
# mount /dev/mapper/test /mnt/zip/ -v
# cryptsetup status test
/dev/mapper/test is active and is in use.
  type:    LUKS1
  cipher:  aes-xts-plain64
  keysize: 256 bits
  device:  /dev/sdb3
  offset:  4096 sectors
  size:    66057568 sectors
  mode:    read/write

== Unmount and close it ==
# umount /mnt/zip  
# cryptsetup close test



== TIPS ==
To mount the encrypted partition remotely e.g. when it detects a reboot (or just hourly. It seems harmless to run lots):

ssh -tti host.pem ec2-user@ip sudo cryptsetup open --type luks /dev/xvdf my_enc_fs < password-in-this-file
ssh -tti host.pem ec2-user@ip sudo mount /dev/mapper/my_enc_fs /encrypted_vol

Great instructions.

=== USE keyfile ===
# dd bs=512 count=4 if=/dev/urandom of=/etc/mykeyfile iflag=fullblock
# chmod 0400 /etc/mykeyfile

# cryptsetup luksAddKey /dev/sdb3 /etc/mykeyfile
sudo cryptsetup luksRemoveKey /dev/sdb1 /etc/mykeyfile
sudo cryptsetup luksOpen /dev/sdb1 systec --key-file /etc/mykeyfile 
# cat /etc/crypttab 
test /dev/sdb3  /etc/mykeyfile luks

# tail -1 /etc/fstab
/dev/mapper/test        /mnt/sdb3     ext4    defaults        0       0



==  Slot about ==
sudo cryptsetup luksKillSlot /dev/sdb1 1

== Reference ==

https://www.linux.com/learn/tutorials/836841-how-to-encrypt-a-linux-file-system-with-dm-crypt

http://silvexis.com/2011/11/26/encrypting-your-data-on-amazon-ec2/

https://www.howtoforge.com/tutorial/how-to-encrypt-a-linux-partition-with-dm-crypt-luks/

== extend LUKFS lv ==
{{{
root@darkstar:~# df -h
Filesystem        Size  Used Avail Use% Mounted on
/dev/root         1.4G  341M  1.1G  24% /
/dev/sda1          54M  9.3M   42M  19% /boot
tmpfs             496M     0  496M   0% /dev/shm
/dev/mapper/apps  1.6G  208M  1.4G  13% /opt/apps

root@darkstar:~# pvcreate /dev/sdb
Physical volume "/dev/sdb" successfully created
root@darkstar:~# vgextend vg_systec /dev/sdb 

root@darkstar:~# ls /opt/apps/
apache-tomcat-7.0.63/  jre1.7.0_80/  lost+found/  mysql/
root@darkstar:~# umount  /opt/apps/

root@darkstar:~# cryptsetup luksClose apps
root@darkstar:~# lvextend -L +1G /dev/vg_systec/apps 
Extending logical volume apps to 2.61 GiB
Logical volume apps successfully resized

root@darkstar:~# cryptsetup luksOpen /dev/mapper/vg_systec-apps apps --key-file /opt/.mykeyfile
root@darkstar:~# cryptsetup --verbose resize apps
Command successful.

root@darkstar:~# fsck.ext4 -f /dev/mapper/apps 
e2fsck 1.41.14 (22-Dec-2010)
Pass 1: Checking inodes, blocks, and sizes
Pass 2: Checking directory structure                                           
Pass 3: Checking directory connectivity
Pass 4: Checking reference counts
Pass 5: Checking group summary information
/dev/mapper/apps: 1706/105664 files (0.8% non-contiguous), 59761/422400  blocks 

root@darkstar:~# resize2fs /dev/mapper/apps 
resize2fs 1.41.14 (22-Dec-2010)
Resizing the filesystem on /dev/mapper/apps to 684544 (4k) blocks.
The filesystem on /dev/mapper/apps is now 684544 blocks long.

root@darkstar:~# mount /dev/mapper/apps /opt/apps/
root@darkstar:~# df -h
Filesystem        Size  Used Avail Use% Mounted on
/dev/root         1.4G  341M  1.1G  24% /
/dev/sda1          54M  9.3M   42M  19% /boot
tmpfs             496M     0  496M   0% /dev/shm
/dev/mapper/apps  2.6G  208M  2.4G   8% /opt/apps
}}}
http://www.gigahype.com/resize-luks-encryped-lvm-partition/
http://jordanconway.com/grow-luks-encrypted-lvm-home-partition/
