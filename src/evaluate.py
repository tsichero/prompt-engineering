from __future__ import annotations

import json
from pathlib import Path
from typing import Any

CRITERIA = {
    "task_clarity": 0.25,
    "context": 0.20,
    "constraints": 0.20,
    "output_format": 0.20,
    "examples": 0.15,
}

def score_prompt(prompt: str) -> dict[str, float]:
    """Score prompt structure with a deterministic static heuristic.

    This is not an LLM-as-judge. It measures explicit prompt-design signals
    so experiments remain reproducible without an external model/API.
    """
    text = prompt.lower()
    scores = {
        "task_clarity": 1.0 if any(k in text for k in ("summarize", "extract", "classify", "answer", "identify")) else 0.0,
        "context": 1.0 if any(k in text for k in ("context:", "background:", "document:", "text:")) else 0.0,
        "constraints": 1.0 if any(k in text for k in ("must", "do not", "limit", "only", "maximum")) else 0.0,
        "output_format": 1.0 if any(k in text for k in ("json", "bullet", "format", "schema", "fields")) else 0.0,
        "examples": 1.0 if any(k in text for k in ("example:", "examples:", "input:", "output:")) else 0.0,
    }
    return scores

def weighted_score(scores: dict[str, float]) -> float:
    return round(sum(scores[key] * weight for key, weight in CRITERIA.items()), 3)

def evaluate_cases(cases: list[dict[str, Any]]) -> list[dict[str, Any]]:
    results = []
    for case in cases:
        for variant in case["variants"]:
            dimension_scores = score_prompt(variant["prompt"])
            results.append({
                "case_id": case["id"],
                "variant": variant["name"],
                "dimension_scores": dimension_scores,
                "weighted_score": weighted_score(dimension_scores),
            })
    return results

def load_cases(path: str | Path) -> list[dict[str, Any]]:
    return json.loads(Path(path).read_text(encoding="utf-8"))

def main() -> None:
    root = Path(__file__).resolve().parents[1]
    cases = load_cases(root / "experiments" / "cases.json")
    results = evaluate_cases(cases)
    output = {
        "method": "deterministic_static_prompt_heuristic",
        "weights": CRITERIA,
        "cases": results,
        "limitations": [
            "Measures prompt structure, not model quality.",
            "Does not call an external LLM.",
            "Human or model-based evaluation should be added for semantic quality."
        ],
    }
    output_path = root / "output" / "evaluation.json"
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
