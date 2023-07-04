#!/bin/bash

cat /dev/null > run.bash
chmod ug+x run.bash

echo ". .venv/bin/activate" >> run.bash
echo >> run.bash

echo
echo -e "\033[1;34mMySQL connection settings\033[0m"
echo
read -p "MySQL Hostname (localhost): " MYSQL_HOST
read -p "MySQL Port (3306): " MYSQL_PORT
read -p "MySQL User: " MYSQL_USER
read -r -s -p "User Password: " MYSQL_PASSWORD; echo
read -p "DB Name: " MYSQL_DB


if [ -z "$MYSQL_HOST" ]
    then MYSQL_HOST='localhost'
fi

if [ -z "$MYSQL_PORT" ]
    then MYSQL_PORT=3306
fi

echo -e "export MYSQL_HOST='$MYSQL_HOST'" >> run.bash
echo -e "export MYSQL_PORT='$MYSQL_PORT'" >> run.bash
echo -e "export MYSQL_USER='$MYSQL_USER'" >> run.bash
echo -e "export MYSQL_PASSWORD='$MYSQL_PASSWORD'" >> run.bash
echo -e "export MYSQL_DB='$MYSQL_DB'" >> run.bash
echo >> run.bash
echo -e "python3 server.py" >> run.bash

echo
printf "\033[1;92mrun.bash configured!\033[0m\n"
echo