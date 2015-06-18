= QRencode =
{{{
cat >> my_vcardinfo.txt <<"EOF"
BEGIN:VCARD
VERSION:3.0
N:Washko, Daniel
ORG:Linux in the Shell
TITLE:Host
EMAIL;TYPE=PREF,INTERNET: dann@thelinuxlink.net
END:VCARD
EOF
}}}

== ZBar recognizes several kinds of bar codes, including QR codes. ==
zbarimg -d myVcard.png 
{{{
QR-Code:BEGIN:VCARD
VERSION:3.0
N:Washko, Daniel
ORG:Linux in the Shell
TITLE:Host
EMAIL;TYPE=PREF,INTERNET: dann@thelinuxlink.net
END:VCARD
}}}

qrencode -o myVcard.png < my_vcardinfo.txt


[[http://www.qrcode-monkey.com/#custom-image|with company log QR]]

[[https://www.unitag.io/qrcode]]

http://www.linuxintheshell.org/2012/03/01/entry-001-qrencode/
