---------------------INSTRUCTIONS TO RUN THE TESTS-----------------------

STEPS:
1. Open command prompt or Terminal of the IDE/Editor at the location: "  \HybridALL\feature"
2. Execute the following command: pytest -v --html=report.html
    It will execute all the scripts starting with name "test_" and all the test case method inside it starting with "test_".
    It will also generate a report with the name "report.html" and will be saved in the same location.

Command to run the API tests        > pytest -v --html=report.html test_API.py (Not required in this project)
Command to run the UI tests         > pytest -v --html=report.html test_UI.py
Command to run all the tests        > pytest -v --html=report.html

QUESTION: If you were given more time to improve your solution what would you improve and why?
Answer: If given more time I would have tried implementing the same using more effective locators. As it would be faster and more efficient. 