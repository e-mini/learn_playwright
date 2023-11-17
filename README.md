# Learn Playwright Automation Testing Tool

# Pre Requisites:

1. pytest
2. playwright
3. faker

Test Automation Framework

1. Test Runner - pytest
2. Automation Tool - playwright
3. Assertion Library - pyhamcrest

# Setup Instructions:

1. clone repo
2a. create python virtual environment `python -m venv venv`
2b. activate virtual environment `source venv/bin/activate`
3. install all python packages `python -m pip install -r requirements.txt`


# NOTES:

#### This is how a locator with action method looks like:
    # locator.action_method()

#### This is the template to follow for creating a test case:
    # setup (optional)
    # test itself
    # assertion
    # tear down -revert to orginal state (optional)
    