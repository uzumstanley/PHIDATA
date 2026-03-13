# Multi Agent AI Framework 

Multi-Agent AI Framework is a modular and extensible artificial intelligence system that orchestrates multiple specialized AI agents to collaboratively perform complex tasks. Each agent is designed to handle a specific capability such as web search, financial analysis, reasoning, data analysis, retrieval-augmented generation (RAG), multimedia generation, and Python-based problem solving.

The framework demonstrates how intelligent agents can work independently or as coordinated teams, leveraging tool integrations, structured outputs, and contextual reasoning to deliver scalable AI-powered solutions. It also incorporates advanced features such as monitoring, debugging, human-in-the-loop verification, and multimodal inputs including text, images, and audio.

This project showcases practical implementations of modern AI agent architectures and serves as a foundation for building real-world autonomous AI systems.

Key Features

Specialized AI Agents for tasks such as web search, finance analysis, reasoning, research, and data analytics

Agent Collaboration allowing multiple agents to work together as a team

Retrieval-Augmented Generation (RAG) for knowledge-enhanced responses

Python Tooling Agent capable of executing Python functions and performing computations

Multimodal Capabilities including image, audio, and video generation

Monitoring and Debugging Tools for tracking agent performance and troubleshooting workflows

Human-in-the-Loop Verification for safer and more controlled agent decisions

CLI Application Interface for interacting with agents from the command line

Structured Outputs for reliable data extraction and automation workflows

Example Agents Included

Web Search Agent

Finance Agent

Reasoning Agent

Research Agent

RAG Agent

Data Analyst Agent

Python Execution Agent

Image Generation Agent

Video Generation Agent

Applications

Autonomous research assistants

Intelligent data analysis systems

AI-powered automation tools

Multimodal content generation platforms

Decision-support systems


# Sambanova Cookbook

> Note: Fork and clone this repository if needed

### 1. Create and activate a virtual environment

```shell
python3 -m venv ~/.venvs/aienv
source ~/.venvs/aienv/bin/activate
```

### 2. Export your `SAMBANOVA_API_KEY`

```shell
export SAMBANOVA_API_KEY=***
```

### 3. Install libraries

```shell
pip install -U openai phidata
```

### 4. Run Agent without Tools

- Streaming on

```shell
python cookbook/providers/sambanova/basic_stream.py
```

- Streaming off

```shell
python cookbook/providers/sambanova/basic.py
```
## Disclaimer:

Sambanova does not support all OpenAI features. The following features are not yet supported and will be ignored:

- logprobs
- top_logprobs
- n
- presence_penalty
- frequency_penalty
- logit_bias
- tools
- tool_choice
- parallel_tool_calls
- seed
- stream_options: include_usage
- response_format

Author : Stanley Ekene Uzum 
