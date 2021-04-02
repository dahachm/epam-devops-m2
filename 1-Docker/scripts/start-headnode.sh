#Start namenode
sudo -u hdfs $HADOOP_HOME/bin/hdfs --daemon start namenode

#Start resourcemanager
sudo -u yarn $HADOOP_HOME/bin/yarn --daemon start resourcemanager
