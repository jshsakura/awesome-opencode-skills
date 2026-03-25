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
[![OpenCode](https://img.shields.io/static/v1?label=OpenCode&message=AI%20Coding%20Assistant&color=007AFF&style=classic)](https://opencode.ai/)
</div>


# Awesome OpenCode Skills (Codex Subagents Port)

**This repository is the automated OpenCode-converted version of the original Codex Subagents.**
It takes the 136+ highly specialized Codex `.toml` subagents and translates them 1:1 into the native OpenCode `SKILL.md` format for seamless integration into your OpenCode workflow.



> **Note:** This repository ([jshsakura/awesome-opencode-skills](https://github.com/jshsakura/awesome-opencode-skills)) is an automatically synchronized port of the original [VoltAgent/awesome-codex-subagents](https://github.com/VoltAgent/awesome-codex-subagents). All core subagents and credit belong to the original authors. This project simply adapts the 136+ subagents into the **OpenCode Skills** format (`SKILL.md`) for seamless use in OpenCode.


This repository serves as the definitive collection of [Codex Subagents](https://developers.openai.com/codex/subagents), specialized AI assistants designed for specific development tasks. Written specifically for Codex and aligned with the official docs.


## 🚀 Installation & Deployment

OpenCode loads skills automatically from specific directories on your machine. You can install all 136+ skills via a single command:

**Windows (PowerShell)**:
```powershell
irm https://raw.githubusercontent.com/jshsakura/awesome-opencode-skills/main/install.ps1 | iex
```

**macOS / Linux**:
```bash
curl -sL https://raw.githubusercontent.com/jshsakura/awesome-opencode-skills/main/install.sh | bash
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
### 01. Core Development

| Skill | Description |
|-------|-------------|
| [**api-designer**](skills/api-designer/SKILL.md) | Use when a task needs API contract design, evolution planning, or compatibility review before implementation starts. |
| [**backend-developer**](skills/backend-developer/SKILL.md) | Use when a task needs scoped backend implementation or backend bug fixes after the owning path is known. |
| [**code-mapper**](skills/code-mapper/SKILL.md) | Use when the parent agent needs a high-confidence map of code paths, ownership boundaries, and execution flow before changes are made. |
| [**electron-pro**](skills/electron-pro/SKILL.md) | Use when a task needs Electron-specific implementation or debugging across main/renderer/preload boundaries, packaging, and desktop runtime behavior. |
| [**frontend-developer**](skills/frontend-developer/SKILL.md) | Use when a task needs scoped frontend implementation or UI bug fixes with production-level behavior and quality. |
| [**fullstack-developer**](skills/fullstack-developer/SKILL.md) | Use when one bounded feature or bug spans frontend and backend and a single worker should own the entire path. |
| [**graphql-architect**](skills/graphql-architect/SKILL.md) | Use when a task needs GraphQL schema evolution, resolver architecture, federation design, or distributed graph performance/security review. |
| [**microservices-architect**](skills/microservices-architect/SKILL.md) | Use when a task needs service-boundary design, inter-service contract review, or distributed-system architecture decisions. |
| [**mobile-developer**](skills/mobile-developer/SKILL.md) | Use when a task needs mobile implementation or debugging across app lifecycle, API integration, and device/platform-specific UX constraints. |
| [**ui-designer**](skills/ui-designer/SKILL.md) | Use when a task needs concrete UI decisions, interaction design, and implementation-ready design guidance before or during development. |
| [**ui-fixer**](skills/ui-fixer/SKILL.md) | Use when a UI issue is already reproduced and the parent agent wants the smallest safe patch. |
| [**websocket-engineer**](skills/websocket-engineer/SKILL.md) | Use when a task needs real-time transport and state work across WebSocket lifecycle, message contracts, and reconnect/failure behavior. |

### 02. Language Specialists

| Skill | Description |
|-------|-------------|
| [**angular-architect**](skills/angular-architect/SKILL.md) | Use when a task needs Angular-specific help for component architecture, dependency injection, routing, signals, or enterprise application structure. |
| [**cpp-pro**](skills/cpp-pro/SKILL.md) | Use when a task needs C++ work involving performance-sensitive code, memory ownership, concurrency, or systems-level integration. |
| [**csharp-developer**](skills/csharp-developer/SKILL.md) | Use when a task needs C# or .NET application work involving services, APIs, async flows, or application architecture. |
| [**django-developer**](skills/django-developer/SKILL.md) | Use when a task needs Django-specific work across models, views, forms, ORM behavior, or admin and middleware flows. |
| [**dotnet-core-expert**](skills/dotnet-core-expert/SKILL.md) | Use when a task needs modern .NET and ASP.NET Core expertise for APIs, hosting, middleware, or cross-platform application behavior. |
| [**dotnet-framework-4.8-expert**](skills/dotnet-framework-4.8-expert/SKILL.md) | Use when a task needs .NET Framework 4.8 expertise for legacy enterprise applications, compatibility constraints, or Windows-bound integrations. |
| [**elixir-expert**](skills/elixir-expert/SKILL.md) | Use when a task needs Elixir and OTP expertise for processes, supervision, fault tolerance, or Phoenix application behavior. |
| [**erlang-expert**](skills/erlang-expert/SKILL.md) | Use when a task needs Erlang/OTP and rebar3 expertise for BEAM processes, testing, releases, upgrades, or distributed runtime behavior. |
| [**flutter-expert**](skills/flutter-expert/SKILL.md) | Use when a task needs Flutter expertise for widget behavior, state management, rendering issues, or mobile cross-platform implementation. |
| [**golang-pro**](skills/golang-pro/SKILL.md) | Use when a task needs Go expertise for concurrency, service implementation, interfaces, tooling, or performance-sensitive backend paths. |
| [**java-architect**](skills/java-architect/SKILL.md) | Use when a task needs Java application or service architecture help across framework boundaries, JVM behavior, or large codebase structure. |
| [**javascript-pro**](skills/javascript-pro/SKILL.md) | Use when a task needs JavaScript-focused work for runtime behavior, browser or Node execution, or application-level code that is not TypeScript-led. |
| [**kotlin-specialist**](skills/kotlin-specialist/SKILL.md) | Use when a task needs Kotlin expertise for JVM applications, Android code, coroutines, or modern strongly typed service logic. |
| [**laravel-specialist**](skills/laravel-specialist/SKILL.md) | Use when a task needs Laravel-specific work across routing, Eloquent, queues, validation, or application structure. |
| [**nextjs-developer**](skills/nextjs-developer/SKILL.md) | Use when a task needs Next.js-specific work across routing, rendering modes, server actions, data fetching, or deployment-sensitive frontend behavior. |
| [**php-pro**](skills/php-pro/SKILL.md) | Use when a task needs PHP expertise for application logic, framework integration, runtime debugging, or server-side code evolution. |
| [**powershell-5.1-expert**](skills/powershell-5.1-expert/SKILL.md) | Use when a task needs Windows PowerShell 5.1 expertise for legacy automation, full .NET Framework interop, or Windows administration scripts. |
| [**powershell-7-expert**](skills/powershell-7-expert/SKILL.md) | Use when a task needs modern PowerShell 7 expertise for cross-platform automation, scripting, or .NET-based operational tooling. |
| [**python-pro**](skills/python-pro/SKILL.md) | Use when a task needs a Python-focused subagent for runtime behavior, packaging, typing, testing, or framework-adjacent implementation. |
| [**rails-expert**](skills/rails-expert/SKILL.md) | Use when a task needs Ruby on Rails expertise for models, controllers, jobs, callbacks, or convention-driven application changes. |
| [**react-specialist**](skills/react-specialist/SKILL.md) | Use when a task needs a React-focused agent for component behavior, state flow, rendering bugs, or modern React patterns. |
| [**rust-engineer**](skills/rust-engineer/SKILL.md) | Use when a task needs Rust expertise for ownership-heavy systems code, async runtime behavior, or performance-sensitive implementation. |
| [**spring-boot-engineer**](skills/spring-boot-engineer/SKILL.md) | Use when a task needs Spring Boot expertise for service behavior, configuration, data access, or enterprise API implementation. |
| [**sql-pro**](skills/sql-pro/SKILL.md) | Use when a task needs SQL query design, query review, schema-aware debugging, or database migration analysis. |
| [**swift-expert**](skills/swift-expert/SKILL.md) | Use when a task needs Swift expertise for iOS or macOS code, async flows, Apple platform APIs, or strongly typed application logic. |
| [**typescript-pro**](skills/typescript-pro/SKILL.md) | Use when a task needs strong TypeScript help for types, interfaces, refactors, or compiler-driven fixes. |
| [**vue-expert**](skills/vue-expert/SKILL.md) | Use when a task needs Vue expertise for component behavior, Composition API patterns, routing, or state and rendering issues. |

### 03. Infrastructure

| Skill | Description |
|-------|-------------|
| [**azure-infra-engineer**](skills/azure-infra-engineer/SKILL.md) | Use when a task needs Azure-specific infrastructure review or implementation across resources, networking, identity, or automation. |
| [**cloud-architect**](skills/cloud-architect/SKILL.md) | Use when a task needs cloud architecture review across compute, storage, networking, reliability, or multi-service design. |
| [**database-administrator**](skills/database-administrator/SKILL.md) | Use when a task needs operational database administration review for availability, backups, recovery, permissions, or runtime health. |
| [**deployment-engineer**](skills/deployment-engineer/SKILL.md) | Use when a task needs deployment workflow changes, release strategy updates, or rollout and rollback safety analysis. |
| [**devops-engineer**](skills/devops-engineer/SKILL.md) | Use when a task needs CI, deployment pipeline, release automation, or environment configuration work. |
| [**devops-incident-responder**](skills/devops-incident-responder/SKILL.md) | Use when a task needs rapid operational triage across CI, deployments, infrastructure automation, and service delivery failures. |
| [**docker-expert**](skills/docker-expert/SKILL.md) | Use when a task needs Dockerfile review, image optimization, multi-stage build fixes, or container runtime debugging. |
| [**incident-responder**](skills/incident-responder/SKILL.md) | Use when a task needs broad production incident triage, containment planning, or evidence-driven root cause analysis. |
| [**kubernetes-specialist**](skills/kubernetes-specialist/SKILL.md) | Use when a task needs Kubernetes manifest review, rollout safety analysis, or cluster workload debugging. |
| [**network-engineer**](skills/network-engineer/SKILL.md) | Use when a task needs network-path analysis, service connectivity debugging, load-balancer review, or infrastructure network design input. |
| [**platform-engineer**](skills/platform-engineer/SKILL.md) | Use when a task needs internal platform, golden-path, or self-service infrastructure design for developers. |
| [**security-engineer**](skills/security-engineer/SKILL.md) | Use when a task needs infrastructure and platform security engineering across IAM, secrets, network controls, or hardening work. |
| [**sre-engineer**](skills/sre-engineer/SKILL.md) | Use when a task needs reliability engineering work involving SLOs, alerting, error budgets, operational safety, or service resilience. |
| [**terraform-engineer**](skills/terraform-engineer/SKILL.md) | Use when a task needs Terraform module design, plan review, state-aware change analysis, or IaC refactoring. |
| [**terragrunt-expert**](skills/terragrunt-expert/SKILL.md) | Use when a task needs Terragrunt-specific help for module orchestration, environment layering, dependency wiring, or DRY infrastructure structure. |
| [**windows-infra-admin**](skills/windows-infra-admin/SKILL.md) | Use when a task needs Windows infrastructure administration across Active Directory, DNS, DHCP, GPO, or Windows automation. |

### 04. Quality Security

| Skill | Description |
|-------|-------------|
| [**accessibility-tester**](skills/accessibility-tester/SKILL.md) | Use when a task needs an accessibility audit of UI changes, interaction flows, or component behavior. |
| [**ad-security-reviewer**](skills/ad-security-reviewer/SKILL.md) | Use when a task needs Active Directory security review across identity boundaries, delegation, GPO exposure, or directory hardening. |
| [**architect-reviewer**](skills/architect-reviewer/SKILL.md) | Use when a task needs architectural review for coupling, system boundaries, long-term maintainability, or design coherence. |
| [**browser-debugger**](skills/browser-debugger/SKILL.md) | Use when a task needs browser-based reproduction, UI evidence gathering, or client-side debugging through a browser MCP server. |
| [**chaos-engineer**](skills/chaos-engineer/SKILL.md) | Use when a task needs resilience analysis for dependency failure, degraded modes, recovery behavior, or controlled fault-injection planning. |
| [**code-reviewer**](skills/code-reviewer/SKILL.md) | Use when a task needs a broader code-health review covering maintainability, design clarity, and risky implementation choices in addition to correctness. |
| [**compliance-auditor**](skills/compliance-auditor/SKILL.md) | Use when a task needs compliance-oriented review of controls, auditability, policy alignment, or evidence gaps in a regulated workflow. |
| [**debugger**](skills/debugger/SKILL.md) | Use when a task needs deep bug isolation across code paths, stack traces, runtime behavior, or failing tests. |
| [**error-detective**](skills/error-detective/SKILL.md) | Use when a task needs log, exception, or stack-trace analysis to identify the most probable failure source quickly. |
| [**penetration-tester**](skills/penetration-tester/SKILL.md) | Use when a task needs adversarial review of an application path for exploitability, abuse cases, or practical attack surface analysis. |
| [**performance-engineer**](skills/performance-engineer/SKILL.md) | Use when a task needs performance investigation for slow requests, hot paths, rendering regressions, or scalability bottlenecks. |
| [**powershell-security-hardening**](skills/powershell-security-hardening/SKILL.md) | Use when a task needs PowerShell-focused hardening across script safety, admin automation, execution controls, or Windows security posture. |
| [**qa-expert**](skills/qa-expert/SKILL.md) | Use when a task needs test strategy, acceptance coverage planning, or risk-based QA guidance for a feature or release. |
| [**reviewer**](skills/reviewer/SKILL.md) | Use when a task needs PR-style review focused on correctness, security, behavior regressions, and missing tests. |
| [**security-auditor**](skills/security-auditor/SKILL.md) | Use when a task needs focused security review of code, auth flows, secrets handling, input validation, or infrastructure configuration. |
| [**test-automator**](skills/test-automator/SKILL.md) | Use when a task needs implementation of automated tests, test harness improvements, or targeted regression coverage. |

### 05. Data Ai

| Skill | Description |
|-------|-------------|
| [**ai-engineer**](skills/ai-engineer/SKILL.md) | Use when a task needs implementation or debugging of model-backed application features, agent flows, or evaluation hooks. |
| [**data-analyst**](skills/data-analyst/SKILL.md) | Use when a task needs data interpretation, metric breakdown, trend explanation, or decision support from existing analytics outputs. |
| [**data-engineer**](skills/data-engineer/SKILL.md) | Use when a task needs ETL, ingestion, transformation, warehouse, or data-pipeline implementation and debugging. |
| [**data-scientist**](skills/data-scientist/SKILL.md) | Use when a task needs statistical reasoning, experiment interpretation, feature analysis, or model-oriented data exploration. |
| [**database-optimizer**](skills/database-optimizer/SKILL.md) | Use when a task needs database performance analysis for query plans, schema design, indexing, or data access patterns. |
| [**llm-architect**](skills/llm-architect/SKILL.md) | Use when a task needs architecture review for prompts, tool use, retrieval, evaluation, or multi-step LLM workflows. |
| [**machine-learning-engineer**](skills/machine-learning-engineer/SKILL.md) | Use when a task needs ML system implementation work across training pipelines, feature flow, model serving, or inference integration. |
| [**ml-engineer**](skills/ml-engineer/SKILL.md) | Use when a task needs practical machine learning implementation across feature engineering, inference wiring, and model-backed application logic. |
| [**mlops-engineer**](skills/mlops-engineer/SKILL.md) | Use when a task needs model deployment, registry, pipeline, monitoring, or environment orchestration for machine learning systems. |
| [**nlp-engineer**](skills/nlp-engineer/SKILL.md) | Use when a task needs NLP-specific implementation or analysis involving text processing, embeddings, ranking, or language-model-adjacent pipelines. |
| [**postgres-pro**](skills/postgres-pro/SKILL.md) | Use when a task needs PostgreSQL-specific expertise for schema design, performance behavior, locking, or operational database features. |
| [**prompt-engineer**](skills/prompt-engineer/SKILL.md) | Use when a task needs prompt revision, instruction design, eval-oriented prompt comparison, or prompt-output contract tightening. |

### 06. Developer Experience

| Skill | Description |
|-------|-------------|
| [**build-engineer**](skills/build-engineer/SKILL.md) | Use when a task needs build-graph debugging, bundling fixes, compiler pipeline work, or CI build stabilization. |
| [**cli-developer**](skills/cli-developer/SKILL.md) | Use when a task needs a command-line interface feature, UX review, argument parsing change, or shell-facing workflow improvement. |
| [**dependency-manager**](skills/dependency-manager/SKILL.md) | Use when a task needs dependency upgrades, package graph analysis, version-policy cleanup, or third-party library risk assessment. |
| [**documentation-engineer**](skills/documentation-engineer/SKILL.md) | Use when a task needs technical documentation that must stay faithful to current code, tooling, and operator workflows. |
| [**dx-optimizer**](skills/dx-optimizer/SKILL.md) | Use when a task needs developer-experience improvements in setup time, local workflows, feedback loops, or day-to-day tooling friction. |
| [**git-workflow-manager**](skills/git-workflow-manager/SKILL.md) | Use when a task needs help with branching strategy, merge flow, release branching, or repository collaboration conventions. |
| [**legacy-modernizer**](skills/legacy-modernizer/SKILL.md) | Use when a task needs a modernization path for older code, frameworks, or architecture without losing behavioral safety. |
| [**mcp-developer**](skills/mcp-developer/SKILL.md) | Use when a task needs work on MCP servers, MCP clients, tool wiring, or protocol-aware integrations. |
| [**powershell-module-architect**](skills/powershell-module-architect/SKILL.md) | Use when a task needs PowerShell module structure, command design, packaging, or profile architecture work. |
| [**powershell-ui-architect**](skills/powershell-ui-architect/SKILL.md) | Use when a task needs PowerShell-based UI work for terminals, forms, WPF, or admin-oriented interactive tooling. |
| [**refactoring-specialist**](skills/refactoring-specialist/SKILL.md) | Use when a task needs a low-risk structural refactor that preserves behavior while improving readability, modularity, or maintainability. |
| [**slack-expert**](skills/slack-expert/SKILL.md) | Use when a task needs Slack platform work involving bots, interactivity, events, workflows, or Slack-specific integration behavior. |
| [**tooling-engineer**](skills/tooling-engineer/SKILL.md) | Use when a task needs internal developer tooling, scripts, automation glue, or workflow support utilities. |

### 07. Specialized Domains

| Skill | Description |
|-------|-------------|
| [**api-documenter**](skills/api-documenter/SKILL.md) | Use when a task needs consumer-facing API documentation generated from the real implementation, schema, and examples. |
| [**blockchain-developer**](skills/blockchain-developer/SKILL.md) | Use when a task needs blockchain or Web3 implementation and review across smart-contract integration, wallet flows, or transaction lifecycle handling. |
| [**embedded-systems**](skills/embedded-systems/SKILL.md) | Use when a task needs embedded or hardware-adjacent work involving device constraints, firmware boundaries, timing, or low-level integration. |
| [**fintech-engineer**](skills/fintech-engineer/SKILL.md) | Use when a task needs financial systems engineering across ledgers, reconciliation, transfers, settlement, or compliance-sensitive transactional flows. |
| [**game-developer**](skills/game-developer/SKILL.md) | Use when a task needs game-specific implementation or debugging involving gameplay systems, rendering loops, asset flow, or player-state behavior. |
| [**iot-engineer**](skills/iot-engineer/SKILL.md) | Use when a task needs IoT system work involving devices, telemetry, edge communication, or cloud-device coordination. |
| [**m365-admin**](skills/m365-admin/SKILL.md) | Use when a task needs Microsoft 365 administration help across Exchange Online, Teams, SharePoint, identity, or tenant-level automation. |
| [**mobile-app-developer**](skills/mobile-app-developer/SKILL.md) | Use when a task needs app-level mobile product work across screens, state, API integration, and release-sensitive mobile behavior. |
| [**payment-integration**](skills/payment-integration/SKILL.md) | Use when a task needs payment-flow review or implementation for checkout, idempotency, webhooks, retries, or settlement state handling. |
| [**quant-analyst**](skills/quant-analyst/SKILL.md) | Use when a task needs quantitative analysis of models, strategies, simulations, or numeric decision logic. |
| [**risk-manager**](skills/risk-manager/SKILL.md) | Use when a task needs explicit risk analysis for product, operational, financial, or architectural decisions. |
| [**seo-specialist**](skills/seo-specialist/SKILL.md) | Use when a task needs search-focused technical review across crawlability, metadata, rendering, information architecture, or content discoverability. |

### 08. Business Product

| Skill | Description |
|-------|-------------|
| [**business-analyst**](skills/business-analyst/SKILL.md) | Use when a task needs requirements clarified, scope normalized, or acceptance criteria extracted from messy inputs before engineering work starts. |
| [**content-marketer**](skills/content-marketer/SKILL.md) | Use when a task needs product-adjacent content strategy or messaging that still has to stay grounded in real technical capabilities. |
| [**customer-success-manager**](skills/customer-success-manager/SKILL.md) | Use when a task needs support-pattern synthesis, adoption risk analysis, or customer-facing operational guidance from engineering context. |
| [**legal-advisor**](skills/legal-advisor/SKILL.md) | Use when a task needs legal-risk spotting in product or engineering behavior, especially around terms, data handling, or externally visible commitments. |
| [**product-manager**](skills/product-manager/SKILL.md) | Use when a task needs product framing, prioritization, or feature-shaping based on engineering reality and user impact. |
| [**project-manager**](skills/project-manager/SKILL.md) | Use when a task needs dependency mapping, milestone planning, sequencing, or delivery-risk coordination across multiple workstreams. |
| [**sales-engineer**](skills/sales-engineer/SKILL.md) | Use when a task needs technically accurate solution positioning, customer-question handling, or implementation tradeoff explanation for pre-sales contexts. |
| [**scrum-master**](skills/scrum-master/SKILL.md) | Use when a task needs process facilitation, iteration planning, or workflow friction analysis for an engineering team. |
| [**technical-writer**](skills/technical-writer/SKILL.md) | Use when a task needs release notes, migration notes, onboarding material, or developer-facing prose derived from real code changes. |
| [**ux-researcher**](skills/ux-researcher/SKILL.md) | Use when a task needs UI feedback synthesized into actionable product and implementation guidance. |
| [**wordpress-master**](skills/wordpress-master/SKILL.md) | Use when a task needs WordPress-specific implementation or debugging across themes, plugins, content architecture, or operational site behavior. |

### 09. Meta Orchestration

| Skill | Description |
|-------|-------------|
| [**agent-installer**](skills/agent-installer/SKILL.md) | Use when a task needs help selecting, copying, or organizing custom agent files from this repository into Codex agent directories. |
| [**agent-organizer**](skills/agent-organizer/SKILL.md) | Use when the parent agent needs help choosing subagents and dividing a larger task into clean delegated threads. |
| [**context-manager**](skills/context-manager/SKILL.md) | Use when a task needs a compact project context summary that other subagents can rely on before deeper work begins. |
| [**error-coordinator**](skills/error-coordinator/SKILL.md) | Use when multiple errors or symptoms need to be grouped, prioritized, and assigned to the right debugging or review agents. |
| [**it-ops-orchestrator**](skills/it-ops-orchestrator/SKILL.md) | Use when a task needs coordinated operational planning across infrastructure, incident response, identity, endpoint, and admin workflows. |
| [**knowledge-synthesizer**](skills/knowledge-synthesizer/SKILL.md) | Use when multiple agents have returned findings and the parent agent needs a distilled, non-redundant synthesis. |
| [**multi-agent-coordinator**](skills/multi-agent-coordinator/SKILL.md) | Use when a task needs a concrete multi-agent plan with clear role separation, dependencies, and result integration. |
| [**performance-monitor**](skills/performance-monitor/SKILL.md) | Use when a task needs ongoing performance-signal interpretation across build, runtime, or operational metrics before deeper optimization starts. |
| [**task-distributor**](skills/task-distributor/SKILL.md) | Use when a broad task needs to be broken into concrete sub-tasks with clear boundaries for multiple agents or contributors. |
| [**workflow-orchestrator**](skills/workflow-orchestrator/SKILL.md) | Use when the parent agent needs an explicit Codex subagent workflow for a complex task with multiple stages. |

### 10. Research Analysis

| Skill | Description |
|-------|-------------|
| [**competitive-analyst**](skills/competitive-analyst/SKILL.md) | Use when a task needs a grounded comparison of tools, products, libraries, or implementation options. |
| [**data-researcher**](skills/data-researcher/SKILL.md) | Use when a task needs source gathering and synthesis around datasets, metrics, data pipelines, or evidence-backed quantitative questions. |
| [**docs-researcher**](skills/docs-researcher/SKILL.md) | Use when a task needs documentation-backed verification of APIs, version-specific behavior, or framework options. |
| [**market-researcher**](skills/market-researcher/SKILL.md) | Use when a task needs market landscape, positioning, or demand-side research tied to a technical product or category. |
| [**research-analyst**](skills/research-analyst/SKILL.md) | Use when a task needs a structured investigation of a technical topic, implementation approach, or design question. |
| [**search-specialist**](skills/search-specialist/SKILL.md) | Use when a task needs fast, high-signal searching of the codebase or external sources before deeper analysis begins. |
| [**trend-analyst**](skills/trend-analyst/SKILL.md) | Use when a task needs trend synthesis across technology shifts, adoption patterns, or emerging implementation directions. |

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

This repository (`awesome-opencode-skills`) is strictly for automated porting and packaging for OpenCode. 
If you want to contribute new agents, improve definitions, or report logic bugs, please submit your PRs directly to the original repository:
👉 [VoltAgent/awesome-codex-subagents](https://github.com/VoltAgent/awesome-codex-subagents)

Once your contribution is merged upstream, GitHub Actions will automatically synchronize it here within a week!

## License

MIT License - see [LICENSE](LICENSE)

This repository is a curated collection of subagent definitions contributed by both the maintainers and the community. All subagents are provided "as is" without warranty. We do not audit or guarantee the security or correctness of any subagent. Review before use, the maintainers accept no liability for any issues arising from their use.

If you find an issue with a listed subagent or want your contribution removed, please open an issue in this repository and we'll address it promptly.
