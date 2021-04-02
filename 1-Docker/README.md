# 1-Docker

# Headnode

Получение:

```
$ docker pull dahachm/hadoop-headnode:1.0
```

**headnode** - главная нода HDFS-кластера, при старте контейнера запускаются NameNode(HDFS) и ResourceManager(YARN). 


Запуск контейнера **headnode**

Запуск без указания парметров (docker сам все настроит вольюмы и сеть):
```
$ docker run -tdP --name headnode dahachm/hadoop-headnode:1.0
```

С указанием дополнительных параметров:
```
$ docker run -v /opt/namenode-dir:/opt/namenode-dir -p 8088:8088 -tdP --name headnode dahachm/hadoop-headnode:1.0
```

  - **-v** - подключение вольюмов: 

      *<каталог хостовой системы, где нужно сохранить данные контейнера>*:*<путь монтирования каталога в контейнере>*
      
      Если не указывать этот параметр отдельно, docker сам выделит вольюм. Путь к нему можно будет посмотреть с помощью команды `docker inspect hadoop:headnode | grep Volumes`. 

  - **-p** - проброс портов из контейнера в хост систему:
 
      *<порт_хоста>*:*<порт_контейнера>*

      Если не указывать отдельно, куда перенаправлять трафик с некоторых портов (в данном случае для удобство отдельно указываем порт доступа к WebUI RewourceManager'а), то
      docker сам перенаправит порты, перечисленные в EXPOSE, на свободные в хостовой системе (при указании параметра **-P**). Посмотреть правила проброса портов запущенного
      контейнера можно с помощью команды `docker ps`.

# Worker

Получение: 

```
$ docker pull dahachm/hadoop-worker:1.0
```

**worker** - первая (и единственная) slave-нода кластера, при старте контейнера запускаются DataNode (HDFS) и NodeManager (YARN).

Запуск контейнера **worker**

Запуск без указания парметров:
```
$ docker run -tdP --name worker dahachm/hadoop-headnode:1.0
```

Запуск с дополнительными параметрами:
```
$ docker run -v /opt/nodemanager-log-dir:/opt/nodemanager-log-dir -p 8042:8042 -tdP --name worker dahachm/hadoop-headnode:1.0
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

![Screenshot_3](https://user-images.githubusercontent.com/40645030/113363978-0af3f800-935b-11eb-8a43-8ba5805fb368.png)

![Screenshot_4](https://user-images.githubusercontent.com/40645030/113363982-0deee880-935b-11eb-8d4e-219e35bce41e.png)

![Screenshot_6](https://user-images.githubusercontent.com/40645030/113363991-10e9d900-935b-11eb-8fa8-81a94a12a86c.png)

![Screenshot_7](https://user-images.githubusercontent.com/40645030/113332471-e2073f00-9329-11eb-99eb-0da674078642.png)

