import nox
from nox_poetry import session

PYTHON_VERSIONS = ["3.6", "3.8", "3.9.7", "3.10.4"]
SPHINX_VERSIONS = ["4.1", "4.2", "4.3", "4.4", "4.5"]
TEST_DEPENDENCIES = [
    "pytest",
    "pytest-xdist",
    "pyparsing!=3.0.4",
]


def is_supported(python: str, sphinx: str) -> bool:
    return not (python in ["3.10.4"] and sphinx in ["4.1"])


def run_tests(session, sphinx):
    session.install(".")
    session.install(*TEST_DEPENDENCIES)
    session.run("pip", "install", f"sphinx=={sphinx}", silent=True)
    session.run("pip", "install", "-r", "docs/requirements.txt", silent=True)
    session.run("echo", "TEST FINAL PACKAGE LIST")
    session.run("pip", "freeze")
    session.run("make", "test", external=True)


@session(python=PYTHON_VERSIONS)
@nox.parametrize("sphinx", SPHINX_VERSIONS)
def tests(session, sphinx):
    if is_supported(session.python, sphinx):
        run_tests(session, sphinx)
    else:
        session.skip("unsupported combination")


@session(python="3.9")
def linkcheck(session):
    session.install(".")
    # LinkCheck cn handle rate limits since Sphinx 3.4, which is needed as
    # our doc has to many links to github.
    session.run("pip", "install", "sphinx==3.5.4", silent=True)

    session.run("pip", "install", "-r", "docs/requirements.txt", silent=True)
    session.run("make", "docs-linkcheck", external=True)
