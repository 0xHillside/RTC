#!/usr/bin/env python3
import os
import subprocess
import argparse
import base64
import re

# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional arguments
parser.add_argument("-f", "--file", help="The txt file containing the base64 ticket")
parser.add_argument("-r", "--read", help="The base64 text itself containing the ticket")

# Read arguments from command line
args = parser.parse_args()

# Handle file argument
if args.file:
    print(f"[+] text file provided: {args.file}")
    with open(args.file, "r") as input_file:
        file_content = input_file.read()
    decoded_file = base64.b64decode(file_content)
    cut_name = re.split(r'\W+', args.file)[0]
    with open(f'{cut_name}.kirbii', "wb") as f:
        f.write(decoded_file)
    print(f"[+] kirbii file saved: {cut_name}.kirbii")
    os.system(f'impacket-ticketConverter {cut_name}.kirbii "{cut_name}.ccache"')
    print(f"[+] ccache file saved: {cut_name}.cacche")


if args.read:
    print(f"[+] text provided: {args.read}")
    decoded_read = base64.b64decode(args.read)
    with open(f'ticket.kirbii', "wb") as f:
        f.write(decoded_read)
    print(f"[+] text file saved: ticket.kirbii")
    os.system(f'impacket-ticketConverter ticket.kirbii "ticket.ccache"')
    print(f"[+] cacche saved: ticket.cacche")
