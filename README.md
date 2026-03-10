# Supply Chain Analytics - Single Source of Truth

This repository contains a Python-based data pipeline designed to manage and analyze supply chain operations. The project bridges the gap between raw database storage (PostgreSQL) and actionable business intelligence, focusing on vendor reliability and inventory movement.

## 🚀 Project Overview
The system is divided into two main phases:
1.  **Database Initialization:** Setting up the relational schema and injecting initial datasets.
2.  **Analytics & Visualization:** Querying the "Single Source of Truth" to generate performance reports and interactive charts.



---

## 🛠️ Tech Stack
* **Database:** PostgreSQL
* **ORM/Driver:** SQLAlchemy, Psycopg2
* **Data Manipulation:** Pandas, NumPy
* **Environment Management:** Python-Dotenv
* **Visualization:** Plotly Express

---

## 📊 Database Schema
The project initializes a relational database with four interconnected tables to maintain data integrity:

| Table | Key Columns | Purpose |
| :--- | :--- | :--- |
| **suppliers** | `supplier_id`, `supplier_name` | Profiles of global parts providers. |
| **parts** | `part_id`, `part_name`, `category` | Product catalog and unit costing. |
| **purchase_orders** | `po_id`, `expected_arrival`, `actual_arrival` | Tracks inbound logistics and delays. |
| **customer_deliveries** | `delivery_id`, `customer_name`, `status` | Tracks outbound sales and fulfillment. |



---

## 📈 Key Analytics Features

### 1. Vendor Delay Analysis
The system identifies inefficiencies in the supply chain by calculating the delta between expected and actual arrival dates.
* **KPIs:** Total delays per supplier, average delay days, and maximum delay recorded.
* **Visuals:** Bar charts with automated average-delay trend lines.

### 2. Inventory & Sales Trends
Automated reporting on "Top Selling Items" filtered by timeframes (All-time vs. Last 30 days).
* **Segmentation:** Data is grouped by part category (Electronics, Mechanical, Structure).
* **Visuals:** Color-coded bar charts showing volume by category.

---

## ⚙️ Installation & Setup

### 1. Environment Configuration
Create a `.env` file in the root directory and add your PostgreSQL credentials:
```env
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=your_host
DB_PORT=5432
DB_NAME=postgres
```

### 2. Initialize the Database
Run the initialization script to create tables and inject mock data:
**This script handles:**
1. Connection via SQLAlchemy engine
2. Table creation (CREATE TABLE IF NOT EXISTS)
3. Data injection using df.to_sql()

### 3. Run Analytics
Execute the analytics module to generate insights:
**This script handles:**
1. SQL Querying (JOINs for optimized data retrieval)
2. Delay calculation logic
3. Plotly figure rendering
