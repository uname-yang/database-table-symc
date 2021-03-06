sudo docker network create --driver overlay dbt

sudo docker service create --name dbms --publish 10000:3306 --network=dbt -e MYSQL_ROOT_PASSWORD=passwd mysql
sudo docker service create --name dbsv --publish 9999:3306 --network=dbt -e MYSQL_ROOT_PASSWORD=passwd mysql

sudo docker build -t twitter_importer .

sudo docker service create --name tweets \
--network=dbt \
--env ACCESS_TOKEN=851652975957127168-kCdHaLXCHAf3yBzynoKc62jG7fxI71O \
--env ACCESS_TOKEN_SECRET=iV330tl5xRtN960uXHHyImcTwBlt5CYSqwb7EH4EJcCWy \
--env CONSUMER_KEY=PRUgkvxvKCAvfT6cnoG8ZueMg \
--env CONSUMER_SECRET=WwtS8oKDT3H7dqQxNdQ7idUk5gMYX1ZeWXDA199QOHKLWIQhoQ \
--env KEYWORDS_LIST=python,golang,scala,ruby,javascript,sql \
--env MYSQL_HOST_NAME=dbms \
--env MYSQL_ROOT_PASSWORD=passwd \
twitter_importer

sudo docker service scale tweets=10
sudo docker service ls

mysql -h 127.0.0.1 -P 10000 -uroot -ppasswd
mysql -h 127.0.0.1 -P 9999 -uroot -ppasswd
