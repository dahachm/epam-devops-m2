# 1-Docker

# Headnode

Получение:

```
$ docker pull dahachm/hadoop:headnode
```

**headnode** - главная нода HDFS-кластера, при старте контейнера запускаются NameNode(HDFS) и ResourceManager(YARN). 


Запуск контейнера **headnode**

Запуск без указания парметров (docker сам все настроит вольюмы и сеть):
```
$ docker run -tdP --name headnode dahachm/hadoop:headnode
```

С указанием дополнительных параметров:
```
$ docker run -v /opt/namenode-dir:/opt/namenode-dir -p 8088:8088 -tdP --name headnode --network my-network --ip 172.19.0.2 --hostname headnode dahachm/hadoop:headnode
```

  - **-v** - подключение вольюмов: 

      *<каталог хостовой системы, где нужно сохранить данные контейнера>*:*<путь монтирования каталога в контейнере>*
      
      Если не указывать этот параметр отдельно, docker сам выделит вольюм. Путь к нему можно будет посмотреть с помощью команды `docker inspect hadoop:headnode | grep Volumes`. 

  - **-p** - проброс портов из контейнера в хост систему:
 
      *<порт_хоста>*:*<порт_контейнера>*

      Если не указывать отдельно, куда перенаправлять трафик с некоторых портов (в данном случае для удобство отдельно указываем порт доступа к WebUI RewourceManager'а), то
      docker сам перенаправит порты, перечисленные в EXPOSE, на свободные в хостовой системе (при указании параметра **-P**). Посмотреть правила проброса портов запущенного
      контейнера можно с помощью команды `docker ps`.
      
  - **--netwrok** и  **--ip** - указываем созданную ранее собственную сеть и адрес, назначаемый контейнеру в этой сети
      Если не указывать отдельно, docker добавит контейнер к дефолтную сеть и сам выделит ему адрес. Внутри контейнера зашит скрипт, который добавляет в /etc/hosts 
      свой IP с указанием имени *headnode* и адрес, следующий от своего IP, с указаением имени *worker* (см. [set-hosts-headnode.sh](scrips/set-hosts-headnode.sh)).
   

# Worker

Получение: 

```
$ docker pull dahachm/hadoop:worker
```

**worker** - первая (и единственная) slave-нода кластера, при старте контейнера запускаются DataNode (HDFS) и NodeManager (YARN).

Запуск контейнера **worker**

Запуск без указания парметров:
```
$ docker run -tdP --name worker dahachm/hadoop:worker
```

Запуск с дополнительными параметрами:
```
$ docker run -v /opt/nodemanager-log-dir:/opt/nodemanager-log-dir -p 8042:8042 -tdP --name worker --network my-network --ip 172.19.0.3 --hostname worker dahachm/hadoop:worker
```

Описание и назначение параметров запуска **worker** почти совпадает с описанием выше, добавлю только следующее:
  - каталогов для монтирования (вольюмы) 3 штуки:
      - /opt/datanode-dir
      - /opt/nodemanager-local-dir
      - /opt/nodemanager-log-dir
    
    Если не указывать с парметром **-v** путь к вольюму в хостовой системе, docker сам выделит под него каталог, найти который, опять-таки, можно через вызов `docker inspect` (см.выше).
  - WebUI NodeManager'а доступен на порту 8042, для удобства предлагаю отдельно указать его с параметром **-p** при запуске контейнера

## Результат

Если необходимо - настроить проброс портов с ВМ.

В браузере: 

localhost:8088 - ResourceManager WebUI

localhost:8042 - NodeManager WebUI

Результаты:

![Screenshot_1](https://user-images.githubusercontent.com/40645030/113220633-30fe9700-928c-11eb-82d5-9f7686b0cc9b.png)
![Screenshot_2](https://user-images.githubusercontent.com/40645030/113220641-3360f100-928c-11eb-91a6-dc1e1d299cbb.png)

## Docker файл для сборки образа headnode
см. [*headnode_dockerfile*](headnode_dockerfile)

## Docker файл для сборки образа worker
см. [*worker_dockerfile*](worker_dockerfile)

## Ссылка на профиль в Docker Hub

https://hub.docker.com/r/dahachm/hadoop

## Docker-compose

Файл [docker-compose.yml](docker-compose.yml) запускает оба образа (предварительно получая их из репозитория на Docker Hub).

Старт сборки docker-compose:

```
$ docker-compose -f focker-compose.yml up -d
```

Результат сборки:

![Screenshot_3](https://user-images.githubusercontent.com/40645030/113332443-d9af0400-9329-11eb-8527-a984966e1b4e.png)
![Screenshot_4](https://user-images.githubusercontent.com/40645030/113332451-dca9f480-9329-11eb-9de3-9134c095bf32.png)
![Screenshot_6](https://user-images.githubusercontent.com/40645030/113332464-df0c4e80-9329-11eb-8399-2de2221ce9ea.png)
![Screenshot_7](https://user-images.githubusercontent.com/40645030/113332471-e2073f00-9329-11eb-99eb-0da674078642.png)

