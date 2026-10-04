# Awesome Agent Security [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Curated list of AI agent security tools, papers and datasets: runtime controls, sandboxes, scanners for MCP servers and skills, static analysis, red teaming, incident records, threat models and standards.

An AI agent is a model that can read untrusted content and call tools with real privileges. Securing one means controlling what it may touch, isolating what it runs, scanning what it loads, and measuring how it fails. Every entry below exists on GitHub and is maintained; descriptions are the projects' own words, shortened. Maintained by [Muhammad Basit Ali](https://github.com/basitalisandhu); projects by the maintainer are listed in their sections like any other entry. See [contributing.md](contributing.md) for the inclusion criteria.

## Contents

- [Runtime controls and authorization](#runtime-controls-and-authorization)
- [Sandboxes](#sandboxes)
- [Scanners for MCP servers and skills](#scanners-for-mcp-servers-and-skills)
- [Static analysis](#static-analysis)
- [Red teaming and evaluation](#red-teaming-and-evaluation)
- [Datasets and incident records](#datasets-and-incident-records)
- [Threat modelling and taxonomies](#threat-modelling-and-taxonomies)
- [Standards and guidance](#standards-and-guidance)
- [Papers](#papers)
- [Talks](#talks)
- [Related lists](#related-lists)
- [Contributing](#contributing)
- [Sibling projects](#sibling-projects)

## Runtime controls and authorization

Brokers, gateways, policy engines and guardrails that sit between an agent and the tools, credentials and data it uses.

- [Masoon Broker](https://basitalisandhu.github.io/masoon/masoon-broker.html) - Scoped, short-lived credentials for AI agents with human approvals, a kill switch and a tamper-evident audit log.
- [llm-agent-control-plane](https://github.com/basitalisandhu/llm-agent-control-plane) - Deterministic policy enforcement point for LLM agents with provenance and approval rules, evaluated on AgentDojo.
- [jentic-one](https://github.com/jentic/jentic-one) - Self-hosted execution layer that connects agents to APIs, scopes what they can touch and keeps credentials out of the agent's hands.
- [hermes-vault](https://github.com/asimons81/hermes-vault) - Local-first credential broker, scanner and encrypted vault for the Hermes agent.
- [ADR](https://github.com/uber/ADR) - Observability, security benchmarking and threat detection for enterprise AI agents, from Uber.
- [invariant](https://github.com/invariantlabs-ai/invariant) - Guardrails and policy rules for agent tool calls and traces.
- [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) - Toolkit for adding programmable guardrails to LLM-based conversational systems.
- [Guardrails](https://github.com/guardrails-ai/guardrails) - Framework for input and output validators around LLM calls.
- [OpenAI Guardrails](https://github.com/openai/openai-guardrails-python) - Python guardrails library from OpenAI.
- [PurpleLlama](https://github.com/meta-llama/PurpleLlama) - Meta's tools for assessing and improving LLM security, including Prompt Guard, Llama Guard, LlamaFirewall and CyberSecEval.
- [DefenseClaw](https://github.com/cisco-ai-defense/defenseclaw) - Security governance for agentic AI, from Cisco AI Defense.
- [mcp-gateway](https://github.com/lasso-security/mcp-gateway) - Plugin-based gateway that proxies other MCP servers and adds security plugins.
- [mcp-guardian](https://github.com/eqtylab/mcp-guardian) - Manage, proxy and secure MCP servers with message approval and logging.
- [agentgateway](https://github.com/agentgateway/agentgateway) - Proxy for AI agents and MCP servers with policy, observability and multiplexing.
- [Docker MCP Gateway](https://github.com/docker/mcp-gateway) - Docker's MCP gateway and `docker mcp` CLI plugin for running servers in containers.
- [ToolHive](https://github.com/stacklok/toolhive) - Platform for running and managing MCP servers with isolation and policy, including a Kubernetes operator.
- [mcp-context-protector](https://github.com/trailofbits/mcp-context-protector) - Security wrapper for MCP servers from Trail of Bits that pins tool descriptions and guards context.
- [Vigil](https://github.com/deadbits/vigil-llm) - Detects prompt injections, jailbreaks and other risky LLM inputs with YARA rules and models.

## Sandboxes

Isolation for the code and processes an agent runs.

- [nono](https://github.com/nolabs-ai/nono) - Micro-sandboxes for agent runtimes with zero setup and zero latency.
- [Wassette](https://github.com/microsoft/wassette) - Security-oriented runtime that runs WebAssembly components via MCP with capability-based permissions.
- [onecli](https://github.com/onecli/onecli) - Sandboxed agent harness for teams with built-in secret management.
- [sandbox-runtime](https://github.com/anthropics/sandbox-runtime) - OS-level filesystem and network restrictions for arbitrary processes without a container.
- [E2B](https://github.com/e2b-dev/E2B) - Secure sandboxed environments for running agent-generated code.
- [microsandbox](https://github.com/superradcompany/microsandbox) - Local-first microVM runtime and library for untrusted code.
- [Firecracker](https://github.com/firecracker-microvm/firecracker) - MicroVMs for serverless workloads, used underneath several agent sandboxes.
- [gVisor](https://github.com/google/gvisor) - Application kernel that isolates containers from the host kernel.
- [bubblewrap](https://github.com/containers/bubblewrap) - Low-level unprivileged sandboxing tool used by Flatpak and agent runtimes.
- [nsjail](https://github.com/google/nsjail) - Process isolation with Linux namespaces, cgroups, rlimits and seccomp-bpf filters.

## Scanners for MCP servers and skills

Tools that inspect MCP servers, agent skills, plugins and configuration before an agent loads them.

- [SkillSpector](https://github.com/NVIDIA/SkillSpector) - Scanner for agent skills that detects prompt injection, data exfiltration and supply-chain risks before installation.
- [skill-scanner](https://github.com/cisco-ai-defense/skill-scanner) - Security scanner for agent skills from Cisco AI Defense.
- [agent-scan](https://github.com/snyk/agent-scan) - Security scanner for AI agents, MCP servers and agent skills, maintained by Snyk.
- [mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner) - Scans MCP servers for threats and security findings.
- [a2a-scanner](https://github.com/cisco-ai-defense/a2a-scanner) - Scans agents that speak the A2A protocol for threats and security issues.
- [agentshield](https://github.com/affaan-m/agentshield) - Scanner for agent configurations, MCP servers and tool permissions, available as a CLI, GitHub Action and GitHub App.
- [AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) - Red teaming platform with agent, skill, MCP and infrastructure scans and jailbreak evaluation.
- [mcp-shield](https://github.com/riseandignite/mcp-shield) - Security scanner for MCP servers.
- [MCPSafetyScanner](https://github.com/johnhalloran321/mcpSafetyScanner) - Agent-driven MCP safety auditing and remediation, with an accompanying paper.
- [agent-config-audit](https://github.com/basitalisandhu/agent-config-audit) - Audits agent configuration files (Claude Code settings, `.mcp.json`, Cursor rules, hooks, plugins) for risky permissions, secrets, unpinned servers and prompt injection.
- [agent-security-skills](https://github.com/basitalisandhu/agent-security-skills) - Claude Code plugin and skill pack for agent security reviews: threat modelling, config audits, MCP server review and incident lookup.

## Static analysis

Rules and analysers that find insecure agent code and workflows before they run.

- [agentic-semgrep-rules](https://github.com/basitalisandhu/agentic-semgrep-rules) - Semgrep rule pack for agent code in Python, TypeScript and JavaScript: model output reaching shells, SQL, URLs and files, over-broad tools, MCP servers without auth, leaked keys.
- [agentic-radar](https://github.com/splx-ai/agentic-radar) - Security scanner that maps agentic workflows and reports their weaknesses.
- [Semgrep](https://github.com/semgrep/semgrep) - Static analysis engine the rule packs above run on.
- [Gitleaks](https://github.com/gitleaks/gitleaks) - Secret scanner for repositories, files and agent configuration.
- [aibom](https://github.com/cisco-ai-defense/aibom) - Generates an AI bill of materials by scanning source code.

## Red teaming and evaluation

Attack frameworks, benchmarks and vulnerable targets for measuring how an agent fails.

- [garak](https://github.com/NVIDIA/garak) - LLM vulnerability scanner with probes for injection, leakage and jailbreaks.
- [PyRIT](https://github.com/microsoft/PyRIT) - Python Risk Identification Tool for red teaming generative AI systems.
- [promptfoo](https://github.com/promptfoo/promptfoo) - Tests and red-teams prompts, agents and RAG pipelines with declarative configs and CI integration.
- [DeepTeam](https://github.com/confident-ai/deepteam) - Framework for red teaming LLMs and AI agents.
- [Giskard](https://github.com/Giskard-AI/giskard-oss) - Evaluation and testing library for LLM agents.
- [AgentDojo](https://github.com/ethz-spylab/agentdojo) - Dynamic environment to evaluate prompt injection attacks and defences for LLM agents.
- [InjecAgent](https://github.com/uiuc-kang-lab/InjecAgent) - Benchmark for indirect prompt injection in tool-integrated agents.
- [Agent Security Bench](https://github.com/agiresearch/ASB) - Benchmark of attacks and defences for LLM-based agents.
- [Agent-SafetyBench](https://github.com/thu-coai/Agent-SafetyBench) - Safety benchmark for LLM agents across risk categories and environments.
- [SafeArena](https://github.com/McGill-NLP/safearena) - Benchmark for assessing the harmful capabilities of web agents.
- [inspect_evals](https://github.com/UKGovernmentBEIS/inspect_evals) - Collection of evaluations for the Inspect framework, including agent safety tasks such as AgentHarm.
- [HarmBench](https://github.com/centerforaisafety/HarmBench) - Evaluation framework for automated red teaming and robust refusal.
- [JailbreakBench](https://github.com/JailbreakBench/jailbreakbench) - Open robustness benchmark for jailbreaking language models.
- [Cybench](https://github.com/andyzorigin/cybench) - Capture-the-flag tasks for evaluating the cybersecurity capabilities and risks of agents.
- [agentshield-benchmark](https://github.com/doronp/agentshield-benchmark) - Open benchmark for agent security tools covering prompt injection, exfiltration, tool abuse and provenance.
- [mcp-injection-experiments](https://github.com/invariantlabs-ai/mcp-injection-experiments) - Code to reproduce MCP tool poisoning attacks.
- [Damn Vulnerable MCP Server](https://github.com/harishsg993010/damn-vulnerable-MCP-server) - Deliberately vulnerable MCP server for learning and testing scanners.

### Offensive security agents and skills

Agents that use models to find vulnerabilities; useful as targets and as references for how tool-using agents are built and constrained.

- [Strix](https://github.com/usestrix/strix) - AI penetration testing agent that finds and fixes application vulnerabilities.
- [Shannon](https://github.com/KeygraphHQ/shannon) - AI pentester for web applications and APIs that analyses source code and executes exploits to prove findings.
- [pentest-ai](https://github.com/0xSteph/pentest-ai) - AI pentester that re-runs each exploit and ships a replayable proof for every finding.
- [open-kritt](https://github.com/Kritt-ai/open-kritt) - Self-hosted vulnerability research tool that orchestrates agents to find and validate issues in code.
- [AutoCVE](https://github.com/larlarua/AutoCVE) - Agent-driven platform for source code auditing, vulnerability verification and report generation.
- [Pentest-Swarm-AI](https://github.com/Armur-Ai/Pentest-Swarm-AI) - Autonomous penetration testing with a swarm of specialised agents.
- [Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) - Structured cybersecurity skills for agents, mapped to MITRE ATT&CK, NIST CSF, MITRE ATLAS and D3FEND.

## Datasets and incident records

Structured records of attacks, incidents and vulnerabilities.

- [ai-agent-incidents](https://github.com/basitalisandhu/ai-agent-incidents) - Open dataset of publicly documented AI agent security incidents, mapped to OWASP and MITRE ATLAS, with a browsable site and RSS feed.
- [AI Incident Database](https://github.com/responsible-ai-collaborative/aiid) - Source of the AI Incident Database, which catalogues harms caused by AI systems.
- [AVID](https://github.com/avidml/avid-db) - AI Vulnerability Database of reported model and system vulnerabilities.
- [tensor-trust-data](https://github.com/HumanCompatibleAI/tensor-trust-data) - Prompt injection attacks and defences collected through the Tensor Trust game.
- [jailbreak_llms](https://github.com/verazuo/jailbreak_llms) - Dataset of in-the-wild prompts, including jailbreak prompts, from Reddit, Discord and websites.
- [prompt-injections](https://github.com/Giskard-AI/prompt-injections) - Collection of prompt injections used by the Giskard scan.
- [prompt-injection-defenses](https://github.com/tldrsec/prompt-injection-defenses) - Catalogue of practical and proposed defences against prompt injection.

## Threat modelling and taxonomies

Ways to describe an agent system and enumerate what can go wrong.

- [agent-threat-model](https://github.com/basitalisandhu/agent-threat-model) - Describe an agent architecture in YAML and get a STRIDE and OWASP Agentic threat model with a control checklist, diagram and SARIF.
- [Agent-Wiz](https://github.com/Repello-AI/Agent-Wiz) - CLI for threat modelling and visualising agents built with LangGraph, AutoGen, CrewAI and other frameworks.
- [crosswalk](https://github.com/GenAI-Security-Project/crosswalk) - Cross-reference between the OWASP GenAI Security Project documents and other security frameworks.
- [asi](https://github.com/vineethsai/asi) - Threat models, verification standards and controls for agent architectures built on OWASP AISVS and NIST AI RMF.

## Standards and guidance

Published frameworks and specifications that agent security work maps to. GitHub repositories are linked so every entry can be checked.

- [OWASP Top 10 for LLM Applications](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications) - The OWASP GenAI Security Project's Top 10 for LLM applications and related agentic guidance.
- [OWASP Agentic Skills Top 10](https://github.com/OWASP/www-project-agentic-skills-top-10) - OWASP project on the top risks of agent skills.
- [OWASP AI Exchange](https://github.com/OWASP/www-project-ai-security-and-privacy-guide) - OWASP's AI security and privacy guide with controls and threat coverage.
- [OWASP Machine Learning Security Top 10](https://github.com/OWASP/www-project-machine-learning-security-top-10) - OWASP's top ten security issues for machine learning systems.
- [MITRE ATLAS data](https://github.com/mitre-atlas/atlas-data) - Tactics, techniques and case studies of the MITRE ATLAS knowledge base in machine-readable form.
- [Dioptra](https://github.com/usnistgov/dioptra) - NIST's test platform for characterising AI technologies, companion to the NIST AI Risk Management Framework.
- [Model Context Protocol](https://github.com/modelcontextprotocol/modelcontextprotocol) - The MCP specification, including its authorization and security best practices documents.

## Papers

Research with code. Each entry links to the paper's official repository.

- [llm-security](https://github.com/greshake/llm-security) - Code and demonstrations for "Not what you've signed up for", the paper that introduced indirect prompt injection against application-integrated LLMs.
- [llm-attacks](https://github.com/llm-attacks/llm-attacks) - Code for "Universal and Transferable Adversarial Attacks on Aligned Language Models".
- [camel-prompt-injection](https://github.com/google-research/camel-prompt-injection) - Code for "Defeating Prompt Injections by Design", which separates control and data flows around the model.
- [SecAlign](https://github.com/facebookresearch/SecAlign) - Code for "SecAlign: Defending Against Prompt Injection with Preference Optimization".
- [StruQ](https://github.com/Sizhe-Chen/StruQ) - Code for "StruQ: Defending Against Prompt Injection with Structured Queries" (USENIX Security 2025).
- [ToolEmu](https://github.com/ryoungj/ToolEmu) - Emulation framework for identifying the risks of tool-using agents (ICLR 2024).
- [R-Judge](https://github.com/Lordog/R-Judge) - Benchmark for safety risk awareness of LLM agents (EMNLP Findings 2024).

## Talks

Talk and workshop material that is published in a repository. Recordings are added only when a public page for the talk can be verified; please propose them with a link.

- [AI Village workshops](https://github.com/aivillage/workshops) - Workshop materials published by the AI Village, the DEF CON village for AI security.
- [llm_verification](https://github.com/aivillage/llm_verification) - CTFd plugin from the AI Village for running LLM prompt attack challenges at hacker CTFs.

## Related lists

- [awesome-llm-security](https://github.com/corca-ai/awesome-llm-security) - Tools, documents and projects about LLM security.
- [awesome-mcp-security](https://github.com/Puliczek/awesome-mcp-security) - Security research, writeups and tools for the Model Context Protocol.
- [awesome-ai-safety](https://github.com/Giskard-AI/awesome-ai-safety) - Papers and articles on AI quality and safety.
- [awesome-blackhat-arsenal](https://github.com/elbraino/awesome-blackhat-arsenal) - Security tools featured at Black Hat Arsenal events.

## Contributing

See [contributing.md](contributing.md). Every entry must be a public, maintained project with documentation and a one-line description in the project's own words; archived and unmaintained projects are removed. Run `python3 scripts/check_links.py` before opening a pull request.

## Sibling projects

This list is maintained alongside [Masoon](https://github.com/basitalisandhu/masoon), open-source trust infrastructure for AI agents.
