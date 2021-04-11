VM1 - IP: 10.0.5.1

VM2 - IP: 10.0.5.2

VM3 - IP: 10.0.5.3

*****

# 1.	On one of VMs install Ansible and create a user.

   Install Ansible on **VM1**:
    
   ```
   # python3 -m pip install ansible
   ```

   ![Screenshot_1](https://user-images.githubusercontent.com/40645030/114198972-90c80280-995c-11eb-908f-0875c456d6c8.png)

   Create new user *moomin*:

   ```
   # useradd moomin
   ```

# 2.	Using ansible ad-hoc create the same user on the rest of machines.

   At first, have to create inventory file [hosts.yml](hosts.yml):
    
   ```yml
   moomin_hosts:
       hosts:
           host-1:
                   ansible_host: 10.0.5.1
           host-2:
                   ansible_host: 10.0.5.2
           host-3:
                   ansible_host: 10.0.5.3
   ```

   At second, move a copy of public key to remote hosts:

   ```
   # ssh-copy-id -i ~/.ssh/id_rsa.pub 10.0.5.1
   # ssh-copy-id -i ~/.ssh/id_rsa.pub 10.0.5.2
   # ssh-copy-id -i ~/.ssh/id_rsa.pub 10.0.5.3
   ```

   Create user *moomin* on machines from *moomin_hosts* group using ad-hoc:

   ```
   # ansible -i hosts.yml -m user -a "name=moomin state=present" moomin_hosts
   ```

   ![Screenshot_2](https://user-images.githubusercontent.com/40645030/114199054-a2a9a580-995c-11eb-8699-47314735c11b.png)

# 3.	Setup SSH keys and sudo for that user.

   1) On VM1 create SSH keys:

   ```
   # ssh-keygen -P '' -f host-1_rsa
   # ssh-keygen -P '' -f host-2_rsa
   # ssh-keygen -P '' -f host-3_rsa
   ```

   2) Create playbook:

   [set-ssh.yml](set-ssh.yml):
   
   ```yml
   - name: Custom
  hosts: moomin_hosts

  tasks:
  - name: Update all packages on the systems
    yum:
        name: '*'
        state: latest

  - name: Add epel-release repo
    yum: 
        name: epel-release
        state: present 

  - name: Add MySQL repo
    yum:
        name: http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm

  - name: Install NTP, ngnix, MySQL
    yum:
        name: 
          - ntp
          - nginx
          - mysql-server
          - python3
          - python-pip
          - python-PyMySQL
          - python3-PyMySQL
        state: present
  
  - name: Replaces NTP default config
    copy:
        src: ntp.conf
        dest: /etc/ntp.conf
        force: yes

  - name: Start NTP
    service:
        name: ntpd
        state: started

  - name: Start nginx
    service:
        name: nginx
        state: started      

  - name: Start mysql
    service:
        name: mysqld
        state: started

  - name: Create user in MySQL
    mysql_user:
        name: moomin
        priv: '*.*:ALL'
        state: present

  - name: Create database in MySQL
    mysql_db:
        name: moomin_db
        state: present
   ```

   3) Run [set-ssh.yml](set-ssh.yml) with created public keys as arguments:

   ```
   # ansible-playbook -i hosts.yml set-ssh.yml  -e "pubkey1='$(cat host-1_rsa.pub)' pubkey2='$(cat host-2_rsa.pub)' pubkey3='$(cat host-3_rsa.pub)'"
   ```
   
   ***
   In this playbook I use **MySQL 5.6** as it set *root* user password to '' (empty). 
   
   **MySQL 5.7** and **MySQL8.0** put root password in *.log* file so it requires additional steps to extract root password and create new user/db.
   ***
   
   4) The result:

   Ansible output:
    
   ![Screenshot_4](https://user-images.githubusercontent.com/40645030/114200103-8b1eec80-995d-11eb-85af-2c83e066d58c.png)

   Login from host-2 to host-3 using SSH:
   
   ![Screenshot_5](https://user-images.githubusercontent.com/40645030/114200456-e5b84880-995d-11eb-9cba-4465e8b1acb0.png)

   Try to execute command with sudo on host-3:
  
   ![Screenshot_6](https://user-images.githubusercontent.com/40645030/114200705-21eba900-995e-11eb-85aa-cabdd4d1f9a2.png)


# 4.	write a playbook which:

  > •	updates all packages on the systems
  > 
  > •	installs NTP, Nginx and MySQL
  > 
  > •	for NTP replaces default config with your own (you can find NTP server configs on the internet)
  > 
  > •	for MySQL creates user and database (using corresponding module)
  

  To use `mysql_user` and `mysql_db` had to install extra packages:
  
  ```
  # ansible-galaxy collection install community.mysql
  ```
 
  [playbook.yml](playbook.yml):
   
   ```yml
   - name: Custom
     hosts: moomin_hosts

     tasks:
       - name: Update all packages on the systems
         yum:
          name: '*'
          state: latest

      - name: Add epel-release repo
        yum: 
          name: epel-release
          state: present 

      - name: Install NTP, ngnix, MySQL
        yum:
          name: 
            - ntp
            - nginx
            - mysql-server
            - python3
            - python-pip
            - python2-PyMySQL
          state: present
  
      - name: Install PyMySql
        pip:
          name: PyMySql
          state: present
          executable: pip3

      - name: Replaces NTP default config
        copy:
          src: ntp.conf
          dest: /etc/ntp.conf
          force: yes

      - name: Start NTP
        service:
          name: ntpd
          state: started

      - name: Start nginx
        service:
          name: nginx
          state: started      

      - name: Start mysql
        service:
          name: mysqld
          state: started

      - name: Create user in MySQL
        mysql_user:
          name: moomin
          priv: '*.*:ALL'
          state: present

      - name: Create database in MySQL
        mysql_db:
          name: moomin_db
          state: present   
   ```
   
   Run playbook:
   
   ```
   # ansible-playbook -i hosts.yml playbook.yml
   ```

   The result:
   
   ![Screenshot_7](https://user-images.githubusercontent.com/40645030/114201532-f6b58980-995e-11eb-8a76-48f4813a475e.png)


   **NTP**
   
   [Here is used custom ntp.conf](ntp.conf)
   
   on VM1:
   ```
   $ ntpstat
   $ ntpdc -c sysinfo
   ```
   
   ![Screenshot_8](https://user-images.githubusercontent.com/40645030/114202211-a25ed980-995f-11eb-912f-fcb1b062bae0.png)

   ![Screenshot_9](https://user-images.githubusercontent.com/40645030/114202234-a7bc2400-995f-11eb-89a4-c13273f4d63e.png)

   Time is synchronized:
   
   ![Screenshot_10](https://user-images.githubusercontent.com/40645030/114202249-ac80d800-995f-11eb-8763-ee4c567ffba1.png)

   **nginx**:
   
   ```
   # systemctl status nginx
   ```
   
   ![Screenshot_11](https://user-images.githubusercontent.com/40645030/114202534-f36ecd80-995f-11eb-9819-1f443fd45b5f.png)


   **MySQL**:
   
   ```
   # mysql
   ...
   > SELECT user FROM mysql.user;
   ...
   > SHOW DATABASES;
   ...
   ```
   
   ![Screenshot_12](https://user-images.githubusercontent.com/40645030/114203291-b22aed80-9960-11eb-89d7-d5ea9223fc58.png)
   
   ![Screenshot_13](https://user-images.githubusercontent.com/40645030/114203316-b6570b00-9960-11eb-8ca6-21933fa1019a.png)
   
   ![Screenshot_14](https://user-images.githubusercontent.com/40645030/114203331-bb1bbf00-9960-11eb-963c-d9f94cd3314f.png)

# 4*. Setup nginx web-site
   
   This playbook setup nginx web server configuration and required sources for web site:
      
   - copy *web/* directory with recuired sources to hosts (*images/* directory and index.html)
		
   - copy and replace *nginx.conf* file
		
   - restart nginx
		
   - add firewall rule for port 8080/tcp
   
   - set required SELinux context to *web/* directory
      
   [*setup-nginx.conf*](setup-nginx.conf):
   
   ```yml
   - name: Set up web-server sources
  hosts: moomin_hosts

  tasks:
    - name: Create moomin dir
      file:
        name: /moomin
        state: directory
        mode: 0755

    - name: Copy web sources  
      copy:
        src: web
        dest: /moomin 
        directory_mode: yes
        mode: 0755

    - name: Put nginx.conf
      copy:
        src: nginx.conf
        dest: /etc/nginx/nginx.conf
        force: yes

- name: Put host-1 welcome page
  hosts: host-1

  tasks:
    - name: Put host-1 welcome page
      copy:
          src: html/host-1-welcome-page.html
          dest: /moomin/web/index.html

- name: Put host-2 welcome page
  hosts: host-2

  tasks:
    - name: Put host-2 welcome page
      copy:
          src: html/host-2-welcome-page.html
          dest: /moomin/web/index.html

- name: Put host-3 welcome page
  hosts: host-3

  tasks:
    - name: Put host-3 welcome page
      copy:
          src: html/host-3-welcome-page.html
          dest: /moomin/web/index.html

- name:           
  hosts: moomin_hosts

  tasks:
    - name: Check nginx
      yum:
        name: nginx
        state: present

    - name: Stop nginx
      service:
        name: nginx
        state: stopped

    - name: Start nginx
      service:
        name: nginx
        state: started          

    - name: Add firewall rule for port 8080/tcp
      firewalld:
        port: 8080/tcp
        permanent: yes
        state: enabled  

    - name: Setup SELinux context for web/
      command: chcon -Rv system_u:object_r:httpd_sys_content_t:s0 /moomin/web
   ```
   
   **The result:**
   
   ![Screenshot_15](https://user-images.githubusercontent.com/40645030/114299007-c9352100-9ac1-11eb-8c12-6742333c98a3.png)
   
   ![Screenshot_16](https://user-images.githubusercontent.com/40645030/114299009-cdf9d500-9ac1-11eb-944b-b3cc079cdfb4.png)
   
   ![Screenshot_17](https://user-images.githubusercontent.com/40645030/114299012-d0f4c580-9ac1-11eb-9a62-457713eca045.png)



   
   
