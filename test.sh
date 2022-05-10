#!/bin/bash
#cp -r /home/ec2-user/test/gitRepo/pythonApp/ /var/www/html/python_code/
#cd /var/www/html/python_code/pythonApp/
cd /home/ec2-user/test/gitRepo/pythonApp
pip install flask
session="flasksession"
# Check if the session exists, discarding output
# We can check $? for the exit status (zero for success, non-zero for failure)
tmux has-session -t $session 2>/dev/null
if [ $? != 0 ]; then
  tmux new -s $session
fi
# Attach to created session
tmux attach-session -t $session
curl 'http://<IP>:<PORT>/shutdown'
sudo python python.py
tmux detach
