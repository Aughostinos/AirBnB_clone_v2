#!/usr/bin/python3
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Compress before sending
    """
    # Create versions directory if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Create the archive name
    now = datetime.now()
    archive_name = "versions/web_static_{}.tgz".format(now.strftime(
                                                        "%Y%m%d%H%M%S"))

    # Create the archive
    command = "tar -cvzf {} web_static".format(archive_name)
    result = local(command)

    if result.succeeded:
        return archive_name
    else:
        return None