#!/bin/bash
docker build . -t disposable-message-admin-bot:latest
docker run -it -p5000:5000 --cap-add=SYS_ADMIN disposable-message-admin-bot:latest
