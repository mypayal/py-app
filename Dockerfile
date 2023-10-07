FROM python:3
WORKDIR /app
COPY app/ /app/
RUN pip install -r /app/requirements.txt
RUN apt-get update && apt-get install -y nginx
RUN rm /etc/nginx/sites-enabled/default
RUN service nginx start
COPY nginx/nginx.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled/
EXPOSE 80
CMD ["python", "app.py"]
