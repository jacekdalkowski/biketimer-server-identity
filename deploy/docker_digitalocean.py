import subprocess
import re
import os
import time
import sh
import time
from docker_digitalocean_identity import *

ssh_con_str = "root@67.205.147.105"

print "NOTICE: this script has to be run as a user with access to SSH keys."
print "Deployment to remote server (" + ssh_con_str + ") started."

ssh = sh.ssh.bake('-oStrictHostKeyChecking=no', ssh_con_str)

print "Successfully connected to remote server."

kill_and_remove_all_containers(ssh, 'biketimer-web-identity')

copy_identity_src_to_remote_host(ssh_con_str)
build_identity_continer_in_remote_host(ssh)
run_identity_container(ssh)



