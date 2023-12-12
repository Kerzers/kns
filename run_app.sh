#!/bin/bash

export KNS_MYSQL_USER=KNS_dev
export KNS_MYSQL_PWD=KNS_dev_pwd
export KNS_MYSQL_HOST=localhost
export KNS_MYSQL_DB=KNS_dev_db
export KNS_API_HOST=0.0.0.0
export KNS_API_PORT=5000

python3 -m api.v1.app
