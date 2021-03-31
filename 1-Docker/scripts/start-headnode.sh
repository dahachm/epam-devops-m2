#Set network configurations
echo "172.19.0.3      worker" >> /etc/hosts 

#Creating new cluster fs
chown hdfs:hadoop /opt/namenode-dir
chmod g+w /opt/namenode-dir
sudo -u hdfs $HADOOP_HOME/bin/hdfs namenode -format cluster1

chmod 775 $HADOOP_HOME/logs

#Start namenode
sudo -u hdfs $HADOOP_HOME/bin/hdfs --daemon start namenode

#Start resourcemanager
sudo -u yarn $HADOOP_HOME/bin/yarn --daemon start resourcemanager
