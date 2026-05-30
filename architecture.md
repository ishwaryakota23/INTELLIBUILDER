# IntelliBuilder Architecture Document

## Overview

IntelliBuilder is an AI-powered application generation platform that converts natural language prompts into structured application configurations and interactive web applications.

The system follows a compiler-inspired architecture where user prompts pass through multiple processing stages before a fully functional application is generated.

---

# Technology Stack

## Frontend

* HTML
* CSS
* JavaScript

## Backend

* Python
* Flask
* Flask-CORS

## AI Layer

* Groq API
* Llama 3.3 Model

---

# System Architecture

User Prompt
↓
Intent Extraction
↓
Module Discovery
↓
Schema Generation
↓
Validation Engine
↓
Repair Engine
↓
Runtime Generation
↓
Interactive Application

---

# Compiler Pipeline

## Stage 1: Intent Extraction

Purpose:

Identify the business domain from the user prompt.

Example:

Prompt:

"Build a Hospital Management System"

Output:

Domain = Hospital

---

## Stage 2: Module Discovery

Purpose:

Identify required modules for the detected domain.

Example:

Hospital Domain:

* Patients
* Doctors
* Appointments
* Billing
* Pharmacy

---

## Stage 3: Schema Generation

Purpose:

Generate a structured JSON configuration.

Generated Artifacts:

* Navigation
* Pages
* Roles
* Permissions
* Business Rules
* Database Tables
* API Endpoints

---

## Stage 4: Validation Engine

Purpose:

Verify generated configurations before rendering.

Validation Checks:

* Missing Pages
* Missing Roles
* Missing APIs
* Missing Database Tables
* Invalid Structures

Benefits:

* Prevents runtime failures
* Improves output reliability

---

## Stage 5: Repair Engine

Purpose:

Automatically recover from configuration issues.

Example Repairs:

* Missing Permissions
* Missing Roles
* Missing Business Rules
* Missing APIs
* Invalid Page Types

Benefits:

* Fault Tolerance
* Self-Healing Configuration Generation

---

## Stage 6: Runtime Generation

Purpose:

Convert validated configuration into a working application.

Generated Components:

* Dashboard
* Forms
* Tables
* Cards
* Sidebar Navigation

---

# JSON Contract

Each generated application follows a structured contract.

Fields:

* domain
* app_name
* navigation
* pages
* roles
* permissions
* business_rules
* database_tables
* api_endpoints

This contract ensures predictable and consistent generation.

---

# Domain Generalization

The system supports multiple business domains.

Validated Domains:

* Hospital Management
* Banking Management
* HR Management
* University Management
* Food Delivery
* Inventory Management
* CRM Systems

The same pipeline dynamically adapts to each domain.

---

# Reliability Features

## Validation Layer

Detects invalid or incomplete configurations.

## Repair Layer

Automatically repairs configuration issues.

## Compiler Logs

Provides visibility into each pipeline stage.

## Generated JSON Viewer

Displays the final generated configuration for transparency.

---

# User Interface

The frontend provides:

* Landing Page
* Prompt Input Interface
* Compiler Pipeline Visualization
* Compiler Logs
* Generated Application Preview
* JSON Viewer
* Roles Viewer
* Permissions Viewer
* Business Rules Viewer
* Database Schema Viewer
* API Endpoint Viewer

---

# Design Decisions

### Why Groq?

* Fast inference speed
* Low latency
* Suitable for real-time generation

### Why JSON-Based Generation?

* Structured output
* Easy validation
* Easy rendering

### Why Compiler Architecture?

* Clear separation of responsibilities
* Better reliability
* Easier debugging
* Scalable pipeline design

---

# Conclusion

IntelliBuilder demonstrates an AI-driven compiler architecture capable of converting natural language requirements into structured application configurations and interactive web applications with built-in validation, repair, and runtime generation capabilities.
