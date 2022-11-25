import json

INPUT_FILE = "input.csv"


# TODO реализовать конвертер из csv в json
def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
    dicts = []
    with open(filename) as f:
        file = "".join(f.readlines())
        lines = [line.strip().split(delimiter) for line in file.split(new_line)]
        headers = lines[0]
        data = lines[1:]

    for line in data:
        dicts.append({x[0]: x[1] for x in zip(headers, line)})

    return dicts


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
