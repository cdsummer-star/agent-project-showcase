from agent_showcase import CASES, build_overview


def test_cases_count():
    assert len(CASES) == 4


def test_overview_shape():
    overview = build_overview()
    assert len(overview) == 4
    assert overview[0]["key"]
