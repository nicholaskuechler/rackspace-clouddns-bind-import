$TTL    3600

example.com.       IN      SOA     ns1.example.com. root.example.com. (
                                2011051701 ; Serial
                                3600      ; Refresh
                                900       ; Retry
                                1209600   ; Expire
                                3600 )    ; Minimum

example.com.       IN  MX 1    ASPMX.L.GOOGLE.COM.
example.com.       IN  MX 5    ALT1.ASPMX.L.GOOGLE.COM.
example.com.       IN  MX 5    ALT2.ASPMX.L.GOOGLE.COM.
example.com.       IN  MX 10   ASPMX2.GOOGLEMAIL.COM.
example.com.       IN  MX 10   ASPMX3.GOOGLEMAIL.COM.
example.com.       IN  MX 10   ASPMX4.GOOGLEMAIL.COM.
example.com.       IN  MX 10   ASPMX5.GOOGLEMAIL.COM.

$ORIGIN example.com.

example.com.    IN      A       127.0.0.1
www             IN      A       127.0.0.1
; google services
mail        IN  CNAME   ghs.google.com.
docs        IN  CNAME   ghs.google.com.
calendar    IN  CNAME   ghs.google.com.
