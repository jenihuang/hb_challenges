"""Turn a string of 24h time into words.

You can trust that you'll be given a valid string (it will
always have a two-digit hour 00-23, and a two-digit minute
00-59). Hours 0-11 are am, and hours 12-23 are pm.

Handle noon and midnight specially:

    >>> time_word("00:00")
    'midnight'

    >>> time_word("12:00")
    'noon'

Otherwise, covert times to text:

    >>> time_word("01:00")
    "one o'clock am"

    >>> time_word("06:01")
    'six oh one am'

    >>> time_word("06:10")
    'six ten am'

    >>> time_word("06:18")
    'six eighteen am'

    >>> time_word("06:30")
    'six thirty am'

    >>> time_word("10:34")
    'ten thirty four am'

Don't forget to handle early morning properly:

    >>> time_word("00:12")
    'twelve twelve am'

For times after noon, add 'pm'

    >>> time_word("12:09")
    'twelve oh nine pm'

    >>> time_word("23:23")
    'eleven twenty three pm'

By Joel Burton <joel@joelburton.com>.
"""


def time_word(time):
    """Convert time to text."""


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. YOU'RE A TIME WIZARD!\n")