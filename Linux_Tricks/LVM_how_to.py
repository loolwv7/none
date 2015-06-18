/dev/hdc media not found:
lvmdiskscan
pvcreate /dev/sdb
vgextend VolGroup00 /dev/sdb
lvcreate -l 100%FREE -n toshiba VolGroup00
mkfs.ext4 /dev/VolGroup/toshiba
