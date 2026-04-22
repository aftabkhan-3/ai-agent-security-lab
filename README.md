\# 🔐 AI Agent Security Lab



A hands-on project exploring \*\*security risks in AI agents\*\*, focusing on prompt injection, tool misuse, and trust boundary failures.



\---



\## 🚀 Overview



This project evaluates:



\* \*\*Claude Code (model-level security)\*\*

\* \*\*Custom AI agent with tools (system-level security)\*\*



\### Key Insight



> \*\*AI model safety ≠ AI system safety\*\*



Even if the model is secure, poor system design can introduce vulnerabilities.



\---



\## 🧪 What This Project Demonstrates



\### ✅ Claude Model Behavior



\* Detects prompt injection

\* Refuses secret exfiltration

\* Ignores malicious instructions



\### ⚠️ Agent System Vulnerability



\* Tool output can act as hidden instructions

\* No trust boundary between data and execution

\* Risk of command execution \& data leakage



\---



\## 🏗️ Project Structure



```bash

ai-agent-security-lab/

├── vulnerable\_agent/   # Insecure implementation

├── secure\_agent/       # Fixed implementation

├── attack\_scenarios/   # Attack examples

├── demo/               # How to reproduce

├── report/             # Full analysis

```



\---



\## 🔥 Core Vulnerability



The vulnerable agent blindly trusts tool output:



```python

messages.append({"role": "tool", "content": result})

```



This allows:



```

Tool → Injected Instruction → Agent → Action

```



\---



\## 🧪 Demo



\### 1. Run vulnerable agent



```bash

python vulnerable\_agent/main.py

```



Type:



```

debug

```



👉 The agent executes a command from tool output (unsafe)



\---



\### 2. Run secure agent



```bash

python secure\_agent/main.py

```



👉 The agent blocks execution and treats tool output as untrusted



\---



\## 🛠️ Fixes Implemented



\* Tool output sanitization

\* Trust boundary enforcement

\* Command allowlisting

\* Restricted file access



\---



\## 🧠 Key Takeaway



> The biggest risk in AI systems is not the model — but how it is integrated with tools and external inputs.



\---



\## 📌 Author



Aftab Khan



\---



