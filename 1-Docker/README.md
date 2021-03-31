# 1-Docker

## Установка docker

Добавление репозитория docker:
```
$ sudo yum install -y yum-utils
$ sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
$ sudo yum-config-manager --setopt="docker-ce-stable.baseurl=https://download.docker.com/linux/centos/7/x86_64/stable" --save
```

Установка docker-ce:
```
$ sudo yum install docker-ce docker-ce-cli containerd.io
```

Старт docker и настройка его автоматического запуска при последующих стартах системы:
```
$ sudo systemctl start docker
$ sudo systemctl enable docker
```

Добавление текущего пользователя в группу docker, чтобы была возможность выполнять команды docker без root-прав:
```
$ sudo usermod -aG docker $(whoami)
```

Проверка:
```
$ sudo docker --version
$ docker--version
```

## Установка Docker Compose
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
```
sudo chmod +x /usr/local/bin/docker-compose
```

Проверка:
````
docker-compose --version
````

## Docker файл для сборки образа headnode
см. [*headnode_dockerfile*](headnode_dockerfile)

## Docker файл для сборки образа worker
см. [*worker_dockerfile*](worker_dockerfile)

# Создание своей подсети

```
docker network create --subnet 172.19.0.0/24 my-network
```

## Сборка образов

```
docker build -f headnode_dockerfile -t hadoop:namenode .
```

```
docker build -f headnode_dockerfile -t hadoop:worker .
```

## Запуск контейнеров
```
docker run -p 8088:8088 -itP --name headnode --network my-network --ip 172.19.0.2 --hostname headnode hadoop:headnode
```

```
docker run -p 8042:8042 -itP --name worker --network my-network --ip 172.19.0.3 --hostname worker hadoop:worker
```

## Результат

Если необходимо - настроить проброс портов с ВМ.

В браузере: 
localhost:8088 - ResourceManager WebUI
localhost:8042 - NodeManager WebUI

Результаты:

![Screenshot_1.png](screenshots/Screenshot_1.png)
![Screenshot_2.png](screenshots/Screenshot_2.png)
