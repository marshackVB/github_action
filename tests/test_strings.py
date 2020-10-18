import pytest
from transformers.string_sim import token_set

@pytest.mark.parametrize("x, y, score", [("Hellop", "Hello", 91),
                                         ("This is a word", "word this is", 100)])
def test_TokenRemover_remove_tokens(x, y, score):
    sim_score = token_set(x, y)
    assert sim_score == score



