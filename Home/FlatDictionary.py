def flatten(dictionary):
    stack = [((), dictionary)]              #Testing
    result = {}
    while stack:
        path, current = stack.pop()
        for k, v in current.items():
            if isinstance(v, dict):
                stack.append((path + (k,), v))
            else:
                result["/".join((path + (k,)))] = v
    print(result)
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}
    assert flatten({"empty": {}}) == {"empty": ""}
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}