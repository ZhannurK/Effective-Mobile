FROM python:3.11-slim AS builder

WORKDIR /app

COPY app.py .

FROM python:3.11-slim

WORKDIR /app

RUN useradd -m -u 1000 appuser && chown appuser:appuser /app

COPY --from=builder --chown=appuser:appuser /app/app.py .

USER appuser

EXPOSE 8080

CMD ["python", "app.py"]
