FROM python
LABEL maintainer="Mohamed Hussein"
ENV PYTHONUNBEFFERED 1
COPY ./packages.txt ./packages.txt
RUN pip install -r ./packages.txt
RUN mkdir /app
WORKDIR /app
COPY ./app ./app
RUN useradd -s /bin/bash user
USER user