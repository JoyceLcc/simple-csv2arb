## Getting Started

This script is used to convert csv file with specified format into .arb files.

### Columns of csv file

| category      | text          | description         | en                     | zh                   | spain                     |
| ------------- | ------------- | ------------------  | ---------------------- | -------------------- | ------------------------- |
| button_       | ok            |                     | OK                     | OK                   | Okay                      |
| text_         | welcome       | welcome someone     | Hi! {name}             | Hello! {name}        | Hola! {name}              |
| text_         | balance       | someone's balance   | {name} has ${int_1234} | {name}有{int_1234}蚊  | {name} tiene ${int_1234}  |

An output of en.arb files is as below
```
{
    "button_ok", "OK",
    "text_welcome": "Hi! {name}",
    "@text_welcome": {
        "description": "welcome someone"
        "placeholders": {
            "name": { "type": "String" }
        }
    },
    "text_balance": "{name} has ${int_1234}"
    "@text_visit": {
        "description": "someone's balance"
        "placeholders": {
            "name": { "type": "String" },
            "int_1234": { "type": "int" },
        }
    }
}
```

### Placeholder type

Default parameter type is string.

If the parameter contains a keyword as below, the type will be changed.
| keyword        | type          | example         |
| -------------- | ------------- | --------------- |
| int_           | int           | {int_123}       |
| double_        | double        | {double_value}  |
| number_        | number        | {number_}       |

### Usage
```
python3 generateArb.py {your_csv_file}
```