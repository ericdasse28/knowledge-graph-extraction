import pytest
from knowledge_extraction import get_entity_pairs


@pytest.mark.parametrize(
    "sentence, entities",
    [
        ("Santa gives presents", ("Santa", "presents")),
        ("Yusei loves Akiza", ("Yusei", "Akiza")),
        ("Micheal plays basketball", ("Micheal", "basketball")),
    ],
)
def test_can_extract_entity_pairs_from_a_sentence(sentence, entities):
    sentence = sentence

    extracted_entity_pairs = get_entity_pairs(sentence)

    assert extracted_entity_pairs == entities
