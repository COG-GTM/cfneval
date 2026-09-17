import json
from behave import given
from cfn_flip import to_json
from cfneval import TemplateEvaluator


@given('the inline cfn template:')
@given('the inline cfn template')
def step_impl(context):
    context.evaluator = TemplateEvaluator()

    try:
        template = json.loads(to_json(context.text))
    except:
        template = json.loads(context.text)

    context.evaluator.set_template(template)