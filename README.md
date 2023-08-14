# Scouts Panel
[ENG version here](https://github.com/rkarolina/robotframework_scoutpanel/tree/main) <p>
Aplikacja umożliwiająca zbieranie informacji o zawodnikach przez skautów piłkarskich (informacje kontaktowe, klub, główna i alternatywna pozycja, osiągnięcia) <p>
Funkcje:
- tworzenie profilów zawodników
- dodawanie meczów i wyników
- raporty

# O projekcie
[ENG version here](https://github.com/rkarolina/robotframework_scoutpanel/tree/main) <p>
Projekt wykonywany w ramach Dare IT Challenge na ścieżce QA: Wstęp do Testów Automatycznych. 💪 <p>
Na początku na podstawie moich poprzednich doświadczeń wykonałam testy eksploracyjne w celu zapoznania się z aplikacją. <p>
Następnie utworzyłam plan testów oraz scenariusze/przypadki testowe. <p>
Na koniec zostały one zaimplementowane w automatyzacji testów.

# Narzędzia
<img alt="Pycharm" src="https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white"/> <img alt="Github" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"/> 
# Technologie
<img alt="Python" src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/> <img alt="Selenium" src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white"/>
## <h1> _Zadanie 1: konfiguracja oprogramowania._

### <h2> _Zadanie 1: Dlaczego zdecydowałem się wziąć udział w wyzwaniu Dare IT Challenge?_

**Cześć, mam na imię Karolina. Poniżej przedstawiam główne powody dołączenia do wyzwania,
a ponieważ lubię konkretne odpowiedzi wszystko poniżej będzie złożone z list i punktów:**

1. Chcę nauczyć się korzystać ze środowisk i narzędzi używanych do testów automatycznych.
2. W przyszłości chciałabym zostać testerem automatyzującym.
3. Lubię wyzwania (motywują do pracy) 🙂
4. Mam nadzieję, że ~~uda mi się~~ stworzę świetne portfolio na moim profilu [GitHub](https://github.com/rkarolina)

<h3>Aby zbliżyć się do celu będę systematycznie wykonywać nowe zadania.
<h4>W pierwszym tygodniu wyzwania:

- [x] Pobrałam niezbędne narzędzia.
- [x] Sklonowałam repozytorium.
- [x] Edytowałam swój pierwszy plik README w języku markdown!
- [x] Ukończyłam Subtask 1 commitując plik do zdalnego repozytorium.
### <h2> _Zadanie 2: selektory_

Scouts Panel

1. selektor z atrybutem id <br/>
```
   //*[@id="__next"]/form/div/div[1]/h5
```
2. selector z class<br/>
```
   //*[contains(@class, "gutterBottom")]
```
3. Selector z text<br/>
```
   //*[text()="Scouts Panel"]
```

Login Input 

1. selector z id<br/>
```
//*[@id="login"]
```
2. selector z class oraz id<br/>
```
//*[@class="MuiInputBase-input MuiInput-input"][@id="login"]
```
3. selector z input<br/>
```
//input[@type="text"]<br/>
input[id="login"]
```

Password Input

1. selector z id <br/>
```
   //*[@id="password"]
```
2. selector z input password<br/>
```
   //input[@type="password"]
   input[id="password"]
```
3. selector z class oraz id<br/>
```
   //*[@class="MuiInputBase-input MuiInput-input"][@id="password"]
```

Remind Password

1. selector z id <br/>
```
   //*[@id="__next"]/form/div/div[1]/a
```
2. selector z class<br/>
```
   //*[contains(@class, "colorPrimary")]
```
3. Last<br/>
```
   //*[last()][name()="a"]
```

English

1. selector z id<br/>

```
   //*[@id="__next"]/form/div/div[2]/div
```
2. Selector z text<br/>
```
   //*[text()="English"]
```
3. selector z class<br/>
```
   //*[starts-with(@class, "MuiSelect-root MuiSelect-select")]
```

Zmiana języka (dropdown)

1. selector z class<br/>
```
   //*[@class= "MuiSelect-nativeInput"]
```
2. selector z id<br/>
```
   //*[@id="__next"]/form/div/div[2]/div/input
```
3. selector z input<br/>
```
   input[class= "MuiSelect-nativeInput"]<br/>
   input[value= "pl"]
```
SIGN IN/Zaloguj button

1. selector z id<br/>
```
//*[@id="__next"]/form/div/div[2]/button/span[1]
```
2. selector z class<br/>
```
//*[@class="MuiButton-label"]
```
3. Selector z button<br/>
```
//button
```

### <h2> _Zadanie 4: Refactor, debugger i przypadki testowe_
[Google Drive link](https://drive.google.com/drive/folders/1Ran9GG_hgc1ndgp329C0nR6x7XVIvla5?usp=drive_link)

### <h2> _Zadanie 5:_
[Robot Framework Scout Panel](https://github.com/rkarolina/robotframework_scoutpanel)

### <h2> _﻿Zadanie 6:_ ﻿
_Subtask 2: Zgłaszanie błędów_
[Google Drive link](https://drive.google.com/drive/folders/1RSEK60i_cfWxJxVkaQcRkpO-BhqzUcYi?usp=drive_link)

_Subtask 3: Raport z testów_
[Google Drive link](https://drive.google.com/drive/folders/1Q_FLVSkBQQV0HUVxH-FWU8VjpoOrpBng?usp=drive_link)

_﻿Subtask 4: Stwórz portfolio_
[GitHub link](https://github.com/rkarolina)
