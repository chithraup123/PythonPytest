from pytest import mark


@mark.ui
def test_can_navigate_to_swagLabs(edge_driver):
    edge_driver.get("https://www.amazon.com/")

