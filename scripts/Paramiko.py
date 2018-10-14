import paramiko
import time

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    print 'Is the SSH active: ', client.get_transport().is_active()
    return client

def copy_file(hostname, port, username, password, src, dst):
    ssh = createSSHClient(hostname, port, username, password)
    sftp = ssh.open_sftp()
    t1 = time.time()
    sftp.put(src, dst)
    t2 = time.time()
    print src + ' >>> ' + dst
    print(t2 - t1)
    print
    sftp.close()
    ssh.close()

def get_file(hostname, port, username, password, src, dst):
    ssh = createSSHClient(hostname, port, username, password)
    sftp = ssh.open_sftp()
    t1 = time.time()
    sftp.get(src, dst)
    t2 = time.time()
    print src + ' >>> ' + dst
    print(t2 - t1)
    print
    sftp.close()
    ssh.close()

copy_file("js4.es.aau.dk", 22, "breise18", "", "/Users/reiserbalazs/Desktop/starter_picture.png", "./arrived_picture.png")
get_file("js4.es.aau.dk", 22, "breise18", "", "./arrived_picture.png", "/Users/reiserbalazs/Desktop/traveller_picture.png")






