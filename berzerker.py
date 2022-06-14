import os
import argparse

from dotenv import load_dotenv
from malwarebazaar.api import Bazaar
from pkg_resources import require

__author__ = "Brian Sypher"
__email__ = "bseyeph@gmail.com"

load_dotenv()
BZ = Bazaar(os.getenv("API_KEY"))

def download_sample(hash: str):
    try:
        sample = BZ.download_file(hash)
        with open(f"{hash}.zip", "wb") as danger:
            danger.write(sample)
        return True
    except Exception as exc:
        print(f"Failed: {exc}")
        return False


if __name__ == "__main__":
    # Top level parser
    parser = argparse.ArgumentParser(description="Interact with Malware Bazaar API")
    sub_parsers = parser.add_subparsers(help='Sub command help')
    # Download subparser
    parser_download = sub_parsers.add_parser('download', help='Download a sample from Malware Bazaar')
    parser_download.add_argument('--sample', '-s', type=str, required=True, help="SHA-256 hash of the sample to be downloaded")

    args = parser.parse_args()

    if args.sample:
        download_sample(args.sample)