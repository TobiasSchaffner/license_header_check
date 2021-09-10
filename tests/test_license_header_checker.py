import license_header_check.__main__ as lhc  # noqa: WPS301


def test_check_licenses():
    lhc.check_licenses("LICENSE", "license_header_check")
