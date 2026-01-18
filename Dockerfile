# --- Stage 1: Builder ---
FROM python:3.11-slim as builder

WORKDIR /app

# Only install what is necessary to build wheels
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
# Install to a local folder to make copying easy
RUN pip install --no-cache-dir --user -r requirements.txt

# --- Stage 2: Final Runtime ---
FROM python:3.11-slim

WORKDIR /app

# Copy only the installed python packages from the builder
COPY --from=builder /root/.local /root/.local
COPY . .

# Update PATH to include the local user bin where streamlit lives
ENV PATH=/root/.local/bin:$PATH

EXPOSE 8501

# Run with lean settings
ENTRYPOINT ["streamlit", "run", "notebooks/streamlit_playground.py", "--server.port=8501", "--server.address=0.0.0.0", "--browser.gatherUsageStats=false"]
