from pathlib import Path

import psycopg
import typer

from cvbankas.parse import run_parse
from cvbankas.parse_discovery import run_parse_discovery
from cvbankas.scrape import run_scrape
from cvbankas.scrape_discovery import run_scrape_discovery

app = typer.Typer(help="available commands: 'scrape_discovery', 'parse_discovery', 'scrape', 'parse'")


@app.command()
def scrape(downloader: str) -> None:
    run_scrape(downloader)


@app.command()
def scrape_discovery(downloader: str) -> None:
    run_scrape_discovery(downloader)


@app.command()
def parse() -> None:
    run_parse()


@app.command()
def parse_discovery() -> None:
    run_parse_discovery()


# initialize schema.sql
DB_URL = "postgresql://user:password@localhost:5432/cvbankas_db"


@app.command()
def init_db(schema_path: Path = Path("cvbankas/schema.sql")) -> None:
    # initialize postgres db with schema file
    if not schema_path.exists():
        typer.echo(f"Error: Schema file not found at {schema_path}", err=True)
        raise typer.Exit(1)

    try:
        # connect to postgres and exceute schema
        with psycopg.connect(DB_URL) as conn:
            with conn.cursor() as cur:
                sql_script = schema_path.read_text(encoding="utf-8")
                cur.execute(sql_script)

            typer.echo("DB initialized")

    except Exception as e:  # pylint: disable=broad-exception-caught
        typer.echo(f"error: {e}", err=True)


if __name__ == "__main__":
    app()
