# Targeted Lobbying on Council Networks

Final paper for 14.18 (Economics of Networks, MIT), Spring 2026.

## Overview

This paper studies a static game in which a single lobbyist allocates persuasion effort across the members of a voting council embedded in a social network. Council members influence one another's beliefs along network edges before casting votes, so the lobbyist's problem is to identify which members are worth targeting. The main result characterizes the optimal targeting strategy in terms of Katz-Bonacich centrality: under standard assumptions on the influence technology and the lobbyist's budget, the optimal effort allocation is proportional to each member's Katz-Bonacich centrality in the council graph. The model is solved in closed form and illustrated numerically.

## Repository Structure

```
.
├── paper/
│   ├── draft/          # Original LaTeX draft (main.tex, paper.tex, refs.bib)
│   └── final/          # Working copy for final submission
├── presentations/      # Final presentation PDF
├── resources/          # Proposal PDF and reference papers
├── src/
│   └── lobbying_research/   # Python package for model numerics
├── tests/              # pytest test suite
├── beamer_math_template/    # Beamer presentation template
├── lobbying-model-formalization.md  # Model formalization notes
├── pyproject.toml
└── uv.lock
```

## Quick Start

Install dependencies and run the test suite:

```bash
uv sync
pytest
```
