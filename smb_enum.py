from smbconnection import SMBConnection
from argparse import ArgumentParser


def list_shares(ip_address, username, password=None):
    conn = SMBConnection(ip_address, ip_address)
    conn.login(username, password)
    shares = conn.listShares()
    for share in shares:
        print(f"Share name: {share['shi1_netname']}")
        print(f"Share type: {share['shi1_type']}")
        print(f"Share comment: {share['shi1_remark']}")
        print("")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("ip_address", help="IP address of the remote machine")
    parser.add_argument("username", help="Username to connect to the remote machine")
    args = parser.parse_args()
    list_shares(args.ip_address, args.username, password=None)

