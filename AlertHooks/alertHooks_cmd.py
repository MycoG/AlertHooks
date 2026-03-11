#!/usr/bin/env python3

from argparse import ArgumentParser

def send_msg(args):
    pass

def add_alias(args):
    pass

def remove_alias(args):
    pass

def list_alias(args):
    print("listing webhooks...")
    pass

def main():
    pass

def parse_args():
    parser = ArgumentParser(prog="alerthooks",
                            description="A simple program to send webhook messages using cmd-line",
                            epilog="---Myco Torres 2026---")
    subparsers = parser.add_subparsers(dest="command" )

    #create command
    add_parser = subparsers.add_parser("add", aliases=['a'], help="add webhook alias")
    add_parser.add_argument("alias", help="name of webhook to add")
    add_parser.add_argument("url", help="url of webhook to add")
    add_parser.set_defaults(func=add_alias)

    remove_parser = subparsers.add_parser("remove", aliases=["rm"], help="remove webhook alias")
    remove_parser.add_argument("alias", help="name of webhook alias to remove")
    remove_parser.add_argument("-f", "--force", help="ignore prompt for removal")
    remove_parser.set_defaults(func=remove_alias)

    list_parser = subparsers.add_parser("list", aliases=["ls"], help="list available aliases", 
                                        description="lists availabe aliases and their urls")
    list_parser.set_defaults(func=list_alias)

    send_parser = subparsers.add_parser("send", aliases=["s"], help="send txt to webhook")
    send_parser.add_argument("alias", help="name of webhook to send to")
    send_parser.add_argument("msg", help="msg content")
    send_parser.set_defaults(func=send_msg)

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    if hasattr(args, 'func'):
        args.func(args)
