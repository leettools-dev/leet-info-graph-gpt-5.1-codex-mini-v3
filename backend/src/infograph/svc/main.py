"""Service CLI entry point."""

import click
import uvicorn

from .api_service import create_app


@click.command()
@click.option("--host", default="0.0.0.0", help="Host to bind to")
@click.option("--port", default=8000, help="Port to bind to")
def main(host: str, port: int) -> None:
    """Start the FastAPI backend."""
    app = create_app()
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    main()
