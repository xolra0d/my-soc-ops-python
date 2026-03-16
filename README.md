# 🎯 Soc Ops — Social Bingo & AI Agent Lab

[Play the Game 🎮](https://madebygps.github.io/vscode-github-copilot-agent-lab/) • [Read the Lab Guide 📚](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/) • [GitHub Repo 💻](https://github.com/copilot-dev-days/agent-lab-python)

![Python 3.13+](https://img.shields.io/badge/Python-3.13+-blue.svg)
![uv](https://img.shields.io/badge/package--manager-uv-green.svg)
![FastAPI](https://img.shields.io/badge/framework-FastAPI-009688.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

---

### **Turn Your Mixers into a Mission**
**Soc Ops** (Social Operations) is a bingo-style social mixer game designed for tech events and in-person meetups. The goal? Break the ice by finding people who match the fun, quirky, and "too-real" tech traits on your card.

Beyond the game, this project serves as a **hands-on playground for VS Code GitHub Copilot Agents**, showcasing how AI can accelerate development from design to deployment.

---

## ✨ Key Features

- 🎲 **Dynamic Bingo Generation** — Every card is unique, generated from a curated list of social prompts.
- ⚡ **Lightning Fast** — Built with **FastAPI** and **uv** for a near-instant developer experience.
- 🎨 **Utility-First UI** — Clean, responsive design using a semantic, utility-based CSS system.
- 🤖 **Agent-Ready Architecture** — Includes specialized agents for linting, design review, TDD, and quiz generation.
- 🌐 **Auto-Deploy** — GitHub Actions ready for seamless deployment to GitHub Pages.

---

## 🛠️ The Lab: AI Agent Journey

This project is the core of the **VS Code GitHub Copilot Agent Lab**. You'll use AI agents to:

1. **Context Engineering** — Master how to "talk" to the codebase.
2. **Design-First Development** — Redesign the entire UI using architectural plans.
3. **Custom Quiz Masters** — Use AI to generate entirely new game themes.
4. **Multi-Agent TDD** — Build complex features (like Scavenger Hunt modes) with Red-Green-Refactor agent cycles.

---

## 🚀 Quick Start

### 1. Prerequisites
Ensure you have [Python 3.13+](https://www.python.org/downloads/) and [uv](https://docs.astral.sh/uv/) installed.

### 2. Setup
```bash
# Clone and sync dependencies
uv sync
```

### 3. Launch
```bash
# Start the dev server
uv run uvicorn app.main:app --reload
```
Open **[localhost:8000](http://localhost:8000)** to start playing!

---

## 🧪 Development Workflow

| Task | Command |
| :--- | :--- |
| **Test** | `uv run pytest` |
| **Lint** | `uv run ruff check . --fix` |
| **Format** | `uv run ruff format .` |

---

## 📚 Lab Chapters

| Chapter | Title | Link |
| :---: | :--- | :--- |
| **00** | Overview & Checklist | [View](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/step.html?step=00-overview) |
| **01** | Setup & Context Engineering | [View](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/step.html?step=01-setup) |
| **02** | Design-First Frontend | [View](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/step.html?step=02-design) |
| **03** | Custom Quiz Master | [View](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/step.html?step=03-quiz-master) |
| **04** | Multi-Agent Development | [View](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/step.html?step=04-multi-agent) |

---

## 🤝 Contributing
Found a bug or have a feature idea? Open an issue or submit a PR! This project is MIT licensed and open for all.

---
*Built with ❤️ for the developer community by [MadeByGPS](https://github.com/madebygps) & the VS Code team.*
