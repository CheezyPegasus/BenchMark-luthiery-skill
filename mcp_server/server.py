"""Read-only MCP lookup for curated BenchMark wiring cases."""

import json
from pathlib import Path

from mcp.server.fastmcp import FastMCP

CASES = Path(__file__).resolve().parent / "references"
CASE_FILES = {
    "rg80f": CASES / "rg80f.json",
    "steggy": CASES / "steggy.json",
}

mcp = FastMCP("benchmark-wiring")


@mcp.tool()
def get_wiring_case(case_id: str) -> dict:
    """Retrieve sources, control goals, and source limitations for a wiring case.

    Use rg80f for Fishman Fluence Open Core Classic 8-string wiring with
    two push-pulls, or steggy for Free-Way 5B5-01 B004 Scheme B 1V/1T.
    """
    case_id = case_id.strip().lower()
    if case_id not in CASE_FILES:
        return {"error": "Unknown case ID.", "available_cases": sorted(CASE_FILES)}

    return json.loads(CASE_FILES[case_id].read_text(encoding="utf-8"))


if __name__ == "__main__":
    mcp.run(transport="stdio")
