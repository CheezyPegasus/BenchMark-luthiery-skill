# BenchMark Wiring Reviewer

## What it does

`wiring-reviewer` checks a proposed guitar wiring plan against the relevant diagrams and documentation. I use it before soldering or changing a wiring layout. It reports findings as `MATCH`, `CONFLICT`, or `UNVERIFIED` and points out what I still need to check on the actual hardware.

The `get_wiring_case` MCP tool looks up two wiring projects.

- `rg80f` retrieves the Fishman Fluence Classic Open Core references for my Ibanez RG80F, including the two push-pull controls and the scope of the baseline rewiring.
- `steggy` retrieves the Free-Way 5B5-01 B004 Scheme B reference for my Strat and the pickup combinations for all ten switch positions.

## Why I built it

I’ve made some expensive wiring mistakes while working on my guitars. I wanted a way to catch mistakes before soldering so I could spend less time redoing work and stressing about frying another wire.

The Fishman pickup’s solder jumper is a good example of why I wanted the lookup. Fishman technical support explained that removing the jumper was relevant to the separate inner/outer coil-selection mod I was considering. For my initial two-push-pull setup, I wanted to leave the jumper alone. The case record gives the agent that context when it reviews the plan.

**Skill motivation from HW6.** I asked, “where is it currently located? and can we test something like "need to dye fretboard," and "doesn't affect inlays"” The combined query still surfaced a staining case. That’s why this checker evaluates each constraint separately and marks claims without enough evidence `UNVERIFIED`. [HW6 BenchMark prompt log](https://github.com/CheezyPegasus/BenchMark-luthiery/blob/main/prompt_log.md#fretboard-query-experiment)

**MCP motivation from HW7.** When the agent was helping me set up the Last Train handoff, I told the agent “current repository is still my 02-120 fork” after it kept giving setup steps for the wrong project. I wanted wiring reviews to start with the actual instrument’s context, so the MCP tool returns a named case with the matching hardware, diagrams, and scope. [HW7 Last Train prompt log](https://github.com/CheezyPegasus/last-train-phase2/blob/main/prompt_log.md#important-prompts-and-scope-verbatim)

## Setup and verification

The skill lives at `.agents/skills/wiring-reviewer/SKILL.md`. The MCP server lives at `mcp_server/server.py` and uses the Python MCP SDK. With Codex CLI and Python 3.10 or newer installed, run these commands from the project root.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r mcp_server/requirements.txt
codex mcp add benchmark-wiring -- "$PWD/.venv/bin/python" "$PWD/mcp_server/server.py"
codex mcp list
```

`$PWD` expands to the absolute path of your project folder. Launch `codex` from that same folder and invoke `$wiring-reviewer` in your prompt. To check the MCP connection, ask Codex to call `get_wiring_case` with `case_id` set to `rg80f` and look for the tool call in the trace.

I tested this on my Mac with **Codex CLI 0.167.0**. In my RG80F smoke test, the reviewer opened with **Before soldering** and flagged the conflict between the stock diagram’s pull-for-Voice-2 layout and my goal of Voice 2 with the volume pushed in. In my Steggy run, the terminal showed an actual `benchmark-wiring.get_wiring_case` call before Codex wrote the checklist.

See [the demonstration](DEMONSTRATION.md) for run evidence and [the iteration](ITERATION.md) for the Voice 3 precedence change.

## Sources and AI use

- Fishman’s Open Core Classic wiring diagram and install guide provide the wiring and voice-switching references. I also used guidance from Fishman technical support about the pickup solder jumper. [Wiring diagram](https://fishman.com/wp-content/uploads/2025/02/Fluence_Classic_Open_Core_1xVol_1xT_Toggle_Switch_9V.pdf) · [Install guide](https://fishman.com/wp-content/uploads/2025/02/Fluence-Open-Core-Install-Guide.pdf)
- Free-Way’s 5B5-01 schematics provide the B004 Scheme B wiring and switch-position chart on page 2. [Free-Way schematics](https://www.freewayswitch.com/app/download/8112261315/5B5-01+3PU+2Pot+Part1.pdf?t=1693907521#page=2)
- The reviewer’s soldering precautions draw on CMU Environmental Health and Safety’s guidance. [CMU soldering guidance](https://www.cmu.edu/ehs/Laboratory-Safety/chemical-safety/documents/ehs-guideline---soldering-safety.pdf)
- The MCP server uses FastMCP from the Python SDK. [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

I used ChatGPT and Codex to help build the skill and MCP server, organize the reference cases, troubleshoot setup, and revise this README. I supplied the wiring diagrams and project goals, ran the toolkit in Codex CLI on my Mac, and reviewed the output against the wiring I wanted.

The demonstration includes my HW8 prompt and output excerpts from the [RG80F smoke test](DEMONSTRATION.md#mac-cli-smoke-test) and the [Steggy tool call](DEMONSTRATION.md#mac-cli-working-session).
