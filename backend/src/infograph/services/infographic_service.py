from __future__ import annotations

import os
from typing import List
from PIL import Image, ImageDraw, ImageFont

from infograph.stores.abstract_infographic_store import AbstractInfographicStore
from infograph.core.schemas.infographic import InfographicCreate
from infograph.stores.duckdb.duckdb_client import DuckDBClient


class InfographicService:
    """Simple template-based infographic generator.

    Generates a basic PNG with title and bullet points from layout_data and
    saves it to the configured INFOGRAPHIC_PATH.
    """

    def __init__(self, infographic_store: AbstractInfographicStore, output_dir: str | None = None) -> None:
        self._store = infographic_store
        import tempfile
        self._output_dir = output_dir or os.getenv("INFOGRAPHIC_PATH") or tempfile.gettempdir()
        try:
            os.makedirs(self._output_dir, exist_ok=True)
        except OSError:
            # Environment may be read-only (tests). Fall back to system temp dir.
            self._output_dir = tempfile.gettempdir()

    def generate_basic(self, session_id: str, layout_data: dict) -> str:
        """Generate a basic infographic PNG.

        layout_data expected keys:
        - title: str
        - bullets: list[str]
        """
        title = layout_data.get("title", "Infographic")
        bullets: List[str] = layout_data.get("bullets", [])

        # Image canvas
        width, height = 800, 600
        background_color = (255, 255, 255)
        image = Image.new("RGB", (width, height), color=background_color)
        draw = ImageDraw.Draw(image)

        # Load a default font
        try:
            font_path = os.path.join(os.path.dirname(__file__), "../../fonts/DejaVuSans.ttf")
            font = ImageFont.truetype(font_path, 28)
            small_font = ImageFont.truetype(font_path, 18)
        except Exception:
            font = ImageFont.load_default()
            small_font = ImageFont.load_default()

        # Draw title
        margin = 40
        y = margin
        draw.text((margin, y), title, fill=(0, 0, 0), font=font)
        y += 60

        # Draw bullets
        for bullet in bullets:
            draw.text((margin + 20, y), f"• {bullet}", fill=(0, 0, 0), font=small_font)
            y += 30

        # Footer with source count if provided
        source_count = layout_data.get("source_count")
        if source_count is not None:
            footer = f"Sources: {source_count}"
            draw.text((margin, height - margin - 20), footer, fill=(80, 80, 80), font=small_font)

        # Save image
        filename = f"infographic_{session_id}.png"
        path = os.path.join(self._output_dir, filename)
        image.save(path)

        # Persist record in store
        infographic_create = InfographicCreate(
            session_id=session_id,
            image_path=path,
            template_type="basic",
            layout_data=layout_data,
        )
        self._store.create_infographic(infographic_create)

        return path
