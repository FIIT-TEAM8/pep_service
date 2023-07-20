#!/bin/bash

# Variables for db connection
mongo_container="mongo_db"
database="whatever"
username="fiitkar"
password="xxxxxxxx"
auth_database="admin"

# Variables for the first collection
collection="pep"
csv_file="peps.new.csv"

# Variables for the second collection
collection2="sanctions"
csv_file2="sanctions.new.csv"

# import data to container
docker cp "$csv_file" ffce868e5ce3:/"$csv_file"
docker cp "$csv_file2" ffce868e5ce3:/"$csv_file2"

echo "data skopirovane do kontajnera :)"

# import data to collections
docker exec -it "$mongo_container" mongoimport -d "$database" -c "$collection" --type csv --file "$csv_file" --headerline --username "$username" --password "$password" --authenticationDatabase "$auth_database"
docker exec -it "$mongo_container" mongoimport -d "$database" -c "$collection2" --type csv --file "$csv_file2" --headerline --username "$username" --password "$password" --authenticationDatabase "$auth_database"

echo "data naimportovane"

echo "Great success"
