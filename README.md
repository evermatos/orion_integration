Orion Context Broker Integration
========================

**Description:** This is a simple Python project to facilitate the use of the FIWARE [Orion Context Broker](https://fiware-orion.readthedocs.io/en/latest/). The following steps to run FIWARE properly are based on the [FIWARE step-by-step documentation](https://github.com/Fiware/tutorials.Step-by-Step/blob/master/docs/getting-started.md).

## Starting the containers

First pull the necessary Docker images from Docker Hub and create a network for our containers to connect to:

```bash
docker pull mongo:3.6
docker pull fiware/orion
docker network create fiware_default
```

A Docker container running a [MongoDB](https://www.mongodb.com/) database can be started and connected to the network
with the following command:

```bash
docker run -d --name=mongo-db --network=fiware_default \
  --expose=27017 mongo:3.6 --bind_ip_all --smallfiles
```

The Orion Context Broker can be started and connected to the network with the following command:

```bash
docker run -d --name fiware-orion -h orion --network=fiware_default \
  -p 1026:1026  fiware/orion -dbhost mongo-db
```

> **Note:** If you want to clean up and start again you can do so with the following commands
>
> ```
> docker stop fiware-orion
> docker rm fiware-orion
> docker stop mongo-db
> docker rm mongo-db
> docker network rm fiware_default
> ```

### Starting server

The subscriptions and notifications require some process to play the role of the consumer
application able to receive notifications.
It is a very simple "dummy" application that simply listens to a given URL
(the example below uses localhost:1028, but a different
host and/or port can be specified) and echoes whatever it receives in the
terminal window where it is executed. Run it using the following
command:

```
./dummy-web-server.py 1028
```
