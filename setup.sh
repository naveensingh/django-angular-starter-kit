#!/usr/bin/env bash

function create_project_core_databases(){
	MYSQLPROJECTDB='project_admin'
	MAINDB='test_project_db'
	MYSQLROOTPASS='Pasy4d!WO39&x$4V'
	mysql -uroot -p -e "CREATE DATABASE ${MAINDB};"
    mysql -uroot -p -e "GRANT ALL PRIVILEGES ON ${MAINDB}.* TO '${MYSQLPROJECTDB}'@'localhost' identified by '${MYSQLROOTPASS}';"
    mysql -uroot -p -e "FLUSH PRIVILEGES;"
}
create_project_core_databases

pip install -r requirements.txt
cd projectfrontend && pwd && npm install && cd ..
pwd
echo 'All Done!'
