If you want resize/resue you disk, you can use parted.


 Command: rescue START END
     Rescue a lost partition that used to be located approximately
     between START and END.  If such a partition is found, Parted will
     ask you if you want to create a partition for it.  This is useful
     if you accidently deleted a partition with parted's rm command,
     for example.

     Example:

          (parted) print
          Disk geometry for /dev/hdc: 0.000-8063.507 megabytes
          Disk label type: msdos
          Minor    Start       End     Type      Filesystem  Flags
          1          0.031   8056.032  primary   ext3
          (parted) rm
          Partition number? 1
          (parted) print
          Disk geometry for /dev/hdc: 0.000-8063.507 megabytes
          Disk label type: msdos
          Minor    Start       End     Type      Filesystem  Flags

     OUCH!  We deleted our ext3 partition!!!  Parted comes to the
     rescue...
(parted) rescue
          Start? 0
          End? 8056
          Information: A ext3 primary partition was found at 0.031MB ->
          8056.030MB.  Do you want to add it to the partition table?
          Yes/No/Cancel? y
          (parted) print
          Disk geometry for /dev/hdc: 0.000-8063.507 megabytes
          Disk label type: msdos
          Minor    Start       End     Type      Filesystem  Flags
          1          0.031   8056.032  primary   ext3

     It's back!  :)		12-28-2010
