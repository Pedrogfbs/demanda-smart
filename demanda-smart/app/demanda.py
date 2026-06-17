def analisar_demanda(picos_kw, margem=0.15, demanda_contratada=None):
    if not picos_kw:
        raise ValueError("Lista de picos não pode ser vazia")

    pico_max = max(picos_kw)

    top3 = sorted(picos_kw, reverse=True)[:3]
    media_top3 = sum(top3) / len(top3)

    base = max(pico_max, media_top3)

    demanda_ideal = base * (1 + margem)

    risco_multa = False

    if demanda_contratada:
        if demanda_ideal > demanda_contratada:
            risco_multa = True

        excesso = demanda_contratada - demanda_ideal

        if excesso > demanda_contratada * 0.15:
            sugestao = "Você está pagando excesso de demanda"
        elif risco_multa:
            sugestao = "Risco de multa: considere aumentar demanda"
        else:
            sugestao = "Contrato equilibrado"
    else:
        sugestao = "Informe demanda contratada para análise completa"

    return {
        "pico_max": round(pico_max, 2),
        "media_top3": round(media_top3, 2),
        "demanda_ideal": round(demanda_ideal, 2),
        "risco_multa": risco_multa,
        "sugestao": sugestao
    }