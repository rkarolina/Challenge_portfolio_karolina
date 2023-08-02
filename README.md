## <h1> _Podzadanie 1: konfiguracja oprogramowania._

### <h2> _Podzadanie 1: Dlaczego zdecydowałem się wziąć udział w wyzwaniu Dare IT Challenge?_

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
- [ ] Ukończyłam Subtask 1 commitując (dziwnie pisze się po polsku używając zapożyczeń z innych języków) plik do zdalnego repozytorium.

### <h2> _Zadanie 2: selektory_

<h4> Scouts Panel

1. selektor z atrybutem id <br/>
   //*[@id="__next"]/form/div/div[1]/h5
2. selector z class<br/>
   //*[contains(@class, "gutterBottom")]
3. Selector z text<br/>
   //*[text()="Scouts Panel"]

<h4>Login Input 

1. selector z id<br/>
//*[@id="login"]
2. selector z class oraz id<br/>
//*[@class="MuiInputBase-input MuiInput-input"][@id="login"] 
3. selector z input<br/>
//input[@type="text"]<br/>
input[id="login"]

<h4> Password Input

1. selector z id <br/>
   //*[@id="password"]
2. selector z input password<br/>
   //input[@type="password"]
   input[id="password"]
3. selector z class oraz id<br/>
   //*[@class="MuiInputBase-input MuiInput-input"][@id="password"]

<h4> Remind Password

1. selector z id <br/>
   //*[@id="__next"]/form/div/div[1]/a
2. selector z class<br/>
   //*[contains(@class, "colorPrimary")]
3. Last<br/>
   //*[last()][name()="a"]

<h4> English

1. selector z id<br/>
   //*[@id="__next"]/form/div/div[2]/div
2. Selector z text<br/>
   //*[text()="English"]
3. selector z class<br/>
   //*[starts-with(@class, "MuiSelect-root MuiSelect-select")]

<h4> Zmiana języka (dropdown)

1. selector z class<br/>
   //*[@class= "MuiSelect-nativeInput"]
2. selector z id<br/>
   //*[@id="__next"]/form/div/div[2]/div/input
3. selector z input<br/>
   input[class= "MuiSelect-nativeInput"]<br/>
   input[value= "pl"]

<h4>SIGN IN/Zaloguj button

1. selector z id<br/>
//*[@id="__next"]/form/div/div[2]/button/span[1]
2. selector z class<br/>
//*[@class="MuiButton-label"]
3. Selector z button<br/>
//button

### <h2> Zadanie 4: Refactor, debugger i przypadki testowe
Link do Google Drive: [Here](https://drive.google.com/drive/folders/1Ran9GG_hgc1ndgp329C0nR6x7XVIvla5?usp=drive_link)

### <h2> ﻿Zadanie 6: ﻿
Subtask 2: Zgłaszanie błędów
Link do Google Drive: [Here](https://drive.google.com/drive/folders/1RSEK60i_cfWxJxVkaQcRkpO-BhqzUcYi?usp=drive_link)

﻿Subtask 3: Raport z testów
Link do Google Drive: [Here](https://drive.google.com/drive/folders/1Q_FLVSkBQQV0HUVxH-FWU8VjpoOrpBng?usp=drive_link)
