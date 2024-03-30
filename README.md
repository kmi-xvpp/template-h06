# L10E01: TicTacToe
Ve složce `tictactoe` naleznete balíček obsahující jednoduchou implementaci hry TicTacToe (piškvorky na hrací desce 3x3). Během řešení tohoto úkolu je možné používat i věci nad rámec semináře (hlavně v kontextu knihovny `pytest` a `typing`).

Ukázka použití

```python
% > ipython
Python 3.10.0 (default, Oct 13 2021, 06:45:00) [Clang 13.0.0 (clang-1300.0.29.3)]
Type 'copyright', 'credits' or 'license' for more information
IPython 7.28.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from tictactoe import TicTacToe

In [2]: game = TicTacToe()

In [3]: game.play(0, 0)
Out[3]: TicTacToe(3x3, turn=2, active_stone=X, winner=None)

In [4]: print(game)
O |   |  
––––––––––
  |   |  
––––––––––
  |   |  
Turn: 2
Stone on turn: X
Winner: 

In [5]: game.play(0, 0)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-5-b7f49aa95ba3> in <module>
----> 1 game.play(0, 0)

~/Gits/kmi-jp-templates/template-L10E01/tictactoe/tictactoe.py in play(self, x, y)
     36         # if coords already contains stone
     37         if self.board[x][y] != " ":
---> 38             raise ValueError(f"Position {x},{y} is already occupied.")
     39 
     40         # place stone

ValueError: Position 0,0 is already occupied.

In [6]: game.play(0, 1).play(1,1).play(2, 0).play(2, 2)
Out[6]: TicTacToe(3x3, turn=6, active_stone=O, winner=O)

In [7]: print(game)
O | X |  
––––––––––
  | O |  
––––––––––
X |   | O
Turn: 6
Stone on turn: O
Winner: O
```

## Soubor `setup.py`
Balíčku vytvořte soubor `setup.py`. Stačí pokud bude obsahovat základní informace a balíček půjde nainstalovat pomocí `pip install -e .`.

## Typování
Balíčku (metodám) dopiště kompletní typování (pomoci modulu `typing`, včetně krátkých docstringů obsahující typy).

Balíček obsahuje třídu `Stone`. Jedná se o třídu výčtového typu (`Enum`). Tyto třídy slouží k uchovávání výčtu údajů. Třídu `Stone` můžeme používat pro reprezentaci hracího kamene (což je vhodnější než použití řetězce):

```python
class Stone(Enum):
    """Represents stones for TicTacToe game."""

    # more information about Enum avaliable here
    # https://docs.python.org/3/library/enum.html

    X = "X"
    O = "O"

    def __str__(self):
        return self.value

# v kódu poté můžeme používat
Stone.X
# namísto
"X"
# pokud však převedeme Stone na řetězec získáme hodnotu "X"
str(Stone.X)
# hlavní výhodou je, že pokud se rozhodneme reprezentaci změnit na "x", 
# stačí přepsat třídu Stone, nikoli celý zdrojový kód
```

## Testování
K balíčku `tictactoe` dopiště kompletní sadu unit-testů (umístěte je do složky `tests`). Testy musí být po instalaci `pip install -e .` spustitelné pomoci příkazu `pytest`. Snažte se docílit co největší code coverage. Pokud balíček bude obsahovat chyby, opravte jej (tím neříkám, že tam nějaké jsou :)).

Třída `tictactoe.TicTacToe` obsahuje následující vlastnosti:

* `self.board` - samotná herní deska, dvojrozměrný seznam obsahující `" "` pokud na políčku není položený kámen, jinak obsahuje `Stone.X` nebo `Stone.O`.
* `self.turn` - číslo aktuálního tahu, začíná na hodnotě `1`
* `self.active_stone` - náhodně vybraný počáteční kámen (`Stone.X` nebo `Stone.O`).
* `self.winner` - pokud je hra ukončená obsahuje výherní kámen, jinak hodnotu `None`

Krátký popis metod (v pořadí od nejjednoduššího po nejsložitější):

* `tictactoe.TicTacToe._all_active_stones` - otestuje zda jsou v předaném iterable všechny kameny rovny aktuálnímu kamenu
* `tictactoe.TicTacToe.__repr__` a `tictactoe.TicTacToe.__str__` - otestujte zda vrací výstup v odpovídajícím formátu
* `tictactoe.TicTacToe.play` - odehraje jeden tah položením aktuálního kamene na souřadnice `x` a `y` (číslováno od `0`). Funkce vrací `self` (aby bylo možné volání `play` řetězit). Je nutné testovat všechny možné exception, to zda se hra správně ukončí (v případě výherce musí být po volání `play` vlastnost `winner` nastavena na výherní kámen), že dochází k inkrementaci počtu kol a že byl herní kámen na desku opravdu položen. Testy pro tuto metodu rozdělte na několik testovacích funkcí.
* `tictactoe.TicTacToe.eval` - vyhodnotí zda již hru někdo vyhrál v opačném případě vrací `None` Nutné testovat všechny výherní kombinace.


