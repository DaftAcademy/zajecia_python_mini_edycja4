# Narzędzia programisty Python

![Logo warsztatów](logo.jpg)


Długość: 1 godzina. Głównie rozmowy i małej ilości demonstracji, bez slajdów. Celem jest wymiana doświadczeń i opinii nt. narzędzi, których używaja zawodowi _pythonowcy_.

## Wstęp.

Przybiorę formę gry z rolami. Załóżmy, że pracujemy razem w normalnym zespole programistycznym gdzie główną technologią jest Python, ja jestem odpowiedzialny za produktywność, a Ty od nie dawna jesteś w zespole. Razem będziemy _dowozić_ nowe funkcje, sprinty, wgrywać kod na serwery produkcyjna, gasić pożary i naprawiać błędy w kodzie. Każdej stronie zależy, żeby nie marnować czasu, żeby było go jak najwięcej na piłkarzyki i myślenie, nie chcemy wykonywac dodatkowej pracy tylko dlatego, że nie znamy krótszej drogi.

Nic co zaproponuję nie jest prawdą, a jedynie opinią. Moje rekomendacje można obalić, a proponowanej logice zaprzeczyć, ale zgódźmy się co nadrzędnej zasady. **Narzędzia się liczą.** _Tools Matter_. I co do drugiej pomocniczej, nie ma dobrego powodu, żeby znać narzędzie słabo, troszkę i mniej więcej. Spędzimy z nimi tysiące godzin i lata, warto już od samego początku dążyć do aktywnego poznawania ich i mistrzostwa. Tak, mistrzostwa. Wybierz dobre narzędzia i znaj każdą ich moc. Sprawdź to, stań się mistrzem swoich narzędzi, jak się nie opłąci, zwrócę Ci pieniądze.

Przerywaj mi, sugeruj własne, kontruj, pytaj i męcz. Z chęcią się dowiem czegoś nowego.

## O wyborze narzędzi ogólnie.

Wybierz narzędzie sam, ale spośród tego co znają ludzie, z którymi pracujesz, zawodowo czy hobbistycznie. Wymieniaj się wiedzą, pokazuj co odkryłeś sam i pytaj o triki innych. Nie bądź tym jednym emacsem na całym _openspejsie_ (chyba, że już jesteś jego mistrzem).

Jeżeli cała Twoja drużyna korzysta z foo, a Ty od zawsze korzystasz z bar, ale jakoś specjalnie Ci nie zależy, to spróbuj się dostosować. Nie mocno, nie na siłę, nie ze stratą w produktywności ale rozważ. Ja uwielbiam narzędzia i nie raz byłem fanatykiem własnych, chciałem przekonywać do moich ścieżek i chyba traciłem na tym. Jak wszyscy wokół Ciebie korzystają z Ubuntu ale zostawiają Ci wolną rękę, to nie wybieraj Gentoo, a jak wszyscy wokół Ciebie korzystają z Gentoo to ucz się `portage`! Przyjdzie taki zły piątek, kiedy będziecie w sześć osób na Twoim dziwnym systemie naprawiali Twój błąd a Ty nie będziesz wiedzieć jak znaleźć paczkę która zawiera pliki `v4l-*-24xxx-01.fw` i Ci Jacek nie pomoże, a mógłby.

Rób tak jak Twoja drużyna, no ale też bez przesady.


## Wielkie tematy IDE/edytor tekstu

[IDE czy nie IDE?](https://youtu.be/VN3ak9HKvyM?t=29s). Czym jest IDE? Kiedy IDE? Kiedy nie IDE?

#### [PyCharm](https://www.jetbrains.com/pycharm/download/)
- nawigacja, do klasy, do pliku, do każdego _symbolu_, nawigacja po edycjach, nawigacja po nawigacji, po metodach
- refaktoring, wyciągnij/wciągnij kod,
- znajdź użycia, także pod zmienioną postacią, znajdź implemetacje
- integracja z gitem, cofanie sekcji do stanu z repozytorium
- zmień nazwę symbolu
- czyszczenie kodu (code analysis)
- nadpisz metodę
- współpracuje z dockerem
- ukradli multikursor _sablajmowi_ i ulepszyli go
- szift+enter!
- repozytorium konfiguracji

minusy:
- prędkość
- zeżre prawie wszystkie zasoby na średnim komputerze
- tak rozbudowany program my setki małych irytujących błędów, także w regresji
- poznanie całości zabierze miesiące, może lata, ale warto
- czasami kosztuje pieniądze
- debugger powolny, a konsola tragicznie zaimplementowana
- rozpieszcza tak, że niektórzy nigdy się gita nie nauczą
- _sablajmowcy_ będą przewracać oczami i pytać się kiedy się nawrócisz
- słabe, słabe, słabe pluginy

co na początek:
- Help -> Keymap reference
- Menu Navigate
- Menu Refactor

#### SublimeText/[Anaconda](https://github.com/DamnWidget/anaconda),

- szybkość
- multikursor
- _Goto Anything_,
- konfiguracja w plikach, Customize Anything
- pluginy, szybkośc instalacji pluginów
- nie ma za dużo cudów, więc da się go nauczyć i zająć się pracą

minusy:
- [abandonware](https://en.wikipedia.org/wiki/Abandonware) [ostatnia wersja "23 September 2016", 4 wersje w 2016]
- przenoszenie konfiguracji to ból w rzyci, chyba, że coś się zmieniło

#### vim

Musisz znać jedno narzędzie, którym sprawnie zedytujesz plik gdzieś gdzie nia ma [_iksów_](https://en.wikipedia.org/wiki/Display_server) i które jest powszechnie dostępne, dlatego chcesz znać vima.

na początek:
- :wq, dd, p, P, o, O, A, I, :%s, /cokolwiek, ciw, x, r, dw, d$
potem vimtutor, i może kolekcjonować pluginy od tych co się znają

Uważaj na ten kiepski "żart":
```
$ docker run -it atlassian/ubuntu-minimal bash
root@471ca357b97a:/# type vi vim
vi is /usr/bin/vi
bash: type: vim: not found
root@471ca357b97a:/# ls -l /usr/bin/vi
lrwxrwxrwx 1 root root 20 Sep  4  2014 /usr/bin/vi -> /etc/alternatives/vi
```

#### [Visual Studio Code](http://donjayamanne.github.io/pythonVSCode/)

Rafał mówi, że bardzo dobre.

---

Wszystko inne... no jak kto woli, ale ja bym nie tracił czasu.
Nie Atom, NIE gedit, NIE nano,

Pogadajmy, co kto używa?

## Hardware
- dlaczego i7
- kiedy hardware ma znaczenie i jakie ma znaczenie?

## System operacyjny, System operacyjny jako narzędzie, terminal, bash/zsh

- Linux czy MacOS
- kiedy da się pracować pod Windowsem
- dystrubucja... o co ta wojna? centos, arch, debian/ubuntu, gentoo, fedora, puppy


prawdziwy zapis komend z mojej historii, żadna ze mnie wyrocznia, nie ma kanonu komend do poznania ale nie stracisz, jeżeli poznasz właśnie te

```
alias ag apt apt-get apt-file apt-cache awk arp-scan ansible-playbook apg arandr autossh
bash bg bzip2 bunzip2 basename bind
cat cd chmod chown cp cron cal curl clear
date du df dd detox diff dmesg docker dpkg dos2unix
echo env exec export encfs egrep
find for free fg file
grep gzip git gpg gpg-agent groups gunzip gosu
hash -r hg history htop hwinfo head hostname
ifconfig ifup ifdown if if info ipython isort iwconfig
jobs
kill killall keepassx
less locate ll ls ln -s lowriter lsof lsusb
man make mv mc mbank-cli? meld mkdir mount
netstat nano ncdu nginx nm-applet nmtui
openssl
ping pip `ps aux` pass pwd py.test pyenv python3! pavucontrol pg_dump pgrep pipdeptree pkill printf
rsync reboot rm read readlink -f resolvconf
scp sh sed sort source sleep ssh ssh-keygen ssh-keyscan ssh-agent stat su sudo sync screen shutdown strace setxkbmap_-option_caps:none
touch tree type tar tmux top tr tail telnet
uniq uname umount unzip unzip usermod_-aG_docker_bartek uptime
vim vlc
which wget wc while whoami watch wine wmctrl
xrandr xdg-open xargs (wym zargs!) xsel xev xterm
yes
zip zcat zenity
```

bash minimal:
- ctrl-a ctrl-e
- ctrl-k ctrl-u
- ctrl-c ctrl-d
- alt kropka



## Debuggery, ipdb, pdb, pdbpp?, print('pupa'), śledzenie kodu, logging.

```
import ipdb; ipdb.set_trace()
import pdb; pdb.set_trace()
```

## IPython, REPL na sterydach, Jupyter

demo!

- ?, ??, _, timeit
- jupyter-qtconsole
- IPython jako shell

- jest jeszcze [bpython](https://github.com/bpython/bpython)

## [Virtualenv](https://virtualenv.pypa.io/en/stable/), [pyenv](https://github.com/pyenv/pyenv), [venv](https://docs.python.org/3/library/venv.html), docker, site-packages, [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/), instalacja pakietów

demo!

- najprosztszy setup.py:

```
$ cat setup.py
from setuptools import find_packages, setup

setup(
    name='kinro',
    version='0.2',
    packages=find_packages(),
)
```

- setuptools to piekło, [ma "osobnego" BDFLa-delegata](http://python-notes.curiousefficiency.org/en/latest/pep_ideas/core_packaging_api.html)
- [przejrzyj setup.py na githubie](https://github.com/search?utf8=%E2%9C%93&q=filename%3Asetup.py+language%3Apython&type=Code)

## testowanie

- [py.test](https://docs.pytest.org/en/latest/contents.html#), [nosetests](http://nose.readthedocs.io/en/latest/), [unittest](https://docs.python.org/3/library/unittest.html),
- [mock](https://docs.python.org/3/library/unittest.mock.html),
- [freezegun](https://github.com/spulec/freezegun),
- BDD/cucumber/gherkin/?

## [Standardy kodu](https://github.com/PyCQA).

```
In [23]: import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

- [pep8](http://pep8.org/)
- [pylint](https://www.pylint.org/), [pyflakes](https://github.com/PyCQA/pyflakes), [flake8](http://flake8.pycqa.org/en/latest/), [mccabe](https://github.com/pycqa/mccabe)

---

na to nie starczy czasu:

## dzwonki i gwizdki, może kiedyś użyjesz

line profiler,
concurrency visualizer

## git, mercurial, svn

## github, gitlab, bitbucket

## ssh, tunele

## Alternatywne implementacje Pythona,
- [pypy](https://pypy.org/),
- [anaconda](https://www.continuum.io/downloads), Continuum Analytics! _pay attention!_
- [micropython](https://github.com/micropython/micropython)

cmentarz: ironpython, jython, [CL-Python](https://github.com/metawilm/cl-python), brython, srajton,

## moje ulubione biblioteki
- [pygments](http://pygments.org/)
- [Requests: HTTP for Humans](http://docs.python-requests.org/en/master/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Django](https://www.djangoproject.com/)
- [cookiecutter](https://github.com/audreyr/cookiecutter)
- [arrow](http://arrow.readthedocs.io/en/latest/)/[moment](https://github.com/zachwill/moment)
- :|, do walki z chaosem [lxml](http://lxml.de/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/), [xmltodict](https://github.com/martinblech/xmltodict)

## Przykłady narzędzi **w Pythonie**.

- [httpie](https://github.com/jakubroztocil/httpie),
- [ansible](https://www.ansible.com/),
- [supervisor](http://supervisord.org/),
- [mycli](http://mycli.net/),
- [pgcli](https://www.pgcli.com/),
- [docker-compose](https://docs.docker.com/compose/),
- [sentry](http://sentry.io),
- [uWSGI](https://uwsgi-docs.readthedocs.io/)

## Grube koty

- [NLTK](http://www.nltk.org/),
- [scipy](http://www.scipy.org/),
- [scikit-learn](http://scikit-learn.org/)

## Kradnięcie Internetu:

- [Scrapy](https://scrapy.org/)

## Varia:

- https://github.com/vinta/awesome-python
- [ciekawa dyskusja pokazująca _benewolencję_ Guido](https://github.com/PyCQA/pycodestyle/issues/466)