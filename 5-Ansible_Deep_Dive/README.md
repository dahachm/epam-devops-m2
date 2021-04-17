# 5 Ansible Deep Dive

This is an ansible playbok that performs following tasks using roles:
  
  - Create new user on remote hosts and deploy SSH keys for each
  
  - Install, configure and start ntp
  
  - Install nginx, configure web-server and setup web-site

  - Instal MySQL, create a user and database

## Role user
  
  Create new user named `{{ user_name }}` on remote hosts and add this user to *sudoers*. 
  
  Put private keys on remote hosts and add public keys to authorized keys.

## Role common
  
  Add epel-release repository.
  
  Update all packages.
  
## Role ntp
  
  Install ntp.
  
  Copy custom *ntp.conf* from files and replace original .conf file with it.
  
  Start and enable ntp unit.

## Role mysql

  Add MySQL 5.6 repository.
  
  Install MySQL 5.6. 
  
  Start and enable mysqld.
  
  Create new user in MySQL named `{{ user_name }}`.
  
  Create new database in MySQL named `{{ db_name }}`.

## Role nginx
  
  Install nginx.
  
  Copy *nginx.conf* from files/ with server configuration on port 8080.
  
  Start and enable nginx.
  
  Copy web-site sources from files/.
  
  Add firewall rule to open port 8080/tcp.
  
  Update SELinux context on web/ directory (the one that contain web-sources).
  
## Group vars
  
  **user_name** - name for new user (also used when creating new user in MySQL)
  
  **db_name** - name fore database in MySQL. If not definaed, database will not be created.
  
  **ntp_conf_file** - name for *ntp.conf* file in files/. If not defined, original .conf file for ntp will not be replaced.
  
## Host vars

  **private_key** - name of file with *private key* for new user on host. File with this name is copid to remote host as SSH private key file.
  
  **port_num** - port number for web-site access.
  
# The result
  
  ### Ansible output
  
  ![Screenshot_18](https://user-images.githubusercontent.com/40645030/114357742-ca765480-9b7a-11eb-9f71-cedba521c52a.png)
  
  ### ntp
  
  ![Screenshot_1](https://user-images.githubusercontent.com/40645030/114357780-d3672600-9b7a-11eb-89c6-5cf2b9402759.png) 
  
  ### MySQL
  
  ![Screenshot_2](https://user-images.githubusercontent.com/40645030/114357800-d8c47080-9b7a-11eb-8885-d918c4f83d12.png)
  
  ### user
  
  Able to connect to host-2 and host-3 from host-1 via SSH withod password:
  
  ![Screenshot_3](https://user-images.githubusercontent.com/40645030/114357828-e0841500-9b7a-11eb-8387-72bb9eeabc51.png)
  
  ### nginx
  
  on port 8080:
  
  ![Screenshot_4](https://user-images.githubusercontent.com/40645030/114367493-2940cb80-9b85-11eb-943e-a8c61f2575b3.png)
  
  ![Screenshot_5](https://user-images.githubusercontent.com/40645030/114367499-2b0a8f00-9b85-11eb-9171-780bf5ef4d9b.png)
  
  ![Screenshot_6](https://user-images.githubusercontent.com/40645030/114367506-2cd45280-9b85-11eb-98c4-36fbb93c1683.png)
  
  on port that was defined as extra var:
  
  ```
  # ansible-playbook -i hosts big_installation.yml -e port_num=60000
  ```
  
  ![Screenshot_7](https://user-images.githubusercontent.com/40645030/114370608-58a50780-9b88-11eb-8aa9-ff4646003fcd.png)
  
  ![Screenshot_8](https://user-images.githubusercontent.com/40645030/114370613-59d63480-9b88-11eb-8ac4-081774903376.png)
  
  ![Screenshot_9](https://user-images.githubusercontent.com/40645030/114370621-5c388e80-9b88-11eb-8091-23972380d179.png)

  
  


  
  
