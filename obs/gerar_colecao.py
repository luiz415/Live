#!/usr/bin/env python3
"""Gerador da coleção v6.1 do exoriservice.
- Sem cena 00 ADMIN.
- Party Tracker é fonte ÚNICA com editor na parte inferior (abaixo dos 1080px);
  altura da fonte = 1560px (1080 ao vivo + ~480 painel). OBS clippa pra 1080px ao ar
  via crop_bottom=480 para que o painel de edição não apareça — no Interagir você
  rola/expandir a janela pra alcançar a parte de baixo (fora do ar).
- Audio sources APENAS: Discord, Meu Mic, Spotify, Widget LivePIX, Alertas SE, Navegador.
  (Desktop Audio removido.)
"""
import json, uuid, os

U = lambda: str(uuid.uuid4())
BASE = "C:/twitch/exoriservice"
A    = BASE + "/assets"

def mk_src(name, sid, kind, settings, volume=1.0, mixers=0, monitoring=0, filters=None):
    return {
        "prev_ver": 503316480, "name": name, "uuid": sid, "id": kind,
        "mixers": mixers, "sync": 0, "flags": 0, "volume": volume, "balance": 0.5,
        "enabled": True, "muted": False, "push-to-mute": False, "push-to-talk": False,
        "hotkeys": {}, "deinterlace_mode": 0, "deinterlace_field_order": 0,
        "monitoring_type": monitoring, "private_settings": {},
        "filters": filters or [], "settings": settings,
    }

def browser(name, sid, local=None, url=None, w=1920, h=1080, reroute=False,
            shutdown=True, restart_active=False, volume=1.0, control_level=1,
            crop_bottom=0, monitoring=0):
    s = {
        "css": "body { background-color: rgba(0,0,0,0); margin:0 auto; overflow:hidden; }",
        "fps": 60, "width": w, "height": h, "reroute_audio": reroute,
        "restart_when_active": restart_active, "shutdown": shutdown,
        "visibility": "always", "webpage_control_level": control_level,
    }
    if local:
        s["is_local_file"] = True
        s["local_file"]    = local
        s["url"]           = "file:///" + local
    else:
        s["is_local_file"] = False
        s["url"]           = url or ""
    return mk_src(name, sid, "browser_source", s,
                  volume=volume, mixers=1 if reroute else 0, monitoring=monitoring)

def wasapi(name, sid, device_id, kind, monitoring=0):
    return mk_src(name, sid, kind, {"device_id": device_id},
                  volume=1.0, mixers=2 if kind=="wasapi_input_capture" else 1,
                  monitoring=monitoring)

def dshow(name, sid, device_id=""):
    return mk_src(name, sid, "dshow_input",
                  {"device_id": device_id, "video_fmt": "I420", "framerate": "30",
                   "resolution": "1920x1080", "res_type": 1, "flip": False,
                   "fps_type": 1, "color_space": 6, "color_range": 2},
                  mixers=0)

def gamecap(name, sid):
    return mk_src(name, sid, "game_capture",
                  {"capture_mode": "window", "window": "", "priority": 1,
                   "capture_cursor": True, "allow_transparency": False,
                   "srgb": False, "force_sdr": False})

def moncap(name, sid):
    return mk_src(name, sid, "monitor_capture",
                  {"monitor_id": 0, "method": "auto", "show_cursor": True})

def img(name, sid, file):
    return mk_src(name, sid, "image_source", {"file": file})

def item(name, sid, x=0.0, y=0.0, sx=1.0, sy=1.0, visible=True, locked=False, iid=1,
         crop_bottom=0, crop_top=0, crop_left=0, crop_right=0):
    return {
        "name": name, "source_uuid": sid, "visible": visible, "locked": locked,
        "rot": 0.0, "pos": {"x": x, "y": y}, "scale": {"x": sx, "y": sy}, "align": 5,
        "bounds_type": 0, "bounds_align": 0, "bounds": {"x":0.0,"y":0.0},
        "crop_left":crop_left,"crop_top":crop_top,"crop_right":crop_right,"crop_bottom":crop_bottom,
        "id": iid, "group_item_backup": False, "scale_filter":"disable",
        "blend_method":"default","blend_type":"normal",
        "show_transition":{"duration":0},"hide_transition":{"duration":0},
        "private_settings":{},"type":"input"
    }

def scene(name, sid, items):
    return mk_src(name, sid, "scene",
                  {"custom_size": False, "id_counter": len(items)+10, "items": items},
                  mixers=0)

# ── UUIDs ──
IDS = {k: U() for k in [
    "starting","brb","enc",
    "overlay","car","cover",
    "alerts","chat","livepix",
    "game","mon","bgjc",
    "tick","rodape","moldW","contador",
    "moldG","moldJ","moldJC",
    "party",                  # fonte única (live + editor)
    "webcam",
    # áudios do mixer
    "mic","discord","spotify",
    "sc1","sc2","sc3","sc4","sc5","sc6",
    "grp_webcam",
]}
sources = []

# ── TELAS ──
sources.append(browser("💤 TELAS · Starting Soon", IDS["starting"],
                       local=f"{A}/telas/starting-soon.html", restart_active=True))
sources.append(browser("⏸ TELAS · BRB",           IDS["brb"],    local=f"{A}/telas/brb.html"))
sources.append(browser("🏁 TELAS · Encerramento", IDS["enc"],    local=f"{A}/telas/encerramento.html"))

# ── OVERLAYS / WIDGETS ──
sources.append(browser("🕹 OVERLAY · Gameplay",         IDS["overlay"], local=f"{A}/overlay/overlay-gameplay.html"))
sources.append(browser("📣 WIDGET · Carrossel Serviços", IDS["car"],    local=f"{A}/overlay/carrossel-servicos.html"))
sources.append(browser("🛡 COBERTURA · Chat do Jogo",   IDS["cover"],  local=f"{A}/overlay/cobertura-chat.html", w=700, h=300))
sources.append(browser("📨 TICKER · Comandos",          IDS["tick"],   local=f"{A}/overlay/ticker.html", w=1920, h=72))
sources.append(browser("📝 RODAPÉ · Animado",           IDS["rodape"], local=f"{A}/overlay/rodape.html", w=1920, h=200))
sources.append(browser("🖼 MOLDURA · Webcam",           IDS["moldW"],  local=f"{A}/overlay/moldura-webcam.html", w=480, h=400))
sources.append(browser("⏱ CONTADOR · Twitch",          IDS["contador"], local=f"{A}/overlay/contador-twitch.html", w=400, h=120))
sources.append(browser("🖼 MOLDURA · Monitor",          IDS["moldG"],  local=f"{A}/overlay/moldura-monitor.html"))
sources.append(browser("🖼 MOLDURA · Jogo (mini)",      IDS["moldJ"],  local=f"{A}/overlay/moldura-jogo.html", w=480, h=270))
sources.append(browser("🖼 MOLDURA · Just Chatting",    IDS["moldJC"], local=f"{A}/overlay/moldura-jc.html"))

# ── EXTERNOS ──
# StreamElements ALERTAS — com áudio roteado (sai no mixer "Alertas StreamElements")
sources.append(browser("🔔 ALERTAS · StreamElements ⚠️ TROCAR URL", IDS["alerts"],
                       url="https://streamelements.com/embed/overlay/TROCAR/TROCAR",
                       w=880, h=600, reroute=True, volume=0.8, monitoring=0))
sources.append(browser("💬 CHAT · StreamElements ⚠️ TROCAR URL", IDS["chat"],
                       url="https://streamelements.com/embed/chat/TROCAR/TROCAR",
                       w=560, h=920))
# LivePIX — widget com áudio (ex: alertas de Pix)
sources.append(browser("💚 WIDGET · LivePIX ⚠️ TROCAR URL", IDS["livepix"],
                       url="https://widget.livepix.gg/embed/TROCAR",
                       w=800, h=600, reroute=True, volume=0.9, monitoring=0))

# ── CAPTURAS ──
sources.append(gamecap("🎮 CAPTURA · Tibia ⚠️ SELECIONAR JANELA", IDS["game"]))
sources.append(moncap ("🖥 CAPTURA · Monitor ⚠️ SELECIONAR",      IDS["mon"]))
sources.append(dshow  ("🎥 WEBCAM · Câmera ⚠️ SELECIONAR",        IDS["webcam"]))
sources.append(img    ("🖼 BG · Just Chatting",                  IDS["bgjc"],
                       file=f"{A}/extras/justchatting-1920x1080.png"))

# ── PARTY TRACKER (fonte ÚNICA)
# Altura extra (480px) abaixo dos 1080px = painel de edição. Em todas as cenas
# usamos crop_bottom=480 pra que o painel NÃO apareça no ar. Para editar, o
# usuário abre Interagir (que mostra o conteúdo completo, sem crop) e aperta E.
PARTY_H = 1080 + 480
PARTY_CROP = 480
sources.append(browser("🐺 WIDGET · Party Tracker", IDS["party"],
                       local=f"{A}/overlay/party-tracker.html",
                       w=1920, h=PARTY_H, control_level=2))

# ── ÁUDIO (Mixer) - conforme solicitado ──
# Cada app é capturado via WASAPI output; o usuário preenche o device_id ou
# deixa '' (padrão) no primeiro uso e seleciona nas propriedades.
sources.append(wasapi("🎤 Meu Mic",         IDS["mic"],     "", "wasapi_input_capture",  monitoring=2))
sources.append(wasapi("🎧 Discord",         IDS["discord"], "", "wasapi_output_capture", monitoring=0))
sources.append(wasapi("🎵 Spotify",         IDS["spotify"], "", "wasapi_output_capture", monitoring=0))

# Obs: Widget LivePIX e Alertas StreamElements já são browser_source com
# reroute_audio=True e aparecem automaticamente no mixer com os nomes das
# próprias fontes. O navegador (Chrome) — quando você usa o overlay que abre
# páginas no browser do sistema — é representado aqui por uma fonte
# wasapi_output_capture genérica "🌐 Navegador".
sources.append(wasapi("🌐 Navegador",       U(), "", "wasapi_output_capture", monitoring=0))
IDS["browser_audio"] = [s for s in sources if s["name"]=="🌐 Navegador"][0]["uuid"]

# ── GRUPO WEBCAM ──
def webcam_group_items():
    return [
        item("🎥 WEBCAM · Câmera ⚠️ SELECIONAR", IDS["webcam"],  x=0,  y=0,  iid=1),
        item("🖼 MOLDURA · Webcam",              IDS["moldW"],   x=0,  y=0,  iid=2),
        item("⏱ CONTADOR · Twitch",             IDS["contador"],x=0,  y=-70,iid=3),
    ]
grp_webcam = mk_src("🎬 GRUPO · Webcam", IDS["grp_webcam"], "group", {
    "id_counter": 5, "items": webcam_group_items(),
    "custom_size": False, "group_item_backup": False
}, mixers=0)
sources.append(grp_webcam)

# ── CENAS ──
PARTY_ITEM = lambda iid,lock=True: item(
    "🐺 WIDGET · Party Tracker", IDS["party"], x=0, y=0, locked=lock, iid=iid,
    crop_bottom=PARTY_CROP  # oculta a faixa de edição no ar
)

sources.append(scene("01 · STARTING", IDS["sc1"], [
    item("🎮 CAPTURA · Tibia ⚠️ SELECIONAR JANELA", IDS["game"],  iid=1),
    item("💤 TELAS · Starting Soon",                IDS["starting"], iid=2),
    item("📣 WIDGET · Carrossel Serviços",          IDS["car"],   iid=3, locked=True),
    item("📨 TICKER · Comandos",                    IDS["tick"],  x=0, y=1008, iid=4),
]))

sources.append(scene("02 · GAMEPLAY", IDS["sc2"], [
    item("🎤 Meu Mic",                    IDS["mic"],           visible=False, iid=1),
    item("🎧 Discord",                    IDS["discord"],       visible=False, iid=2),
    item("🎵 Spotify",                    IDS["spotify"],       visible=False, iid=3),
    item("🌐 Navegador",                  IDS["browser_audio"], visible=False, iid=4),
    item("🎮 CAPTURA · Tibia ⚠️ SELECIONAR JANELA", IDS["game"],  iid=5),
    item("🛡 COBERTURA · Chat do Jogo",             IDS["cover"], x=0, y=780, iid=6),
    item("🕹 OVERLAY · Gameplay",                   IDS["overlay"], iid=7),
    PARTY_ITEM(iid=8, lock=True),
    item("🎬 GRUPO · Webcam",             IDS["grp_webcam"], x=1420, y=20,  iid=9),
    item("📣 WIDGET · Carrossel Serviços", IDS["car"],   iid=10, locked=True),
    item("🔔 ALERTAS · StreamElements ⚠️ TROCAR URL", IDS["alerts"], x=520, y=36, iid=11),
    item("💚 WIDGET · LivePIX ⚠️ TROCAR URL", IDS["livepix"], x=520, y=260, iid=12),
    item("📨 TICKER · Comandos",          IDS["tick"],  x=0, y=1008, iid=13),
]))

sources.append(scene("03 · JUST CHATTING", IDS["sc3"], [
    item("🎤 Meu Mic",                    IDS["mic"],           visible=False, iid=1),
    item("🎧 Discord",                    IDS["discord"],       visible=False, iid=2),
    item("🎵 Spotify",                    IDS["spotify"],       visible=False, iid=3),
    item("🌐 Navegador",                  IDS["browser_audio"], visible=False, iid=4),
    item("🖼 BG · Just Chatting",                   IDS["bgjc"], iid=5),
    item("🕹 OVERLAY · Gameplay",                   IDS["overlay"], iid=6),
    item("🖼 MOLDURA · Just Chatting",              IDS["moldJC"], iid=7),
    item("🎬 GRUPO · Webcam",             IDS["grp_webcam"], x=1420, y=80, iid=8),
    item("💬 CHAT · StreamElements ⚠️ TROCAR URL",  IDS["chat"],  x=1330, y=80, iid=9),
    item("🔔 ALERTAS · StreamElements ⚠️ TROCAR URL", IDS["alerts"], x=520, y=36, iid=10),
    item("💚 WIDGET · LivePIX ⚠️ TROCAR URL", IDS["livepix"], x=520, y=260, iid=11),
    item("📣 WIDGET · Carrossel Serviços",          IDS["car"],   iid=12, locked=True),
    item("📨 TICKER · Comandos",                    IDS["tick"],  x=0, y=1008, iid=13),
]))

sources.append(scene("04 · BRB", IDS["sc4"], [
    item("🎮 CAPTURA · Tibia ⚠️ SELECIONAR JANELA", IDS["game"], iid=1),
    item("⏸ TELAS · BRB",                          IDS["brb"],  iid=2),
    item("📣 WIDGET · Carrossel Serviços",          IDS["car"],  iid=3, locked=True),
    item("📨 TICKER · Comandos",                    IDS["tick"], x=0, y=1008, iid=4),
]))

sources.append(scene("05 · ENCERRAMENTO", IDS["sc5"], [
    item("🎮 CAPTURA · Tibia ⚠️ SELECIONAR JANELA", IDS["game"], iid=1),
    item("🏁 TELAS · Encerramento",                 IDS["enc"],  iid=2),
    item("📣 WIDGET · Carrossel Serviços",          IDS["car"],  iid=3, locked=True),
    item("📨 TICKER · Comandos",                    IDS["tick"], x=0, y=1008, iid=4),
]))

sources.append(scene("06 · TELA", IDS["sc6"], [
    item("🎤 Meu Mic",                    IDS["mic"],           visible=False, iid=1),
    item("🎧 Discord",                    IDS["discord"],       visible=False, iid=2),
    item("🎵 Spotify",                    IDS["spotify"],       visible=False, iid=3),
    item("🌐 Navegador",                  IDS["browser_audio"], visible=False, iid=4),
    item("🖥 CAPTURA · Monitor ⚠️ SELECIONAR",      IDS["mon"],   iid=5),
    item("🎮 CAPTURA · Tibia ⚠️ SELECIONAR JANELA", IDS["game"],  x=32, y=738, sx=0.25, sy=0.25, iid=6),
    item("🖼 MOLDURA · Monitor",                    IDS["moldG"], iid=7),
    item("🖼 MOLDURA · Jogo (mini)",                IDS["moldJ"], x=32, y=738, iid=8),
    item("🔔 ALERTAS · StreamElements ⚠️ TROCAR URL", IDS["alerts"], x=520, y=36, iid=9),
    item("💚 WIDGET · LivePIX ⚠️ TROCAR URL", IDS["livepix"], x=520, y=260, iid=10),
    item("📨 TICKER · Comandos",                    IDS["tick"],  x=0, y=1008, iid=11),
]))

collection = {
    "__NOTE__": "exoriservice v6.1 — gerado por obs/gerar_colecao.py",
    "ActiveDuplicateSources": False,
    "DuplicateSources": False,
    "name": "EXORISERVICE v6.1",
    "current_scene": "01 · STARTING",
    "current_program_scene": "01 · STARTING",
    "scene_order": ["01 · STARTING","02 · GAMEPLAY","03 · JUST CHATTING",
                    "04 · BRB","05 · ENCERRAMENTO","06 · TELA"],
    "current_transition": "⚡ STINGER EXORI",
    "transitions": [
        {"name":"Corte","duration":300},
        {"name":"Fade","duration":300},
        {"name":"⚡ STINGER EXORI","duration":500,"id":"stinger_transition",
         "settings":{"transition_point_type":0,"transition_point":50,
                     "media_file":f"{A}/stinger/stinger-transicao.webm",
                     "looping":False,"switch_point":50,
                     "audio_fade_style":0,"video_fade_style":0,"hw_decode":True}},
    ],
    "sources": sources,
}

OUT = os.path.join(os.path.dirname(__file__), "exoriservice-cenas.json")
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(collection, f, ensure_ascii=False, indent=2)

# Validação
with open(OUT, encoding="utf-8") as f:
    data = json.load(f)
names = [s["name"] for s in data["sources"]]
scenes= [s for s in data["sources"] if s.get("id") in ("scene","group")]
uuids = {s["uuid"] for s in data["sources"]}
assert len(names) == len(set(names)), "nomes duplicados"
assert len(uuids) == len(data["sources"]), "uuids duplicados"
for sc in scenes:
    for it in sc.get("settings",{}).get("items",[]):
        assert it["source_uuid"] in uuids, f"órfão: {sc['name']} → {it['name']}"
audio_srcs = [s['name'] for s in data['sources'] if s.get('mixers',0)>0]
print(f"✔ {OUT}")
print(f"  {len([s for s in data['sources'] if s.get('id')=='scene'])} cenas + 1 grupo webcam")
print(f"  {len(data['sources'])} fontes no total")
print(f"  fontes com áudio (mixer): {audio_srcs}")
