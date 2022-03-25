# Inserting Comments into Local Docker Mongo Database

You will need to download a version of `comments.bson` (You probably do not want the ~37GB version)

Use `docker compose up -d <container name>` to start the mongo container, this should be `mongo` (or you can use `./devup` and start all of the containers)

Use `docker ps` to list the container ids

You will need to then copy the bson file to the docker container's home directory `docker cp <path to comments.bson> <container id>:/`

Now you will have to open a terminal into that container with `docker exec -it <container name> bash` In this case the container name should be `capstone2022_mongo_1`

Once you are in a bash terminal you need to restore the mongo database using `mongodump --db <database_name> --collection <collection name>` In this case the database name is `mirrulations` and the collection name is `comments`

```
docker compose up -d mongo
docker ps
docker cp <path to comments.bson> <container id>:/
docker exec -it capstone2022_mongo_1 bash
mongodump --db mirrulations --collection comments
```
