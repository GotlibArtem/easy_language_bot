# ������� �����
FROM python:3.10

# ������������� ������� ����������
WORKDIR /app

# ��������� pip
RUN pip install --upgrade pip

# �������� ����� � ������������� �����������
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# �������� ������ � ���������
COPY . /app/

# ��������� ������
CMD ["sh", "-c", "python language_bot_api/manage.py migrate && python language_bot_api/manage.py runserver 0.0.0.0:8000"]
