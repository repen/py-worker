#docker build -t build_name:latest .
#docker run --name container_name -d build_name:latest
#docker run --name container_name -d -p 8120:5000 build_name:latest
#docker run --name container_name -d -v volume:/volume -p 8120:5000 build_name:latest
FROM python:3.8

ENV DIR_SCRIPT /home/pyuser/script
RUN useradd -ms /bin/bash pyuser && mkdir ${DIR_SCRIPT}
RUN mkdir /volume
RUN chown -R pyuser:pyuser /volume
USER pyuser

ENV APP_DIR ${DIR_SCRIPT}

WORKDIR ${BASE_DIR}

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY script ${DIR_SCRIPT}

CMD python main.py