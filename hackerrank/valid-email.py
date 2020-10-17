# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import email.utils
import re


def parse_mail(s):
    res = email.utils.parseaddr(s)
    if len(res) != 2:
        return

    r = re.search("^[a-zA-Z].[a-zA-Z0-9._-]*", res[0])
    if r is None:
        return

    r = re.search("^[a-zA-Z].[a-zA-Z0-9._-]*@[a-zA-Z]*[.]([a-zA-Z]){1,3}$", res[1])
    if r is None:
        return

    print(email.utils.formataddr((res[0], res[1])))


if __name__ == '__main__':
    parse_mail('this <is_som@radom.stuff>')

    n = int(input())

    for i in range(0, n):
        parse_mail(input())
