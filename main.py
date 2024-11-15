import openai

# Klucz API OpenAI
openai.api_key = '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'


def read_article(file_path):
    """Funkcja do odczytu artykułu z pliku (poprawione kodowanie)."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def save_html(content, file_path):
    """Funkcja zapisująca wygenerowany HTML do pliku (poprawione kodowanie)."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def fallback_html(content):
    """Generowanie prostego kodu HTML w razie niepowodzenia."""
    lines = content.split("\n")
    html_output = ["<h1>Generated Article</h1>"]

    for line in lines:
        line = line.strip()
        if line.startswith("Sztuczna inteligencja"):
            html_output.append(f"<h1>{line}</h1>")
        elif line.startswith("Wyzwania") or line.startswith("Automatyzacja"):
            html_output.append(f"<h2>{line}</h2>")
        elif line:
            html_output.append(f"<p>{line}</p>")
            html_output.append(
                "<img src='image_placeholder.jpg' alt='Default AI image'>"
                "<p class='image-caption'>Default caption</p>"
            )

    return "\n".join(html_output)


if __name__ == '__main__':
    # Ścieżki plików
    article_path = 'C:/Users/jghhd/Pyback_exercise/1/Nowy folder (2)/OXIDO/artykul.txt'
    output_path = 'C:/Users/jghhd/Pyback_exercise/1/Nowy folder (2)/OXIDO/artykul.html'

    # Odczytaj artykuł
    article_content = read_article(article_path)

    # Wygeneruj HTML w trybie awaryjnym
    fallback_content = fallback_html(article_content)
    save_html(fallback_content, output_path)
    print(f"Plik HTML został zapisany pod ścieżką: {output_path}")
