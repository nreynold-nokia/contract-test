# contract-test

## Generate Schema
1. In project root
2. `python dump_openapi.py`

## Generate Types
1. In the `fe` directory
2. `npm run generate-types`

## TODO
* Fire up swagger editor > make changes > see openapi diffed between swagger editor and fastapi-generated code > change fastapi code > see diff again > also see diff with TS gen
* Github Actions to check schema and types
* Helper script to check schemas locally
* Example actually using types - export the schemas we need
