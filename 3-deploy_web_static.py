#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to your web servers"""

from fabric.api import *
import os
from datetime import datetime

env.hosts = ['54.209.116.255', '52.91.144.185']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        if not os.path.exists("versions"):
            os.makedirs("versions")
        now = datetime.now()
        archive_name = "versions/web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except Exception as e:
        print("Error creating archive: {}".format(e))
        return None


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False

    archive_name = os.path.basename(archive_path)
    archive_wout_ext = archive_name.split('.')[0]

    tmp_path = "/tmp/{}".format(archive_name)
    release_dir = "/data/web_static/releases/{}/".format(archive_wout_ext)
    current_symlink = "/data/web_static/current"

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, tmp_path)
        
        # Create the directory and uncompress the archive to the folder
        run("mkdir -p {}".format(release_dir))
        run("tar -xzf {} -C {}".format(tmp_path, release_dir))
        
        # Delete the archive from the web server
        run("rm {}".format(tmp_path))
        
        # Simplify the structure
        run("mv {}/web_static/* {}".format(release_dir, release_dir))
        run("rm -rf {}/web_static".format(release_dir))
        
        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf {}".format(current_symlink))
        
        # Create a new symbolic link /data/web_static/current on the web server
        run("ln -s {} {}".format(release_dir, current_symlink))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False


def deploy():
    """Creates and distributes an archive to web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
