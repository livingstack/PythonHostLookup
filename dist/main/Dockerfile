FROM ubuntu:22.04
MAINTAINER livingstack@gmail.com
WORKDIR /bin/
copy * ./
copy main ./
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

EXPOSE 8080
ENTRYPOINT ["main"]
