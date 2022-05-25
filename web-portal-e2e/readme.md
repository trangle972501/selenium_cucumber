# Fiber-digitalization-frontend web portal tests

This folder contains the end to end test code that automatically tests the web portal. This document explains
how to run the tests, and how the code is organized.

## Pre-Requisites

Before running the tests, you need to have the following installed:

- Python 3
- The packages `behave`, `selenium`
- The Firefox webdriver (`Geckodriver`)

## How to run

The steps to run the tests:

1. Start the web-portal and the user-authentication
2. Open a terminal in this folder
3. Run `behave`

## Folder structure

The rood directory contains the feature files, as well as the `environment.py` file. The step
definitions can be found in the `steps` subdirectory.

### File clarification

The `environment.py` file contains all environment, set-up and teardown code used by behave.
Each feature file has a corresponding python file in the `steps` subdirectory that implements the tests.


============ Latest update =================

Install Python 3.10.4 and Pip
Install dependencies: pip install -r requirement.txt

Add PYTHON_HOME env
Add %PYTHON_HOME%\Lib; %PYTHON_HOME%; %PYTHON_HOME%\Scripts to Path
Import project File -> Open Projects From File System

== Run scripts ====

Run debug by vscode: Ctrl+ Shift+ D
Run by command line:
behave ./tests/features/login/login.feature

Run code to get allure report

behave -f allure_behave.formatter::AllureFormatter -o reports/ tests/features/login/login.feature

Generate allure report
 npm install -g allure-commandline --save-dev
 allure serve reports/  

