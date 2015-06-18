# unshadow /etc/passwd /etc/shadow > passwd.1
# john passwd.1
brightmoon ~ # john passwd.1 
Warning: detected hash type "sha512crypt", but the string is also recognized
as "crypt"
Use the "--format=crypt" option to force loading these as that type instead
Warning: detected hash type "sha512crypt", but the string is also recognized
as "sha512crypt-opencl"
Use the "--format=sha512crypt-opencl" option to force loading these as that
type instead
Loaded 4 password hashes with 4 different salts (sha512crypt [64/64])
654321           (openstack)
1                (merlyn)

DOC
/usr/share/doc/johntheripper-1.7.9-r6/EXAMPLES.bz2

