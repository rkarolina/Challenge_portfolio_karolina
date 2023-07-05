
## <h1> *Podzadanie 1: konfiguracja oprogramowania.*
### <h2> *Podzadanie 1: Dlaczego zdecydowałem się wziąć udział w wyzwaniu Dare IT Challenge?*
__Cześć, mam na imię Karolina. Poniżej przedstawiam główne powody dołączenia do wyzwania, 
a ponieważ lubię konkretne odpowiedzi wszystko poniżej będzie złożone z list i punktów:__ 
1. Chcę nauczyć się korzystać ze środowisk i narzędzi używanych do testów automatycznych.
2. W przyszłości chciałabym zostać testerem automatyzującym.
3. ~~Bo~~ Lubię wyzwania (motywują do pracy) 🙂
4. Mam nadzieję, że uda mi się stworzyć świetne portfolio na moim profilu [GitHub](https://github.com/rkarolina)

<h3>Aby zbliżyć się do celu będę systematycznie wykonywać nowe zadania.
<h4>W pierwszym tygodniu wyzwania:

- [x] Pobrałam niezbędne narzędzia.
- [x] Sklonowałam repozytorium.
- [x] Edytowałam swój pierwszy plik README w języku markdown!
- [ ] Ukończyłam Subtask 1 commitując (dziwnie pisze się po polsku używając zapożyczeń z innych języków) plik do zdalnego repozytorium.



### <h2> *Zadanie 2: selektory*
#login
<h6> Scouts Panel
1. selektor z atrybutem id 
//*[@id="__next"]/form/div/div[1]/h5  
2. selector z class
//*[@class="MuiTypography-root MuiTypography-h5 MuiTypography-gutterBottom"] 
3. selector z div
//div/form/div/div/*//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[1]/span[1]

<h6>Login
1. selector z id
//*[@id="login"]
2. selector z class
//*[contains(@class, "MuiInputBase-input MuiInput-input")] 
3. selector z input
//input[@type="text"] 

<h6> Password

1. selector z id
//*[@id="password"]
2. selector z input#password
//input[@type="password"] 
3. selector z class
//*[starts-with(@class="MuiInputBase-input MuiInput-input")] 

<h6> Remind Password

1. selector z id
//*[@id="__next"]/form/div/div[1]/a
2. selector z class
//*[@class="MuiTypography-root MuiLink-root MuiLink-underlineHover jss4 MuiTypography-colorPrimary"]
3. Last
//*[last()][name()="a"]

<h6> English

1. selector z id
//*[@id="__next"]/form/div/div[2]/div//*[@id="__next"]/form/div/div[2]/div

<h6>SIGN IN button
1. id
//*[@id="__next"]/form/div/div[2]/button/span[1]
2. Class
//*[@class="MuiButton-label"]


<h6> Form

1. id
    //*[@id="__next"]/form
