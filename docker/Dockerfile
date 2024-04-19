FROM python:3.12

WORKDIR /code

ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
RUN /install.sh && rm /install.sh

COPY requirements/requirements.txt /code/requirements.txt

RUN /root/.cargo/bin/uv pip install --system --no-cache -r /code/requirements.txt

COPY app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]