---
type: chatgpt-export-conversation
topic: "Antigravity-Brain"
title: "zclaw AI Assistant"
conversation_id: "69a2772a-6cbc-83ab-a616-51645d1b8fee"
imported_at_utc: "2026-03-03T05:32:15+00:00"
turn_count: 3
chars: 3045
topic_score: 2
---

# zclaw AI Assistant

- topic: `Antigravity-Brain`
- source: `0de9e284f70b860fe63b5e28aaddc0ee7a22bd1dab6fc430bd0bf284a7a94070-2026-02-28-12-01-06-6b187fa97d244cc5beb7efa352c5af1f.zip::conversations-001.json`
- source_txt: `/mnt/c/Users/jhk92/OneDrive/문서/GitHub/ai/Moltbot/tools/handoff/bridge_outbox_tabs/69a2772a-6cbc-83ab-a616-51645d1b8fee_zclaw_AI_Assistant.txt`
- conversation_id: `69a2772a-6cbc-83ab-a616-51645d1b8fee`
- matched_keywords: brain
- card: [[workspace-links/_catalog/cards/Antigravity-Brain|에이전트 브레인 R&D 허브]]

## Summary
https://github.com/tnm/zclaw

## Transcript

## 1. user

https://github.com/tnm/zclaw

## 2. assistant

search("https://github.com/tnm/zclaw")

## 3. assistant

Here’s a summary of what the project you linked — **entity["software","tnm/zclaw","GitHub"]** — actually *is* and why it’s drawing attention 👇:

### 🚀 What **zclaw** Is  
**zclaw** is an **open-source personal AI assistant firmware** designed to run on *very low-power microcontrollers*, especially the **ESP32 family**. It squeezes an AI assistant stack plus networking into a super-tiny firmware under **~888 KiB total**, with the core application logic being only ~35 KB of C code! citeturn0search3turn0search6

### 🤖 Key Features (Crazy Compact)  
- **Tiny AI Assistant Runtime:** Runs on **ESP32-C3/S3/C6** boards with a strict firmware size cap ≤ 888 KiB (including Wi-Fi, TLS, and realtime OS). citeturn0search6  
- **Natural Language Control:** Accepts commands in natural language and performs actions like automations or GPIO control. citeturn0search6  
- **GPIO & Hardware Control:** Directly interacts with hardware (GPIO reads/writes, sensors, etc.). citeturn0search6  
- **Cron-like Scheduling:** Built-in scheduler to run tasks at set times. citeturn0search6  
- **Persistent Memory:** Stores state across reboots. citeturn0search6  
- **Custom Tools & Integrations:** Supports defining and invoking custom “tools” via natural language interfaces. citeturn0search6  
- **LLM API Support:** Works with cloud LLM providers like OpenAI, Anthropic, OpenRouter, and can be pointed at custom endpoints (e.g., Ollama). citeturn0view0  
- **Chat Interfaces:** Interfaces via Telegram or hosted web relay. citeturn0view0

### 🔧 How It Works  
Unlike fully self-contained local AI inference on the chip (which is basically impossible at this size), **zclaw mostly acts as a smart agent harness** that:

1. Connects to a LLM backend over the network  
2. Processes natural language into actions  
3. Executes those actions on the embedded device (GPIO, schedules, etc.)  
4. Sends responses back via chat interface 🗣️ citeturn0search3

So the AI *brain* is remote, but the *actuator/assistant layer* is local and embedded.

### 🛠️ Project Details  
- **Written in:** C (plus some shell, Python, HTML/CSS for dev + docs) citeturn0view0  
- **License:** MIT License citeturn0view0  
- **Getting Started:** Scripts for bootstrap, provisioning Wi-Fi and credentials, connecting your Telegram bot, etc. citeturn0view0  
- **Recommended Board:** Seeed XIAO ESP32-C3 or similar. citeturn0view0  
- **Stars & Activity:** ~1.5k ⭐ and active development. citeturn0view0

### 🧠 Why It’s Interesting  
This project shows how **lightweight AI assistants can live at the edge** with tiny hardware, enabling direct control over physical devices and scheduled tasks with natural language — all within extreme resource constraints! citeturn0search8

Would you like a **practical breakdown of how to build and flash this onto an ESP32 step-by-step**? (e.g., hardware requirements + dev flow)
