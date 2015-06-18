1) 
mkdir -p /var/www/moinmoin
virtualenv /var/www/moinmoin/python-env
cd /tmp/moin-1.9.8
source /var/www/moinmoin/python-env/bin/activate
python setup.py install
cp -rv ./wiki /var/www/moinmoin
cd /var/www/moinmoin/wiki
cp -v config/wikiconfig.py ./
cp -v server/moin.wsgi ./

# vi moin.wsgi
sys.path.insert(0, '/var/www/moinmoin/python-env/lib64/python2.7/site-packages')

2) uwsgi
==>> /etc/init.d/uwsgi2
#!/sbin/runscript
 
UWSGI_CONF="/etc/uwsgi.d/uwsgi.ini"
UWSGI_LOG="/var/log/uwsgi.log"
UWSGI_PID="/var/run/uwsgi.pid"
#UWSGI_OPTS="-x $UWSGI_CONF -d $UWSGI_LOG --vacuum  --plugin python33  --enable-threads --pidfile $UWSGI_PID"
UWSGI_OPTS="--ini $UWSGI_CONF -d $UWSGI_LOG --pidfile $UWSGI_PID"
 
depend() {
    need net
    use nginx
}
 
start() {
    ebegin "Starting uwsgi server"
    start-stop-daemon --start --exec /usr/bin/uwsgi -- $UWSGI_OPTS
    eend $? "Failed to start uwsgi"
}
 
stop() {
    ebegin "Stopping uwsgi server"
    kill -HUP `pidof uwsgi` &> /dev/null
    sleep 3
    eend $? "Failed to stop uwsgi"
}


==>> cat /etc/uwsgi.d/uwsgi.ini 
[uwsgi]
socket = /tmp/uwsgi.sock
chmod-socket = 777
plugin = python27

chdir = /var/www/moinmoin/wiki
wsgi-file = /var/www/moinmoin/wiki/moin.wsgi

master
workers = 2
max-requests = 20
harakiri = 60




https://wiki.archlinux.org/index.php/Moinmoin
http://garfileo.is-programmer.com/2011/4/24/run-moinmoin-on-uwsgi-and-nginx.26347.html
