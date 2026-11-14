# 📖 AuraFolio — The Curated Aesthetic Book Sanctuary

> An editorial, dark-academia-inspired book management web application built with **Python**, **Django**, **HTML5**, **CSS3**, and **Bootstrap 5.3**.

---

## 🌟 Resume Project Description

You can showcase this project on your resume with either of these polished options:

### Option 1 (High Impact & Comprehensive - Recommended):
> **AuraFolio – Aesthetic Book Library Management System** | *Python, Django, Bootstrap 5, HTML5/CSS3, SQLite*
> - Engineered an editorial-grade book repository application implementing full CRUD lifecycles to catalog, view, edit, and delete literary records.
> - Modeled relational database schemas to track metadata including reading statuses (Want to Read, Currently Reading, Completed), star ratings, custom aesthetic mood tags, and literary excerpts.
> - Designed a warm, responsive frontend with Bootstrap 5.3 and custom CSS featuring 3D book spine cards, glassmorphic navigation, and multi-parameter filtering (full-text search, genre, reading progress).
> - Integrated user authentication (registration, split-screen login, session-managed logout) and access control with pre-seeded curated titles and dynamic cover visualizers.

### Option 2 (Concise & Focused):
> **AuraFolio – Django Book Library Platform** | *Python, Django, Bootstrap, SQLite*
> - Built a responsive Django application to manage book collections with complete CRUD functionality.
> - Implemented secure authentication (login/logout/register) and dynamic search, genre filtering, and reading status tracking.
> - Designed an aesthetic editorial interface using Bootstrap 5 and custom typography with live cover preview and 3D card presentations.

---

## ✨ Features & Architecture

- **🏛️ Aesthetic Landing Page (Sanctuary):**
  - Editorial hero section with 3D perspective book displays and atmospheric typography (*Playfair Display*, *Cormorant Garamond*, *Plus Jakarta Sans*).
  - Live statistics bar tracking total catalogued titles, active reading journeys, finished books, and curated genres.
  - Featured showcase and rotating literary quote highlights.
- **📚 Complete Book CRUD Operations:**
  - **Create / Add:** Inscribe new books with title, author, genre, reading status, star rating, quotes, tags, year, pages, language, and ISBN.
  - **Read / Detail:** Magazine-style book view with cover lighting effects, excerpts, metadata grid, and related books in the same genre.
  - **Update / Refine:** Edit existing records with a live cover image preview (supports both web URLs and file uploads).
  - **Delete / Remove:** Safe modal and view confirmation with permanent removal safeguards.
- **🔍 Multi-Dimensional Search & Filtering:**
  - Real-time search across title, author, synopsis, quotes, and aesthetic mood tags.
  - Status pill tabs (*All*, *Currently Reading*, *Finished*, *Want to Read*, *On Hold*) with live record counters.
  - Genre dropdown and sorting by newest, oldest, highest rated, title (A-Z), and page count.
- **🔐 Secure Authentication:**
  - Aesthetic split-screen sign-in and sign-up interfaces.
  - Graceful logout and session management.
  - User-specific collection scoping with support for public seed collections.
- **🖼️ Cover Support:**
  - Live preview visualizer in the creation form.
  - Accepts direct high-resolution web image URLs (Unsplash, OpenLibrary) or local file uploads.

---

## 🚀 Quick Start Guide

### 1. Requirements
- Python 3.10+ (Tested on Python 3.14)
- Django 5.x / 6.x
- Pillow

### 2. Setup & Database Migration
```bash
# Clone or navigate to the project directory
cd Aesthetic_book_library

# Apply database migrations
python manage.py migrate

# Seed curated aesthetic books (pre-loads 8 titles)
python manage.py seed_books
```

### 3. Run the Development Server
```bash
python manage.py runserver
```

Open your browser and navigate to:
```
http://127.0.0.1:8000/
```

---

## 🔑 Pre-Configured Demo Credentials

For quick evaluation and testing:
- **Username:** `curator`
- **Password:** `aurafolio123`

*(The login screen also features a one-click **Autofill** button for instant access!)*

---

## 🧪 Running Automated Tests

Run the complete test suite:
```bash
python manage.py test
```
All unit tests covering landing views, library filtering, detail pages, authentication, and the complete CRUD lifecycle run out-of-the-box.

