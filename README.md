# Docker Networking

In this demo, we will create a Docker network and run two applications, MySQL and Myapp, that can communicate with each other.

# Instructions

Building the "Myapp" Docker Image
Build the Docker image for the "Myapp" application using the following command:

```
docker build -t myapp .
```
Creating a Docker Bridge Network

Create a Docker bridge network called "app-mysql-network" for the applications to communicate with each other:

```
docker network create app-mysql-network
```

Deploying the MySQL Container

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

Deploying the "Myapp" Application

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

