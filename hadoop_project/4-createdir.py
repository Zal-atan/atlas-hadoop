#!/usr/bin/python3
"""Module creating function createdir(l)"""
from snakebite.client import Client


def createdir(l):
    """
    Creates the directories listed on l within HDFS

    Inputs:
    l - list of directories
    """
    client = Client('127.0.0.1', 9000)

    for new_dir in client.mkdir(l, create_parent=True):
        print(new_dir)

