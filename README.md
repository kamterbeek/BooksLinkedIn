Automatically convert your reading history into polished LinkedIn posts using AI.

Read2Linked is an end-to-end data engineering project that extracts reading data, transforms it into engaging professional content, stores reading history in PostgreSQL, and automates publishing to LinkedIn.

---

## Features

- Import Goodreads reading history
- Detect newly finished books
- Store reading history in PostgreSQL
- Generate AI-powered summaries
- Create professional LinkedIn posts
- Browser automation using Playwright
- Scheduled ETL with GitHub Actions
- Docker support

---

## Architecture

Goodreads
        │
        ▼
Python ETL
        │
        ▼
PostgreSQL
        │
        ▼
OpenAI
        │
        ▼
Playwright
        │
        ▼
LinkedIn

---

## Tech Stack
