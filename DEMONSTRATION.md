# Demonstration

## Run 1 — RG80F Fishman wiring

The two push-pulls currently control the pickups’ voices separately. For the baseline I want one push-pull for master V1/V2 and the other for Voice 3. I want V2 with the volume pushed in. The mini-toggle stays bypassed for this pass. Global coil selection is a separate project.

### Development run

**Working agent.** Called `get_wiring_case` for `rg80f` over MCP stdio and drafted a wiring plan. Excerpt:

> Fishman's diagram shows pull for Voice 2, so confirm the alternate contact assignment on the actual pot before soldering.

**Separate checker agent.** Reviewed that plan and distinguished expected Voice 3 behavior from physical verification. It also flagged a gap in the plan’s test sequence:

> The proposal schedules continuity and all 12 functional combinations. Add explicit unpowered short, return-path and polarity checks before reconnecting.

### Mac CLI smoke test

My prompt:

> Use $wiring-reviewer and call `get_wiring_case` for `rg80f`. Review this plan: “I’ll copy the Fishman diagram as drawn to get Voice 2 with the volume pushed in.”

The reviewer reported:

> Copying the Fishman diagram as drawn conflicts with your goal: it selects Voice 2 when the volume is pulled, with the tone pushed in.

The reviewer also marked the pot contacts, pickup revisions, and selector terminals as unverified. This was one combined session on my Mac.

### My assessment

The status labels help me decide which findings I can trust and which ones I need to verify. I still need to check the physical pot, the existing wiring, and which contacts close in each push-pull position. My goal is to get V2 as the default voice instead of the standard PAF tone in V1 without damaging the circuit.

## Run 2 — Steggy Free-Way B004

The task was to check the ten positions on Steggy’s completed Free-Way 5B5-01 B004 rewiring, plus the master controls and the unused middle pot.

### Development run

**Working agent.** Called `get_wiring_case` for `steggy` over MCP stdio and drafted a wiring plan. Excerpt:

> Use the front view to make a ten-position check table and the reverse view to map solder terminals.

**Separate checker agent.** Reviewed that plan against B004, verified the expected position chart, and identified hardware checks still open. One finding was to “use continuity or resistance measurements with volume up to distinguish series from parallel.”

### Mac CLI working session

The tool trace showed:

```text
Called benchmark-wiring.get_wiring_case
    "10": "Middle + neck in series"
```

Codex then created `steggy-checklist.md`. It reported that the checklist covered both switch banks, the master volume and tone, and the unused middle pot, with measurements pending. The separate checker excerpt above is from the development plan. It predates this Mac checklist.

### My assessment

My November 6 bench notes say that “volume and tone has been tested, some variance in the tone of the instrument and everything seems to be working in order.” I’d already reassembled the guitar and was happy with how it worked. Those checks support the checklist’s master-control tests and tell me that the switch settings sound different. The checker’s suggestion to measure series versus parallel is useful because my notes don’t record that measurement for each position.
