import json

j = """{
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": 50
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}
"""


def to_swagger(data, level, spaces="  "):
    for k, v in data.items():
        if isinstance(v, str):
            print(level * spaces + f"{k}:")
            print((level + 1) * spaces + "type: string")
            print((level + 1) * spaces + f"example: {v}")

        elif isinstance(v, dict):
            print(level * spaces + f"{k}:")
            print((level + 1) * spaces + "types: object")
            print((level + 1) * spaces + "properties:")
            to_swagger(v, level + 2, spaces=spaces)

        elif isinstance(v, int):
            print(level * spaces + f"{k}:")
            print((level + 1) * spaces + "type: integer")

        elif isinstance(v, float):
            print(level * spaces + f"{k}:")
            print((level + 1) * spaces + "type: number")

        else:
            raise ValueError


data = json.loads(j)
to_swagger(data, 0, spaces="  ")
