from src.evaluate import evaluate_cases, score_prompt, weighted_score

def test_structured_prompt_scores_higher_than_baseline():
    baseline = score_prompt("Summarize the text.")
    structured = score_prompt(
        "Summarize the text. Context: technical document. "
        "You must use at most 5 bullet points. Format: JSON. Example: input and output."
    )
    assert weighted_score(structured) > weighted_score(baseline)

def test_case_evaluation_is_reproducible():
    cases = [{
        "id": "demo",
        "variants": [
            {"name": "baseline", "prompt": "Answer the question."},
            {"name": "structured", "prompt": "Answer the question. Context: document. Must use JSON format."},
        ],
    }]
    first = evaluate_cases(cases)
    second = evaluate_cases(cases)
    assert first == second
    assert len(first) == 2
