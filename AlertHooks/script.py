#!/usr/bin/env python3
from .alertHooks import AlertHooks
from argparse import ArgumentParser

def send_msg(args):
    AlertHooks().send(args.alias, args.msg)

def add_alias(args):
    AlertHooks().add_alias(args.alias, args.url)

def remove_alias(args):
    AlertHooks().rm_alias(args.alias)

def list_alias(args):
    AlertHooks().list_config()


def parse_args():
    parser = ArgumentParser(prog="alerthooks",
                            description="A simple program to send webhook messages using cmd-line",
                            epilog="---MycoG 2026---")
    subparsers = parser.add_subparsers(dest="cmd" )
    subparsers.required = True

    #add cmd
    add_parser = subparsers.add_parser("add", aliases=['a'], help="add webhook alias")
    add_parser.add_argument("-a", "--alias", help="name of webhook to add", required=True)
    add_parser.add_argument("-u", "--url", help="url of webhook to add", required=True)
    add_parser.set_defaults(func=add_alias)

    #remove cmd
    remove_parser = subparsers.add_parser("remove", aliases=["rm"], help="remove webhook alias")
    remove_parser.add_argument("-a", "--alias", help="name of webhook alias to remove", required=True)
    remove_parser.set_defaults(func=remove_alias)

    #lst cmd
    list_parser = subparsers.add_parser("list", aliases=["ls"], help="list available aliases", 
                                        description="lists availabe aliases and their urls")
    list_parser.set_defaults(func=list_alias)

    #send cmd
    send_parser = subparsers.add_parser("send", aliases=["s"], help="send txt to webhook")
    send_parser.add_argument("-a","--alias", help="name of webhook to send to", required=True)
    send_parser.add_argument("-m","--msg", help="msg content", required=True)
    send_parser.set_defaults(func=send_msg)

    return parser.parse_args()

def main():
    args = parse_args()
    if hasattr(args, 'func'):
        args.func(args)

if __name__ == "__main__":
    main()
