
---

# 🛒 RetailSense – Product Support & Warranty Assistance Chatbot

**Mini Project | Deployed & Live**

🔗 **Live Demo:** [https://retailsense-support-assistance.onrender.com/](https://retailsense-support-assistance.onrender.com/)

---

## 📌 Project Overview

**RetailSense** is a **hybrid AI-powered product support chatbot** designed to assist customers with **warranty, replacement, and product issue queries** using natural language input and optional product image analysis.

The system is built from a **product manager’s perspective**, focusing on reliability, safety, and real-world customer support workflows rather than pure automation. It acts as a **decision-assist system**, not a decision-maker.

This project is deployed as a **full-stack FastAPI application** with a lightweight HTML interface, making it easy to demo, test, and extend.

---

## 🎯 Problem Statement

Customer support teams frequently handle repetitive queries such as:

* “Is this issue covered under warranty?”
* “Can I get a replacement for this damage?”
* “Is physical damage included in warranty?”

Manually resolving these queries is time-consuming and error-prone.

**RetailSense** addresses this problem by:

* Interpreting customer issues via text
* Optionally analyzing uploaded product images
* Reasoning over warranty policies
* Providing clear, safe, and explainable responses

---

## ✨ Key Features

* 🧠 **Hybrid AI Design**

  * Rule-based warranty & policy reasoning (deterministic)
  * AI-powered natural language explanations (OpenAI)
  * Graceful fallback when AI services are unavailable

* 📝 **Text-Based Support Queries**

  * Warranty eligibility questions
  * Replacement guidance
  * Product issue explanations

* 🖼️ **Optional Image Analysis**

  * Basic defect classification (e.g., physical damage vs manufacturing defect)
  * Image input enhances confidence, never overrides policy logic

* 🔒 **Product-Safe Responses**

  * No automatic approvals
  * Clear disclaimers
  * Manual verification always required

* 🌐 **Simple Web Interface**

  * Single-page HTML UI
  * Text input + image upload
  * Clean display of results

---

## 🧠 System Architecture

```
User (Browser)
   ↓
HTML UI (Static)
   ↓
FastAPI Backend
   ↓
Text + Image Analysis
   ↓
Warranty Policy Engine
   ↓
AI Explanation (Optional)
   ↓
Final Support Response
```

---

## 🛠️ Tech Stack

### Backend

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python\&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi\&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI_Server-333333?logo=gunicorn\&logoColor=white)

* Python
* FastAPI
* Uvicorn

---

### AI & Logic

![OpenAI](https://img.shields.io/badge/OpenAI-LLM-412991?logo=openai\&logoColor=white)
![AI](https://img.shields.io/badge/AI-Hybrid_Reasoning-orange)
![Rules](https://img.shields.io/badge/Rule--Based-Policy_Engine-blue)

* OpenAI API (LLM-based explanation layer)
* Rule-based warranty & policy engine
* Fallback logic for reliability

---

### Image Handling

![Pillow](https://img.shields.io/badge/Pillow-Image_Processing-4CAF50?logo=python\&logoColor=white)
![Computer Vision](https://img.shields.io/badge/Computer_Vision-Basic-blueviolet)

* Pillow
* Basic image classification logic

---

### Frontend

![HTML](https://img.shields.io/badge/HTML5-Markup-E34F26?logo=html5\&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-Styling-1572B6?logo=css3\&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Vanilla-F7DF1E?logo=javascript\&logoColor=black)

* HTML
* CSS
* Vanilla JavaScript

---

### Deployment

![Render](https://img.shields.io/badge/Render-Cloud_Deployment-46E3B7?logo=render\&logoColor=black)
![Deployment](https://img.shields.io/badge/Status-Deployed-success)

* Render (Full-stack deployment)

---

## 🚀 Live Demo

You can access the deployed application here:

👉 **[https://retailsense-support-assistance.onrender.com/](https://retailsense-support-assistance.onrender.com/)**

### Try:

* Submitting a text-only issue
* Uploading an image with a damage-related query
* Checking warranty eligibility responses

---

## ⚠️ Disclaimer

This chatbot is an **AI-based support assistant** created for demonstration and learning purposes.
**Final warranty or replacement approval is subject to manual inspection by the support team.**

---

## 📈 What This Project Demonstrates

* Product-oriented system design
* Safe AI integration in customer support workflows
* Hybrid reasoning (rules + LLM)
* Backend API development with FastAPI
* Image + text handling
* Deployment-ready, real-world architecture

---

## 📌 Project Type

**Mini Project**
Focused on showcasing **core backend, AI reasoning, and product design skills** rather than large-scale infrastructure.

---

## 🔮 Future Enhancements (Optional)

* Advanced computer vision models for defect detection
* Role-based support dashboards
* Integration with ticketing or CRM systems
* Analytics on common customer issues

---

## 👤 Author

**Akhil Saurabh**
Computer Science Engineer | AI & Backend Enthusiast

---
