from .execute_commands import ShowCommand


class ShowTests(ShowCommand):
    def __call__(self, resource, format, filter, write):
        if not write:
            return "This command only works with write argument"
        return super().__call__(resource, format, filter, write)


def show_tests(token, format, filter, write):
    tests = ShowTests(token)
    show_tests = tests("tests", format, filter, write)
    return show_tests
