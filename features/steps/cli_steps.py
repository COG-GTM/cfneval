import os
import tempfile
from behave import given, then, when
from click.testing import CliRunner
from cfneval.cli import cli


@given('a template file named "{name}"')
def step_impl(context, name):
    context.template_dir = tempfile.mkdtemp()
    context.template_path = os.path.join(context.template_dir, name)
    with open(context.template_path, "w") as f:
        f.write(context.text)


@when("I run the cfneval cli")
def step_impl(context):
    context.cli_result = CliRunner().invoke(cli, ["-t", context.template_path])
    assert context.cli_result.exit_code == 0, context.cli_result.output


@then('the cli output is "{fmt}"')
def step_impl(context, fmt):
    output = context.cli_result.output.strip()
    if fmt == "json":
        assert output.startswith("{"), output
    else:
        assert not output.startswith("{"), output


@then('the cli output contains "{text}"')
def step_impl(context, text):
    assert text in context.cli_result.output, context.cli_result.output
