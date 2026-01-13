# Research Agent (CrewAI + OpenAI)

## Overview
This repository contains a **Research Agent** built using **CrewAI** and **OpenAI**.  
The agent automates structured research and long-form content generation by coordinating multiple specialized AI agents (Planner, Writer, Editor). It is designed for research, analysis, and high-quality written outputs on any given topic.

The system follows a **plan → write → edit** workflow and produces publication-ready markdown content.

---

## Architecture
The research agent consists of three roles:

- **Content Planner**  
  Researches trends, key players, audiences, SEO keywords, and sources.

- **Content Writer**  
  Converts the research plan into a structured, insightful article.

- **Editor**  
  Proofreads and aligns the content with professional writing standards.

Each role is implemented as a CrewAI `Agent`, coordinated through sequential `Task`s.

---

## LLM Provider
- **OpenAI** (configured via environment variables)

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/research-agent.git
cd research-agent
````

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install crewai python-dotenv ipython
```

### 4. Configure environment variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## Usage

Run the research agent:

```bash
python main.py
```

You can change the research topic inside `main.py`:

```python
result = crew.kickoff(inputs={"topic": "Artificial Intelligence In Cyber Security"})
```

---

## Example Output

### Content Plan (Excerpt)

```
Content Plan: Artificial Intelligence In Cyber Security

I. Introduction
- Definition of AI in Cyber Security
- Importance of AI in combating cyber threats

II. Latest Trends
- Machine learning for threat detection
- Automation of incident response

III. Key Players
- IBM Security
- Palo Alto Networks
- Darktrace
- CrowdStrike
```

### Final Article (Excerpt)

```markdown
# Artificial Intelligence In Cyber Security

## Introduction
Artificial Intelligence (AI) in Cyber Security refers to the use of advanced technologies and algorithms to enhance cybersecurity measures and combat cyber threats.

## Latest Trends
Machine learning algorithms are increasingly used for threat detection, allowing organizations to identify anomalies and respond faster to attacks.
```

---

## Use Cases

* Automated research reports
* Blog and article generation
* Educational content creation
* Technology and industry analysis

---

## Notes

* Outputs may vary between runs due to LLM behavior.
* Results are generated in **Markdown** format.
* Best suited for research, documentation, and content pipelines.

---

## License

This project is provided as-is for research and educational purposes.

```
```
