cat xxx.iso | cdrecord -v dev=/dev/cdrom speed=10 fs=8m -tao -eject -data -
growisofs -dvd-compat -Z /dev/dvd=xxx_dvd.iso
growisofs -Z /dev/dvd -R -J /folder/

mkisofs -fRrlJ -A Disc_Volume_Label -o - name_of_folder | sudo cdrecord dev=/dev/cdrom -

mkisofs -fRrlJ -A Disc_Volume_Label_Goes_Here -o name_of_iso_file.iso name_of_folder
