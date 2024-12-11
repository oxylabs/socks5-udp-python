#!/usr/bin/python3

import argparse
import socket
import socks

PROXY_URL = "socks.pr.oxylabs.io"
PROXY_PORT = 7777
TARGET = "echo-udp.oxylabs.io"
TARGET_PORT = 42000
CONTENT = "Hello UDP!"


def parse_bool(s: str) -> bool:
    try:
        return {
            'true': True,
            'false': False,
            '1': True,
            '0': False,
        }[s.lower().strip()]
    except KeyError:
        raise argparse.ArgumentTypeError(f"unable to parse argument into boolean (received value: `{s}`)")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-u", "--username", help="Proxy username", type=str, required=True)
    parser.add_argument("-p", "--password", help="Proxy password", type=str, required=True)
    parser.add_argument("-pu", "--proxy_url", help="Proxy URL", type=str, default=PROXY_URL)
    parser.add_argument("-pp", "--proxy_port", help="Proxy port", type=int, default=PROXY_PORT)
    parser.add_argument("-t", "--target", help="Target (URL or IP)", type=str, default=TARGET)
    parser.add_argument("-tp", "--target_port", help="Target port", type=int, default=TARGET_PORT)
    parser.add_argument("-rdns", "--remote_dns", help="Resolve DNS remotely", type=parse_bool, default=True)
    parser.add_argument("-c", "--content", help="UDP datagram content to send", type=str, default=CONTENT)
    args = parser.parse_args()

    s = socks.socksocket(socket.AF_INET, socket.SOCK_DGRAM)
    s.set_proxy(socks.SOCKS5, args.proxy_url, args.proxy_port, args.remote_dns, args.username, args.password)
    s.settimeout(5) # Timeout set to 5 seconds
    try:
        s.sendto(bytes(args.content, "utf-8"), (args.target, args.target_port))
        (rsp, address) = s.recvfrom(4096)
    except Exception as e:
        print("Failed due to exception: ", e.__repr__())
    else:
        print("Response: ", rsp)
