from .lib.parse import Parse
import argparse
import sys

def argument():
    if len(sys.argv) == 1:
        sys.argv.append("--help")
    parser = argparse.ArgumentParser(description="This is a command to check if crawls are allowed for URL.  Also, you can also get the Allow list and Disallow list by using the option")
    parser.add_argument("URL", help="URL you want to crawl")
    parser.add_argument("-u", "--user-agent", default="*", help="User-agent you want to check")
    parser.add_argument("-a", "--allow", action="store_true")
    parser.add_argument("-d", "--disallow", action="store_true")
    return parser.parse_args()

def main():
    args = argument()
    p = Parse(args.URL)
    if not args.allow and not args.disallow:
        if p.can_crawl(args.URL, useragent=args.user_agent):
            print("Y")
        else:
            print("N")
    else:
        if args.allow:
            print("\n".join(p.Allow(args.user_agent)))
        if args.disallow:
            print("\n".join(p.Disallow(args.user_agent)))

if __name__ == "__main__":
    main()