print("🔥 MAIN ATIVO - IRRIGATION NATION")

from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.energia import router as energia_router

# ==================================
# APP
# ==================================

app = FastAPI(
    title="Demand Smart",
    version="2.0.0"
)

# inclui router (IMPORTANTE)
app.include_router(energia_router)

# ==================================
# DIRETÓRIOS
# ==================================

BASE_DIR = Path(__file__).resolve().parent

TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"

print(f"[INFO] TEMPLATES_DIR: {TEMPLATES_DIR}")

# ==================================
# STATIC
# ==================================

if STATIC_DIR.exists():
    app.mount(
        "/static",
        StaticFiles(directory=str(STATIC_DIR)),
        name="static"
    )

# ==================================
# TEMPLATES
# ==================================

templates = Jinja2Templates(
    directory=str(TEMPLATES_DIR)
)

# ==================================
# HOME
# ==================================

@app.get("/")
async def home(request: Request):

    arquivo = TEMPLATES_DIR / "dashboard.html"

    if not arquivo.exists():
        return JSONResponse(
            status_code=404,
            content={
                "erro": "dashboard.html não encontrado",
                "caminho": str(arquivo)
            }
        )

    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request}
    )

# ==================================
# STATUS
# ==================================

@app.get("/status")
async def status():
    return {
        "api": "online",
        "versao": "2.0.0"
    }

# ==================================
# HEALTH CHECK
# ==================================

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "app": "Demand Smart",
        "templates_dir": str(TEMPLATES_DIR),
        "running": True
    }

# ==================================
# DASHBOARD API
# ==================================

@app.get("/dashboard")
async def dashboard_api():
    return {
        "demanda_atual_kw": 205,
        "potencia_disponivel_kw": 95,
        "quantidade_pivos": 4,
        "pivos_ligados": [
            "Pivô 1",
            "Pivô 2"
        ]
    }

# ==================================
# CONSUMO ANUAL
# ==================================

@app.get("/dashboard-anual")
async def dashboard_anual():
    return {
        "consumo_mensal": [
            12000, 14000, 13500, 16000,
            18000, 21000, 24000, 23000,
            19500, 17000, 15000, 13000
        ]
    }

# ==================================
# PÁGINAS
# ==================================

@app.get("/pivos")
async def pivos(request: Request):
    return templates.TemplateResponse("pivos.html", {"request": request})


@app.get("/manutencao")
async def manutencao(request: Request):
    return templates.TemplateResponse("manutencao.html", {"request": request})


@app.get("/relatorios")
async def relatorios(request: Request):
    return templates.TemplateResponse("relatorios.html", {"request": request})


@app.get("/financeiro")
async def financeiro(request: Request):
    return templates.TemplateResponse("financeiro.html", {"request": request})

# ==================================
# GESTÃO DE ENERGIA (CORRETO)
# ==================================

@app.get("/gestao-energia")
async def gestao_energia(request: Request):
    return templates.TemplateResponse(
        "gestao_energia.html",
        {"request": request}
    )

# ==================================
# TESTE
# ==================================

@app.get("/teste")
async def teste():
    return {
        "templates": str(TEMPLATES_DIR),
        "dashboard_existe": (TEMPLATES_DIR / "dashboard.html").exists(),
        "base_existe": (TEMPLATES_DIR / "base.html").exists(),
        "gestao_energia_existe": (TEMPLATES_DIR / "gestao_energia.html").exists(),
        "pivos_existe": (TEMPLATES_DIR / "pivos.html").exists(),
        "manutencao_existe": (TEMPLATES_DIR / "manutencao.html").exists(),
        "relatorios_existe": (TEMPLATES_DIR / "relatorios.html").exists(),
        "financeiro_existe": (TEMPLATES_DIR / "financeiro.html").exists()
    }