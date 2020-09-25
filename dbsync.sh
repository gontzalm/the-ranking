#!/bin/bash

source .env
LOCALDBURI=$DBURL
echo "WARNING!!! REMOTE DATA WILL BE DESTROYED"
echo "Copy from $LOCALDBURI"
echo "Paste your MongoDBAtlas URI:"
read REMOTEDBURI
echo "Sync data from $LOCALDBURI to $REMOTEDBURI"

mongodump --uri $LOCALDBURI
mongorestore --uri $REMOTEDBURI --drop