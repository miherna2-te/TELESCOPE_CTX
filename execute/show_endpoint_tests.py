from .execute_commands import ShowCommand


def show_endpoint_tests(token, format, filter, write):
    endpoint_tests = ShowCommand(token)
    show_endpoint_tests = endpoint_tests(
        "endpoint/tests/scheduled-tests", format, filter, write
    )
    return show_endpoint_tests
