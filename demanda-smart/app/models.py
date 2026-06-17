from pydantic import BaseModel
from typing import Optional, List


# =========================
# PIVÔ
# =========================

class PivoCreate(BaseModel):
    nome: str
    potencia_kw: float

    fabricante: Optional[str] = ""
    modelo: Optional[str] = ""

    area_irrigada_ha: Optional[float] = 0
    comprimento_m: Optional[float] = 0
    vazao_m3_h: Optional[float] = 0

    tensao_v: Optional[float] = 380

    cultura: Optional[str] = ""
    setor: Optional[str] = ""

    ligado: Optional[bool] = False


# =========================
# SIMULAÇÃO
# =========================

class SimulacaoRequest(BaseModel):
    demanda_atual: float
    demanda_contratada: float
    nova_carga: float


class SimulacaoCustoRequest(BaseModel):
    potencia_kw: float
    horas: float
    tarifa_kwh: float


# =========================
# DEMANDA
# =========================

class DemandaRequest(BaseModel):
    picos_kw: List[float]
    margem: float = 0.15
    demanda_contratada: Optional[float] = None


class DemandaResponse(BaseModel):
    pico_max: float
    media_top3: float
    demanda_ideal: float
    risco_multa: bool
    sugestao: str