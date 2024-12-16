FROM python:3.9-slim

# Install a shell (optional utilities)
RUN apt-get update && apt-get install -y bash
# Install curl and other required utilities
RUN apt-get update && apt-get install -y curl

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]