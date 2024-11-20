"""Do this now """


def main():
    string = "?name=Bob&age=99&day=Wed"

    pairs = extract_pairs(string)
    result = [('name', 'Bob'), ('age', 99), ('day', 'Wed')]
    assert pairs == result
    print(pairs)


def extract_pairs(string):
    """Extract name-value pairs as tuples in a list from a query string"""
    if not string.startswith('?'):
        return []
    pairs = []
    parts = string[1:].split('&')
    for part in parts:
        pair = part.split('=')
        try:
            pairs.append(tuple((pair[0], int(pair[1]))))
            # pair[1] = int(pair[1])
        except ValueError:
            # pass
            pairs.append(tuple(pair))
    return pairs


main()
