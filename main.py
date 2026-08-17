import os
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.theme import Theme
from nasa_api import NasaClient
from converter import bytes_to_ascii

color_theme = Theme({
    "info": "cyan",
    "warning": "yellow",
    "error": "bold red",
    "success": "bold green"
})

def main():
    console = Console(theme=color_theme)

    API_key = os.getenv("NASA_API_KEY", "DEMO_KEY")
    client = NasaClient(API_key)

    console.print(Panel.fit(
        "[bold cyan]NASA SPACE VOYAGER[/bold cyan]",
        border_style="bright_blue"
    ))


    while True:
        console.print("\n[info]Available commands:[/info] [white]'YYYY-MM-DD', 'exit', Enter (today photo)[/white]")
        user_input = Prompt.ask("[bold]Enter you request[/bold]").strip().lower()

        if user_input == 'exit':
            console.print("[warning]Bye! You should listen to a song called “Voyager” written by an author from the CIS[/warning]")
            break
        try:
            with console.status("[bold green]Working working..."):
                data = client.get_apod_data(date=user_input)
                
                if data.get("media_type") != "image":
                    console.print("[warning]⚠ On this day, the video was published. Try a different date.[/warning]")
                    continue

                img_bytes = client.get_image_bytes(data["url"])
                
                ascii_art = bytes_to_ascii(img_bytes, target_width=console.width - 10)

            console.print(Panel(
                ascii_art, 
                title=f"[bold yellow]{data.get('title')}[/bold yellow]",
                subtitle=f"[gray]{data.get('date')}[/gray]",
                expand=False
            ))

            console.print(Panel(
                data.get("explanation"),
                title="[info]Scientific Description[/info]",
                width=console.width - 4,
                border_style="blue"
            ))
        except Exception as e:
            console.print(f"[error]Error:[/error] {e}")
            console.print("[info]Check date format or API-key, may be the problems with connection.[/info]")

if __name__ == "__main__":
    main()