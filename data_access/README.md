# data access service

## Description
service that listen on a folder of recorded data by CITROS cli (runs folder)
and create a "hot reload" API that can be consumed by other services

## The motivation
when recording a lot of multiple bags (mcap or other) there is a huge problems:
- maintaining the data - a log of bags without any metadata.
- accessing the bags for data analysis as the data is not indexed and can be access only sequentially and not to a sertain index.
As DB is much more expensive and we do not want to hold the DB active all the time so this service is creating a "cache" layer that is listening in a recordings folder and it will loads the data apon request of the user. 

after a user requesting a sertain data to be loaded, afetr it loads to the **PGDB** the user can access it and query all the data for analysis. 


# Input

- input folder
- create PG or connect to existing one
- port to listen on for the **API**



# API

## REST API
The user can check the availability of the data in a rest api that will be created by the service.

### check the availability of the data
GET http://{domain}:{port}/{batch run name}
```json
{
    "status": "unloaded",
    "last access": "2020-01-01 00:00:00",
    ...
}
```
### request access for batch run
POST http://{domain}:{port}/{batch run name}
```json
{
    "status": "loading",
    "last access": "2020-01-01 00:00:00",
    ...
}
```

# run
uvicorn app.main:app
