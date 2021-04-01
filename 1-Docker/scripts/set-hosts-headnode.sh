
my_IP=$(awk 'END{print $1}' /etc/hosts)

echo "$my_IP headnode" >> /etc/hosts

dev_num=$(( $(echo $my_IP | awk -F"." '{print $4}')+1 ))
worker_IP=$(echo $my_IP | awk -F"." -v dev_num="$dev_num" '{print $1 "." $2 "." $3 "." dev_num}')
echo "$worker_IP worker" >> /etc/hosts






