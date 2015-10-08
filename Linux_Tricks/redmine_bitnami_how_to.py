http://www.cyberciti.biz/faq/import-mysql-dumpfile-sql-datafile-into-my-database/
https://github.com/ricardochimal/taps/issues/128
http://adam.herokuapp.com/past/2009/2/11/taps_for_easy_database_transfers/
http://www.redminecrm.com/boards/4/topics/448-installing-redmine-2-5-passenger-nginx-rvm-on-ubuntu-12-04-lts-and-14-04-lts

[root@squid ~]# /opt/redmine-2.2.0-0/mysql/bin/mysql -u bitnami -pb26fce7a77


#mysql
USERNAME:root
PASSWORD:bitnami

1) backup&restore mysql database.
backup:
 /opt/redmine-2.2.0-0/mysql/bin/mysqldump -u root -pbitnami bitnami_redmine > bitnami_redmine.sql
then restore
 /opt/redmine-2.2.0-0/mysql/bin/mysql -u root -pbitnami bitnami_redmine < /root/bitnami_remine.sql

2) Restart mysql&apache
[root@squid scripts]# /opt/redmine-2.2.0-0/ctlscript.sh restart mysql
/opt/redmine-2.2.0-0/mysql/scripts/ctl.sh : mysql stopped
140825 08:18:06 mysqld_safe Logging to '/opt/redmine-2.2.0-0/mysql/data/mysqld.log'.
140825 08:18:06 mysqld_safe Starting mysqld.bin daemon with databases from /opt/redmine-2.2.0-0/mysql/data
/opt/redmine-2.2.0-0/mysql/scripts/ctl.sh : mysql  started at port 3306

[root@squid scripts]# /opt/redmine-2.2.0-0/ctlscript.sh restart apache
Syntax OK
/opt/redmine-2.2.0-0/apache2/scripts/ctl.sh : httpd stopped
Syntax OK
/opt/redmine-2.2.0-0/apache2/scripts/ctl.sh : httpd started at port 80

3) install redmine with nginx
cd redmine 
gem install passenger --no-ri --no-rdoc
passenger-install-nginx-module
bundle install --without development test postgres sqlite
rake generate_secret_token
RAILS_ENV=production rake db:migrate # 生成表结构
RAILS_ENV=production rake redmine:load_default_data $ 初始化数据

#nginx
vi /etc/nginx/nginx.conf

server {
   listen     80;
   server_name localhost; 
   root /var/www/redmine/public; # 确保指向到public目录
   passenger_enabled on;
      }
}

4) select user,host from mysql.user;

5) 
create database bitnami_redmine character set utf8;
grant all privileges on bitnami_redmine.* to 'bitnami'@'localhost' identified by 'bitnami';
flush privileges;
quit;

6) cd redmine 
 ruby script/rails server webrick -e production
 passenger-status

#backup all databases in one file (eventually add the option --add-locks):
mysqldump -u username -p -all-databases > file.sql

#backup all databases in one gzipped file:
mysqldump -u username -p -all-databases | gzip > file.sql.gz

#restore all databases:
mysql -u username -p < file.sql 

7) troubleshooting
https://www.phusionpassenger.com/documentation/Users%20guide%20Nginx.html#_nginx

#Could not find jquery-rails-2.0.0 in any of the sources
bundle update jquery-rails

#update plugins
 rake redmine:plugins:migrate RAILS_ENV="production"

# delete plugins from redmine
rake redmine:plugins:migrate VERSION=0 RAILS_ENV=production NAME=redmine_agile 


# Setting the default Ruby 
rvm --default use 2.0.0
# To switch back to your system ruby: 
rvm use system

# brightmoon redmine # RAILS_ENV=production rake db:migrate
# rake aborted!
#ActiveRecord::StatementInvalid: PG::InsufficientPrivilege: ERROR:  permission denied for relation
schema_migrations

==>> postgresql table role problem!
https://mindlev.wordpress.com/2010/05/26/297/

# worklog error.
==>> resetting the worklog in Adminitrator/Setting page.



8) for postgresql
postgres=# create user bitnami_redmine password 'bitnami' nosuperuser;
CREATE ROLE
postgres=# create database bitnami_redmine owner bitnami_redmine;

# Convert Mysql DB to PostgreSQL DB!!!
http://www.redmine.org/boards/2/topics/12825?r=40571
 taps server mysql://root:bitnami@localhost/bitnami_redmine tmpuser tmppass
 == Sinatra/1.0 has taken the stage on 5000 for production with backup from
 WEBrick
 [2015-03-02 18:28:30] INFO  WEBrick 1.3.1
 [2015-03-02 18:28:30] INFO  ruby 2.2.0 (2014-12-25) [x86_64-linux]
 [2015-03-02 18:28:30] INFO  WEBrick::HTTPServer#start: pid=827 port=5000

taps pull postgres://bitnami_redmine:bitnami@localhost/bitnami_redmine http://tmpuser:tmppass@localhost:5000
Receiving schema
Unable to fetch tables information from http://tmpuser:tmppass@localhost:5000.
Please check the server log.

brightmoon redmine # taps pull postgres://postgres:postgres@localhost/bitnami_redmine
http://tmpuser:tmppass@192.168.2.33:5000
Receiving schema
Schema:          0% |
| ETA:  --:--:--
Schema:          1% |=
| ETA:  00:01:00
Schema:          3% |===
| ETA:  00:00:55

mysqldump --compatible=postgresql --default-character-set=utf8 -r /tmp/bitnami_redmine.sql -u root -p bitnami_redmine
psql dbname < infile

# taps server Arch Linux
[root@127_new redmine]# gem env
RubyGems Environment:
  - RUBYGEMS VERSION: 2.4.6
  - RUBY VERSION: 2.0.0 (2014-11-13 patchlevel 598) [x86_64-linux]
  - INSTALLATION DIRECTORY: /usr/local/rvm/gems/ruby-2.0.0-p598
  - RUBY EXECUTABLE: /usr/local/rvm/rubies/ruby-2.0.0-p598/bin/ruby
  - EXECUTABLE DIRECTORY: /usr/local/rvm/gems/ruby-2.0.0-p598/bin
  - SPEC CACHE DIRECTORY: /root/.gem/specs
  - SYSTEM CONFIGURATION DIRECTORY: /usr/local/rvm/rubies/ruby-2.0.0-p598/etc
  - RUBYGEMS PLATFORMS:
    - ruby
    - x86_64-linux
  - GEM PATHS:
     - /usr/local/rvm/gems/ruby-2.0.0-p598
     - /usr/local/rvm/gems/ruby-2.0.0-p598@global
  - GEM CONFIGURATION:
     - :update_sources => true
     - :verbose => true
     - :backtrace => false
     - :bulk_threshold => 1000
  - REMOTE SOURCES:
     - https://rubygems.org/
  - SHELL PATH:
     - /usr/local/rvm/gems/ruby-2.0.0-p598/bin
     - /usr/local/rvm/gems/ruby-2.0.0-p598@global/bin
     - /usr/local/rvm/rubies/ruby-2.0.0-p598/bin
     - /usr/local/sbin
     - /usr/local/bin
     - /usr/bin
     - /root/.gem/ruby/2.2.0/bin
     - /usr/local/rvm/bin
     - /usr/bin/site_perl
     - /usr/bin/vendor_perl
     - /usr/bin/core_perl


# taps client Gentoo Linux

RubyGems Environment:
  - RUBYGEMS VERSION: 2.4.6
  - RUBY VERSION: 2.0.0 (2014-11-13 patchlevel 598) [x86_64-linux]
  - INSTALLATION DIRECTORY: /usr/local/rvm/gems/ruby-2.0.0-p598
  - RUBY EXECUTABLE: /usr/local/rvm/rubies/ruby-2.0.0-p598/bin/ruby
  - EXECUTABLE DIRECTORY: /usr/local/rvm/gems/ruby-2.0.0-p598/bin
  - SPEC CACHE DIRECTORY: /root/.gem/specs
  - SYSTEM CONFIGURATION DIRECTORY: /usr/local/rvm/rubies/ruby-2.0.0-p598/etc
  - RUBYGEMS PLATFORMS:
    - ruby
    - x86_64-linux
  - GEM PATHS:
     - /usr/local/rvm/gems/ruby-2.0.0-p598
     - /usr/local/rvm/gems/ruby-2.0.0-p598@global
  - GEM CONFIGURATION:
     - :update_sources => true
     - :verbose => true
     - :backtrace => false
     - :bulk_threshold => 1000
     - :sources => ["https://rubygems.org/"]
  - REMOTE SOURCES:
     - https://rubygems.org/
  - SHELL PATH:
     - /usr/local/rvm/gems/ruby-2.0.0-p598/bin
     - /usr/local/rvm/gems/ruby-2.0.0-p598@global/bin
     - /usr/local/rvm/rubies/ruby-2.0.0-p598/bin
     - /usr/local/sbin
     - /usr/local/bin
     - /usr/sbin
     - /usr/bin
     - /sbin
     - /bin
     - /opt/bin
     - /usr/x86_64-pc-linux-gnu/gcc-bin/4.7.3
     - /usr/local/rvm/bin
     - /srv/pub/android/bin
     - /opt/IBM_DS/jre/bin
     - /opt/IBM_DS/jre/bin
Environment

    Bundler   1.8.3
    Rubygems  2.4.6
    Ruby      2.0.0p598 (2014-11-13 revision 48408) [x86_64-linux]
    GEM_HOME  /usr/local/rvm/gems/ruby-2.0.0-p598
    GEM_PATH  /usr/local/rvm/gems/ruby-2.0.0-p598:/usr/local/rvm/gems/ruby-2.0.0-p598@global
    RVM       1.26.10 (latest)
    Git       2.0.5
    rubygems-bundler (1.4.4)

Bundler settings

    without
      Set for your local app (/var/www/redmine/.bundle/config): "development:test"

Gemfile

    source 'https://rubygems.org'
    
    gem "rails", "3.2.13"
    gem "jquery-rails", "~> 2.0.2"
    gem "coderay", "~> 1.0.9"
    gem "fastercsv", "~> 1.5.0", :platforms => [:mri_18, :mingw_18, :jruby]
    gem "builder", "3.0.0"
    
    # Optional gem for LDAP authentication
    group :ldap do
      gem "net-ldap", "~> 0.3.1"
    end
    
    # Optional gem for OpenID authentication
    group :openid do
      gem "ruby-openid", "~> 2.3.0", :require => "openid"
      gem "rack-openid"
    end
    
    # Optional gem for exporting the gantt to a PNG file, not supported with jruby
    platforms :mri, :mingw do
      group :rmagick do
        # RMagick 2 supports ruby 1.9
        # RMagick 1 would be fine for ruby 1.8 but Bundler does not support
        # different requirements for the same gem on different platforms
        gem "rmagick", ">= 2.0.0"
      end
    end
    
    platforms :jruby do
      # jruby-openssl is bundled with JRuby 1.7.0
      gem "jruby-openssl" if Object.const_defined?(:JRUBY_VERSION) && JRUBY_VERSION < '1.7.0'
      gem "activerecord-jdbc-adapter", "~> 1.2.6"
    end
    
    # Include database gems for the adapters found in the database
    # configuration file
    require 'erb'
    require 'yaml'
    database_file = File.join(File.dirname(__FILE__), "config/database.yml")
    if File.exist?(database_file)
      database_config = YAML::load(ERB.new(IO.read(database_file)).result)
      adapters = database_config.values.map {|c| c['adapter']}.compact.uniq
      if adapters.any?
        adapters.each do |adapter|
          case adapter
          when 'mysql2'
            gem "mysql2", "~> 0.3.11", :platforms => [:mri, :mingw]
            gem "activerecord-jdbcmysql-adapter", :platforms => :jruby
          when 'mysql'
            gem "mysql", "~> 2.8.1", :platforms => [:mri, :mingw]
            gem "activerecord-jdbcmysql-adapter", :platforms => :jruby
          when /postgresql/
            gem "pg", ">= 0.11.0", :platforms => [:mri, :mingw]
            gem "activerecord-jdbcpostgresql-adapter", :platforms => :jruby
          when /sqlite3/
            gem "sqlite3", :platforms => [:mri, :mingw]
            gem "activerecord-jdbcsqlite3-adapter", :platforms => :jruby
          when /sqlserver/
            gem "tiny_tds", "~> 0.5.1", :platforms => [:mri, :mingw]
            gem "activerecord-sqlserver-adapter", :platforms => [:mri, :mingw]
          else
            warn("Unknown database adapter `#{adapter}` found in config/database.yml, use Gemfile.local to load your own database gems")
          end
        end
      else
        warn("No adapter found in config/database.yml, please configure it first")
      end
    else
      warn("Please configure your config/database.yml first")
    end
    
    group :development do
      gem "rdoc", ">= 2.4.2"
      gem "yard"
    end
    
    group :test do
      gem "shoulda", "~> 3.3.2"
      gem "mocha", "~> 0.13.3"
      gem 'capybara', '~> 2.0.0'
      gem 'nokogiri', '< 1.6.0'
      gem 'selenium-webdriver', '2.35.1'
    end
    
    local_gemfile = File.join(File.dirname(__FILE__), "Gemfile.local")
    if File.exists?(local_gemfile)
      puts "Loading Gemfile.local ..." if $DEBUG # `ruby -d` or `bundle -v`
      instance_eval File.read(local_gemfile)
    end
    
    # Load plugins' Gemfiles
    Dir.glob File.expand_path("../plugins/*/Gemfile", __FILE__) do |file|
      puts "Loading #{file} ..." if $DEBUG # `ruby -d` or `bundle -v`
      instance_eval File.read(file)
    end

Gemfile.lock

    GEM
      remote: https://rubygems.org/
      specs:
        actionmailer (3.2.13)
          actionpack (= 3.2.13)
          mail (~> 2.5.3)
        actionpack (3.2.13)
          activemodel (= 3.2.13)
          activesupport (= 3.2.13)
          builder (~> 3.0.0)
          erubis (~> 2.7.0)
          journey (~> 1.0.4)
          rack (~> 1.4.5)
          rack-cache (~> 1.2)
          rack-test (~> 0.6.1)
          sprockets (~> 2.2.1)
        activemodel (3.2.13)
          activesupport (= 3.2.13)
          builder (~> 3.0.0)
        activerecord (3.2.13)
          activemodel (= 3.2.13)
          activesupport (= 3.2.13)
          arel (~> 3.0.2)
          tzinfo (~> 0.3.29)
        activeresource (3.2.13)
          activemodel (= 3.2.13)
          activesupport (= 3.2.13)
        activesupport (3.2.13)
          i18n (= 0.6.1)
          multi_json (~> 1.0)
        arel (3.0.3)
        builder (3.0.0)
        capybara (2.0.3)
          mime-types (>= 1.16)
          nokogiri (>= 1.3.3)
          rack (>= 1.0.0)
          rack-test (>= 0.5.4)
          selenium-webdriver (~> 2.0)
          xpath (~> 1.0.0)
        childprocess (0.5.5)
          ffi (~> 1.0, >= 1.0.11)
        coderay (1.0.9)
        erubis (2.7.0)
        fastercsv (1.5.5)
        ffi (1.9.6)
        hike (1.2.3)
        i18n (0.6.1)
        journey (1.0.4)
        jquery-rails (2.0.3)
          railties (>= 3.1.0, < 5.0)
          thor (~> 0.14)
        json (1.8.2)
        mail (2.5.4)
          mime-types (~> 1.16)
          treetop (~> 1.4.8)
        metaclass (0.0.4)
        mime-types (1.25.1)
        mocha (0.13.3)
          metaclass (~> 0.0.1)
        multi_json (1.10.1)
        mysql2 (0.3.18)
        net-ldap (0.3.1)
        nokogiri (1.5.11)
        pg (0.18.1)
        polyglot (0.3.5)
        rack (1.4.5)
        rack-cache (1.2)
          rack (>= 0.4)
        rack-openid (1.4.2)
          rack (>= 1.1.0)
          ruby-openid (>= 2.1.8)
        rack-ssl (1.3.4)
          rack
        rack-test (0.6.3)
          rack (>= 1.0)
        rails (3.2.13)
          actionmailer (= 3.2.13)
          actionpack (= 3.2.13)
          activerecord (= 3.2.13)
          activeresource (= 3.2.13)
          activesupport (= 3.2.13)
          bundler (~> 1.0)
          railties (= 3.2.13)
        railties (3.2.13)
          actionpack (= 3.2.13)
          activesupport (= 3.2.13)
          rack-ssl (~> 1.3.2)
          rake (>= 0.8.7)
          rdoc (~> 3.4)
          thor (>= 0.14.6, < 2.0)
        rake (10.4.2)
        rdoc (3.12.2)
          json (~> 1.4)
        rmagick (2.13.4)
        ruby-openid (2.3.0)
        rubyzip (0.9.9)
        selenium-webdriver (2.35.1)
          childprocess (>= 0.2.5)
          multi_json (~> 1.0)
          rubyzip (< 1.0.0)
          websocket (~> 1.0.4)
        shoulda (3.3.2)
          shoulda-context (~> 1.0.1)
          shoulda-matchers (~> 1.4.1)
        shoulda-context (1.0.2)
        shoulda-matchers (1.4.1)
          activesupport (>= 3.0.0)
        sprockets (2.2.3)
          hike (~> 1.2)
          multi_json (~> 1.0)
          rack (~> 1.0)
          tilt (~> 1.1, != 1.3.0)
        thor (0.19.1)
        tilt (1.4.1)
        treetop (1.4.15)
          polyglot
          polyglot
          polyglot
          polyglot
          polyglot
          polyglot
          polyglot
          polyglot
          polyglot
          polyglot
          polyglot
          polyglot
          polyglot
          polyglot
          polyglot
          polyglot
          polyglot
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
          polyglot (>= 0.3.1)
        tzinfo (0.3.43)
        websocket (1.0.7)
        xpath (1.0.0)
          nokogiri (~> 1.3)
        yard (0.8.7.6)
    
    PLATFORMS
      ruby
    
    DEPENDENCIES
      activerecord-jdbc-adapter (~> 1.2.6)
      activerecord-jdbcmysql-adapter
      activerecord-jdbcpostgresql-adapter
      builder (= 3.0.0)
      capybara (~> 2.0.0)
      coderay (~> 1.0.9)
      fastercsv (~> 1.5.0)
      jquery-rails (~> 2.0.2)
      mocha (~> 0.13.3)
      mysql2 (~> 0.3.11)
      net-ldap (~> 0.3.1)
      nokogiri (< 1.6.0)
      pg (>= 0.11.0)
      rack-openid
      rails (= 3.2.13)
      rdoc (>= 2.4.2)
      rmagick (>= 2.0.0)
      ruby-openid (~> 2.3.0)
      selenium-webdriver (= 2.35.1)
      shoulda (~> 3.3.2)
      yard



--nginx_modules_http_upload_progress --pcre --ssl

