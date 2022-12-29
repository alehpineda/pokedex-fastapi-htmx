from dataclasses import dataclass

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


@dataclass
class DatabaseConfig:
    filename: str

    def _url(self) -> str:
        return f"sqlite:///{self.filename}"

    def engine(self) -> Engine:
        return create_engine(self._url(), echo=True)  # echo=True sql traceback
