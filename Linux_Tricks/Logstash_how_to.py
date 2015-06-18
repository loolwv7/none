#format wiki
#languange en

= Logstash =
<<TableOfContents>>
== what is logstash ==
Logstash is an open source tool for collecting and managing log files. It’s
part of an open-source stack which includes ElasticSearch for indexing and
searching through data and Kibana for charting and visualizing data. Together
they form a powerful Log management solution.

== how to install ==

=== install requirement ===
What is elasticsearch 
 I. is a Java based log indexer. You can search through Elasticsearch indices  using Lucene search syntax for more complicated query. But, simple wildcard search works too.
What is kibana
 I. It provides the web frontend for Elasticsearch, written on Java Script and PHP, requires only one line to be edited for this to work out off the box.
What is curator
 I. Like a museum curator manages the exhibits and collections on display, Elasticsearch Curator helps you curate, or manage your Elasticsearch indices.

 I. Curator performs many operations on your Elasticsearch indices, from delete to snapshot to shard allocation routing.

{{{
emerge -av app-misc/elasticsearch www-apps/kibana-bin \
app-admin/logstash-forwarder app-admin/logstash-bin \
dev-python/click dev-python/elasticsearch-py elasticsearch-curator
}}}

{{{
brightmoon ~ # /etc/init.d/elasticsearch start
elasticsearch          | * /etc/elasticsearch/elasticsearch.in.sh must be
copied into place
elasticsearch          | * ERROR: elasticsearch failed to start
}}}

{{{
bzip2 -dv /usr/share/doc/elasticsearch-1.5.0/examples/elasticsearch.in.sh.bz2
bzip2 -dv /usr/share/doc/elasticsearch-1.5.0/examples/logging.yml.bz2 
bzip2 -dv /usr/share/doc/elasticsearch-1.5.0/examples/elasticsearch.yml.bz2

cp -vi /usr/share/doc/elasticsearch-1.5.0/examples/elasticsearch.in.sh /etc/elasticsearch/elasticsearch.in.sh
cp -vi /usr/share/doc/elasticsearch-1.5.0/examples/elasticsearch.yml /etc/elasticsearch/elasticsearch.yml
cp -vi /usr/share/doc/elasticsearch-1.5.0/examples/logging.yml /etc/elasticsearch/
}}}

=== start it ===
brightmoon ~ # /etc/init.d/elasticsearch start
{{{
elasticsearch          | * Starting elasticsearch ...
elasticsearch          | * /var/lib/elasticsearch: correcting mode
elasticsearch          | * /var/lib/elasticsearch: correcting owner
elasticsearch          | * /var/log/elasticsearch: correcting mode
elasticsearch          | * /var/log/elasticsearch: correcting owner
elasticsearch          | * /run/elasticsearch: creating directory
elasticsearch          | * /run/elasticsearch: correcting owner
elasticsearch          | * /var/lib/elasticsearch/_default: creating directory
elasticsearch          | * /var/lib/elasticsearch/_default: correcting owner
elasticsearch          | * /var/log/elasticsearch/_default: creating directory
elasticsearch          | * /var/log/elasticsearch/_default: correcting
owner [ ok ]csearch          |
}}}

=== Install plugins ===
[[http://www.elastic.co/guide/en/elasticsearch/reference/current/modules-plugins.html#analysis-plugins]]
{{{
cd /usr/share/elasticsearch
brightmoon elasticsearch # bin/plugin --install mobz/elasticsearch-head
-> Installing mobz/elasticsearch-head...
Trying https://github.com/mobz/elasticsearch-head/archive/master.zip...
Downloading
..................................................................................................................................................................................................................................................................................................................................................................................DONE
Installed mobz/elasticsearch-head into /usr/share/elasticsearch/plugins/head
Identified as a _site plugin, moving to _site structure ...

bin/plugin --install lukas-vlcek/bigdesk --verbose
bin/plugin --install elasticsearch/elasticsearch-analysis-smartcn/2.5.0 --verbose
bin/plugin --install elasticsearch/elasticsearch-analysis-icu/2.5.0
bin/plugin --install karmi/elasticsearch-paramedic
bin/plugin install elasticsearch/elasticsearch-lang-javascript/2.5.0
bin/plugin install elasticsearch/elasticsearch-lang-python/2.5.0
bin/plugin -u https://github.com/NLPchina/elasticsearch-sql/releases/download/1.3.2/elasticsearch-sql-1.3.2.zip --install sql
bin/plugin --install royrusso/elasticsearch-HQ
bin/plugin --install andrewvc/elastic-hammer
bin/plugin --install polyfractal/elasticsearch-inquisitor
bin/plugin --install xyu/elasticsearch-whatson/0.1.3
bin/plugin --install polyfractal/elasticsearch-segmentspy
bin/plugin --install info.johtani/elasticsearch-extended-analyze/1.5.0  #will be removed
bin/plugin -install elasticsearch/elasticsearch-mapper-attachments/1.6.0
bin/plugin -url https://oss-es-plugins.s3.amazonaws.com/elasticsearch-jetty/elasticsearch-jetty-1.2.1.zip -install elasticsearch-jetty-1.2.1
}}}

=== testing plugins ===
[[http://localhost:9200/_plugin/sql/]]

[[http://localhost:9200/_plugin/HQ/]]

[[http://localhost:9200/_plugin/elastic-hammer/]]

[[http://localhost:9200/_plugin/paramedic/index.html]]

[[http://localhost:9200/_plugin/inquisitor]]

[[http://localhost:9200/_plugin/whatson/]]

[[http://localhost:9200/_plugin/segmentspy/]]

=== Removing plugin ===
{{{
bin/plugin --remove <pluginname>
}}}


== TEST ==

=== test elasticsearch ===
{{{
# curl http://localhost:9200/_cat/plugins?v
 name            component version type url               
 Captain Germany head      NA      s    /_plugin/head/    
 Captain Germany bigdesk   NA      s    /_plugin/bigdesk/
[[http://localhost:9200/_plugin/head/]]
[[http://localhost:9200/_plugin/bigdes/]]
}}}

=== test logstash ===
logstash -e 'input { stdin { } } output { elasticsearch { host => localhost }}'
[[http://localhost:9200/_search?pretty]]
{{{
# curl 'http://localhost:9200/_search?pretty'
{
  "took" : 3,
  "timed_out" : false,
  "_shards" : {
    "total" : 11,
    "successful" : 11,
    "failed" : 0
  },
  "hits" : {
    "total" : 9,
    "max_score" : 1.0,
    "hits" : [ {
      "_index" : ".kibana",
      "_type" : "config",
      "_id" : "4.0.2",
      "_score" : 1.0,
      "_source":{"buildNum":6004,"defaultIndex":"logstash-*"}
    }, {
      "_index" : ".kibana",
      "_type" : "index-pattern",
      "_id" : "logstash-*",
      "_score" : 1.0,
      "_source":{"title":"logstash-*","timeFieldName":"@timestamp","customFormats":"{}","fields":"[{\"type\":\"string\",\"indexed\":false,\"analyzed\":false,\"name\":\"_index\",\"count\":0,\"scripted\":false},{\"type\":\"string\",\"indexed\":true,\"analyzed\":false,\"name\":\"_type\",\"count\":0,\"scripted\":false},{\"type\":\"geo_point\",\"indexed\":true,\"analyzed\":false,\"doc_values\":false,\"name\":\"geoip.location\",\"count\":0,\"scripted\":false},{\"type\":\"string\",\"indexed\":true,\"analyzed\":false,\"doc_values\":false,\"name\":\"@version\",\"count\":0,\"scripted\":false},{\"type\":\"string\",\"indexed\":false,\"analyzed\":false,\"name\":\"_source\",\"count\":2,\"scripted\":false},{\"type\":\"string\",\"indexed\":false,\"analyzed\":false,\"name\":\"_id\",\"count\":0,\"scripted\":false},{\"type\":\"string\",\"indexed\":true,\"analyzed\":false,\"doc_values\":false,\"name\":\"message.raw\",\"count\":0,\"scripted\":false},{\"type\":\"string\",\"indexed\":true,\"analyzed\":false,\"doc_values\":false,\"name\":\"host.raw\",\"count\":0,\"scripted\":false},{\"type\":\"string\",\"indexed\":true,\"analyzed\":true,\"doc_values\":false,\"name\":\"message\",\"count\":0,\"scripted\":false},{\"type\":\"date\",\"indexed\":true,\"analyzed\":false,\"doc_values\":false,\"name\":\"@timestamp\",\"count\":0,\"scripted\":false},{\"type\":\"string\",\"indexed\":true,\"analyzed\":true,\"doc_values\":false,\"name\":\"host\",\"count\":0,\"scripted\":false}]"}
    }, {
      "_index" : "logstash-2015.04.23",
      "_type" : "logs",
      "_id" : "3nfCwlzmRXK79m5qpWVxNw",
      "_score" : 1.0,
      "_source":{"message":"help","@version":"1","@timestamp":"2015-04-23T08:42:34.052Z","host":"brightmoon"}
    }, {
      "_index" : "logstash-2015.04.23",
      "_type" : "logs",
      "_id" : "gJtDgbKZQgOunIr5vWe2lQ",
      "_score" : 1.0,
      "_source":{"message":"lkjfasd","@version":"1","@timestamp":"2015-04-23T08:42:31.515Z","host":"brightmoon"}
    }, {
      "_index" : "logstash-2015.04.23",
      "_type" : "logs",
      "_id" : "dEwfXHmNTpaiXd_QRcA7Ag",
      "_score" : 1.0,
      "_source":{"message":"z","@version":"1","@timestamp":"2015-04-23T08:42:35.496Z","host":"brightmoon"}
    }, {
      "_index" : "logstash-2015.04.23",
      "_type" : "logs",
      "_id" : "Yu59_SXfRrG-FvPeVhwUNA",
      "_score" : 1.0,
      "_source":{"message":"s","@version":"1","@timestamp":"2015-04-23T08:42:36.388Z","host":"brightmoon"}
    }, {
      "_index" : "logstash-2015.04.24",
      "_type" : "logs",
      "_id" : "nw1boXLoQvi0chZb93LfYQ",
      "_score" : 1.0,
      "_source":{"message":"help","@version":"1","@timestamp":"2015-04-24T01:03:04.278Z","host":"brightmoon"}
    }, {
      "_index" : "logstash-2015.04.24",
      "_type" : "logs",
      "_id" : "drmhv6j9SeWEOiVuDzmzqA",
      "_score" : 1.0,
      "_source":{"message":"help","@version":"1","@timestamp":"2015-04-24T01:03:02.729Z","host":"brightmoon"}
    }, {
      "_index" : "logstash-2015.04.24",
      "_type" : "logs",
      "_id" : "91YTHiYfSSqEWvh45690LQ",
      "_score" : 1.0,
      "_source":{"message":"Good morning","@version":"1","@timestamp":"2015-04-24T01:03:20.239Z","host":"brightmoon"}
    } ]
  }
}
}}}
 *if not work property will print like this
{{{
{
  "took" : 35,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 4,
    "failed" : 0
  },
  "hits" : {
    "total" : 0,
    "max_score" : null,
    "hits" : [ ]
  }
}
}}}

=== syslog test ===

{{{
cat > /etc/logstash/conf.d/logstash-syslog.conf << "EOF"
input {
  tcp {
    port => 5000
    type => syslog
  }
  udp {
    port => 5000
    type => syslog
  }
}

filter {
  if [type] == "syslog" {
    grok {
      match => { "message" => "%{SYSLOGTIMESTAMP:syslog_timestamp} %{SYSLOGHOST:syslog_hostname} %{DATA:syslog_program}(?:\[%{POSINT:syslog_pid}\])?: %{GREEDYDATA:syslog_message}" }
      add_field => [ "received_at", "%{@timestamp}" ]
      add_field => [ "received_from", "%{host}" ]
    }
    syslog_pri { }
    date {
      match => [ "syslog_timestamp", "MMM  d HH:mm:ss", "MMM dd HH:mm:ss" ]
    }
  }
}

output {
  elasticsearch { host => localhost }
  stdout { codec => rubydebug }
}
EOF

logstash -f /etc/logstash/conf.d/logstash-syslog.conf
}}}

[[ http://localhost:5000 ]]

=== test stdin&stdout ===
logstash --verbose -e 'input { stdin { } } output { stdout { codec => rubydebug } }'
{{{
hello
Pipeline started {:level=>:info}
{
       "message" => "hello",
      "@version" => "1",
    "@timestamp" => "2015-04-23T08:06:19.270Z",
          "host" => "brightmoon"
}
}}}

=== Use Logstash Config File ===
vi logstash-simple.conf 
{{{
input { stdin { } } 
output { 
elasticsearch { host => localhost } 
stdout { codec => rubydebug } 
}
}}}
logstash -f logstash-simple.conf


=== server ===
cat server.conf
{{{
input {
  redis {
    host => "127.0.0.1"
    type => "redis"
    data_type => "list"
    key => "logstash"
  }
}
output {
  stdout { }
  elasticsearch {
    cluster => "localhost"
  }
}
}}}

java -jar /opt/logstash/ agent -v -f /etc/logstash/conf.d/server.conf --log /var/log/logstash/server.log

=== Starting server ===
/etc/init.d/logstash start
{{{
logstash               | * Checking your configuration ...
logstash               |Sending logstash logs to
/var/log/logstash/logstash.log.
logstash               |Using milestone 2 input plugin 'redis'. This plugin
should be stable, but if you see strange behavior, please let us know! For more
information on plugin milestones, see
http://logstash.net/docs/1.4.2/plugin-milestones {:level=>:warn}
logstash               |Configuration OK
logstash               |Configuration
OK
[ ok ]sh               |
logstash               | * /run/logstash: creating directory
logstash               | * /var/log/logstash: correcting mode
logstash               | * /var/log/logstash/logstash.log: correcting mode
logstash               | * Starting
logstash ...
[ ok ]sh               |
}}}
/etc/init.d/kibana start

http://127.0.0.1:5601

== Troubleshooting ==
elasticsearch-kopf is a plugin for elasticsearch, not logstash. You'll need to
download elasticsearch separately, depending on your version of logstash and
then run `./bin/plugin -install lmenezes/elasticsearch-kopf` there. Take a look
here: http://www.elasticsearch.org/overview/elkdownloads/


References
http://www.slashroot.in/logstash-tutorial-linux-central-logging-server
[[http://www.thegeekstuff.com/2014/12/logstash-setup/|logstash setup]]
[[http://logstash.net/docs/1.4.2/tutorials/getting-started-with-logstash]]
[[https://groups.google.com/forum/#!topic/logstash-users/e3z8iD5PXnw]]
[[https://github.com/medcl/elasticsearch-rtf]]

http://riskfocus.com/splunk-vs-elk-part-1-cost/

http://www.slashroot.in/logstash-tutorial-linux-central-logging-server
