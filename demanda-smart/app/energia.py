PIVOS = [
    {
        "id": 1,
        "nome": "Pivô 1",
        "fabricante": "Valley",
        "modelo": "8120",
        "potencia_kw": 110,
        "area_irrigada_ha": 95,
        "comprimento_m": 650,
        "vazao_m3_h": 420,
        "tensao_v": 380,
        "cultura": "Milho",
        "setor": "A",
        "ligado": True
    },
    {
        "id": 2,
        "nome": "Pivô 2",
        "fabricante": "Lindsay",
        "modelo": "Zimmatic",
        "potencia_kw": 95,
        "area_irrigada_ha": 80,
        "comprimento_m": 600,
        "vazao_m3_h": 350,
        "tensao_v": 380,
        "cultura": "Soja",
        "setor": "B",
        "ligado": True
    }
]


# =========================
# CONSULTAS
# =========================

def listar_pivos():
    return PIVOS


def obter_pivo(pivo_id: int):
    return next(
        (p for p in PIVOS if p["id"] == pivo_id),
        None
    )


# =========================
# CÁLCULOS
# =========================

def calcular_demanda_atual():
    return sum(
        p["potencia_kw"]
        for p in PIVOS
        if p["ligado"]
    )


def calcular_demanda_total():
    return sum(
        p["potencia_kw"]
        for p in PIVOS
    )


def calcular_potencia_disponivel(
    demanda_contratada: float
):
    return max(
        0,
        demanda_contratada - calcular_demanda_atual()
    )


# =========================
# CADASTRO
# =========================

def cadastrar_pivo(pivo: dict):

    novo_id = max(
        [p["id"] for p in PIVOS],
        default=0
    ) + 1

    novo = {
        "id": novo_id,
        "nome": pivo.get("nome"),
        "fabricante": pivo.get("fabricante"),
        "modelo": pivo.get("modelo"),
        "potencia_kw": float(
            pivo.get("potencia_kw", 0)
        ),
        "area_irrigada_ha": float(
            pivo.get("area_irrigada_ha", 0)
        ),
        "comprimento_m": float(
            pivo.get("comprimento_m", 0)
        ),
        "vazao_m3_h": float(
            pivo.get("vazao_m3_h", 0)
        ),
        "tensao_v": float(
            pivo.get("tensao_v", 380)
        ),
        "cultura": pivo.get("cultura"),
        "setor": pivo.get("setor"),
        "ligado": bool(
            pivo.get("ligado", False)
        )
    }

    PIVOS.append(novo)

    return novo


# =========================
# UPDATE
# =========================

def atualizar_pivo(
    pivo_id: int,
    dados: dict
):

    pivo = obter_pivo(pivo_id)

    if not pivo:
        return None

    dados.pop("id", None)

    pivo.update(dados)

    return pivo


# =========================
# DELETE
# =========================

def excluir_pivo(pivo_id: int):

    for i, p in enumerate(PIVOS):

        if p["id"] == pivo_id:
            del PIVOS[i]
            return True

    return False


# =========================
# LIGA / DESLIGA
# =========================

def ligar_pivo(pivo_id: int):

    p = obter_pivo(pivo_id)

    if p:
        p["ligado"] = True

    return p


def desligar_pivo(pivo_id: int):

    p = obter_pivo(pivo_id)

    if p:
        p["ligado"] = False

    return p