import click
import uvicorn

from infograph.svc.api_service import create_app


@click.command()
@click.option("--host", default="0.0.0.0", help="Host to bind the server to.")
@click.option("--port", default=8000, help="Port to run the server on.", type=int)
@click.option("--reload/--no-reload", default=False, help="Enable auto-reload in development.")
def main(host: str, port: int, reload: bool) -> None:
    """Entry point that starts the Uvicorn server."""
    uvicorn.run("infograph.svc.api_service:app", host=host, port=port, reload=reload)


if __name__ == "__main__":
    main()
