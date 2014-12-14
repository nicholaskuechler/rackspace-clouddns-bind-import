rackspace-clouddns-bind-import
==============================

Rackspace Cloud DNS import tool for BIND DNS zones

## Requirements:

* argparse
* python-clouddns

## Required inputs:

* Rackspace Cloud username
* Rackspace Cloud API key
* Full path to BIND formatted DNZ zone

## BIND DNS zone formatting:

See the example DNS zone (example.com) for BIND formatting. You may need to
replace "@" in your BIND zone with your full domain, such that

    @       IN  MX 1    mail.example.com.

Becomes:

    example.com.       IN  MX 1    mail.example.com.
