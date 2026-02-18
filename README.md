# 🚀 End-to-End Test Automation Framework

A production-grade End-to-End (E2E) Test Automation Framework built using modern automation best practices.

This framework validates complete application workflows across:

- ✅ UI Layer (Playwright)
- ✅ API Layer (Requests)
- ✅ Database Layer (PostgreSQL)
- ✅ CI/CD Integration (GitHub Actions)
- ✅ HTML Reporting
- ✅ Logging & Failure Screenshots

---

## 📌 Tech Stack

- Python 3.10+
- Playwright – UI Automation
- PyTest – Test Runner
- Requests – API Testing
- PostgreSQL (psycopg2) – Database Validation
- pytest-html – HTML Reports
- GitHub Actions – CI/CD

---

## 📁 Project Structure
```
e2e-automation-framework/
│
├── pages/                  # Page Object Model (POM)
│   ├── base_page.py
│   ├── login_page.py
│   └── dashboard_page.py
│
├── tests/                  # UI, API, DB test cases
│   ├── test_login_ui.py
│   ├── test_api_validation.py
│   └── test_db_validation.py
│
├── utils/                  # Reusable utilities
│   ├── api_client.py
│   ├── db_client.py
│   ├── config.py
│   └── logger.py
│
├── reports/
│   ├── html/
│   │   └── report.html
│   └── logs/
│       └── execution.log
│
├── conftest.py             # PyTest fixtures & hooks
├── requirements.txt
└── .github/workflows/ci.yml

```

## ⚙️ Setup Instructions
## 1️⃣ Clone the Repository
```
git clone https://github.com/aadiiiitii001/End-to-End-Test-Automation-Framework.git
cd End-to-End-Test-Automation-Framework
```
## 2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

## 3️⃣ Install Dependencies
pip install -r requirements.txt
playwright install

## ▶️ Running Tests
Run All Tests
pytest

## Run with HTML Report
```
pytest tests/ \
--html=reports/html/report.html \
--self-contained-html

After execution, open:

reports/html/report.html

in your browser.
```
## 📊 Reporting & Logging
✔ HTML Report
- Generated using pytest-html
- Saved under reports/html/

✔ Execution Logs
- Saved under reports/logs/execution.log
- captures test lifecycle events

✔ Screenshots (on failure)
- Automatically captured for failed UI tests
- Stored under reports/screenshots/

## 🔐 Environment Configuration
Sensitive configuration is managed via environment variables.
Example .env file:
```
BASE_URL=https://example.com
API_BASE_URL=https://jsonplaceholder.typicode.com
DB_NAME=testdb
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
```
Never commit .env to version control.

## 🔄 CI/CD Integration

Tests automatically run on:
- Push
- Pull Request

Configured using GitHub Actions:
```
.github/workflows/ci.yml
```

Reports are uploaded as CI artifacts for review.

## 🧠 Key Design Principles
- Page Object Model (POM)
- Modular utility-based architecture
- Separation of concerns
- Centralized configuration
- Clean folder hierarchy
- CI-compatible headless execution
- Scalable for parallel execution

## 📈 Future Enhancements
- Parallel execution using pytest-xdist
- Allure reporting integration
- Dockerized execution
- Slack notifications on failure
- Advanced logging with structured format
- Retry mechanism for flaky tests
