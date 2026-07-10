from hsms_gateway.gem.client import GemClient


def test_create_gem_client():

    client = GemClient(
        "127.0.0.1",
        5001,
    )

    assert client is not None