#!/usr/bin/env python3
"""Etapa 5 — Gera a COLEÇÃO DE CENAS do OBS pronta para importar.
Estrutura: 5 cenas, fontes compartilhadas, stinger configurado, áudio roteado.
Caminho padrão dos arquivos: C:/twitch/exoriservice (ver guia se usar outro)."""
import json, uuid

U = lambda: str(uuid.uuid4())
BASE = "C:/twitch/exoriservice"
A = BASE + "/assets"

def src_input(name, sid, settings, volume=1.0, mixers=0, monitoring=0, filters=None):
    return {"prev_ver": 503316480, "name": name, "uuid": sid, "id": sid and None or None,
            "__kind": None, "mixers": mixers, "sync": 0, "flags": 0, "volume": volume,
            "balance": 0.5, "enabled": True, "muted": False, "push-to-mute": False,
            "push-to-talk": False, "hotkeys": {}, "deinterlace_mode": 0,
            "deinterlace_field_order": 0, "monitoring_type": monitoring,
            "private_settings": {}, "filters": filters or [], "settings": settings}

def browser(name, sid, url=None, local=None, w=1920, h=1080, reroute=False,
            shutdown=True, restart_active=False, volume=1.0):
    s = {"css": "body { background-color: rgba(0, 0, 0, 0); margin: 0 auto; overflow: hidden; }",
         "fps": 60, "width": w, "height": h, "reroute_audio": reroute,
         "restart_when_active": restart_active, "shutdown": shutdown,
         "visibility": "always", "webpage_control_level": 1}
    if local:
        s["is_local_file"] = True
        s["local_file"] = local
    else:
        s["is_local_file"] = False
        s["url"] = url
    return src_input(name, sid, s, volume=volume, mixers=1 if reroute else 0)

def item(name, sid, x=0.0, y=0.0, sx=1.0, sy=1.0, visible=True, locked=False, iid=1):
    return {"name": name, "source_uuid": sid, "visible": visible, "locked": locked,
            "rot": 0.0, "pos": {"x": x, "y": y}, "scale": {"x": sx, "y": sy}, "align": 5,
            "bounds_type": 0, "bounds_align": 0, "bounds": {"x": 0.0, "y": 0.0},
            "crop_left": 0, "crop_top": 0, "crop_right": 0, "crop_bottom": 0,
            "id": iid, "group_item_backup": False, "scale_filter": "disable",
            "blend_method": "default", "blend_type": "normal",
            "show_transition": {"duration": 0}, "hide_transition": {"duration": 0},
            "private_settings": {}, "type": "input"}

def scene(name, sid, items):
    return {"prev_ver": 503316480, "name": name, "uuid": sid, "id": "scene",
            "mixers": 0, "sync": 0, "flags": 0, "volume": 1.0, "balance": 0.5,
            "enabled": True, "muted": False, "hotkeys": {}, "monitoring_type": 0,
            "private_settings": {},
            "settings": {"custom_size": False, "id_counter": len(items) + 5, "items": items}}

# ── UUIDs das fontes compartilhadas ──
IDS = {
    "starting": U(), "brb": U(), "enc": U(), "overlay": U(), "party": U(), "car": U(), "cover": U(),
    "alerts": U(), "chat": U(), "music": U(), "game": U(), "bgjc": U(),
    "mon": U(), "moldG": U(), "moldJ": U(), "moldJC": U(), "tick": U(),
    "sc1": U(), "sc2": U(), "sc3": U(), "sc4": U(), "sc5": U(), "sc6": U(),
}

sources = []

# ── fontes compartilhadas ──
sources.append(browser("💤 TELAS · Starting Soon", IDS["starting"],
                       url=f"file:///{A}/telas/starting-soon.html?t=10", restart_active=True))
sources.append(browser("⏸ TELAS · BRB", IDS["brb"], local=f"{A}/telas/brb.html"))
sources.append(browser("🏁 TELAS · Encerramento", IDS["enc"], local=f"{A}/telas/encerramento.html"))
sources.append(browser("🕹 OVERLAY · Gameplay", IDS["overlay"], local=f"{A}/overlay/overlay-gameplay.html"))
sources.append(browser("🐺 WIDGET · Party Tracker", IDS["party"], local=f"{A}/overlay/party-tracker.html"))
sources.append(browser("📣 WIDGET · Carrossel Serviços", IDS["car"], local=f"{A}/overlay/carrossel-servicos.html"))
sources.append(browser("🔔 ALERTAS · StreamElements ⚠️ TROCAR URL", IDS["alerts"],
                       url="https://streamelements.com/embed/overlay/TROCAR/TROCAR",
                       w=880, h=600, reroute=True, volume=0.7))
sources.append(browser("💬 CHAT · StreamElements ⚠️ TROCAR URL", IDS["chat"],
                       url="https://streamelements.com/embed/chat/TROCAR/TROCAR",
                       w=560, h=920, reroute=False))
sources.append(src_input("🎮 CAPTURA · Tibia ⚠️ SELECIONAR JANELA", IDS["game"], "game_capture",
                         {"capture_mode": "window", "window": "", "priority": 1,
                          "capture_cursor": True, "allow_transparency": False,
                          "srgb": False, "force_sdr": False}))
sources.append(src_input("🖼 BG · Just Chatting", IDS["bgjc"], "image_source",
                         {"file": f"{A}/extras/justchatting-1920x1080.png"}))

sources.append(browser("🛡 COBERTURA · Chat do Jogo", IDS["cover"], local=f"{A}/overlay/cobertura-chat.html", w=700, h=300))
sources.append(src_input("🖥 CAPTURA · Monitor ⚠️ SELECIONAR", IDS["mon"], "display_capture",
                         {"display": 0, "method": "auto", "show_cursor": True,
                          "srgb": False, "force_sdr": False}))
sources.append(browser("🖼 MOLDURA · Monitor", IDS["moldG"], local=f"{A}/overlay/moldura-monitor.html"))
sources.append(browser("🖼 MOLDURA · Jogo (mini)", IDS["moldJ"], local=f"{A}/overlay/moldura-jogo.html", w=480, h=270))
sources.append(browser("🖼 MOLDURA · Just Chatting", IDS["moldJC"], local=f"{A}/overlay/moldura-jc.html"))
sources.append(browser("📨 TICKER · Comandos", IDS["tick"], local=f"{A}/overlay/ticker.html", w=1920, h=72))

# ── cenas ──
sources.append(scene("01 · STARTING", IDS["sc1"], [
    item("🎮 CAPTURA · Tibia ⚠️ SELECIONAR JANELA", IDS["game"], iid=1),
    item("💤 TELAS · Starting Soon", IDS["starting"], iid=2),
    item("📣 WIDGET · Carrossel Serviços", IDS["car"], iid=3, locked=True),
    item("📨 TICKER · Comandos", IDS["tick"], x=0, y=1008, iid=4),
]))
sources.append(scene("02 · GAMEPLAY", IDS["sc2"], [
    item("🎮 CAPTURA · Tibia ⚠️ SELECIONAR JANELA", IDS["game"], iid=1),
    item("🛡 COBERTURA · Chat do Jogo", IDS["cover"], x=0, y=780, iid=2),
    item("🕹 OVERLAY · Gameplay", IDS["overlay"], iid=3),
    item("🐺 WIDGET · Party Tracker", IDS["party"], iid=4, locked=True),
    item("📣 WIDGET · Carrossel Serviços", IDS["car"], iid=5, locked=True),
    item("🔔 ALERTAS · StreamElements ⚠️ TROCAR URL", IDS["alerts"], x=520, y=36, iid=6),
    item("📨 TICKER · Comandos", IDS["tick"], x=0, y=1008, iid=7),
]))
sources.append(scene("03 · JUST CHATTING", IDS["sc3"], [
    item("🎮 CAPTURA · Tibia ⚠️ SELECIONAR JANELA", IDS["game"], iid=1),
    item("🖼 BG · Just Chatting", IDS["bgjc"], iid=2),
    item("🕹 OVERLAY · Gameplay", IDS["overlay"], iid=3),
    item("🖼 MOLDURA · Just Chatting", IDS["moldJC"], iid=4),
    item("💬 CHAT · StreamElements ⚠️ TROCAR URL", IDS["chat"], x=1330, y=80, iid=5),
    item("🔔 ALERTAS · StreamElements ⚠️ TROCAR URL", IDS["alerts"], x=520, y=36, iid=6),
    item("📣 WIDGET · Carrossel Serviços", IDS["car"], iid=7, locked=True),
    item("📨 TICKER · Comandos", IDS["tick"], x=0, y=1008, iid=8),
]))
sources.append(scene("04 · BRB", IDS["sc4"], [
    item("🎮 CAPTURA · Tibia ⚠️ SELECIONAR JANELA", IDS["game"], iid=1),
    item("⏸ TELAS · BRB", IDS["brb"], iid=2),
    item("📣 WIDGET · Carrossel Serviços", IDS["car"], iid=3, locked=True),
    item("📨 TICKER · Comandos", IDS["tick"], x=0, y=1008, iid=4),
]))
sources.append(scene("05 · ENCERRAMENTO", IDS["sc5"], [
    item("🎮 CAPTURA · Tibia ⚠️ SELECIONAR JANELA", IDS["game"], iid=1),
    item("🏁 TELAS · Encerramento", IDS["enc"], iid=2),
    item("📣 WIDGET · Carrossel Serviços", IDS["car"], iid=3, locked=True),
    item("📨 TICKER · Comandos", IDS["tick"], x=0, y=1008, iid=4),
]))
sources.append(scene("06 · TELA", IDS["sc6"], [
    item("🎮 CAPTURA · Tibia ⚠️ SELECIONAR JANELA", IDS["game"], iid=1),
    item("🖥 CAPTURA · Monitor ⚠️ SELECIONAR", IDS["mon"], iid=2),
    item("🎮 CAPTURA · Tibia ⚠️ SELECIONAR JANELA", IDS["game"], x=32, y=738, sx=0.25, sy=0.25, iid=3),
    item("🖼 MOLDURA · Monitor", IDS["moldG"], iid=4),
    item("🖼 MOLDURA · Jogo (mini)", IDS["moldJ"], x=32, y=738, iid=5),
    item("🔔 ALERTAS · StreamElements ⚠️ TROCAR URL", IDS["alerts"], x=520, y=36, iid=6),
    item("📨 TICKER · Comandos", IDS["tick"], x=0, y=1008, iid=7),
]))

collection = {
    "__NOTE__": "Gerarado pelo projeto exoriservice — remover esta linha ao importar não é necessário",
    "ActiveDuplicateSources": False,
    "DuplicateSources": False,
    "name": "EXORISERVICE",
    "current_scene": "01 · STARTING",
    "current_program_scene": "01 · STARTING",
    "scene_order": ["01 · STARTING", "02 · GAMEPLAY", "03 · JUST CHATTING",
                    "04 · BRB", "05 · ENCERRAMENTO", "06 · TELA"],
    "current_transition": "⚡ STINGER EXORI",
    "transitions": [
        {"name": "Corte", "duration": 300},
        {"name": "Fade", "duration": 300},
        {"name": "⚡ STINGER EXORI", "duration": 500, "id": "stinger_transition",
         "settings": {"transition_point_type": 0, "transition_point": 50,
                      "media_file": f"{A}/stinger/stinger-transicao.webm",
                      "looping": False, "switch_point": 50,
                      "audio_fade_style": 0, "video_fade_style": 0,
                      "hw_decode": True}},
    ],
    "sources": sources,
}

# corrige campos de id/kind (src_input recebe id via parâmetro posicional em usos pontuais)
for s in sources:
    if s["id"] is None:
        s.pop("id")
    s.pop("__kind", None)
    if s.get("id") == "game_capture":
        pass
# reinjeta ids corretos por tipo
KIND = {n: k for n, k in [
    ("💤 TELAS · Starting Soon", "browser_source"), ("⏸ TELAS · BRB", "browser_source"),
    ("🏁 TELAS · Encerramento", "browser_source"), ("🕹 OVERLAY · Gameplay", "browser_source"),
    ("🐺 WIDGET · Party Tracker", "browser_source"),
    ("🔔 ALERTAS · StreamElements ⚠️ TROCAR URL", "browser_source"),
    ("💬 CHAT · StreamElements ⚠️ TROCAR URL", "browser_source"),
    ("🎮 CAPTURA · Tibia ⚠️ SELECIONAR JANELA", "game_capture"),
    ("🖼 BG · Just Chatting", "image_source")]}
for s in sources:
    if s.get("id") != "scene":
        s["id"] = KIND.get(s["name"], "browser_source")

out = "/home/user/twitch-pro/obs/exoriservice-cenas.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(collection, f, ensure_ascii=False, indent=2)

# validação
with open(out, encoding="utf-8") as f:
    data = json.load(f)
names = [s["name"] for s in data["sources"]]
scenes = [s for s in data["sources"] if s.get("id") == "scene"]
uuids = {s["uuid"] for s in data["sources"]}
assert len(names) == len(set(names)), "nomes duplicados!"
assert len(uuids) == len(data["sources"]), "uuids duplicados!"
for sc in scenes:
    for it in sc["settings"]["items"]:
        assert it["source_uuid"] in uuids, f"item órfão: {it['name']}"
print(f"✔ JSON válido — {len(scenes)} cenas, {len(data['sources'])} fontes, {sum(len(sc['settings']['items']) for sc in scenes)} itens")
print("arquivo:", out)
