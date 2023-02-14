"""
The main entry point. Invoke as `airdis' or `python -m airdis'.
"""

def main():
    try:
        from airdis.core import main
        exit_status = main()
    except KeyboardInterrupt:
        from airdis.status import ExitStatus
        exit_status = ExitStatus.ERROR_CTRL_C

    return exit_status.value


if __name__ == '__main__':  # pragma: nocover
    import sys
    sys.exit(main())
