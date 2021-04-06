# Task 9

> For this task you need to have docker daemon installed and running. 
>
> The task is to create a python script, that has following functions:
>     1. connects to docker API and print a warning message if there are dead or stopped containers with their ID and name. 
>     2. containers list, similar to docker ps -a  
>     3. image list, similar to docker image ls
>     4. container information, like docker inspect  
> 
> Connection function must accept connection string 
> for example 'http://192.168.56.101:2376' and connect to it or use string from environment if no connection string is given.  
> 
> In order to connect to docker, you can use either Unix socket or reconfigure daemon 
> to use a network socket (https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-socket-option) 

**Docker** class is a Wrapper class for interacting with the docker API.

An object connect to *docker daemon* (listening on unix socket or on port on remote interface) and 
perform listing of docker images, docker containers, and  information about specific conteiner.

If connection string is not provided for Init method and $DOCKER_HOST var is empty, then *Docker.host* is set to default value.

Docker.host default value: 'http+unix://%2Fvar%2Frun%2Fdocker.sock'.

Connection string example:
   - type - http: 'http://192.168.56.101:2376'
   - type - unix-socket: 'unix:/var/run/docker.sock'.
 
 Docker API documentation: https://docs.docker.com/engine/api/v1.41/


##  Docker
  
**Attributes**:
  
  - type: str, type of connetion to docker daemon (unix socket, host\port)
  - host: str, connection string, used to connect to docker daemon

**Methods**:
  
  - ***getData(*str* url)***
    
    Get data from remote URL. Depending on the type of connection (`unix-socket` or `http`) uses `requests_unixsockets` class or `requests` for connection.
    
    
  - ***connect()***
    
    Connects to docker API and print a warning message if there are dead or stopped containers with their ID and name.
    
  - ***list_containers()***
    
    List containers, similar to docker ps -a.
    
  - ***list_images()***
    
    List images, similar to docker images -a.
    
  - ***inspect(*str* id)***
    
    List container information, like docker inspect. String Required (id): ID or name of the container.
    
## Usage 
  
**docker daemon on remote host:**
  
  bind docker daemon to port 2375:
  
  ![Screenshot_21](https://user-images.githubusercontent.com/40645030/113764446-a30b2c00-9723-11eb-853e-cf6350bdc4f8.png)

  add a firewall rule to allow remote access:
  
  ![Screenshot_22](https://user-images.githubusercontent.com/40645030/113764464-ac949400-9723-11eb-95ad-0caa1cdd347b.png)

  Add */path/to/dir/with/task_9.py* to $PYTHONPATH:
  
  ```
  $ export PYTHONPATH='/path/to/dir/with/task_9.py'
  ```
  
  Add connetcion string to $DOCKER_HOME (where *172.25.208.1* remote host IP):
  
  ```
  $ export DOCKER_HOST='http://172.25.208.1:2375'
  ```
  
  ![Screenshot_23](https://user-images.githubusercontent.com/40645030/113764475-b0281b00-9723-11eb-8885-ede51eff0aa8.png)
  
  **Import Docker class from task_9**:
  
  ```
  >>> from task_9 import Docker
  ```
  
  **Create Docker object** without any arguments:
  
  ```
  >>> docker = Docker()
  ```
  
  Since we added connection string to $DOCKER_HOST var earlier, it must set *docker.host* to value from $DOCKER_HOST:
  
  ![Screenshot_24](https://user-images.githubusercontent.com/40645030/113765451-f5008180-9724-11eb-89e8-c69388a4a4ff.png)
  
  
  ***connect()*** method:
  
  ```
  >>> docker.connect()
  ```
  
  ![Screenshot_25](https://user-images.githubusercontent.com/40645030/113765958-9687d300-9725-11eb-80b7-195a1daa9353.png)

  Compare to the output caught from docker-client on the same remote host:
  
  ![Screenshot_26](https://user-images.githubusercontent.com/40645030/113765970-9a1b5a00-9725-11eb-812d-f8a932e91623.png)
  
  ***list_containers()*** method:
  
  ```
  >>> docker.list_containers()
  ```
  
  ![Screenshot_27](https://user-images.githubusercontent.com/40645030/113766326-f4b4b600-9725-11eb-88f1-714489afb511.png)
  
  ***list_images()*** method:
  
  ```
  >>> docker.list_images()
  ```
  
  ![Screenshot_29](https://user-images.githubusercontent.com/40645030/113771451-0d27cf00-972c-11eb-9fe6-9b17900aba79.png)

  Compare to the output caught from docker-client on the same remote host:
  
  ![Screenshot_29](https://user-images.githubusercontent.com/40645030/113766549-380f2480-9726-11eb-811a-8350d1454c44.png)

  ***inspect()*** method (for example, *1-docker_worker_1* container:
  
  ```
  >>> docker.inspect('1-docker_worker_1')
  ```
  
  ![Screenshot_30](https://user-images.githubusercontent.com/40645030/113766816-8d4b3600-9726-11eb-8837-fb3c39e79e0e.png)
  
**docker daemon on localhost:**
  
  On localhost I have only one container and image:
  
  ![Screenshot_31](https://user-images.githubusercontent.com/40645030/113767509-70633280-9727-11eb-8f3c-3eecfe98a6cb.png)
     
  Create new **Docker object**:
  
  ```
  >>> local-docker = Docker('unix:/var/run/docker.sock')
  ```
  
  ![Screenshot_32](https://user-images.githubusercontent.com/40645030/113768596-afde4e80-9728-11eb-9f83-7c6706aa883c.png)
  
  ***connect()*** method:
  
  ```
  >>> local_docker.connect()
  ```
  
  ![Screenshot_33](https://user-images.githubusercontent.com/40645030/113771482-16b13700-972c-11eb-8a52-66ae372e0770.png)

  
  ***list_containers()*** method:
  
  ```
  >>> local_docker.list_containers()
  ```
  
  ![Screenshot_34](https://user-images.githubusercontent.com/40645030/113771504-1d3fae80-972c-11eb-820f-1045e0e12d87.png)
 
  ***list_images()*** method:
  
  ```
  >>> local_docker.list_images()
  ```
  
  ![Screenshot_35](https://user-images.githubusercontent.com/40645030/113771516-216bcc00-972c-11eb-86e4-e6d8998788d8.png)

  ***inspect()*** method (container with id value *93b7407a7105*):
  
  ```
  >>> local_docker.inspect('93b7407a7105')
  ```
  
  ![Screenshot_36](https://user-images.githubusercontent.com/40645030/113771725-6ee83900-972c-11eb-968e-98c7eb377b99.png)

  
## Some extre 

  To avoid *Permission denied* error, rememeber to run python/python script with sudo- command or bu user that is in *docker* group.
  
    
