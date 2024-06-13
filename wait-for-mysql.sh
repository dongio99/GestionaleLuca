#!/bin/bash

set -e

host="$1"
port="$2"
user="$3"
password="$4"
shift 4
cmd="$@"

until mysqladmin ping -h"$host" -P"$port" -u"$user" -p"$password" --silent; do
  >&2 echo "MySQL is unavailable - sleeping"
  sleep 1
done

>&2 echo "MySQL is up - executing command"
exec $cmd
