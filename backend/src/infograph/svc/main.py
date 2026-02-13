import click
import uvicorn
import os

@click.command()
@click.option("--port", default=8000, help="Port to run the server on")
@click.option("--host", default="127.0.0.1", help="Host to bind to")
@click.option("--reload/--no-reload", default=False, help="Enable autoreload")
def main(port: int, host: str, reload: bool):
    """Start the Infograph backend service."""
    # load env
    from dotenv import load_dotenv
    load_dotenv()

    # import app
    from infograph.svc.api_service import app

    uvicorn.run(app, host=host, port=port, reload=reload)

if __name__ == "__main__":
    main()
