#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import datetime
import io
import paramiko
import os
import pings
import sys
import time


def deco_function(func):
    def exec_time_print(*args, **kwargs):
        #print(str(datetime.datetime.now())[:-7] + " " + func.__name__)
        func(*args, **kwargs)
    return exec_time_print


@deco_function
def exec_ping(server_name):
    """

    """
    p = pings.Ping()
    res = p.ping(server_name, times=2)

    if res.is_reached():
        print("[INFO] ping Success")
    else:
        print("[ERROR] ping Failed")


@deco_function
def exec_ssh(server_name, username="root", cmd="hostname"):
    """

    """
    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        key_path = paramiko.RSAKey.from_private_key_file("/root/.ssh/id_rsa")
        ssh.connect(hostname=server_name, port=22, username=username, pkey=key_path)
        stdin, stdout, stderr = ssh.exec_command(cmd)

        for err_line in stderr:
            print("[ERROR] ssh failed" + err_line.strip("\n"))
            sys.exit(1)
        for out_line in stdout:
            print("[INFO] ssh Success " + out_line.strip("\n"))


def exec_service_restart(server_name, services):
    """

    """
    print(server_name, services)


def option_parse():
    """

    """
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("SERVER_NAME", help="Server name to be restarted.")
    parser.add_argument("SERVICE", help="The service to be restarted. [all | httpd_prox | modperl]")
    parser.add_argument("-i", type=str, default="/root/.ssh/id_rsa", help="identity_file")
    return parser.parse_args()


def main(args):
    msg = f"########## DEPLOY INFO ##########\n\
DEPLOY_DATE  : {str(datetime.datetime.now())[:-7]}\n\
SERVER_NAEME : {args.SERVER_NAME}\n\
SERVICE_TYPE : {args.SERVICE}\n\
IDENTITY_FILE : {args.i}"
    print(msg)

    # pingを実行
    exec_ping(args.SERVER_NAME)

    # sshを実行
    exec_ssh(args.SERVER_NAME)

    if args.SERVICE == "all":
        service = ["pwd", "uname"]
    elif args.SERVICE == "test":
        service = ["ls -l", "uname -a", "pwd"]
    else:
        service = [args.SERVICE]

    exec_service_restart(args.SERVER_NAME, service)

    print("#################################")


if __name__ == "__main__":
    args = option_parse()
    main(args)
