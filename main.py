#!/usr/bin/env python3

import argparse
import datetime
from getpass import getpass

__version__ = "v0.1"
__author__ = "GiantDwarf"
__date__ = datetime.datetime(year=2020, month=4, day=4)

sites = ["a", "b", "c", "d"]


def password_generator(**kwargs):
    print(kwargs)
    print("this is a password")


def password_setter(site=None, encryption=None, **kwargs):
    print(kwargs)
    print(f"adding password to {site}")


def password_getter(site=None, encryption=None, **kwargs):
    print(kwargs)
    print(f"getting password of {site}")


def main():
    parser = argparse.ArgumentParser(prog="kb", 
                                     description="Key Bearer, the place to "\
                                                 "store all your passwords.")

    parser.add_argument("--version", action="store_true",
                        help="print the key bearer version.")

    subparser = parser.add_subparsers(help="the action to take")

    # ======================== Generate Password parser =======================
    generate_password = subparser.add_parser("generate",
                                             description="Generate a password")
    generate_password.set_defaults(func=password_generator)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ========================== Set Password parser ==========================
    set_password = subparser.add_parser("set",
                                        description="Add/set a password")
    set_password.add_argument("site", choices=sites, 
                              help="the password for which site.")
    set_password.add_argument("--generate", action="store_true",
                              help="also generate and print a new password.")
    set_password.add_argument("--encryption", "-e", choices=[],
                              help="the encryption method to use.")
    set_password.set_defaults(func=password_setter)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ========================== Get Password parser ==========================
    get_password = subparser.add_parser("get",
                                        description="Get a password")
    get_password.add_argument("site", choices=sites, 
                              help="the password for which site.")
    get_password.add_argument("--encryption", "-e", choices=[],
                              help="the encryption method to use.")
    get_password.set_defaults(func=password_getter)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    args = parser.parse_args()

    # Version printing
    if args.version:
        print(f"KeyBearer (kb) version {__version__}.",
              f"created by {__author__} at {__date__:%x}")
        return 0

    args.func(**vars(args))

if __name__ == "__main__":
    exit(main())