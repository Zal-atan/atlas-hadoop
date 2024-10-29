#!/usr/bin/python3
"""Module which creates the deletedir(l)"""
from snakebite.client import Client


def deletedir(l):
    """
    Removes the directories listed on l within HDFS

    Inputs:
    l - list of directories to be deleted
    """
    client = Client('127.0.0.1', 9000)

    try:
        for rm_dir in client.delete(l, recurse=True):
            print(rm_dir)
    except Exception as e:
        pass
