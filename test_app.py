import dash
from app import app


def test_001_elements_present(dash_duo):
    dash_duo.start_server(app)

    dash_duo.wait_for_element("#header")
    dash_duo.wait_for_element("#graph")
    dash_duo.wait_for_element("#radio")

    assert dash_duo.find_element("#header").text == "Pink Morsel Sales", "Header should be present"
    assert dash_duo.find_element("#graph") is not None, "Graph should be present"
    assert dash_duo.find_element("#radio") is not None, "Radio should be present"