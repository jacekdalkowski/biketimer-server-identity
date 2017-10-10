import os
from docker_digitalocean_common import *

def copy_identity_src_to_remote_host(ssh_con_str):
	pwd = run_local_command("pwd").rstrip()
	local_dir = pwd + "/../*"
	print "Copying web-identity src (" + local_dir + ") to remote host."
	rsync_cmd = "rsync -azP --delete --exclude '*/node_modules' " + local_dir + " " + ssh_con_str + ":/root/apps/biketimer/web-identity"
	print "rsync command: " + rsync_cmd
	os.system(rsync_cmd)
	print "Copying web-identity src to remote host finished."

def build_identity_continer_in_remote_host(ssh):
	print "Building biketimer/web-identity image in remote host."
	result = ssh("docker build -t biketimer/web-identity /root/apps/biketimer/web-identity")
	print "Building biketimer/web-identity image in remote host result: "
	print result

def run_identity_container(ssh):
	print "Starting biketimer-web-identity container in remote host."
	result = ssh("docker run -p 8080:8080 --name biketimer-web-identity --link biketimer-web-db:biketimer-db -d biketimer/web-identity")
	print "Starting biketimer-web-identity container in remote host result: "
	print result

