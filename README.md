# Docker Networking

In this demo, we will create a Docker network and run two applications, MySQL and Myapp, that can communicate with each other.

# Instructions

## Building the "Myapp" Docker Image

Build the Docker image for the "Myapp" application using the following command:

```
docker build -t myapp .
```
## Creating a Docker Bridge Network

Create a Docker bridge network called "app-mysql-network" for the applications to communicate with each other:

```
docker network create app-mysql-network
```

## Deploying the MySQL Container

Deploy a MySQL container using the following command:

```
docker run -d --name mysql_host \
--network app-mysql-network \
-e MYSQL_ROOT_PASSWORD=prabin123 \
-e MYSQL_USER=prabin \
-e MYSQL_PASSWORD=prabin \
-e MYSQL_DATABASE=mydatabase \
mysql:latest
```

Wait for approximately 30 seconds to ensure the MySQL container is fully initialized.

or check the logs with following command and when the mysql is up and running, deploy "Myapp" Application;

```
docker logs -f mysql_host
```

## Deploying the "Myapp" Application

Deploy the "Myapp" application within the same network using the following command:

```
docker run -d --name myapp \
-p 5000:5000 \
--network app-mysql-network \
myapp
```

# Description
This demo demonstrates the setup of a Docker network and the deployment of two applications, MySQL and Myapp. The applications are connected within the "app-mysql-network" bridge network, enabling them to communicate with each other. The MySQL container provides a database backend, and the "Myapp" application serves as a web application accessible on port 5000.

Make sure to follow the instructions in the order specified to successfully run the demo.

# Using Docker Compose

The earlier process of running multiple containers can be greatly simplified using Docker Compose. To run the application with Docker Compose, follow these steps:

    1.Make sure you have Docker Compose installed on your system.

    2.Create a file named docker-compose.yml in your project directory and copy the following contents into it:

```
version: '3.9'
services:
  myapp:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: myapp
    ports:
      - 5000:5000
    networks:
      - myapp-mysql-network
    depends_on:
      - mysql_host

  mysql_host:
    image: mysql:latest
    volumes:
      - myapp-mysql-data:/var/lib/mysql
    networks:
      - myapp-mysql-network
    environment:
      - MYSQL_ROOT_PASSWORD=prabin12345
      - MYSQL_USER=prabin
      - MYSQL_PASSWORD=prabin
      - MYSQL_DATABASE=mydatabase

networks:
  myapp-mysql-network:

volumes:
  myapp-mysql-data:
```

Run the following command to start the containers:

```
docker-compose up -d
```

## Accessing the Application

Once the containers are up and running, you can access the "Myapp" application by opening a web browser and visiting http://localhost:5000. You should see the following page:

	![Myapp Running APP](https://github.com/prabinkc2046/Docker-Networking/blob/main/Screenshot/Screenshot-Myapp%20is%20running.png)

## Connecting to MySQL

The "Myapp" application is now connected to a MySQL database running in a separate container. You can interact with the database using the following credentials:

    - Host: mysql_host
    - Port: 3306
    - Username: prabin
    - Password: prabin
    - Database: mydatabase

You should see the following page:

	![MyAPP connecting to MySQL container](https://github.com/prabinkc2046/Docker-Networking/blob/main/Screenshot/Screenshot-Myapp%20connecting%20to%20Mysql.png)


## Stopping the Application

To stop the application and the associated containers, run the following command:
```
docker-compose down
```


That's it! By using Docker Compose, the process of running multiple containers has been greatly simplified.
