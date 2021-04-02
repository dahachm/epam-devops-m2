#Load configuration files
curl -o $HADOOP_HOME/etc/hadoop/hadoop-env.sh  https://gist.githubusercontent.com/rdaadr/2f42f248f02aeda18105805493bb0e9b/raw/6303e424373b3459bcf3720b253c01373666fe7c/hadoop-env.sh
curl -o $HADOOP_HOME/etc/hadoop/core-site.xml https://gist.githubusercontent.com/rdaadr/64b9abd1700e15f04147ea48bc72b3c7/raw/2d416bf137cba81b107508153621ee548e2c877d/core-site.xml
curl -o $HADOOP_HOME/etc/hadoop/hdfs-site.xml  https://gist.githubusercontent.com/rdaadr/2bedf24fd2721bad276e416b57d63e38/raw/640ee95adafa31a70869b54767104b826964af48/hdfs-site.xml
curl -o $HADOOP_HOME/etc/hadoop/yarn-site.xml  https://gist.githubusercontent.com/Stupnikov-NA/ba87c0072cd51aa85c9ee6334cc99158/raw/bda0f760878d97213196d634be9b53a089e796ea/yarn-site.xml

#Set required vars
sed -i -r 's|(export JAVA_HOME=)(.*)|\1/usr/lib/jvm/java-1.8-openjdk/jre|' $HADOOP_HOME/etc/hadoop/hadoop-env.sh
sed -i -r 's|(export HADOOP_HOME=)(.*)|\1/usr/local/hadoop-3.1.2|' $HADOOP_HOME/etc/hadoop/hadoop-env.sh
sed -i -r 's|(export HADOOP_HEAPSIZE_MAX=)(.*)|\1512|' $HADOOP_HOME/etc/hadoop/hadoop-env.sh

sed -i 's/%HDFS_NAMENODE_HOSTNAME%/headnode/' $HADOOP_HOME/etc/hadoop/core-site.xml

sed -i 's|%NAMENODE_DIRS%|/opt/namenode-dir|' $HADOOP_HOME/etc/hadoop/hdfs-site.xml
sed -i 's|%DATANODE_DIRS%|/opt/datanode-dir|' $HADOOP_HOME/etc/hadoop/hdfs-site.xml

sed -i 's|%YARN_RESOURCE_MANAGER_HOSTNAME%|headnode|' $HADOOP_HOME/etc/hadoop/yarn-site.xml
sed -i 's|%NODE_MANAGER_LOCAL_DIR%|/opt/nodemanager-local-dir|' $HADOOP_HOME/etc/hadoop/yarn-site.xml
sed -i 's|%NODE_MANAGER_LOG_DIR%|/opt/nodemanager-log-dir|' $HADOOP_HOME/etc/hadoop/yarn-site.xml
