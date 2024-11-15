
# OXIDO - Aplikacja Python do generowania artykułów HTML

## Opis projektu

Ten projekt to aplikacja w Pythonie, która:

1. Odczytuje plik tekstowy z artykułem (`artykul.txt`).
2. Łączy się z API OpenAI w celu przetworzenia treści artykułu na HTML.
3. Generuje plik HTML zawierający:
   - Strukturalny kod z użyciem tagów HTML.
   - Miejsca na obrazy oznaczone tagiem `<img>` z atrybutami `alt` i podpisami.
4. Zapisuje wynikowy plik jako `artykul.html`.
5. W przypadku braku dostępu do API OpenAI (np. przekroczony limit zapytań), aplikacja generuje awaryjny HTML z użyciem wbudowanej logiki.

## Wymagania

- **Python**: 3.9+
- **Biblioteki**: 
  - `openai`

## Instalacja i uruchomienie

### 1. Sklonuj repozytorium:

\`\`\`bash
git clone https://github.com/TwojUzytkownik/nazwa-repozytorium.git
cd nazwa-repozytorium
\`\`\`

### 2. Zainstaluj wymagane biblioteki:

Upewnij się, że używasz środowiska wirtualnego:

\`\`\`bash
python -m venv .venv
source .venv/bin/activate  # Na Windows: .venv\Scripts\activate
\`\`\`

Zainstaluj wymagane zależności:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

Jeśli plik \`requirements.txt\` nie istnieje, możesz go stworzyć ręcznie i dodać linię:

\`\`\`
openai
\`\`\`

### 3. Ustaw klucz API OpenAI:

Zmień wartość \`openai.api_key\` w pliku \`main.py\`, wstawiając swój klucz API:

\`\`\`python
openai.api_key = "twoj-klucz-api"
\`\`\`

### 4. Przygotuj plik tekstowy z artykułem:

Umieść plik \`artykul.txt\` w katalogu głównym projektu. Przykład zawartości pliku:

\`\`\`
Sztuczna inteligencja: wpływ i wyzwania

Sztuczna inteligencja to dziedzina nauki i technologii zajmująca się...
\`\`\`

### 5. Uruchom skrypt:

\`\`\`bash
python main.py
\`\`\`

### 6. Sprawdź wynik:

Otwórz wygenerowany plik \`artykul.html\` w przeglądarce, aby zobaczyć wynik.

## Struktura plików

\`\`\`
/nazwa-repozytorium
|-- main.py             # Główny skrypt aplikacji
|-- artykul.txt         # Plik wejściowy z artykułem
|-- artykul.html        # Wygenerowany plik HTML
|-- README.md           # Dokumentacja projektu
|-- requirements.txt    # Lista wymaganych bibliotek
\`\`\`

## Przykład działania

### Plik wejściowy (\`artykul.txt\`):

\`\`\`
Sztuczna inteligencja: wpływ i wyzwania

Sztuczna inteligencja to dziedzina nauki i technologii zajmująca się...
\`\`\`

### Wygenerowany plik HTML (\`artykul.html\`):

\`\`\`html
<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sztuczna inteligencja: wpływ i wyzwania</title>
</head>
<body>
    <h1>Sztuczna inteligencja: wpływ i wyzwania</h1>
    <p>Sztuczna inteligencja to dziedzina nauki...</p>
    <img src="image_placeholder.jpg" alt="AI usage example">
    <p class="image-caption">Przykład wykorzystania AI</p>
</body>
</html>
\`\`\`

## Uwagi

- Jeśli API OpenAI nie jest dostępne, aplikacja wygeneruje awaryjny HTML, który może być użyty zamiast wyników AI.
- Możesz modyfikować prompt w \`main.py\`, aby dostosować generowanie HTML do swoich potrzeb.

## Licencja

Projekt jest udostępniany na licencji MIT. Szczegóły znajdują się w pliku \`LICENSE\`.
