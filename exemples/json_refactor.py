i_dict = {
    "srv1": {
        "cpu": "70%",
        "owner": "max"
    },
    "srv2": {
        "cpu": "30%",
        "owner": "dima"
    },
    "srv3": {
        "cpu": "50%",
        "owner": "max"
    },
}

outp = {
    "max": [
        {"srv1": {
            "cpu": "70%"}
        },
        {"srv3": {
            "cpu": "50%"}
        }
    ],
    "dima": [
        {"srv2": {
            "cpu": "30%"}
        }
    ]
}


def func(inp: dict):
    output = {}
    owners = {}
    for srv, value in inp.items():
        owners = value["owner"]
        if owners not in output:
            output[owners] = []
        output[owners].append({srv: value["cpu"]})
    print(output)

func(i_dict)
