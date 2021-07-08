pytest -v -s -n=2 testCases\test_Login.py --browser chrome  #run test parallel
pytest -v -s testCases\test_Login.py --browser chrome
pytest -v -s testCases\test_Login.

>pytest -v -s --html=Reports\reports.html testCases\test_DDTLogin.py --browser chrome  # run html report

pytest -v -s -n=2 --html=Reports\reports.html testCases\test_Login.py --browser chrome


