from pyisac import Main
from behave import *
from hamcrest import *

@given(u'the user runs pyisac from the command line')
def step_impl(context):
    context.Main = Main()

@when(u'no arguments are given')
def step_impl(context):
    pass
    #context.Main.run("")

@then(u'a banner should be shown')
def step_impl(context):
    pass
    #context.expected_banner = "Python InfraStructure As Code - Open Source"
    #assert_that(context.stdout_capture.getvalue(), contains_string(context.expected_banner))

@then(u'the GPL license should be shown')
def step_impl(context):
    pass
    #context.expected_license = "Released under the GPU v2 - http://www.gnu.org/licenses/old-licenses/gpl-2.0.html"
    #assert_that(context.stdout_capture.getvalue(), contains_string(context.expected_license))
