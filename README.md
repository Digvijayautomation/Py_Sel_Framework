## Selenium Webdriver, Python and Pytest

**Demo-Site** :(https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)

With 2 Sets of Data(Valid and Invalid)

### Setup instructions

1. Clone this repository.

2. Open project with Pycharm (suggested IDE).

3. Add a new interpreter with Virtualenv Environment (venv)

4. In Pycharm, open a new terminal and run  pip install -r requirements.txt

5. To run the framework use command:  pytest --html=reports/report.html

6. If we want to rerun only failed testcases automatically after the execution ends, we can use --reruns 2(number of time you want to run)

7. If we want to run the test cases in parallel we can use -n 4(On how many threads you want to run it on)

