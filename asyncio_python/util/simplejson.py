def loads(data):
    if isinstance(data, bool):
        return "true" if data else "false"

    # hard cases as python int is arbitary percision integer
    if isinstance(data, (int, float)):
        return str(data)

    if isinstance(data, str):
        return f'"{data}"'

    if isinstance(data, dict):
        return "{" + ",".join('"{}": {}'.format(k, loads(v)) for (k, v) in data.items()) + "}"

    if isinstance(data, list):
        return "[" + ",".join(loads(v) for v in data) + "]"

    raise ValueError()


def isInt(d):
    try:
        int(d)
        return True
    except ValueError:
        return False


def isFloat(d):
    try:
        float(d)
        return True
    except ValueError:
        return False


def isBool(d):
    return d in ["true", "false"]


def splitOnComma(d):
    l = 0
    object_level = 0
    array_level = 0

    for i, ch in enumerate(d):
        if ch == "{":
            object_level += 1
        elif ch == "}":
            object_level -= 1
        elif ch == "[":
            array_level += 1
        elif ch == "]":
            array_level -= 1

        if ch == "," and object_level == 0 and array_level == 0:
            yield d[l: i]
            l = i + 1

    yield d[l:]


def dumps(data):
    data = data.strip()
    # if it is a dict
    if data.startswith("{"):
        if not data.endswith("}"):
            raise ValueError("dict is malformed")
        result = dict()
        for pair in splitOnComma(data[1:-1]):
            pair = pair.strip()
            key, value = pair.split(":", 1)
            key = key.strip()
            if not key.startswith('"') or not key.endswith('"'):
                raise ValueError()
            if '"' in key[1:-1] or ":" in key:
                raise ValueError()
            result[key[1:-1]] = dumps(value)

    elif data.startswith("["):
        if not data.endswith("]"):
            raise ValueError("array is malformed")
        result = []
        for element in splitOnComma(data[1:-1]):
            result.append(dumps(element))

    elif data.startswith('"'):
        if not data.endswith('"'):
            raise ValueError("string is malformed")
        result = data[1:-1]

    elif isInt(data):
        result = int(data)

    elif isFloat(data):
        result = float(data)

    elif isBool(data):
        result = True if data == "true" else False

    else:
        raise ValueError()

    return result


if __name__ == '__main__':
    data = {"a": ['abc', 'cde'], "b": True, "c": 36.1}
    data2 = '{"a":[[[[ "abc",     {"b":{"c": "cde"}  }]]]], "b": true, "c": 36.1}'

    print("my implementation:", loads(data))
    print(dumps(data2))
