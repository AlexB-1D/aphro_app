#!/bin/bash
export MONGODB_URI="mongodb+srv://<user>:<pass>@cluster.mongodb.net/dbname"
exec gunicorn main:app \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8000 \
    --workers 4
