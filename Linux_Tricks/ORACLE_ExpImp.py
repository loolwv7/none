http://allthingsoracle.com/migrating-a-2tb-database-to-a-new-operating-system-with-different-endianness/

nohup impdp system/secret NETWORK_LINK=olddb FULL=y  PARALLEL=25 &

impdp system attach
Import> status
Import> parallel=30 << this will increase the parallel processes if you want

