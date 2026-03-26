# Bridgewell

BridgeWell is a mental health employer support tool that combines **PostgreSQL**, **Neo4j**, **FastAPI**, and **Streamlit** to analyze country-level mental health data and recommend wellbeing programs for employers.

The project uses:
- **PostgreSQL** for structured survey and health-related data
- **Neo4j** for graph-based relationships between countries, needs, and wellbeing programs
- **FastAPI** as the backend API layer
- **Streamlit** as the frontend user interface

---

## Features

- Country-level mental health analysis
- Employer support gap summaries
- Lifestyle risk summaries
- Treatment gap summaries
- Graph-based wellbeing program recommendations
- Company registration with tailored recommendations
- Interactive Streamlit dashboard

---

## Project Structure

```text
BridgeWell/
│── db.py
│── main.py
│── Ui.py
│── load_graph.py
│── load_data.py
│── schemas.sql
│── mental_health.csv
│── test_neo4j.py
│── .env
