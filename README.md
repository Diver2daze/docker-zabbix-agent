# Docker Zabbix agent

This Docker container provides a patched Zabbix agent to monitor a real server and all his containers.
It's monitor docker via python api
+ It has scripts for monitoring rabbitMQ (via python + HTTP API)  https://github.com/jasonmcintosh/rabbitmq-zabbix

sudo docker run -d -p 10050:10050 -v /proc:/host/proc -v /sys:/host/sys -v /dev:/host/dev -v /var/run/docker.sock:/var/run/docker.sock --name zabbix-agent -h zabbix-agent interair/docker-zabbix-agent zabbix-agent zabbix-server
