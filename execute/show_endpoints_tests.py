from .execute_commands import ShowCommand


def show_endpoints_tests(token, format, filter, write):
    endpoints_tests = ShowCommand(token)
    show_endpoints_tests = endpoints_tests(
        "endpoint/tests/scheduled-tests", format, filter, write
    )
    return show_endpoints_tests
