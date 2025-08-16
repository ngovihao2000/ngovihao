# Dùng Python base image nhẹ
FROM python:3.9-slim

# Set thư mục làm việc trong container
WORKDIR /app

# Copy file requirements trước để tận dụng cache
COPY requirements.txt .

# Cài dependencies
RUN pip install -r requirements.txt

# Copy toàn bộ source code vào container
COPY . .

# Expose port 5000
EXPOSE 5000

# Chạy ứng dụng Flask
CMD ["python", "app.py"]
