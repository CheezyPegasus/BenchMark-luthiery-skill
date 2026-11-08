# Iteration

## What went wrong

In the early RG80F review, the task was to check a two-push-pull wiring plan with Voice 2 as the pushed-in default and Voice 3 available on the tone push-pull. The early reviewer flagged the mismatch with the diagram but left **Voice 3 with both volume settings** as `UNVERIFIED`.

> The Controls labels give the individual switch functions, but they don’t establish what happens on your installed revisions when both voice inputs are active.

## Diagnosis

The wiring drawing labels each switch’s purpose. Fishman’s separate install guide documents how the voice inputs interact. The early review treated two different questions together: which voice takes precedence according to the manufacturer, and whether that behavior has been verified on the installed hardware.

<!-- Add your own observation about why this gap mattered to your wiring plan. -->

## What changed

- `mcp_server/references/rg80f.json` gained a direct reference to the Fishman install guide’s **Connection Points & Functions** section.
- `.agents/skills/wiring-reviewer/SKILL.md` now asks the reviewer to consult the manufacturer’s connection or function guide for interacting controls and distinguish documented precedence from revision applicability and bench results.

## Later result

My Mac CLI smoke test reported that “grounding V3 selects single-coil mode and overrides V2.” It gave the four expected volume/tone states for the revised switch assignment. It still marked the installed PCB revisions and physical push-pull contacts as unverified.

The Mac smoke test used a shorter prompt than the early review. It shows the revised reviewer finding the rule. A rerun with the original prompt would give a direct comparison.

<!-- If you ran the original prompt again, add the actual result and compare it with the early excerpt. -->
