ORIG to L14

/usr/lib/inithooks/firstboot.d/50admin-db-pass

#!/bin/bash -e
# set odoo db password

. /opt/openerp/odoo/openerp-server.conf

updateconf() {
    CONF=/opt/openerp/odoo/openerp-server.conf

    sed -i "admin_password = admin" / "admin password = ${ODOO_PASS]" $CONF
}
------------
Tendenci Hints Below
-------------
#!/usr/bin/python
"""Set Tendenci admin password and email

Option:
    --pass=     unless provided, will ask interactively
    --email=    unless provided, will ask interactively

"""

import os
import sys
import getopt
import hashlib
import random

import hmac
import struct
import binascii
import operator

from dialog_wrapper import Dialog
from pgsqlconf import PostgreSQL

_trans_5c = "".join([chr(x ^ 0x5C) for x in xrange(256)])
_trans_36 = "".join([chr(x ^ 0x36) for x in xrange(256)])

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def _bin_to_long(x):
    """
    Convert a binary string into a long integer

    This is a clever optimization for fast xor vector math
    """
    return long(x.encode('hex'), 16)


def _long_to_bin(x, hex_format_string):
    """
    Convert a long integer into a binary string.
    hex_format_string is like "%020x" for padding 10 characters.
    """
    return binascii.unhexlify(hex_format_string % x)

def _fast_hmac(key, msg, digest):
    """
    A trimmed down version of Python's HMAC implementation
    """
    dig1, dig2 = digest(), digest()
    if len(key) > dig1.block_size:
        key = digest(key).digest()
    key += chr(0) * (dig1.block_size - len(key))
    dig1.update(key.translate(_trans_36))
    dig1.update(msg)
    dig2.update(key.translate(_trans_5c))
    dig2.update(dig1.digest())
    return dig2

def _get_pbkdf2_hashpass(password):
    salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
    algorithm = 'pbkdf2_sha256'
    iterations = 10000
    digest = hashlib.sha256
    hash = pbkdf2(password, salt, iterations, digest=digest)
    hash = hash.encode('base64').strip()
    return "%s$%d$%s$%s" % (algorithm, iterations, salt, hash)

def _get_hashpass(password):
    salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
    hash = hashlib.sha1(salt + password).hexdigest()
    return 'sha1$%s$%s' % (salt, hash)

def pbkdf2(password, salt, iterations, dklen=0, digest=None):
    """
    Implements PBKDF2 as defined in RFC 2898, section 5.2

    HMAC+SHA256 is used as the default pseudo random function.

    Right now 10,000 iterations is the recommended default which takes
    100ms on a 2.2Ghz Core 2 Duo.  This is probably the bare minimum
    for security given 1000 iterations was recommended in 2001. This
    code is very well optimized for CPython and is only four times
    slower than openssl's implementation.
    """
    assert iterations > 0
    if not digest:
        digest = hashlib.sha256
    hlen = digest().digest_size
    if not dklen:
        dklen = hlen
    if dklen > (2 ** 32 - 1) * hlen:
        raise OverflowError('dklen too big')
    l = -(-dklen // hlen)
    r = dklen - (l - 1) * hlen

    hex_format_string = "%%0%ix" % (hlen * 2)

    def F(i):
        def U():
            u = salt + struct.pack('>I', i)
            for j in xrange(int(iterations)):
                u = _fast_hmac(password, u, digest).digest()
                yield _bin_to_long(u)
        return _long_to_bin(reduce(operator.xor, U()), hex_format_string)

    T = [F(x) for x in range(1, l + 1)]
    return ''.join(T[:-1]) + T[-1][:r]

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'email='])
    except getopt.GetoptError, e:
        usage(e)

    password = ""
    email = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--email':
            email = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "Tendenci Password",
            "Enter new password for the Tendenci 'admin' account.")

    if not email:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        email = d.get_email(
            "Tendenci Email",
            "Enter email address for the Tendenci 'admin' account.",
            "admin@example.com")

    hashpass = _get_pbkdf2_hashpass(password)

    p = PostgreSQL(database='tendenci')

    p.execute("UPDATE auth_user SET email='%s' WHERE username='admin';" % email)
    p.execute("UPDATE auth_user SET password='%s' WHERE username='admin';" % hashpass)

if __name__ == "__main__":
    main()
