from datetime import datetime


def horario_ponta():
    """
    Considera horário de ponta entre 18h e 21h.
    Ajuste conforme a concessionária.
    """

    hora = datetime.now().hour

    return 18 <= hora < 21


def avaliar_demanda(
    demanda_atual: float,
    demanda_contratada: float,
    nova_carga: float
):
    """
    Avalia se uma nova carga pode ser ligada
    sem ultrapassar o limite de demanda.
    """

    limite = demanda_contratada * 1.05

    demanda_projetada = demanda_atual + nova_carga

    autorizado = demanda_projetada <= limite

    excesso = max(
        0,
        demanda_projetada - limite
    )

    margem_disponivel = max(
        0,
        limite - demanda_projetada
    )

    percentual_utilizado = round(
        (demanda_projetada / limite) * 100,
        2
    )

    alerta = "NORMAL"

    if percentual_utilizado >= 95:
        alerta = "CRÍTICO"
    elif percentual_utilizado >= 85:
        alerta = "ATENÇÃO"

    return {
        "demanda_atual_kw": demanda_atual,
        "demanda_contratada_kw": demanda_contratada,
        "limite_kw": limite,
        "demanda_projetada_kw": demanda_projetada,
        "autorizado": autorizado,
        "excesso_kw": excesso,
        "margem_disponivel_kw": margem_disponivel,
        "percentual_utilizado": percentual_utilizado,
        "alerta": alerta,
        "horario_ponta": horario_ponta()
    }


def estimar_custo_hora(
    potencia_kw: float,
    tarifa_kwh: float
):
    """
    Calcula custo horário do pivô.
    """

    return round(
        potencia_kw * tarifa_kwh,
        2
    )


def estimar_custo_operacao(
    potencia_kw: float,
    horas: float,
    tarifa_kwh: float
):
    """
    Calcula custo total da operação.
    """

    consumo = potencia_kw * horas

    custo = consumo * tarifa_kwh

    return {
        "consumo_kwh": round(consumo, 2),
        "custo_total": round(custo, 2)
    }