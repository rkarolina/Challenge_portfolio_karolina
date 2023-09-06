# Navigation

* [Introduction](#introduction)
* [Tools](#tools)
* [Technologies](#technologies)
* [Tasks](#tasks)
  - [Configuration](#configuration)
  - [Selectors](#selectors)
  - [Scenarios](#scenarios)
  - [Robotframework](#robotframework)
  - [Bugs](#bugs)
  - [Report](#report)
* [Portfolio](#portfolio)


<a name='introduction'></a>
## Introduction

It's an application which enables gathering info about players by football scouts (contact details, current club, main and second position, achievements etc.)

Features:

- [x] creating player's profiles
- [x] adding matches and results
- [x] reports <p>

Project performed as part of the Dare IT Challenge on the QA track: Introduction to Automated Testing. 💪
<br/>First, based on my previous experience, I did exploratory testing to learn about the application, then I've created a test plan and test scenarios/cases.
<br/>Finally, they were implemented in test automation.
<br/>At the end test cases were executed and after that I've collected bugs list and created overall report.

<a name='tools'></a>
## Tools

<img alt="Pycharm" src="https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white"/> <img alt="Github" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"/> 
<a name='technologies'></a>

## Technologies

<img alt="Python" src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/> <img alt="Selenium" src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white"/>
<a name='tasks'></a>

## Tasks
<a name='configuration'></a>

### Configuration

- [x] Preparing tools for the challenge. 
- [x] Cloning a repository.
- [x] Creating README file in Markdown
- [x] Adding a code to the repository
- [x] Committing and pushing changes to the Github 
<a name='selectors'></a>
### Selectors

<a name='selectors'></a>
<details>
<summary>Login page</summary>

Examples of selectors found on [Scouts Panel login page](https://scouts-test.futbolkolektyw.pl/) <br/>

**Please note that these selectors were only for training purposes, only some of them were used in the project [direct link to the page](https://github.com/rkarolina/Challenge_portfolio_karolina/blob/main/pages/login_page.py)<br/>**
_Scouts Panel string_

1. Attribute selector (id)<br/>
```
   //*[@id="__next"]/form/div/div[1]/h5
```
2. Attribute selector (class) <br/>
```
   //*[contains(@class, "gutterBottom")]
```
3. Text match <br/>
```
   //*[text()="Scouts Panel"]
```

_Login input field_

1. Attribute selector (id) <br/>
```
//*[@id="login"]
```
2. Attribute selector (class) and (id)<br/>
```
//*[@class="MuiInputBase-input MuiInput-input"][@id="login"]
```
3. Attribute selector (input) <br/>
```
//input[@type="text"]<br/>
input[id="login"]
```

_Password input field_

1. Attribute selector (id) <br/>
```
   //*[@id="password"]
```
2. Attribute selector (input) <br/>
```
   //input[@type="password"]
   input[id="password"]
```
3. Attribute selector (class) and (id) br/>
```
   //*[@class="MuiInputBase-input MuiInput-input"][@id="password"]
```

_Remind Password option_

1. Attribute selector (id)<br/>
```
   //*[@id="__next"]/form/div/div[1]/a
```
2. Attribute selector (class) <br/>
```
   //*[contains(@class, "colorPrimary")]
```
3. Other selectors (last) <br/>
```
   //*[last()][name()="a"]
```

_Displayed language option_

1. Attribute selector (id) <br/>

```
   //*[@id="__next"]/form/div/div[2]/div
```
2. Text match <br/>
```
   //*[text()="English" or text()="Polski"]
```
3. Attribute selector (class)<br/>
```
   //*[starts-with(@class, "MuiSelect-root MuiSelect-select")]
```

_Language change option (dropdown)_

1. Attribute selector (class)<br/>
```
   //*[@class= "MuiSelect-nativeInput"]
```
2. Attribute selector (id) br/>
```
   //*[@id="__next"]/form/div/div[2]/div/input
```
3. Attribute selector (input)<br/>
```
   input[class= "MuiSelect-nativeInput"]<br/>
   input[value= "pl"]
```
_Sign in/Zaloguj button_

1. Attribute selector (id)<br/>
```
//*[@id="__next"]/form/div/div[2]/button/span[1]
```
2. Attribute selector (class)<br/>
```
//*[@class="MuiButton-label"]
```
3. Button<br/>
```
//button
```
</details>
<details>
<summary>Players page</summary>

Direct link to the [Players page](https://github.com/rkarolina/Challenge_portfolio_karolina/blob/main/pages/players.py) with selectors and methods.

</details>

<details>
<summary>Main page</summary>

Direct link to the [Dasboard page](https://github.com/rkarolina/Challenge_portfolio_karolina/blob/main/pages/dashboard.py) with selectors and methods.
</details>

<details>
<summary>Matches page</summary>

Direct link to the [Matches page](https://github.com/rkarolina/Challenge_portfolio_karolina/blob/main/pages/matches.py) with selectors and methods.
</details>

<details>
<summary>Add match page</summary>

Direct link to the [Add match page](https://github.com/rkarolina/Challenge_portfolio_karolina/blob/main/pages/add_match.py) with selectors and methods.
</details>

<details>
<summary>Add player page</summary>

Direct link to the [Add player page](https://github.com/rkarolina/Challenge_portfolio_karolina/blob/main/pages/add_a_player.py) with selectors and methods.

</details>
<details>
<summary>Edit players page</summary>

Direct link to the [Edit players page](https://github.com/rkarolina/Challenge_portfolio_karolina/blob/main/pages/edit_players.py) with selectors and methods.
</details>

<a name='scenarios'></a>
### Scenarios
[Test cases](https://docs.google.com/spreadsheets/d/16-cDIWCZtrsKerXf4LcxMQzdhwJwX-PI/edit#gid=611878532) prepared for this project in Excel file with test data. <br/>
Below you can find implemented **test cases in Python + Selenium** (links to the repository):
1. TC001 - [Login to the Scouts Panel](https://github.com/rkarolina/Challenge_portfolio_karolina/blob/main/test_cases/login_to_the_system.py)
2. TC002 - [Download CSV file with players ](https://github.com/rkarolina/Challenge_portfolio_karolina/blob/main/test_cases/download_players_csv_list.py)
3. TC003 - [Add a new player](https://github.com/rkarolina/Challenge_portfolio_karolina/blob/main/test_cases/go_to_add_a_new_player.py)
4. TC004 - [Filter player](https://github.com/rkarolina/Challenge_portfolio_karolina/blob/main/test_cases/filter_player.py)
5. TC005 - [Add a new match](https://github.com/rkarolina/Challenge_portfolio_karolina/blob/main/test_cases/add_a_new_match.py)
6. TC006 - [Edit existing Player](https://github.com/rkarolina/Challenge_portfolio_karolina/blob/main/test_cases/go_to_edit_new_player.py)


<a name='robotframework'></a>
### Robotframework

Test cases has been implemented also in Robot Framework. If you are interested you can check it out:
- [Repository](https://github.com/rkarolina/robotframework_scoutpanel)
- [Test cases](https://github.com/rkarolina/robotframework_scoutpanel/blob/main/test_login_rf.robotl)


<a name='bugs'></a>
### Bugs

- [Bugs list](https://docs.google.com/spreadsheets/d/18w4IjEA5mrVF7g3Sd0CvgxQZQvKs2Bft/edit#gid=1397049833)
- [Recordings](https://drive.google.com/drive/folders/1RSEK60i_cfWxJxVkaQcRkpO-BhqzUcYi)

<a name='report'></a>
### Report

On this page you will be redirected to [Report](https://docs.google.com/document/d/1InMpXbcKYLtR9AxborT0N25tK_TkcYiN/edit)  from testing.

<a name='portfolio'></a>
## Portfolio
Here you can find my [GitHub](https://github.com/rkarolina) portfolio.