#!/usr/bin/env python

import os
import argparse
import clouddns


def main(username, api_key, file_path, verbose):
    if os.path.exists(file_path) and os.path.isfile(file_path):
        print "Importing bind9 zone file: %s" % (file_path)

        try:
            with open(file_path, 'r') as f:
                dns = clouddns.connection.Connection(username, api_key)
                dns.import_domain(f)
        except Exception as e:
            print "Error: Problem importing zone: %s" % (file_path)
            print e

    else:
        print "Error: %s does not exist or is not a file!" % (file_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Import a BIND DNS zone in "
                                                 "to Rackspace Cloud DNS")

    parser.add_argument("username", type=str,
                        help="Rackspace Cloud username. "
                             "Example: someuser")
    parser.add_argument("api_key", type=str,
                        help="Rackspace Cloud API key. "
                             "Example: 6832fbadcbd98238428abcabc1231abc")
    parser.add_argument("file_path", type=str,
                        help="Full path to BIND zone file. "
                             "Example: /Users/someuser/bind/example.com")
    parser.add_argument("-v", "--verbose", action="store_true",
                        default=False,
                        help="Increase output verbosity")

    args = parser.parse_args()
    main(args.username, args.api_key, args.file_path, args.verbose)
