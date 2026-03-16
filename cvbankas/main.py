import typer
import psycopg
from pathlib import Path
from cvbankas.scrape import run_scrape
from cvbankas.scrape_discovery import run_scrape_discovery
from cvbankas.parse import run_parse
from cvbankas.parse_discovery import run_parse_discovery

app = typer.Typer(help="available commands: 'scrape_discovery', 'parse_discovery', 'scrape', 'parse'")

@app.command()
def scrape():
    run_scrape()  
 
@app.command()
def scrape_discovery():
    run_scrape_discovery() 
    
@app.command()
def parse():
    run_parse()   
    
@app.command()
def parse_discovery():
    run_parse_discovery()      
 
 
#initialize schema.sql    
DB_URL = "postgresql://user:password@localhost:5432/cvbankas_db"

@app.command()
def init_db(schema_path: Path ="cvbankas/schema.sql"):
    # initialize postgres db with schema file
    if not schema_path.exists():
        typer.echo(f"Error: Schema file not found at {schema_path}", err=True)
        raise typer.Exit(1)
    
    try:
        #connect to postgres and exceute schema
        with psycopg.connect(DB_URL) as conn:
            with conn.cursor() as cur:
                sql_script = schema_path.read_text()
                cur.execute(sql_script)
                
            typer.echo("DB initialized")
        
    except Exception as e:
        typer.echo(f"error: {e}", err=True)

if __name__ == "__main__":
    app()