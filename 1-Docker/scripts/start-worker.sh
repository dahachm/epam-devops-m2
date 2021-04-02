#Creating logs directory
mkdir $HADOOP_HOME/logs
chown hadoop:hadoop $HADOOP_HOME/logs
chmod 775 $HADOOP_HOME/logs

chown hdfs:hadoop /opt/datanode-dir
chmod 775 /opt/datanode-dir
chown yarn:hadoop /opt/nodemanager-local-dir
chmod 775 /opt/nodemanager-local-dir
chown yarn:hadoop /opt/nodemanager-log-dir
chmod 775 /opt/nodemanager-log-dir

#Start datanode
sudo -u hdfs $HADOOP_HOME/bin/hdfs --daemon start datanode

#Start resourcemanager
sudo -u yarn $HADOOP_HOME/bin/yarn --daemon start nodemanager
