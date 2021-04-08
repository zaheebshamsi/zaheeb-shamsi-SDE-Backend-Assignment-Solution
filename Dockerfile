FROM python
MAINTAINER zaheeb.shamsi120815@gmail.com

# Base settings
RUN mkdir -p /flask_api && echo "export PATH=$PATH:/home/itom" > /etc/profile

COPY  ./flask_deploy/* /flask_deploy/

# Image specific pip modules and pyinstaller
RUN pip install -r /python/req.txt
RUN apt-get update --assume-yes && apt-get install sudo python3-dev apt-utils upx --assume-yes

RUN addgroup --gid 1999 --system itom && adduser --home /home/itom --disabled-password itom --uid 1999 --gid 1999  --gecos 'itom,,,,' && echo "itom ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/itom && chmod 0440 /etc/sudoers.d/itom && chown -R itom:itom /flask_deploy

RUN chown -R itom:itom /flask_deploy
RUN rm -rf /python/*.py

USER itom
WORKDIR /

# Volumes
VOLUME  /flask_deploy

ENTRYPOINT ["/bin/sh"]
CMD ["python aws_lambda_requests.py"]
