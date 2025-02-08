# 🌊 Surfer Helper: Transforming Web Browsing into an Audio Experience

*Check out our on-browser speech-to-text experiment! [Click here](https://loukaspastras.github.io/AI_Hackathon_2025)*


## 🚀 Introduction
Welcome to **Surfer Helper**, our innovative AI-powered browser extension designed to transform web browsing into an **audio-first** experience. Our goal is to enable seamless and natural interaction with websites (news sites, blogs, forums, e-shops, etc.) using **voice commands** and **audible feedback**.

Our long-term vision is to evolve Surfer Helper into a **Google Add-on**, allowing users to interact with web pages through **voice commands** and **real-time audio responses**, enhancing accessibility and usability.

## 🎯 Core Concept
By leveraging **Large Language Models (LLMs)** for conversational interfaces, **Text-to-Speech (TTS)** and **Speech-to-Text (STT)** technology, **semantic HTML analysis**, and **image-to-text processing**, Surfer Helper creates a revolutionary hands-free web browsing experience.

Users will be able to navigate and interact with online content solely through voice, making the web more accessible, convenient, and user-friendly.

To ensure a **natural and context-aware interaction**, our approach is based on:
1. **The sitemap** (as used in SEO optimization) of the website being transformed into an audio experience, which can be automatically generated using tools like Screaming Frog SEO Spider and XML-Sitemaps.com.
2. **The HTML hierarchy** of the current page being visited, ensuring structured and relevant interactions.

## ✨ Key Features
During the **AI_Hackathon_2025**, our focus will be on developing a **proof of concept** applied to a specific website, demonstrating the following key capabilities:

- **🔍 Smart Summarization**: Users can request AI-generated summaries of webpage content, making information easier to digest.
- **📌 Clickables Description**: Get an audible description of menus, hyperlinks, and interactive elements, enhancing accessibility.
- **🎯 Voice Navigation**: Move through links and pages using **voice commands**, eliminating the need for manual clicks.
- **🔎 Search Bar Interaction**: If a website has a search function, Surfer Helper will enable users to search via voice input.
- **📚 Article Narration**: Listen to long-form content read aloud, with customizable narration styles (formal, casual, etc.).
- **💬 Discussion Mode**: Engage in an AI-powered conversation about the page's content, ask for explanations, and receive detailed insights.

## 🛠️ Tech Stack & Implementation
To bring Surfer Helper to life, we will employ the following technologies:

### **Frontend**
- **HTML, JavaScript (React)** – Building an intuitive and efficient browser extension UI.

### **Backend**
- **Python (Flask/FastAPI)** – Managing AI models and handling API calls.

### **AI & Audio Processing**
- **LLMs**: OpenAI GPT-4 or an equivalent model for conversational interactions.
- **TTS & STT APIs**: Google Cloud Text-to-Speech & Speech-to-Text for high-quality audio conversion.
- **Computer Vision**: Google Vision AI API for image-to-text conversion (describing non-text elements on a page).
- **Local AI Processing**: Exploring **Ollama + Deepseek** to determine how much processing can be done locally instead of relying on external APIs.

### **Web Scraping & HTML Parsing**
- **BeautifulSoup & Selenium** – Extracting and analyzing webpage structures for smarter interactions.
- **Scrapy** – A powerful open-source framework for large-scale web scraping.
- **Playwright** – A modern web automation tool to simulate user interactions.
- **wappalyzer** – For detecting and categorizing technologies used on a website.
- **SEO Sitemap Generators** – Tools like **Screaming Frog SEO Spider** and **XML-Sitemaps.com** to automatically generate sitemaps from URLs, aiding structured content extraction.

## 🌍 Impact & Future Vision
Surfer Helper aims to revolutionize web browsing by shifting from a **visual-centric** to an **audio-driven** experience. This technology will:
- **Enhance accessibility** for visually impaired users.
- **Enable hands-free browsing** for multitaskers and busy professionals.
- **Improve information retrieval** through intelligent summarization and interactive discussions.

Through **AI_Hackathon_2025**, our team is dedicated to building the first working prototype of Surfer Helper, demonstrating the power of **voice-driven web navigation**.

Stay tuned and join us on this journey to make the web **more inclusive and smarter!** 🚀🎧

