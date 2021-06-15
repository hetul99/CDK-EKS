#!/usr/bin/env python3

from aws_cdk import core

from cdkeks.cdkeks_stack import CdkeksStack
from cdkeks.pipeline_stack import PipelineStack

app = core.App()
#CdkeksStack(app, "cdkeks")
PipelineStack(app, 'PipelineStack', env={
    'account': '128222158613',
    'region': 'us-west-2',
})
app.synth()
