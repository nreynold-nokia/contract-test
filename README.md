# contract-test

## Prerequisites
* Python
* pip
* node + npm

1. `pip install fastapi`
2. `pip install "uvicorn[standard]"`
3. `cd fe && npm install`

## Start
1. Start FastAPI `uvicorn main:app --reload`
2. Docs: http://127.0.0.1:8000/docs
3. Start front-end `cd fe` and `npm run dev`  
4. Frontend: http://localhost:5173/ 

## Generate OpenAPI Schema
1. In project root
2. `python dump_openapi.py`

## Generate Types
1. In the `fe` directory
2. `npm run generate-types`

## TODO
* Helper script to check schemas locally
* Clean up github actions 
