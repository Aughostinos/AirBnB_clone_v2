#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""
from fabric import Connection, task
import os

env_hosts = ['52.3.249.236_web_01', '100.25.20.88_web_02']


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False
    
    archine_name = os.path.basename(archive_path)
    archive_wout_ext = archine_name.split('.')[0]

    tmp_path = "/tmp/{}".format(archine_name)
    release_dir = "/data/web_static/releases/{}/".format(archive_wout_ext)
    current_symplic_link = "/data/web_static/current"

    try:
        #Upload the archive to the /tmp/ directory of the web server
        put(archive_path, tmp_path)
        # Create the directory and Uncompress the archive to the folder 
        # /data/web_static/releases/
        # <archive filename without extension> on the web server
        run("mkdir -p {}".format(release_dir))
        run("tar -xzf {} -C {}".format(tmp_path, release_dir))         
        #Delete the archive from the web server
        run("rm {}".format(tmp_path))
        #simplify the structure
        run("mv{}/web_static/* {}".format(release_dir, release_dir))
        run("rm -rf {}web_static".format(release_dir))
        #Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf {}".format(current_symplic_link))
        #Create a new the symbolic link 
        # /data/web_static/current on the web server,
        # linked to the new version of your code
        # (/data/web_static/releases/<archive filename without extension>)
        run("ln -s {}{}".format(release_dir, current_symplic_link))

        return True

    except Exception as e:
        print("deployment failed: {}".format(e))
        return False