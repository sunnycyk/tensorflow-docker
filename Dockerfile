FROM python:3.6

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 6006
VOLUME ["/usr/src/app/"]

CMD ["bash"]