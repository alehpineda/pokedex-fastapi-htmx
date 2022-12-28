from dataclasses import dataclass

from sqlalchemy import create_engine, engine


@dataclass
class DatabaseConfig:
    filename: str

    def _url(self) -> str:
        return f"sqlite:///{self.filename}"

    def engine(self) -> engine:
        return create_engine(self._url(), echo=True)
