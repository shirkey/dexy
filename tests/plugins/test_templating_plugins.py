import inspect

from dexy.doc import Doc
from dexy.filters.templating import TemplateFilter
from dexy.filters.templating_plugins import TemplatePlugin
from tests.utils import run_templating_plugin as run
from tests.utils import wrap
import dexy.filters.templating_plugins as plugin
import os


def test_base():
    run(TemplatePlugin)


def test_ppjson():
    with run(plugin.PrettyPrintJson) as env:
        assert 'ppjson' in env
        assert hasattr(env['ppjson'][1], '__call__')


def test_python_datetime():
    with run(plugin.PythonDatetime) as env:
        assert inspect.ismodule(env['cal'][1])


def test_dexy_version():
    with run(plugin.DexyVersion) as env:
        assert env['DEXY_VERSION'][1]


def test_simple_json():
    with run(plugin.SimpleJson) as env:
        assert inspect.ismodule(env['json'][1])


def test_python_builtins():
    with run(plugin.PythonBuiltins) as env:
        assert 'hasattr' in env


def test_pygments():
    with run(plugin.PygmentsStylesheet) as env:
        assert 'pastie.tex' in env['pygments'][1].keys()
        assert 'pastie.css' in env['pygments'][1].keys()
        assert 'pastie.html' in env['pygments'][1].keys()


class TestSubdirectory(TemplateFilter):
    """
    test subdir
    """
    aliases = ['testsubdir']
    _settings = {'plugins': ['subdirectories']}


def test_subdirectories():
    with wrap() as wrapper:
        os.makedirs("s1")
        os.makedirs("s2")

        node = Doc("file.txt|testsubdir",
                   wrapper,
            [],
                   contents="hello"
        )

        wrapper.run_docs(node)

        env = node.filters[-1].run_plugins()
        assert 's1' in env['subdirectories'][1]
        assert 's2' in env['subdirectories'][1]


class TestVariables(TemplateFilter):
    """
    test variables
    """
    aliases = ['testvars']
    _settings = {'plugins': ['variables']}


def test_variables():
    with wrap() as wrapper:
        node = Doc("hello.txt|testvars",
                   wrapper,
            [],
                   contents="hello",
                   testvars={"variables": {"foo": "bar", "x": 123.4}}
        )

        wrapper.run_docs(node)

        env = node.filters[-1].run_plugins()
        assert env['foo'][1] == 'bar'
        assert env['x'][1] == 123.4


class TestGlobals(TemplateFilter):
    """
    test globals
    """
    aliases = ['testglobals']
    _settings = {'plugins': ['globals']}


def test_globals():
    with wrap() as wrapper:
        wrapper.globals = "foo=bar"
        node = Doc("hello.txt|testglobals",
                   wrapper,
            [],
                   contents="hello"
        )

        wrapper.run_docs(node)
        env = node.filters[-1].run_plugins()
        assert env['foo'][1] == 'bar'
