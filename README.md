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


# Awesome OpenCode Skills


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

## Categories

### [01. Core Development](categories/01-core-development/)

Essential development subagents for everyday coding tasks.

- [**api-designer**](skills/api-designer/SKILL.md) - REST and GraphQL API architect
- [**backend-developer**](skills/backend-developer/SKILL.md) - Server-side expert for scalable APIs
- [**code-mapper**](skills/code-mapper/SKILL.md) - Code path mapping and ownership boundary analysis
- [**electron-pro**](skills/electron-pro/SKILL.md) - Desktop application expert
- [**frontend-developer**](skills/frontend-developer/SKILL.md) - UI/UX specialist for React, Vue, and Angular
- [**fullstack-developer**](skills/fullstack-developer/SKILL.md) - End-to-end feature development
- [**graphql-architect**](skills/graphql-architect/SKILL.md) - GraphQL schema and federation expert
- [**microservices-architect**](skills/microservices-architect/SKILL.md) - Distributed systems designer
- [**mobile-developer**](skills/mobile-developer/SKILL.md) - Cross-platform mobile specialist
- [**ui-designer**](skills/ui-designer/SKILL.md) - Visual design and interaction specialist
- [**ui-fixer**](skills/ui-fixer/SKILL.md) - Smallest safe patch for reproduced UI issues
- [**websocket-engineer**](skills/websocket-engineer/SKILL.md) - Real-time communication specialist

### [02. Language Specialists](categories/02-language-specialists/)

Language-specific experts with deep framework knowledge.
- [**angular-architect**](skills/angular-architect/SKILL.md) - Angular 15+ enterprise patterns expert
- [**cpp-pro**](skills/cpp-pro/SKILL.md) - C++ performance expert
- [**csharp-developer**](skills/csharp-developer/SKILL.md) - .NET ecosystem specialist
- [**django-developer**](skills/django-developer/SKILL.md) - Django 4+ web development expert
- [**dotnet-core-expert**](skills/dotnet-core-expert/SKILL.md) - .NET 8 cross-platform specialist
- [**dotnet-framework-4.8-expert**](skills/dotnet-framework-4.8-expert/SKILL.md) - .NET Framework legacy enterprise specialist
- [**elixir-expert**](skills/elixir-expert/SKILL.md) - Elixir and OTP fault-tolerant systems expert
- [**erlang-expert**](skills/erlang-expert/SKILL.md) - Erlang/OTP and rebar3 engineering expert
- [**flutter-expert**](skills/flutter-expert/SKILL.md) - Flutter 3+ cross-platform mobile expert
- [**golang-pro**](skills/golang-pro/SKILL.md) - Go concurrency specialist
- [**java-architect**](skills/java-architect/SKILL.md) - Enterprise Java expert
- [**javascript-pro**](skills/javascript-pro/SKILL.md) - JavaScript development expert
- [**kotlin-specialist**](skills/kotlin-specialist/SKILL.md) - Modern JVM language expert
- [**laravel-specialist**](skills/laravel-specialist/SKILL.md) - Laravel 10+ PHP framework expert
- [**nextjs-developer**](skills/nextjs-developer/SKILL.md) - Next.js 14+ full-stack specialist
- [**php-pro**](skills/php-pro/SKILL.md) - PHP web development expert
- [**powershell-5.1-expert**](skills/powershell-5.1-expert/SKILL.md) - Windows PowerShell 5.1 and full .NET Framework automation specialist
- [**powershell-7-expert**](skills/powershell-7-expert/SKILL.md) - Cross-platform PowerShell 7+ automation and modern .NET specialist
- [**python-pro**](skills/python-pro/SKILL.md) - Python ecosystem master
- [**rails-expert**](skills/rails-expert/SKILL.md) - Rails 8.1 rapid development expert
- [**react-specialist**](skills/react-specialist/SKILL.md) - React 18+ modern patterns expert
- [**rust-engineer**](skills/rust-engineer/SKILL.md) - Systems programming expert
- [**spring-boot-engineer**](skills/spring-boot-engineer/SKILL.md) - Spring Boot 3+ microservices expert
- [**sql-pro**](skills/sql-pro/SKILL.md) - Database query expert
- [**swift-expert**](skills/swift-expert/SKILL.md) - iOS and macOS specialist
- [**typescript-pro**](skills/typescript-pro/SKILL.md) - TypeScript specialist
- [**vue-expert**](skills/vue-expert/SKILL.md) - Vue 3 Composition API expert


### [03. Infrastructure](categories/03-infrastructure/)

DevOps, cloud, and deployment specialists.

- [**azure-infra-engineer**](skills/azure-infra-engineer/SKILL.md) - Azure infrastructure and Az PowerShell automation expert
- [**cloud-architect**](skills/cloud-architect/SKILL.md) - AWS/GCP/Azure specialist
- [**database-administrator**](skills/database-administrator/SKILL.md) - Database management expert
- [**deployment-engineer**](skills/deployment-engineer/SKILL.md) - Deployment automation specialist
- [**devops-engineer**](skills/devops-engineer/SKILL.md) - CI/CD and automation expert
- [**devops-incident-responder**](skills/devops-incident-responder/SKILL.md) - DevOps incident management
- [**docker-expert**](skills/docker-expert/SKILL.md) - Docker containerization and optimization expert
- [**incident-responder**](skills/incident-responder/SKILL.md) - System incident response expert
- [**kubernetes-specialist**](skills/kubernetes-specialist/SKILL.md) - Container orchestration master
- [**network-engineer**](skills/network-engineer/SKILL.md) - Network infrastructure specialist
- [**platform-engineer**](skills/platform-engineer/SKILL.md) - Platform architecture expert
- [**security-engineer**](skills/security-engineer/SKILL.md) - Infrastructure security specialist
- [**sre-engineer**](skills/sre-engineer/SKILL.md) - Site reliability engineering expert
- [**terraform-engineer**](skills/terraform-engineer/SKILL.md) - Infrastructure as Code expert
- [**terragrunt-expert**](skills/terragrunt-expert/SKILL.md) - Terragrunt orchestration and DRY IaC specialist
- [**windows-infra-admin**](skills/windows-infra-admin/SKILL.md) - Active Directory, DNS, DHCP, and GPO automation specialist

<details>
<summary><b>04. Quality & Security</b> — Testing, security, and code quality experts (16 agents)</summary>

### [04. Quality & Security](categories/04-quality-security/)

- [**accessibility-tester**](skills/accessibility-tester/SKILL.md) - A11y compliance expert
- [**ad-security-reviewer**](skills/ad-security-reviewer/SKILL.md) - Active Directory security and GPO audit specialist
- [**architect-reviewer**](skills/architect-reviewer/SKILL.md) - Architecture review specialist
- [**browser-debugger**](skills/browser-debugger/SKILL.md) - Browser-based reproduction and client-side debugging
- [**chaos-engineer**](skills/chaos-engineer/SKILL.md) - System resilience testing expert
- [**code-reviewer**](skills/code-reviewer/SKILL.md) - Code quality guardian
- [**compliance-auditor**](skills/compliance-auditor/SKILL.md) - Regulatory compliance expert
- [**debugger**](skills/debugger/SKILL.md) - Advanced debugging specialist
- [**error-detective**](skills/error-detective/SKILL.md) - Error analysis and resolution expert
- [**penetration-tester**](skills/penetration-tester/SKILL.md) - Ethical hacking specialist
- [**performance-engineer**](skills/performance-engineer/SKILL.md) - Performance optimization expert
- [**powershell-security-hardening**](skills/powershell-security-hardening/SKILL.md) - PowerShell security hardening and compliance specialist
- [**qa-expert**](skills/qa-expert/SKILL.md) - Test automation specialist
- [**reviewer**](skills/reviewer/SKILL.md) - PR-style review for correctness, security, and regressions
- [**security-auditor**](skills/security-auditor/SKILL.md) - Security vulnerability expert
- [**test-automator**](skills/test-automator/SKILL.md) - Test automation framework expert

</details>

<details>
<summary><b>05. Data & AI</b> — Data engineering, ML, and AI specialists (12 agents)</summary>

### [05. Data & AI](categories/05-data-ai/)

- [**ai-engineer**](skills/ai-engineer/SKILL.md) - AI system design and deployment expert
- [**data-analyst**](skills/data-analyst/SKILL.md) - Data insights and visualization specialist
- [**data-engineer**](skills/data-engineer/SKILL.md) - Data pipeline architect
- [**data-scientist**](skills/data-scientist/SKILL.md) - Analytics and insights expert
- [**database-optimizer**](skills/database-optimizer/SKILL.md) - Database performance specialist
- [**llm-architect**](skills/llm-architect/SKILL.md) - Large language model architect
- [**machine-learning-engineer**](skills/machine-learning-engineer/SKILL.md) - Machine learning systems expert
- [**ml-engineer**](skills/ml-engineer/SKILL.md) - Machine learning specialist
- [**mlops-engineer**](skills/mlops-engineer/SKILL.md) - MLOps and model deployment expert
- [**nlp-engineer**](skills/nlp-engineer/SKILL.md) - Natural language processing expert
- [**postgres-pro**](skills/postgres-pro/SKILL.md) - PostgreSQL database expert
- [**prompt-engineer**](skills/prompt-engineer/SKILL.md) - Prompt optimization specialist

</details>

<details>
<summary><b>06. Developer Experience</b> — Tooling and developer productivity experts (13 agents)</summary>

### [06. Developer Experience](categories/06-developer-experience/)

- [**build-engineer**](skills/build-engineer/SKILL.md) - Build system specialist
- [**cli-developer**](skills/cli-developer/SKILL.md) - Command-line tool creator
- [**dependency-manager**](skills/dependency-manager/SKILL.md) - Package and dependency specialist
- [**documentation-engineer**](skills/documentation-engineer/SKILL.md) - Technical documentation expert
- [**dx-optimizer**](skills/dx-optimizer/SKILL.md) - Developer experience optimization specialist
- [**git-workflow-manager**](skills/git-workflow-manager/SKILL.md) - Git workflow and branching expert
- [**legacy-modernizer**](skills/legacy-modernizer/SKILL.md) - Legacy code modernization specialist
- [**mcp-developer**](skills/mcp-developer/SKILL.md) - Model Context Protocol specialist
- [**powershell-module-architect**](skills/powershell-module-architect/SKILL.md) - PowerShell module and profile architecture specialist
- [**powershell-ui-architect**](skills/powershell-ui-architect/SKILL.md) - PowerShell UI/UX specialist for WinForms, WPF, Metro frameworks, and TUIs
- [**refactoring-specialist**](skills/refactoring-specialist/SKILL.md) - Code refactoring expert
- [**slack-expert**](skills/slack-expert/SKILL.md) - Slack platform and @slack/bolt specialist
- [**tooling-engineer**](skills/tooling-engineer/SKILL.md) - Developer tooling specialist

</details>

<details>
<summary><b>07. Specialized Domains</b> — Domain-specific technology experts (12 agents)</summary>

### [07. Specialized Domains](categories/07-specialized-domains/)

- [**api-documenter**](skills/api-documenter/SKILL.md) - API documentation specialist
- [**blockchain-developer**](skills/blockchain-developer/SKILL.md) - Web3 and crypto specialist
- [**embedded-systems**](skills/embedded-systems/SKILL.md) - Embedded and real-time systems expert
- [**fintech-engineer**](skills/fintech-engineer/SKILL.md) - Financial technology specialist
- [**game-developer**](skills/game-developer/SKILL.md) - Game development expert
- [**iot-engineer**](skills/iot-engineer/SKILL.md) - IoT systems developer
- [**m365-admin**](skills/m365-admin/SKILL.md) - Microsoft 365, Exchange Online, Teams, and SharePoint administration specialist
- [**mobile-app-developer**](skills/mobile-app-developer/SKILL.md) - Mobile application specialist
- [**payment-integration**](skills/payment-integration/SKILL.md) - Payment systems expert
- [**quant-analyst**](skills/quant-analyst/SKILL.md) - Quantitative analysis specialist
- [**risk-manager**](skills/risk-manager/SKILL.md) - Risk assessment and management expert
- [**seo-specialist**](skills/seo-specialist/SKILL.md) - Search engine optimization expert

</details>

<details>
<summary><b>08. Business & Product</b> — Product management and business analysis (11 agents)</summary>

### [08. Business & Product](categories/08-business-product/)

- [**business-analyst**](skills/business-analyst/SKILL.md) - Requirements specialist
- [**content-marketer**](skills/content-marketer/SKILL.md) - Content marketing specialist
- [**customer-success-manager**](skills/customer-success-manager/SKILL.md) - Customer success expert
- [**legal-advisor**](skills/legal-advisor/SKILL.md) - Legal and compliance specialist
- [**product-manager**](skills/product-manager/SKILL.md) - Product strategy expert
- [**project-manager**](skills/project-manager/SKILL.md) - Project management specialist
- [**sales-engineer**](skills/sales-engineer/SKILL.md) - Technical sales expert
- [**scrum-master**](skills/scrum-master/SKILL.md) - Agile methodology expert
- [**technical-writer**](skills/technical-writer/SKILL.md) - Technical documentation specialist
- [**ux-researcher**](skills/ux-researcher/SKILL.md) - User research expert
- [**wordpress-master**](skills/wordpress-master/SKILL.md) - WordPress development and optimization expert

</details>

<details>
<summary><b>09. Meta & Orchestration</b> — Agent coordination and meta-programming (12 agents)</summary>

### [09. Meta & Orchestration](categories/09-meta-orchestration/)

- [**agent-installer**](skills/agent-installer/SKILL.md) - Browse and install agents from this repository via GitHub
- [**agent-organizer**](skills/agent-organizer/SKILL.md) - Multi-agent coordinator
- [**context-manager**](skills/context-manager/SKILL.md) - Context optimization expert
- [**error-coordinator**](skills/error-coordinator/SKILL.md) - Error handling and recovery specialist
- [**it-ops-orchestrator**](skills/it-ops-orchestrator/SKILL.md) - IT operations workflow orchestration specialist
- [**knowledge-synthesizer**](skills/knowledge-synthesizer/SKILL.md) - Knowledge aggregation expert
- [**multi-agent-coordinator**](skills/multi-agent-coordinator/SKILL.md) - Advanced multi-agent orchestration
- [**performance-monitor**](skills/performance-monitor/SKILL.md) - Agent performance optimization
- [**pied-piper**](https://github.com/sathish316/pied-piper/) - Orchestrate Team of AI Subagents for repetitive SDLC workflows
- [**task-distributor**](skills/task-distributor/SKILL.md) - Task allocation specialist
- [**workflow-orchestrator**](skills/workflow-orchestrator/SKILL.md) - Complex workflow automation

</details>

<details>
<summary><b>10. Research & Analysis</b> — Research, search, and analysis specialists (7 agents)</summary>

### [10. Research & Analysis](categories/10-research-analysis/)

- [**competitive-analyst**](skills/competitive-analyst/SKILL.md) - Competitive intelligence specialist
- [**data-researcher**](skills/data-researcher/SKILL.md) - Data discovery and analysis expert
- [**docs-researcher**](skills/docs-researcher/SKILL.md) - Documentation-backed API and framework verification
- [**market-researcher**](skills/market-researcher/SKILL.md) - Market analysis and consumer insights
- [**research-analyst**](skills/research-analyst/SKILL.md) - Comprehensive research specialist
- [**search-specialist**](skills/search-specialist/SKILL.md) - Advanced information retrieval expert
- [**trend-analyst**](skills/trend-analyst/SKILL.md) - Emerging trends and forecasting expert

</details>

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

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

- Submit new subagents via PR
- Improve existing definitions
- Report issues and bugs


## License

MIT License - see [LICENSE](LICENSE)

This repository is a curated collection of subagent definitions contributed by both the maintainers and the community. All subagents are provided "as is" without warranty. We do not audit or guarantee the security or correctness of any subagent. Review before use, the maintainers accept no liability for any issues arising from their use.

If you find an issue with a listed subagent or want your contribution removed, please open an issue in this repository and we'll address it promptly.
