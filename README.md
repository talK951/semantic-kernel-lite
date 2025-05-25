# Simple Semantic Kernel (Python Only)

This is a simple Python-based implementation of the **[Semantic Kernel](https://github.com/microsoft/semantic-kernel)** project originally developed by Microsoft. It is designed to demonstrate how key features of the Semantic Kernel can be recreated and used without any additional frameworks — using only Python.

---

## ✨ What This Project Does

This lightweight framework supports:

- **Chat-like interactions with OpenAI**: Build LLM-enabled chat functionality.
- **Agent planning and execution**: Create dynamic plans where agents select and call functions to accomplish goals.

It showcases core ideas such as prompt execution, semantic functions, and planning logic — in a minimal and accessible way.

---

## 📂 Project Structure

All scripts in the **root directory** are examples demonstrating various features of this Python Semantic Kernel project:

- Function calling
- Simple planner logic
- LLM interaction (if connected to OpenAI API)
- Extensibility through decorated functions

Each script can be run independently and is meant to be an educational, exploratory example of using Semantic Kernel-style concepts in pure Python.

---

## 🛠 Requirements

- Python 3.8+
- (Optional) OpenAI API key if using LLM functions

To install dependencies:

```bash
pip install -r requirements.txt
