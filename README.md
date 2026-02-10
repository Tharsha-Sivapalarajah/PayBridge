# PayBridge
## ERP to Bank Payment File Integration System

PayBridge is a Python-based integration service that automates payment processing between an ERP system and banking interfaces using file-based integration.

## Problem Statement
Many organizations still rely on manual processes to transfer approved payment data from ERP systems to banks. These processes are error-prone, difficult to audit, and lack reliability.

PayBridge demonstrates a real-world integration solution that validates, transforms, and delivers payment data in bank-compatible formats with full traceability.

## Architecture Overview

ERP API (REST)
    ↓
PayBridge Integration Service
    - Validation
    - Transformation
    - File Generation
    - Retry Handling
    - Audit Logging
    ↓
Bank Payment Files (CSV)

## Features
- REST API integration with ERP system
- Business rule validation
- JSON to bank CSV transformation
- Idempotent payment processing
- Retry handling for failures
- Audit logs and traceability
- SQLite-backed persistence

## Tech Stack
- Python
- Flask
- SQLite
- REST APIs
- JSON

## Running the Project

1. Install dependencies
```bash
pip install -r requirements.txt

