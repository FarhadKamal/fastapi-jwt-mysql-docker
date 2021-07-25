FROM python:3.7
COPY ./app /app
RUN pip3 install fastapi uvicorn pymysql sqlalchemy pydantic PyJWT passlib bcrypt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "15400"]