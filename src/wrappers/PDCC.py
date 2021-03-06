#!/usr/bin/env python

import os
from os import path
from subprocess import check_call

import arg_parser
import context


def main(delta_conf):
    args = arg_parser.receiver_first()

    cc_repo = path.join(context.third_party_dir, 'PDCC')
    recv_src = path.join(cc_repo, 'receiver')
    send_src = path.join(cc_repo, 'sender')

    if args.option == 'deps':
        print ('makepp libboost-dev libprotobuf-dev protobuf-c-compiler '
               'protobuf-compiler libjemalloc-dev libboost-python-dev')
        return

    if args.option == 'setup':
        
        return

    if args.option == 'receiver':
        cmd = [recv_src, args.port]
        check_call(cmd)
        return

    if args.option == 'sender':
        sh_cmd = (
            'export MIN_RTT=1000000 && %s serverip=%s serverport=%s '
            'offduration=1 onduration=1000000 traffic_params=deterministic,'
            'num_cycles=1 cctype=pdc lamda_conf=%s Bd_conf=10 Rc_conf=30'
            % (send_src, args.ip, args.port, delta_conf))

        with open(os.devnull, 'w') as devnull:
            # suppress debugging output to stdout
            check_call(sh_cmd, shell=True, stdout=devnull)
        return


if __name__ == '__main__':
    main('do_ss:compete:auto_theta:auto:1')
