#format wiki
#language zh-tw
= Ansible Configuration Management =
<<TableOfContents>>
== What is ansible ==
Ansible is an extra-simple tool/framework/API for doing 'remote things' over SSH.
Radically simple deployment, model-driven configuration management, and command execution framework

== Installation ==
{{{
emerge -v ansible
ssh-keygen -t rsa -P""
cat .ssh/id_rsa.pub >> .ssh/authorized_keys
chmod 600 .ssh/authorized_keys
}}}

Send authorized_keys to another hosts client.
{{{
cat .ssh/authorized_keys | ssh root@192.168.200.223 "cat >> .ssh/authorized_keys; chmod 600 .ssh/authorized_keys"
}}}
 *OR USE ansible to copy!!
note: you must [[#hosts|ADD HOSTS]] to /etc/ansible/hosts file first.
{{{
ansible ocean -m copy -a 'src=/root/.ssh/authorized_keys dest=/home/grid/.ssh'
192.168.200.12 | success >> {
    "changed": true,
    "checksum": "1cd306386686d791b84177a8c841a8ae2c6d6326",
    "dest": "/home/grid/.ssh/authorized_keys",
    "gid": 54321,
    "group": "oinstall",
    "md5sum": "2b332b200801d79c168d1fb32c4aa1d9",
    "mode": "0644",
    "owner": "grid",
    "size": 1193,
    "src": "/root/.ansible/tmp/ansible-tmp-1429499411.86-239017334470751/source",
    "state": "file",
    "uid": 54322
}

192.168.200.11 | success >> {
    "changed": true,
    "checksum": "1cd306386686d791b84177a8c841a8ae2c6d6326",
    "dest": "/home/grid/.ssh/authorized_keys",
    "gid": 54321,
    "group": "oinstall",
    "md5sum": "2b332b200801d79c168d1fb32c4aa1d9",
    "mode": "0644",
    "owner": "grid",
    "size": 1193,
    "src": "/root/.ansible/tmp/ansible-tmp-1429499411.89-113195298797023/source",
    "state": "file",
    "uid": 54322
}
}}}

== How to use ==
<<Anchor(hosts)>>

=== add hosts ===
{{{
cat /etc/ansible/hosts 
[dhcp]
192.168.200.3
[ocean]
192.168.200.[11:12]
[local]
127.0.0.1
[ESXi]
172.18.22.[201:206]
172.18.22.[211:220]
}}}

=== Ready to excute ===
In Ansible manager host. First, let’s set up SSH-agent so it can remember our credentials
{{{
ssh-agent bash
ssh-add ~/.ssh/id_rsa
}}}

Now to run the command on all servers in a group, in this case, ocean, in 10 parallel forks:
default is 5.
{{{
ansible ocean -a "/sbin/reboot" -f 10
}}}


=== use module ===
 * Gathering Facts
just to get ad-hoc information about your system
{{{
ansible 127.0.0.1 -m setup
}}}

{{{
ansible all -m ping
ansible all -m shell -a 'df -h'
# as bruce
ansible all -m ping -u bruce
# as bruce, sudoing to root
ansible all -m ping -u bruce --sudo
# as bruce, sudoing to batman
ansible all -m ping -u bruce --sudo --sudo-user batman
}}}

ansible all -a "/bin/echo hello"

 * EXAMPLES:
brightmoon ~ # ansible 172.18.22.1 -m copy -a 'src=/root/.ssh/authorized_keys dest=/home/grid/.ssh'
{{{#!highlight python
172.18.22.1 | success >> {
  "changed": true,
  "checksum": "8be4c4e3e182c1f540510bf0d88dc5472dd2b01f",
  "dest": "/home/grid/.ssh/authorized_keys",
  "gid": 6000,
  "group": "oinstall",
  "md5sum": "ef103eb00d6e69d20cca727fbedb3e1e",
  "mode": "0644",
  "owner": "grid",
  "size": 799,
  "src":
  "/root/.ansible/tmp/ansible-tmp-1428915411.68-199979660294699/source",
  "state": "file",
  "uid": 500
}
}}}

{{{
ansible 172.18.22.1 -u grid -m command -a '/g01/app/11.2.0/grid/bin/crsctl status res -t'
ansible all -m raw -a 'export LC_ALL=en_US.UTF-8 ; df -h'
ansible ESXi -m command -a 'uptime'
}}}

{{{
ansible 127.0.0.1 -m raw -a 'df -h | grep "data"'
127.0.0.1 | success | rc=0 >>
/dev/sda3                70G   68G  2.3G  97% /mnt/data
/mnt/dell-data/var       77G   75G  2.8G  97% /var

brightmoon ~ # ansible 127.0.0.1 -m raw -a 'dmesg | egrep -i "error|warn"'
127.0.0.1 | success | rc=0 >>
[    1.342846] i8042: Warning: Keylock active
[    4.007235] Error: Driver 'pcspkr' is already registered, aborting...
[    4.354434] Warning: Processor Platform Limit event detected, but not handled.
[    6.360412] EXT2-fs (sda1): warning: mounting unchecked fs, running e2fsck is recommended
[ 1214.727501] capability: warning: `VirtualBox' uses 32-bit capabilities (legacy support in use)
}}}


==== "msg": "Error: ansible requires a json module ====
[[http://stackoverflow.com/questions/28380771/error-ansible-requires-a-json-module-none-found|How to fix "json err"]]
{{{
ansible -m raw all -a 'uptime'
}}}

=== Man doc ===
USE ansible-doc to show
{{{
ansible-doc command
}}}

=== for Oracle RAC 10/111g ===
{{{
ansible 172.18.22.41 -m raw -u grid -a 'source ~/.bash_profile; crsctl status resource -t'
ansible rac11g  -m raw -a 'cat /root/.ssh/authorized_keys >> /home/grid/.ssh/authorized_keys'
ansible rac10g  -m raw -a 'cat /root/.ssh/authorized_keys >> /u01/app/oracle/.ssh/authorized_keys'

ansible rac11g  -m raw -u grid -a 'source ~/.bash_profile; crsctl status resource -t'
ansible rac10g  -m raw -u oracle -a 'source ~/.bash_profile; crs_stat -t -v'
}}}

=== disable host_key_checking ===
{{{
vi /etc/ansible/ansible.cfg
[defaults]
host_key_checking = False
}}}

=== ESXi host notes ===
127.0.0.1 | FAILED => SSH Error: Permission denied (publickey,password,keyboard-interactive). while connecting to 127.0.0.1:22
{{{
USE -k
ansible local -m ping -k
}}}

=== Managing Services ===
Ensure a service is started on all webservers:
{{{
ansible webservers -m service -a "name=httpd state=started"
}}}
Alternatively, restart a service on all webservers:
{{{
ansible webservers -m service -a "name=httpd state=restarted"
}}}

== Examples copy OSWatcher to collect DATA ==
=== copy OSwatcher to hosts! ===
{{{
ansible dbservers -m copy -a 'src=/tmp/oswbb733.tar dest=/tmp/'
}}}

=== untar oswbb ===
{{{
ansible dbservers1 -m raw -a 'cd /tmp/; tar xvf /tmp/oswbb733.tar'
}}}

=== start oswbb ===
{{{
ansible dbservers1 -m raw -a 'cd /tmp/oswbb/; ./startOSWbb.sh 60 1' -vvvv
}}}

=== stop oswbb ===
{{{
ansible dbservers -m raw -a '/tmp/oswbb/stopOSWbb.sh'
}}}

=== tar oswbb_report ===
{{{
ansible dbservers -m raw -a 'cd /tmp/oswbb; tar -zcvf /tmp/oswbb_`hostname`.tar.gz archive'
}}}

=== copy report files to My host?? ===
{{{
ansible dbservers -m fetch -a 'src=/tmp/oswbb*.gz dest=/tmp/'
}}}

== Cisco switch/router ==
Ansible for Cisco IOS SNMP modules.
https://github.com/networklore/ansible-cisco-snmp
pip install nelsnmp
pip install nelsnmp --upgrade

pip install pycsco

ansible TEST -m raw --ask-pass -c paramiko -a 'show clock'

=== Cisco docker ansible ===
https://github.com/jedelman8/nxos-ansible



=== Playbook how to ===
http://jedelman.com/home/ansible-for-networking/

test.yml
{{{#!highlight python
---
- hosts: testsw
  remote_user: zab
  gather_facts: false
  tasks: 
  - name: copy tftp run
  raw: copy tftp://10.1.78.153/test running-config
}}}

Excution it 

{{{
ansible-playbook test.yml --ask-pass
}}}

For openssh to work with Cisco devices I usually setup my local .ssh/config
like the following:

{{{#!highlight python
Host *
StrictHostKeyChecking no
UserKnownHostsFile=/dev/null
ServerAliveInterval 120
ServerAliveCountMax 2
ControlPath ~/.ssh/master-%r@%h:%p
ControlMain auto
ControlPersist 60s
}}}


== Troubshooting ==
=== ansible unsupported option gssapiauthentication ===

* Your SSH client was built without Kerberos and GSSAPI support.  You
need to rebuld it with "./configure --with-kerberos5" (assuming you
have all of the required bits on your system).

OR

* line 141 of "service.c" has all of the ssh command line. If you remove
-oGSSAPIAuthentication=no and -oVisualHostKey then recompile shellinabox it
works fine. 


https://serversforhackers.com/an-ansible-tutorial

http://www.reddit.com/r/sysadmin/comments/2qb1v2/salt_vs_puppet_vs_ansible_vs/

http://www.saltstack.cn/

http://www.saltstack.cn/projects/cssug-events/wiki/2013-06-30_中国SaltStack用户组之自动化运维专题

http://stackoverflow.com/questions/26141536/run-ansible-single-command-via-ssh

http://stackoverflow.com/questions/26295259/ansible-ad-hoc-commands-dont-work-with-cisco-devices
