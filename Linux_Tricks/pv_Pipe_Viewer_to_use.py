 (tar cf - . | pv -n -s `du -sb . | awk '{print $1}'` | gzip -9 > ../out.tgz) 2>&1 | dialog --gauge 'Progress' 7 70

pv -cN source < Downloads/all-20071007.tar.bz2 | bzcat | pv -cN bzcat | gzip -9 | pv -cN gzip > ok.tar.gz

tar -czf - . | pv > out.tgz

pv /dev/zero > /dev/null

pv -w 2 linux-source.tar.bz2 | tar -xjf -
tar -czf - . | pv > out.tgz

