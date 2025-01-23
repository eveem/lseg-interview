FROM public.ecr.aws/lambda/python:3.13

WORKDIR /app 
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app/app.py"]