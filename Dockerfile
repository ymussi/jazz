FROM python:3.7-stretch
LABEL mantainer="sre-team@madeiramadeira.com.br"
LABEL fileversion=v0.1

WORKDIR /app/jazz

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

COPY . .

RUN pip install -r requirements.txt && \
    python setup.py develop

RUN wget -O /bin/wait-for-it https://github.com/vishnubob/wait-for-it/raw/54d1f0bfeb6557adf8a3204455389d0901652242/wait-for-it.sh; \
    chmod +x /bin/wait-for-it

ENTRYPOINT ["/bin/sh","/app/jazz/entrypoint.sh"]