FROM python:3.13-slim

WORKDIR /todoapp

RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--forwarded-allow-ips", "*", "--proxy-headers"]
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
#https://fastapi.tiangolo.com/advanced/settings/#settings-and-testing
#https://www.hostinger.com/tutorials/docker-cheat-sheet?utm_campaign=Generic-Tutorials-DSA-t1|NT:Se|Lang:EN|LO:MX&utm_medium=ppc&gad_source=1&gad_campaignid=20980195875&gbraid=0AAAAADMy-hYvjYdB_hWE6JWq2zkBogMFm&gclid=EAIaIQobChMI0duthq-QkQMVfyhECB1JThBoEAAYASAAEgJ2GPD_BwE