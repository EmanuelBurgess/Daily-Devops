# Daily-Devops
A AI powered daily Devops coaching pipeline
# Daily DevOps Briefing Automation

An automated, serverless pipeline that leverages the Google Gemini 2.5 Flash model and GitHub Actions to deliver a daily DevOps joke, motivational quote and a tailored "DevOps Skill of the Day" directly to your inbox every morning.

This entire pipeline runs completely within the permanent free tier boundaries of Google AI Studio, GitHub Actions, and Gmail SMTP.

## Features
* **Daily DevOps Joke:** Lighthearted engineering puns, infrastructure jokes, and container humor to kickstart your morning.
* **Skill of the Day:** A high-yield DevOps focus item (Linux tools, Git workflows, Kubernetes patterns, or cloud optimizations) with a practical real-world explanation.
* **Markdown-to-HTML Formatting:** Uses native GitHub Actions extensions to convert raw Gemini markdown output into an easily readable email layout.
* **Zero Infrastructure:** Runs entirely on GitHub-hosted runners using cron scheduling.

---

## Architecture Overview

1. **GitHub Actions Scheduler:** Triggers the pipeline every morning at 8:00 AM EDT via a cron schedule (0 12 * * *).
2. **Python Engine (daily_devops.py):** Uses the modern google-genai SDK to prompt gemini-2.5-flash for the content and writes it to a workspace file (briefing.md).
3. **SMTP Delivery Action (dawidd6/action-send-mail):** Reads the generated markdown, converts it to HTML, authenticates securely via a Google App Password, and dispatches the email.

---

## Prerequisites and Setup

To get this running in your own environment, you need to configure 4 encrypted secrets in your GitHub repository (Settings > Secrets and variables > Actions > New repository secret).

### 1. Google AI Studio Key (GEMINI_API_KEY)
* Go to Google AI Studio.
* Sign in with your Google account and click Create API Key.
* Save the token as GEMINI_API_KEY in your GitHub secrets.

### 2. Gmail SMTP Authentication (GMAIL_APP_PASSWORD)
Because standard password authentication is blocked for third-party automated scripts, you must generate an App Password:
* Go to your Google Account Security Settings.
* Ensure 2-Step Verification is turned ON.
* Search for "App passwords" at the top of the page.
* Create a new password named "GitHub Actions DevOps Cron".
* Copy the 16-character code (strip out spaces) and save it as GMAIL_APP_PASSWORD in your GitHub secrets.

### 3. General Configurations
* `GMAIL_USERNAME`: Your full sending Gmail address (e.g., example@gmail.com).
* `TO_EMAIL`: The destination inbox where you want to receive the daily message.

---
