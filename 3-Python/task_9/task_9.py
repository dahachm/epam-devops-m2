# Task 9
#
# For this task you need to have docker daemon installed and running. 
#
# The task is to create a python script, that has following functions:
#     1. connects to docker API and print a warning message if there are dead or stopped containers with their ID and name. 
#     2. containers list, similar to docker ps -a  
#     3. image list, similar to docker image ls
#     4. container information, like docker inspect  
# 
# Connection function must accept connection string 
# for example 'http://192.168.56.101:2376' and connect to it or use string from environment if no connection string is given.  
# 
# In order to connect to docker, you can use either Unix socket or reconfigure daemon 
# to use a network socket (https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-socket-option) 
#
# Connection string example:
#   - type - http: 'http://192.168.56.101:2376'
#   - type - unix-socket: 'unix:/var/run/docker.sock'.
# 
# If connection string is not provided and $DOCKER_HOST var is empty, then set to default value.
# Default value: 'http+unix://%2Fvar%2Frun%2Fdocker.sock'.
# 
# Docker API documentation: https://docs.docker.com/engine/api/v1.41/
#

import requests
import requests_unixsocket
import os
import sys
import json
from datetime import datetime

def toNiceDurationMessage (timestamp):

    """  Calculate timedelta from given timestamp and current time.
         Return pretty formatted str about timedelta (in days, hours, and minutes """

    now  = datetime.now()
    then = datetime.fromtimestamp(timestamp)
    difference = now - then
    if difference.days > 1:
        niceMessage = '{} days ago'.format(difference.days)
    elif difference.seconds // 3600 > 1:
        niceMessage = '{} hours ago'.format(difference.seconds // 3600)
    else:     
        niceMessage = '{} minutes ago'.format((difference.seconds % 3600) // 60) 
    
    return niceMessage

def toHumanReadable(size):

    """ Conberts number of bytes into human readbale str"""

    suffixes=['B','KB','MB','GB','TB']
    suffixIndex = 0
    while size > 1024 and suffixIndex < 4:
        suffixIndex += 1
        size = size/1024.0 
    return '{:.1f} {}'.format(size,suffixes[suffixIndex])


class Docker:

    """ Wrapper class for interacting with the docker API """

    def __init__(self, remoteHost=''):
        if remoteHost == '':            # if no connection str given
            try:
                if os.environ['DOCKER_HOST'] != '':         # and $DOCKER_HOST value is NOT empty
                    remoteHost = os.environ['DOCKER_HOST']  # set to $DOCKER_HOST value
            except:
                remoteHost = 'http+unix://%2Fvar%2Frun%2Fdocker.sock'   # otherwise set to default     
        
        if remoteHost[:5] == 'unix:':           
            remoteHost.replace('/', '%2F')
            remoteHost = 'http+' + remoteHost       # make str suitable for `requests_unixsocket` class

        if remoteHost.find('unix') > 0:
            self.type = 'unix-socket'
        else:
            self.type = 'http'

        self.host = remoteHost

    def getData(self, url):

        """ Get data from remote URL.
            Depending on the type of connection (`unix-socket` or `http`)
            uses `requests_unixsockets` class or `requests` for connection """
        
        if self.type == 'unix-socket':
            try:
                session = requests_unixsocket.Session()
                r = session.get(url)
                r.raise_for_status()
                return r
            except requests.exceptions.HTTPError as errorMsg:
                print(errorMsg)
                exit()                   
            except:
                print ('Cannot connect to the Docker daemon at "{}"'.format(url[:url.find('.sock')+5])) 
                print('Is the docker daemon running?')
                exit()
                

        if self.type == 'http':
            try:
                r = requests.get(url)
                r.raise_for_status()
                return r
            except requests.exceptions.HTTPError as errorMsg:
                print(errorMsg)
                exit()
            except:
                print('Something went wrong ...')
                print('URL: ', url)
                print(sys.exc_info()[0])
                exit()
        

    def connect (self):
        
        """ Connects to docker API and print a warning message if there are dead or stopped containers with their ID and name """
        
        url = self.host + '/containers/json?all=1'
        
        data = self.getData(url).json()

        exited = list()
        dead = list()
        for container in data:
            if container['State'] == 'exited':
                    name = container['Names'][0]
                    ID   = container['Id']
                    exited.append((name, ID))

            if container['State'] == 'dead':
                    name = container['Names'][0]
                    ID   = container['Id']
                    dead.append((name, ID))

        if len(exited) > 0 or len(dead) > 0:
            print ('\n  WARNING! There are {} stopped containers (in `exited` state) and {} dead containers.\n'.format(len(exited), len(dead)))
            print ('{:^21}     {:^12}     {:^6}'.format('NAME', 'ID', 'STATE'))
            for container in exited:
                print (' {:21}    {:12}    exited'.format(container[0][1:],container[1][:12]))
            for container in dead:
                print (' {:21}    {:12}    dead'.format(container[0][1:], container[1][:12]))    
        else:
            print('Connection established successfully.')

    def list_containers (self):
        
        """ List containers, similar to docker ps -a"""

        url = self.host + '/containers/json?all=1'
        
        data = self.getData(url).json()

        print('{:^15} {:^25} {:^18} {:^16} {:^25} {:^25} {:^25}'.format('CONTAINER ID','IMAGE','COMMAND','CREATED','STATUS','PORTS','NAMES'))

        for container in data:
            ID      = container['Id']
            IMAGE   = container['Image']
            STATUS  = container['Status']
            PORTS   = container['Ports']
            NAMES   = container['Names'][0]
            COMMAND = container['Command']
            CREATED = toNiceDurationMessage(container['Created'])
            if len(COMMAND) > 15:
                COMMAND = COMMAND[:15]+'...'

            print('{:15} {:25} {:18} {:16} {:25} {:^25} {:25}'.format(
                    ID[:12],  
                    IMAGE, 
                    COMMAND, 
                    CREATED, 
                    STATUS, 
                    str(PORTS), 
                    NAMES[1:]))

    def list_images(self):
        
        """ List images, similar to docker images -a"""

        url = self.host + '/images/json?all=1'
        
        data = self.getData(url).json()

        print('{:40} {:25} {:25} {:25} {:25}'.format('REPOSITORY','TAG','IMAGE ID','CREATED','SIZE'))

        for image in data: 
            REPOSITORY = image['RepoTags'][0].split(':')[0]
            TAG        = image['RepoTags'][0].split(':')[1]
            ID         = image['Id']
            CREATED    = toNiceDurationMessage(image['Created'])
            SIZE       = toHumanReadable(image['Size'])


            print('{:40} {:25} {:25} {:25} {:25}'.format(
                    REPOSITORY,  
                    TAG, 
                    ID[ID.find(':'):12], 
                    CREATED, 
                    SIZE))

    def inspect(self, id):

        """ List container information, like docker inspect.
            String Required (id): ID or name of the container"""
        try:
            url = self.host + '/containers/' + id + '/json'
            data = self.getData(url).text
            json_formatted_output = json.dumps(json.loads(data), indent=4)
            print(json_formatted_output)
        except:
            print(sys.exc_info()[0])    
        


