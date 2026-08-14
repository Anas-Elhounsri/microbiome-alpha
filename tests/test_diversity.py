from microbiome_alpha import shannon


def test_shannon_uniform():
    assert round(shannon([10, 10, 10, 10]), 6) == round(1.386294, 6)
