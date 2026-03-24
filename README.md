<a href="https://github.com/VoltAgent/voltagent">
    <img width="1500" height="500" alt="codex" src="https://github.com/user-attachments/assets/35f56654-e3e7-4023-a7d5-acd5215455de" />
</a>

<br />
<br />

<div align="center">
    <strong>The awesome collection of 136+ Codex subagents across 10 categories.</strong>
    <br />
    <br />
</div>

   
<div align="center">
    
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Subagent Count](https://img.shields.io/badge/subagents-136-blue?style=classic)
[![Last Update](https://img.shields.io/github/last-commit/VoltAgent/awesome-codex-subagents?label=Last%20update&style=classic)](https://github.com/VoltAgent/awesome-codex-subagents)
[![Discord](https://img.shields.io/discord/1361559153780195478.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://s.voltagent.dev/discord)

<br />


<div align="center">
    <strong>More awesome collections for developers</strong>
    <br />
    <br />
</div>

[![Agent Skills](https://img.shields.io/static/v1?label=%E2%9A%A1%20Agent&message=Skills%2012k&color=black&style=classic)](https://github.com/VoltAgent/awesome-agent-skills)
[![Claude Code Subagents](https://img.shields.io/static/v1?label=Claude&message=Code%20Subagents%2014k&color=D97757&style=classic&logo=claude&logoColor=D97757)](https://github.com/VoltAgent/awesome-claude-code-subagents)
[![OpenClaw Skills](https://img.shields.io/static/v1?label=%F0%9F%A6%9E%20OpenClaw&message=Skills%2040k&color=f53e36&style=classic)](https://github.com/VoltAgent/awesome-openclaw-skills)
[![AI Agent Papers](https://img.shields.io/static/v1?label=arxiv&message=Agent%20Papers%20328&color=b31b1b&style=classic&logo=arxiv)](https://github.com/VoltAgent/awesome-ai-agent-papers)
</div>


# Awesome OpenCode Skills (Codex Subagents Port)

**This repository is the automated OpenCode-converted version of the original Codex Subagents.**
It takes the 136+ highly specialized Codex `.toml` subagents and translates them 1:1 into the native OpenCode `SKILL.md` format for seamless integration into your OpenCode workflow.



> **Note:** This repository ([jshsakura/awesome-opencode-subagents](https://github.com/jshsakura/awesome-opencode-subagents)) is an automatically synchronized port of the original [VoltAgent/awesome-codex-subagents](https://github.com/VoltAgent/awesome-codex-subagents). All core subagents and credit belong to the original authors. This project simply adapts the 136+ subagents into the **OpenCode Skills** format (`SKILL.md`) for seamless use in OpenCode.


This repository serves as the definitive collection of [Codex Subagents](https://developers.openai.com/codex/subagents), specialized AI assistants designed for specific development tasks. Written specifically for Codex and aligned with the official docs.


## 🚀 Installation & Deployment

OpenCode loads skills automatically from specific directories on your machine. You can install all 136+ skills via a single command:

**Windows (PowerShell)**:
```powershell
irm https://raw.githubusercontent.com/jshsakura/awesome-opencode-subagents/main/install.ps1 | iex
```

**macOS / Linux**:
```bash
curl -sL https://raw.githubusercontent.com/jshsakura/awesome-opencode-subagents/main/install.sh | bash
```

**Alternative (Python)**:
If you cloned the repository locally:
```bash
python install.py
```

## 🔄 Update Cycle & Sync

This repository maintains a 1:1 synchronization with the original `VoltAgent` repository. 
- **GitHub Actions Automation**: A sync job runs every Sunday (`scripts/sync.py`), fetching the latest agents from the original project and automatically updating the native OpenCode `skills/` directory. 
- To update your local OpenCode skills, simply run the installation command above again!

## Available OpenCode Skills Categories

<!-- START_SKILLS_TABLE -->
<!-- END_SKILLS_TABLE -->

## Understanding Subagents

Subagents are specialized AI assistants that enhance Codex's capabilities by providing task-specific expertise. They act as dedicated helpers that Codex can call upon when encountering particular types of work.

### What Makes Subagents Special?

**Independent Context Windows**
Every subagent operates within its own isolated context space, preventing cross-contamination between different tasks and maintaining clarity in the primary conversation thread.

**Domain-Specific Intelligence**
Subagents come equipped with carefully crafted instructions tailored to their area of expertise, resulting in superior performance on specialized tasks.

**Shared Across Projects**
After creating a subagent, you can utilize it throughout various projects and distribute it among team members to ensure consistent development practices.

**Explicit Delegation**
Codex does not spawn subagents automatically. Use explicit delegation prompts to specify which agents to spawn, how to divide the work, and what shape the result should take.

### Core Advantages

- **Memory Efficiency**: Isolated contexts prevent the main conversation from becoming cluttered with task-specific details
- **Enhanced Accuracy**: Specialized prompts and configurations lead to better results in specific domains
- **Workflow Consistency**: Team-wide subagent sharing ensures uniform approaches to common tasks
- **Codex-Native**: Uses `.toml` agent files aligned with official Codex subagent docs

### Example Workflows

**PR review workflow:**
```text
Review this branch with parallel subagents. Have reviewer look for correctness, security, and missing tests. Have docs_researcher verify the framework APIs this patch depends on. Wait for both and summarize the findings with file references.
```

**Bug investigation workflow:**
```text
Investigate the broken settings flow. Have code_mapper trace the owning code paths, browser_debugger reproduce the bug in the browser, and frontend_developer propose the smallest fix after the failure is understood. Wait for the read-heavy agents first, then continue.
```

**Repo exploration and planning workflow:**
```text
Use search_specialist to locate the code related to payment retries, knowledge_synthesizer to summarize the current design, and refactoring_specialist to propose a minimal refactor plan. Return a concrete action list.
```
## Contributing

⚠️ **Please DO NOT submit new agents or logic changes PRs to this repository!** ⚠️

This repository (`awesome-opencode-subagents`) is strictly for automated porting and packaging for OpenCode. 
If you want to contribute new agents, improve definitions, or report logic bugs, please submit your PRs directly to the original repository:
👉 [VoltAgent/awesome-codex-subagents](https://github.com/VoltAgent/awesome-codex-subagents)

Once your contribution is merged upstream, GitHub Actions will automatically synchronize it here within a week!

## License

MIT License - see [LICENSE](LICENSE)

This repository is a curated collection of subagent definitions contributed by both the maintainers and the community. All subagents are provided "as is" without warranty. We do not audit or guarantee the security or correctness of any subagent. Review before use, the maintainers accept no liability for any issues arising from their use.

If you find an issue with a listed subagent or want your contribution removed, please open an issue in this repository and we'll address it promptly.
