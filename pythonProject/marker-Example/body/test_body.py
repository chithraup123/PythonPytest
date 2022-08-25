from pytest import mark


@mark.body
class BodyTest:
    def test_body_functions_as_expected(self):
        assert True

    @staticmethod
    def test_bumper_functions_as_expected():
        assert True
