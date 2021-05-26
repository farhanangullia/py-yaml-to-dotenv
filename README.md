# YAML to dotenv parser

This script parses a YAML file that contains key-value mappings and generates a [dotenv](https://www.npmjs.com/package/dotenv) file to export as environment variables from keys provided. The mappings file can contain nested structures however the keys provided must result in a flat list of key-value pairs.

## Prequisites

* Python 3.x
* Py packages specified in `requirements.txt`

## Setup

```bash
$ pip install -r requirements.txt
```

## Usage

```bash
$ python parse_mappings.py --keys KEYS [KEYS ...] path
```

<img src="docs/help.gif" width="500" height="300">

### Example

Suppose you want to export the key values to dotenv for different environments. Notice how in example/sample_mappings.yaml, the testing environment has child environments which will require another level of key-values.

<img src="docs/sample_mappings.svg" width="200" height="400">

#### staging

<img src="docs/example_stg.gif" width="500" height="300">

`$ python parse_mappings.py example/mappings.yaml --keys staging`

#### chaos

<img src="docs/example_chaos.gif" width="500" height="300">

`$ python parse_mappings.py example/mappings.yaml --keys testing chaos`

