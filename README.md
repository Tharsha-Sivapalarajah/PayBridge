# PayBridge  
## ERP to Bank Payment Integration System

PayBridge is a Python-based integration service that automates payment processing between an ERP system and banking interfaces using REST APIs and file-based integration.

This project demonstrates enterprise-grade integration patterns including:

- Retry mechanisms for external systems
- Idempotent processing
- Business rule validation
- Atomic file generation
- SQLite-backed persistence
- Structured logging
- Unit testing with pytest

This project demonstrates practical integration engineering patterns commonly used in ERP-to-bank and fintech systems. It focuses on reliability, traceability, and production-grade design rather than simple API scripting.

---

# Overview

In many enterprise environments, ERP systems generate approved payment instructions that must be transmitted to banking systems in a strict file format.

These integrations must be:

- Reliable
- Safe to re-run
- Auditable
- Resilient to failures
- Protected against duplicate processing

PayBridge simulates such a real-world integration service.

---

# Architecture

```
ERP REST API (Flask)
        ↓
PayBridge Integration Engine
    ├── ERP Client (Retry + Timeout)
    ├── Validation Layer
    ├── Transformation Layer
    ├── Persistence Layer (SQLite)
    ├── Atomic File Writer
    └── Logging
        ↓
Bank Payment File (CSV)
```

---

# Features

## REST API Integration
Fetches approved payments from a mock ERP REST API built using Flask.

## Retry Mechanism
Retries ERP requests up to a configurable number of attempts with delay and timeout handling.

## Business Rule Validation
Validates:
- Amount must be greater than zero
- Currency must be supported
- Status must be APPROVED
- Bank account must not be empty

## Idempotent Processing
Processed payments are tracked in SQLite to prevent duplicate file generation on re-runs.

## Atomic File Writing
Payment files are written to a temporary file and renamed only after successful write to prevent corrupted or partial files.

## Structured Logging
All execution steps are logged with timestamps and severity levels.

## Unit Testing
Core logic (validation and transformation) is tested using pytest.

---

# Project Structure

```
paybridge/
│
├── app/
│   ├── config.py
│   ├── orchestrator.py
│   ├── logging_config.py
│   │
│   ├── erp/
│   │   └── client.py
│   │
│   ├── validation/
│   │   └── validator.py
│   │
│   ├── transformation/
│   │   └── transformer.py
│   │
│   ├── persistence/
│   │   └── repository.py
│   │
│   └── file_handling/
│       └── file_writer.py
│
├── erp_api/
│   └── app.py
│
├── tests/
│   ├── test_validator.py
│   └── test_transformer.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# How It Works

1. The integration job starts from `main.py`.
2. Logging is initialized.
3. The SQLite database is initialized.
4. The ERP client fetches approved payments.
5. If the ERP call fails, retry logic is triggered.
6. Each payment is:
   - Checked for duplicates
   - Validated against business rules
   - Transformed into bank-compatible format
7. Valid payments are written atomically to a CSV file.
8. Processed payment IDs are stored in SQLite.
9. The integration job completes.

---

# Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/paybridge.git
cd paybridge
```

## 2. Create Virtual Environment

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux
```bash
python -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

## 1. Start Mock ERP API

```bash
python erp_api/app.py
```

API runs at:
```
http://localhost:5000/payments?status=APPROVED
```

## 2. Run Integration Service

Open a new terminal (activate venv again if needed):

```bash
python main.py
```

---

# Running Unit Tests

```bash
pytest
```

Expected output:

```
================= 4 passed =================
```

---

# Example Output

Generated file:

```
BANK_PAYMENTS_20260212_104530.csv
```

Console logs:

```
INFO | Starting PayBridge integration job
INFO | Successfully fetched payments from ERP
WARNING | Validation failed for PAY-1002
INFO | File generated successfully
INFO | Integration job completed
```

---

# Failure Simulation

You can simulate real-world scenarios:

- Stop ERP server → triggers retry mechanism
- Add sleep in ERP endpoint → triggers timeout retry
- Re-run integration → duplicates are skipped
- Force file write error → atomic write prevents partial file

---

# Configuration

Configuration values are defined in:

```
app/config.py
```

Configurable values:

- ERP_BASE_URL
- MAX_RETRIES
- RETRY_DELAY
- DATABASE_NAME
- ALLOWED_CURRENCIES

Environment variables can override defaults.

---

