## Getting Started

This script is used to convert csv file with specified format into .arb files.

### Columns of csv file

| category      | text          | description         | en                | zh              | spain                |
| ------------- | ------------- | ------------------  | ---------------   | -------------   | -------------------  |
| button_       | ok            |                     | OK                | OK              | Okay                 |
| text_         | welcome       | welcome someone     | Hi! {name}        | Hello! {name}   | Hola! {name}         |
| text_         | balance       | someone's balance   | {name} has ${int} | {name}有{int}蚊  | {name} tiene ${int}  |

An output of en.arb files is as below
```yaml
{
    "button_ok", "OK",
    "text_welcome": "Hi! {name}",
    "@text_welcome": {
        "description": "welcome someone"
        "placeholders": {
            "name": { "type": "String" }
        }
    },
    "text_balance": "{name} has ${int}"
    "@text_visit": {
        "description": "someone's balance"
        "placeholders": {
            "name": { "type": "String" },
            "int": { "type": "int" },
        }
    }
}
```

### placeholder type

Default parameter type is string
If the parameter contains some keyword, the type will be changed.
| key           | type          | example        |
| ------------- | ------------- | -------------- |
| int           | int           | {int123}       |
| double        | double        | {doubleValue}  |
| number        | number        | {number}       |

### Usage
```
python3 generateArb.py {your_csv_file}
```