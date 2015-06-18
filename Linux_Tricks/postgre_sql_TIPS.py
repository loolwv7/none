http://www.postgresql.org/docs/9.3/static/sql-alterrole.html
http://www.cyberciti.biz/faq/howto-add-postgresql-user-account/

1, show database in psql
SELECT oid,* from pg_database;


2, Convert mysql to postgresql.
gpg2 --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
curl -sSL https://get.rvm.io | bash -s stable --ruby
gem uninstall  postgres-pr

3, Change a role's password:

ALTER ROLE davide WITH PASSWORD 'hu8jmn3';

4, Remove a role's password:

ALTER ROLE davide WITH PASSWORD NULL;

5, Change a password expiration date, specifying that the password should expire at midday on 4th May 2015 using the time zone which is one hour ahead of UTC:

ALTER ROLE chris VALID UNTIL 'May 4 12:00:00 2015 +1';

6, Make a password valid forever:

ALTER ROLE fred VALID UNTIL 'infinity';


7) export & import Postgres DB

# export with compress
pg_dump -Fc -U openerp -D openerp > openerp.dump
pg_restore -U openerp -d openerp openerp.dump

# export without compress
pg_dump -U openerp -d openerp > openerp.dump
psql -U openerp -d openerp -f openerp.dump

http://codenote.net/psql/1442.html
CREATE EXTENSION
ERROR:  must be owner of extension plpgsql
 
WARNING:  no privileges could be revoked for ``public''
WARNING:  no privileges were granted for ``public''
