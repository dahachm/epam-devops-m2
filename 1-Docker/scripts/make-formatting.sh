#Creating new cluster fs
chown hdfs:hadoop /opt/namenode-dir
chmod g+w /opt/namenode-dir
sudo -u hdfs $HADOOP_HOME/bin/hdfs namenode -format cluster1

chmod 775 $HADOOP_HOME/logs

