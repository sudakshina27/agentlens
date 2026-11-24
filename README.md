# AgentLens

**Observability and evaluation for LLM agents.**

AgentLens records what an AI agent does on every request (each LLM call, each tool call, how long it took, how many tokens it used and whether anything failed) so you can see *why* an agent behaved the way it did, not just what it answered.

## Why

AI agents are hard to debug. A single question can trigger several model calls and tool calls, and when the answer is wrong, slow or expensive, it's not obvious which step caused it. AgentLens makes each run inspectable, the same way tracing tools do for backend services.

## What it does

- **Agent:** a simple tool-using agent (calculator, search, internal document lookup), written from scratch without a framework
- **Tracing:** records every step of every run (inputs, outputs, latency, tokens, errors)
- **Budgets** *(planned)*: enforces cost and step limits per request
- **Evaluation** *(planned)*: scores answers automatically using an LLM-as-judge
- **Regression testing** *(planned)*: reruns a fixed test set after changes and compares results
- **Dashboard** *(planned)*: shows runs, costs, failures and quality scores

## Tech stack

Python · OpenAI API · SQLite · Streamlit · pytest

## Status

🚧 Work in progress, built as a short-term learning project.