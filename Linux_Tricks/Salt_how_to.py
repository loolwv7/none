
 主题纲要:
 1.关于运维
 2.为什么要自动化
 3.自动化的选型
 4.关于salt
 5.运维的智能化
 6.理想中的运维
 记saltstack与zabbix的一次联姻

 副标题: 基于saltstack结合zabbix完成服务自动化部署及监控

 主题纲要:
 1. saltstack与zabbix双方概况介绍
 2. 联姻第一步之saltstack完成zabbix安装部署
 3. 联姻第二步之saltstack完成memcached服务部署
 4. 联姻第三步之saltstack将服务标签传递给zabbix api操作机进行主机添加及服务模板关联


= Saltstack運維自動化 =
== 关于运维 ==
每天大量重複與機器打交道，保證業務網絡和系統正常運行
install Salt at Gentoo 
emerge slat

2, Start slat master server
#/etc/salt/master
# The address of the interface to bind to:
interface: 0.0.0.0

/etc/init.d/slat-master start

3, install slat-minion Client
# sed '/^#/d;/^$/d' /etc/salt/minion 
master: 192.168.1.111

/etc/init.d/slat-minion start

4, How to use Slat?
brightmoon ~ # salt-key -A
The following keys are going to be accepted:
Unaccepted Keys:
windows2003-test01
Proceed? [n/Y] y 
Key for minion windows2003-test01 accepted.

brightmoon ~ # salt-key -L
Accepted Keys:
brightmoon
windows2003-test01
Unaccepted Keys:
Rejected Keys:



# Match all minions:
salt '*' test.ping

salt brightmoon cmd.run 'echo "hello $CITY"' env='{CITY: "Salt Lake City"}' runas=merlyn


#Match all minions in the example.net domain or any of the example domains:
salt '*.example.net' test.ping
salt '*.example.*' test.ping

#Match all the webN minions in the example.net domain (web1.example.net, web2.example.net … webN.example.net):
salt 'web?.example.net' test.ping

#Match the web1 through web5 minions:
salt 'web[1-5]' test.ping

#Match the web1 and web3 minions:
salt 'web[1,3]' test.ping

#Match the web-x, web-y, and web-z minions:
salt 'web-[x-z]' test.ping

# Lists At the most basic level, you can specify a flat list of minion IDs:
salt -L 'web1,web2,web3' test.ping

# Match all CentOS minions:
salt -G 'os:CentOS' test.ping
brightmoon ~ # salt -G 'os:gentoo' test.ping
brightmoon:
    True

#Note that a leading not is not supported in compound matches. Instead, something like the following must be done:
salt 'brightmoon' grains.items
salt -C S@192.168.1.0/24 test.ping

# Gentoo about
salt '*' service.available sshd
salt '*' gentoolkit.revdep_rebuild
brightmoon:
    True


# install package(s)!
brightmoon ~ # salt '*' pkg.install app-text/dos2unix
brightmoon:
    ----------
    app-text/dos2unix:
        ----------
        new:
            6.0.6
        old:
# Windows support
# install Client!!!
Salt-Minion-0.17.0-Setup-amd64.exe /S /master=yoursaltmaster /minion-name=yourminionname

brightmoon ~ #  salt 'windows2003-test01' user.list_users
windows2003-test01:
    - Administrator
    - Guest
    - HelpAssistant
brightmoon ~ #  salt 'windows2003-test01' user.setpassword administrator 'xxxxxx'
windows2003-test01:
    True

# Reboot/Shutdown system
salt '*' system.reboot
salt '*' system.shutdown

#Set the Windows computer description
salt 'minion-id' system.set_computer_desc 'This computer belongs to Merlyn!'

# Shutdown a running system with no timeout or warning
salt '*' system.shutdown_hard



# Salt group support
 Node Groups
       Often the convenience of having a predefined group of minions to execute targets on is desired. This can be accomplished  with  the  new  nodegroups
       feature. Nodegroups allow for predefined compound targets to be declared in the master configuration file:

          nodegroups:
            group1: 'L@foo.domain.com,bar.domain.com,baz.domain.com and bl*.domain.com'
            group2: 'G@os:Debian and foo.domain.com'

       And then used via the -N option:

          salt -N group1 test.ping

