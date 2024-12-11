# OxyLabs SOCKS5 UDP sample with Python

This is a basic example of how to send a UDP datagram over SOCKS5 UDP proxy to a UDP listening server.

Tested with Python 3.8 and PySocks 1.7.1.

Install required module:
```
pip install pysocks
```

Usage:
```
python3 udp_sample.py [-h] -u USERNAME -p PASSWORD [-pu PROXY_URL] [-pp PROXY_PORT] [-t TARGET] [-tp TARGET_PORT] [-rdns REMOTE_DNS] [-c CONTENT]

e.g.
python3 udp_sample.py -u john_proxyuser -p SomeSecurePassword$42
python3 udp_sample.py -pu socks.pr.oxylabs.io -pp 7777 -rdns false -t echo-udp.oxylabs.io -tp 42000  -u john_proxyuser -p SomeSecurePassword$42 -c "Well, hello there!"
```


Arguments:
```
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Proxy username (default: None)
  -p PASSWORD, --password PASSWORD
                        Proxy password (default: None)
  -pu PROXY_URL, --proxy_url PROXY_URL
                        Proxy URL (default: socks.pr.oxylabs.io)
  -pp PROXY_PORT, --proxy_port PROXY_PORT
                        Proxy port (default: 7777)
  -t TARGET, --target TARGET
                        Target (URL or IP) (default: echo-udp.oxylabs.io)
  -tp TARGET_PORT, --target_port TARGET_PORT
                        Target port (default: 42000)
  -rdns REMOTE_DNS, --remote_dns REMOTE_DNS
                        Resolve DNS remotely (default: True)
  -c CONTENT, --content CONTENT
                        UDP datagram content to send (default: Hello UDP!)
```
