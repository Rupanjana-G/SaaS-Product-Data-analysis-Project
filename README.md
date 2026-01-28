
📊 Pricing Strategy & Retention Analysis for a B2B SaaS Product
🧠 Project Overview

This project analyzes user behavior, retention, churn, and pricing strategy for a B2B SaaS product using real-world–style usage data.
The goal is to understand how different subscription plans and usage patterns impact customer retention and revenue, and to derive data-driven pricing insights.

Python is used for data cleaning and feature engineering, while Power BI is used to build an interactive dashboard for business storytelling.

🎯 Objectives

Clean and prepare raw SaaS usage and retention data

Analyze user engagement and churn behavior

Simulate subscription plans and pricing tiers

Study the relationship between usage, plan type, and retention

Visualize insights through an interactive Power BI dashboard

🗂 Dataset

Source: GoMask.ai – B2B SaaS Usage Retention Dataset

Type: Synthetic dataset (privacy-safe)

Description:
The dataset contains user-level usage and retention information for a B2B SaaS product.

 Note: The original dataset does not include pricing or plan tiers. These were simulated realistically during feature engineering to enable pricing analysis.

⚙️ Tools & Technologies
Python

pandas

numpy

📊 Visualization

Power BI

🧰 Development Environment

PyCharm

Python virtual environment

🧭 Project Workflow
1️⃣ Data Import & Cleaning

Loaded raw dataset into Python

Standardized column names

Removed duplicates

Handled missing values

Converted date and numeric fields

Exported cleaned data for further analysis

2️⃣ Feature Engineering

Created subscription plans:

Basic

Pro

Enterprise

Assigned monthly prices to each plan

Simulated:

Effective monthly revenue

Upgrade and downgrade behavior

Derived additional metrics such as:

User tenure

Usage intensity

Revenue per user

3️⃣ Retention & Pricing Analysis

Compared churn rates across subscription plans

Analyzed usage patterns for retained vs churned users

Evaluated revenue distribution across plan tiers

Identified high-risk churn segments

Assessed pricing sustainability based on retention behavior

4️⃣ Power BI Dashboard

An interactive Power BI dashboard was created to present insights, including:

Churn rate by subscription plan

Usage patterns across plans

Revenue and ARPU overview

Plan distribution and retention trends

Filters by plan type and user segment
