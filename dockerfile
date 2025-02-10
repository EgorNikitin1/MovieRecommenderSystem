FROM python:3.13

COPY requirements.txt /workdir/
COPY app/ /workdir/app/
COPY ml/ /workdir/ml/
COPY templates/ /workdir/templates/
COPY data/ /workdir/data/

WORKDIR /workdir

RUN pip install -r requirements.txt

# Run the application
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]