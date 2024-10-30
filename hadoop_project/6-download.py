#!/usr/bin/python3
""" Module creating the download(l) function"""
from snakebite.client import Client


def download(l):
    """
    Retrieves from the HDFS files listed in l and store them in the
    home /tmp folder of the user

    Inputs:
    l - list od files to download
    """
    client = Client('127.0.0.1', 9000)

    for dl in client.copyToLocal(l, '/tmp'):
        print(dl)
