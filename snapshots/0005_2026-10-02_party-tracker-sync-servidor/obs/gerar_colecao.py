#!/usr/bin/env python3
"""Etapa 5 — Gera a COLEÇÃO DE CENAS do OBS pronta para importar (formato do OBS 32.2.2).

Reproduz o estado real do OBS do canal (export de 01/10/2026) já corrigido:
  • 5 cenas: 01 STARTING · 02 GAMEPLAY · 04 BRB · 05 ENCERRAMENTO · 06 TELA
  • capturas com tipo e configuração corretos (jogo = game_capture, tela = monitor_capture)
  • áudio: Meu Mic (supressão -> gate -> limitador -> compressor), Spotify, Discord, Navegador
  • transições: "Limpar" (ativa, 1,5 s) + "⚡ STINGER EXORI" (com as chaves que o OBS lê)
  • UUIDs determinísticos: rodar de novo gera exatamente o mesmo arquivo

URLs privadas (alertas do StreamElements e widget do LivePix) NÃO ficam no repositório:
saem como "about:blank". Depois de importar no OBS, cole as URLs em Propriedades da fonte.

Uso:
  python obs/gerar_colecao.py                        # grava obs/exoriservice-cenas.json
  python obs/gerar_colecao.py --base D:/stream/exo   # outra pasta de instalação no PC
  python obs/gerar_colecao.py --saida outro.json     # outro arquivo de saída
"""
import argparse
import json
import struct
import uuid
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BASE_PADRAO = "C:/twitch/exoriservice"     # pasta no PC onde fica assets/ (barras normais)

OBS_VER = 537001986                         # "prev_ver" gravado pelo OBS 32.2.2
CANVAS_UUID = "6c69626f-6273-4c00-9d88-c5136d61696e"   # canvas principal do OBS ("libobs")
W, H = 1920, 1080
URL_PENDENTE = "about:blank"                # trocar no OBS pela URL privada (nunca versionar)
NS = uuid.UUID("c0a8f5de-3b1e-4f6a-9d27-6e0b4a1c85f3")  # fixo: mantém os UUIDs estáveis

CSS = "body { background-color: rgba(0, 0, 0, 0); margin: 0 auto; overflow: hidden; }"
HK_AUDIO = ["libobs.mute", "libobs.unmute", "libobs.push-to-mute", "libobs.push-to-talk"]
HK_NAV = HK_AUDIO + ["ObsBrowser.Refresh"]
HK_JOGO = HK_AUDIO + ["hotkey_start", "hotkey_stop"]

# ── nomes (fonte única: itens das cenas e fontes usam as mesmas constantes) ──
N_GAME = "🎮 CAPTURA · Tibia"
N_MONITOR = "Captura de monitor"
N_STARTING = "💤 TELAS · Starting Soon"
N_BRB = "⏸ TELAS · BRB"
N_ENC = "🏁 TELAS · Encerramento"
N_OVERLAY = "🕹 OVERLAY · Gameplay"
N_PARTY = "🐺 WIDGET · Party Tracker"
N_CARROSSEL = "📣 WIDGET · Carrossel Serviços"
N_ALERTAS = "🔔 ALERTAS · StreamElements ⚠️ TROCAR URL"
N_COBERTURA = "🛡 COBERTURA · Chat do Jogo"
N_MOLD_MON = "🖼 MOLDURA · Monitor"
N_MOLD_JOGO = "🖼 MOLDURA · Jogo (mini)"
N_TICKER = "📨 TICKER · Comandos"
N_DISCORD = "Discord"
N_MIC = "Meu Mic"
N_NAV = "Navegador"
N_SPOTIFY = "Spotify"
N_LIVEPIX = "WIDGET - LivePix ⚠️ TROCAR URL"
N_WEBCAM = "🎥 WEBCAM · Câmera"
N_MOLD_WEB = "🖼 MOLDURA · Webcam"
N_CONTADOR = "📈 CONTADOR · Twitch"
N_GRP_WEB = "🎬 GRUPO · Webcam (mover junto)"

CENAS = ["01 · STARTING", "02 · GAMEPLAY", "04 · BRB", "05 · ENCERRAMENTO", "06 · TELA"]
ORDEM_NO_OBS = ["06 · TELA", "05 · ENCERRAMENTO", "04 · BRB", "02 · GAMEPLAY", "01 · STARTING"]

# ── layout ajustado à mão no OBS (valores float32 exatos gravados pelo OBS) ──
POS_ALERTA, ESC_ALERTA = (241.0, 0.0), (0.7489583492279053, 0.7490741014480591)      # 1438×809 px
POS_LIVEPIX_GP, ESC_LIVEPIX_GP = (2.0, 578.0), (0.6166666746139526, 0.6156250238418579)  # 148×197 px
POS_LIVEPIX_BRB = (1653.0, 662.0)                                                    # 240×320 px
POS_MOLD_JOGO, ESC_MOLD_JOGO = (27.0, 727.0), (0.9729166626930237, 0.9740740656852722)
POS_TIBIA_MINI, ESC_TIBIA_MINI = (27.0, 728.0), (0.25, 0.25)
POS_COBERTURA = (0.0, 884.0)                                                         # 1920×300 px
POS_TICKER = (0.0, 1008.0)                                                           # 1920×72 px

# ── webcam (formato DVCam): device/device_name em branco; escolher ao importar ──
POS_WEB = (1380.0, 60.0)                                                             # 480×270 px
ESC_WEB = (1.0, 1.0)
POS_TW = (1404.0, 350.0)                                                             # 320×80 px abaixo do grupo
ESC_TW = (1.0, 1.0)
# carrossel no canto inferior esquerdo da cena 02 (versão menor do snapshot)
POS_CAR_GP, ESC_CAR_GP = (40.0, 760.0), (1.0, 1.0)
POS_CAR_GP_BRB = (40.0, 760.0)
POS_CAR_GP_STAR = (40.0, 760.0)
POS_CAR_GP_ENC = (40.0, 760.0)

# ids físicos do hardware do canal (mic e monitor); em outro PC, selecionar de novo no OBS
MIC_DEVICE_ID = "{0.0.1.00000000}.{f4c8d309-8b91-4372-8c18-b52634539a26}"
MONITOR_ID = r"\\?\DISPLAY#ACR03E1#5&30ae2e3f&0&UID4352#{e6f07b5f-ee97-4a90-b076-33f57bf4eaa7}"
JANELA_JOGO = "RubinOT Client:config:rubinot_dx.exe"


def uid(*partes):
    return str(uuid.uuid5(NS, "/".join(partes)))


def f32(x):
    """O OBS guarda posição/escala como float32; reproduz o mesmo arredondamento."""
    return struct.unpack("f", struct.pack("f", x))[0]


class Colecao:
    def __init__(self, base):
        self.A = base.rstrip("/") + "/assets"
        self.fontes = {}       # nome -> dict da fonte (ordem de inserção = ordem no arquivo)
        self.nativas = set()   # criadas direto no OBS 32: seus itens guardam transição de 300 ms
        self.cenas = {}        # nome -> dict da cena

    # ── blocos genéricos ───────────────────────────────────────────────────
    def fonte(self, nome, tipo, settings, volume=1.0, mixers=0, muted=False, monitoring=0,
              hotkeys=(), privado=None, filtros=None, nativa=False):
        assert nome not in self.fontes, "nome de fonte duplicado: " + nome
        f = {"prev_ver": OBS_VER, "name": nome, "uuid": uid("fonte", nome), "id": tipo,
             "versioned_id": tipo, "settings": settings, "mixers": mixers, "sync": 0, "flags": 0,
             "volume": volume, "balance": 0.5, "enabled": True, "muted": muted,
             "push-to-mute": False, "push-to-mute-delay": 0, "push-to-talk": False,
             "push-to-talk-delay": 0, "hotkeys": {k: [] for k in hotkeys},
             "deinterlace_mode": 0, "deinterlace_field_order": 0, "monitoring_type": monitoring,
             "private_settings": privado or {}}
        if filtros is not None:
            f["filters"] = filtros
        self.fontes[nome] = f
        if nativa:
            self.nativas.add(nome)
        return f

    @staticmethod
    def filtro(dono, nome, tipo, settings, versao=None):
        return {"prev_ver": OBS_VER, "name": nome, "uuid": uid("filtro", dono, nome), "id": tipo,
                "versioned_id": versao or tipo, "settings": settings, "mixers": 255, "sync": 0,
                "flags": 0, "volume": 1.0, "balance": 0.5, "enabled": True, "muted": False,
                "push-to-mute": False, "push-to-mute-delay": 0, "push-to-talk": False,
                "push-to-talk-delay": 0, "hotkeys": {}, "deinterlace_mode": 0,
                "deinterlace_field_order": 0, "monitoring_type": 0, "private_settings": {}}

    def pagina(self, nome, arquivo, w=W, h=H):
        """Navegador com arquivo local; sem áudio e escondido no mixer."""
        return self.fonte(nome, "browser_source",
                          {"is_local_file": True, "local_file": f"{self.A}/{arquivo}",
                           "visibility": "always", "width": w, "height": h, "fps": 60,
                           "shutdown": True, "restart_when_active": False,
                           "webpage_control_level": 1, "css": CSS, "reroute_audio": False},
                          hotkeys=HK_NAV, privado={"mixer_hidden": True})

    def pagina_persistente(self, nome, arquivo, w=W, h=H):
        """Navegador que NÃO é descarregado ao sair da cena (útil para polling contínuo)."""
        return self.fonte(nome, "browser_source",
                          {"is_local_file": True, "local_file": f"{self.A}/{arquivo}",
                           "visibility": "always", "width": w, "height": h, "fps": 60,
                           "shutdown": False, "restart_when_active": False,
                           "webpage_control_level": 1, "css": CSS, "reroute_audio": False},
                          hotkeys=HK_NAV, privado={"mixer_hidden": True})

    def item(self, nome, iid, pos=(0.0, 0.0), esc=(1.0, 1.0), travado=False):
        x, y, sx, sy = f32(pos[0]), f32(pos[1]), f32(esc[0]), f32(esc[1])
        dur = 300 if nome in self.nativas else 0
        origem = self.fontes.get(nome) or self.cenas.get(nome)
        assert origem is not None, f"item: nome {nome!r} não existe como fonte nem como cena/grupo"
        return {"name": nome, "source_uuid": origem["uuid"], "visible": True,
                "locked": travado, "rot": 0.0, "scale_ref": {"x": float(W), "y": float(H)},
                "align": 5, "bounds_type": 0, "bounds_align": 0, "bounds_crop": False,
                "crop_left": 0, "crop_top": 0, "crop_right": 0, "crop_bottom": 0,
                "id": iid, "group_item_backup": False, "pos": {"x": x, "y": y},
                "pos_rel": {"x": f32((x - W / 2) / (H / 2)), "y": f32(f32(y / (H / 2)) - 1.0)},
                "scale": {"x": sx, "y": sy}, "scale_rel": {"x": sx, "y": sy},
                "bounds": {"x": 0.0, "y": 0.0}, "bounds_rel": {"x": 0.0, "y": 0.0},
                "scale_filter": "disable", "blend_method": "default", "blend_type": "normal",
                "show_transition": {"duration": dur}, "hide_transition": {"duration": dur},
                "private_settings": {}}

    def cena(self, nome, itens, id_counter, custom_size=False, grupo=False):
        if grupo:
            # grupo do OBS 32: private_settings.is_group=True e custom_size=True;
            # não tem hotkeys nem canvas (os itens do grupo são sub-fontes, não navegação).
            self.cenas[nome] = {
                "prev_ver": OBS_VER, "name": nome, "uuid": uid("cena", nome), "id": "scene",
                "versioned_id": "scene",
                "settings": {"custom_size": True, "id_counter": id_counter, "items": itens},
                "mixers": 0, "sync": 0, "flags": 0, "volume": 1.0, "balance": 0.5, "enabled": True,
                "muted": False, "push-to-mute": False, "push-to-mute-delay": 0,
                "push-to-talk": False, "push-to-talk-delay": 0, "hotkeys": {},
                "deinterlace_mode": 0, "deinterlace_field_order": 0, "monitoring_type": 0,
                "private_settings": {"is_group": True}}
            return
        hotkeys = {"OBSBasic.SelectScene": []}
        for it in itens:
            hotkeys[f"libobs.show_scene_item.{it['id']}"] = []
            hotkeys[f"libobs.hide_scene_item.{it['id']}"] = []
        self.cenas[nome] = {
            "prev_ver": OBS_VER, "name": nome, "uuid": uid("cena", nome), "id": "scene",
            "versioned_id": "scene",
            "settings": {"custom_size": custom_size, "id_counter": id_counter, "items": itens},
            "mixers": 0, "sync": 0, "flags": 0, "volume": 1.0, "balance": 0.5, "enabled": True,
            "muted": False, "push-to-mute": False, "push-to-mute-delay": 0,
            "push-to-talk": False, "push-to-talk-delay": 0, "hotkeys": hotkeys,
            "deinterlace_mode": 0, "deinterlace_field_order": 0, "monitoring_type": 0,
            "canvas_uuid": CANVAS_UUID, "private_settings": {}}

    # ── fontes ─────────────────────────────────────────────────────────────
    def montar_fontes(self):
        A = self.A
        self.pagina(N_BRB, "telas/brb.html")
        self.fonte(N_GAME, "game_capture",
                   {"window": JANELA_JOGO, "capture_mode": "window", "capture_cursor": False},
                   hotkeys=HK_JOGO)
        self.pagina(N_ENC, "telas/encerramento.html")
        self.pagina_persistente(N_PARTY, "overlay/party-tracker.html")
        self.fonte(N_STARTING, "browser_source",
                   {"is_local_file": False, "visibility": "always",
                    "url": f"file:///{A}/telas/starting-soon.html?t=10", "width": W, "height": H,
                    "fps": 60, "shutdown": True, "restart_when_active": True,
                    "webpage_control_level": 1, "css": CSS, "reroute_audio": False},
                   hotkeys=HK_NAV, privado={"mixer_hidden": True})
        self.pagina(N_CARROSSEL, "overlay/carrossel-servicos.html")
        self.pagina(N_TICKER, "overlay/ticker.html", h=72)
        self.fonte(N_ALERTAS, "browser_source",          # URL privada: colar no OBS
                   {"is_local_file": False, "visibility": "always", "url": URL_PENDENTE,
                    "width": W, "height": H, "fps": 60, "shutdown": True,
                    "restart_when_active": False, "webpage_control_level": 1, "css": CSS,
                    "reroute_audio": True},
                   volume=0.9595171809196472, mixers=1, monitoring=2, hotkeys=HK_NAV)
        self.pagina(N_OVERLAY, "overlay/overlay-gameplay.html")
        self.pagina(N_MOLD_JOGO, "overlay/moldura-jogo.html", w=492, h=260)
        self.pagina(N_MOLD_MON, "overlay/moldura-monitor.html")
        self.pagina(N_COBERTURA, "overlay/cobertura-chat.html", h=300)

        # ── DVCam (Webcam via DirectShow): device e device_name vazios para escolher
        # ── no OBS após importar; res_type=0 força captura MJPG (a webcam do canal é
        # ── USB2; sem isso o OBS pode tentar YUY2 e cair para 5 fps).
        self.fonte(N_WEBCAM, "dshow_input",
                   {"device": URL_PENDENTE, "device_name": URL_PENDENTE, "res_type": 0,
                    "resolution": "640x480", "fps": 30, "video_format": "any",
                    "audio_device": URL_PENDENTE, "audio_device_name": URL_PENDENTE,
                    "activate": False, "deactivate_when_not_showing": False,
                    "preview_only": False, "use_custom_audio_device": False},
                   hotkeys=HK_AUDIO)

        # ── moldura transparente sobreposta à webcam (mesma resolução visual)
        self.pagina(N_MOLD_WEB, "overlay/moldura-webcam.html", w=480, h=270)

        # ── contador da Twitch (browser_source 320×80, polling no proxy local)
        self.fonte(N_CONTADOR, "browser_source",
                   {"is_local_file": True,
                    "local_file": f"{self.A}/overlay/contador-twitch.html",
                    "url": URL_PENDENTE, "visibility": "always",
                    "width": 320, "height": 80, "fps": 30,
                    "shutdown": False, "restart_when_active": False,
                    "webpage_control_level": 1, "css": CSS, "reroute_audio": False},
                   hotkeys=HK_NAV, privado={"mixer_hidden": True})

    def montar_fontes_nativas(self):
        """Fontes criadas direto no OBS 32 (captura de tela, áudio e widget LivePix)."""
        self.fonte(N_MONITOR, "monitor_capture", {"method": 2, "monitor_id": MONITOR_ID},
                   nativa=True)
        self.fonte(N_DISCORD, "wasapi_process_output_capture",
                   {"window": "Amigos - Discord:Chrome_WidgetWin_1:Discord.exe", "priority": 2},
                   volume=0.7699615359306335, mixers=255, muted=True, hotkeys=HK_AUDIO,
                   nativa=True, filtros=[
                       self.filtro(N_DISCORD, "Supressão de ruídos", "noise_suppress_filter", {},
                                   "noise_suppress_filter_v2"),
                       self.filtro(N_DISCORD, "Filtro de ruídos", "noise_gate_filter",
                                   {"open_threshold": -29.0, "close_threshold": -30.0}),
                       self.filtro(N_DISCORD, "Compressor", "compressor_filter", {"ratio": 3.0})])
        self.fonte(N_MIC, "wasapi_input_capture", {"device_id": MIC_DEVICE_ID},
                   mixers=255, hotkeys=HK_AUDIO, nativa=True, filtros=[
                       self.filtro(N_MIC, "Supressão de ruídos", "noise_suppress_filter", {},
                                   "noise_suppress_filter_v2"),
                       self.filtro(N_MIC, "Filtro de ruídos", "noise_gate_filter",
                                   {"open_threshold": -31.0, "close_threshold": -32.0,
                                    "attack_time": 40, "hold_time": 400, "release_time": 100}),
                       self.filtro(N_MIC, "Limitador", "limiter_filter", {"threshold": -3.0}),
                       self.filtro(N_MIC, "Compressor", "compressor_filter",
                                   {"ratio": 3.0, "attack_time": 3, "release_time": 100})])
        self.fonte(N_NAV, "wasapi_process_output_capture",
                   {"window": "Commands - Opera:Chrome_WidgetWin_1:opera.exe", "priority": 2},
                   volume=0.7963038086891174, mixers=255, hotkeys=HK_AUDIO, nativa=True)
        self.fonte(N_SPOTIFY, "wasapi_process_output_capture",
                   {"window": "Spotify Premium:Chrome_WidgetWin_1:Spotify.exe", "priority": 2},
                   volume=0.7176818251609802, mixers=255, hotkeys=HK_AUDIO, nativa=True)
        self.fonte(N_LIVEPIX, "browser_source",          # URL privada: colar no OBS
                   {"url": URL_PENDENTE, "width": 240, "height": 320, "reroute_audio": True},
                   mixers=255, hotkeys=HK_NAV, nativa=True)

    # ── cenas (ordem do array = fundo -> topo) ──────────────────────────────
    def montar_cenas(self):
        i = self.item
        # ── GRUPO: webcam+moldura sempre se movem juntas. Criado ANTES da cena 02
        # ── para que o id do item do grupo (12) seja referência válida em cena 02.
        self.cena(N_GRP_WEB, [
            i(N_WEBCAM, 1),
            i(N_MOLD_WEB, 2)], id_counter=3, grupo=True)

        self.cena("01 · STARTING", [
            i(N_GAME, 1), i(N_STARTING, 2), i(N_CARROSSEL, 3, travado=True),
            i(N_TICKER, 4, POS_TICKER), i(N_ALERTAS, 10, POS_ALERTA, ESC_ALERTA),
            i(N_SPOTIFY, 11)], id_counter=11)
        self.cena("02 · GAMEPLAY", [
            i(N_GAME, 1, travado=True), i(N_COBERTURA, 2, POS_COBERTURA),
            i(N_OVERLAY, 3), i(N_PARTY, 4),
            i(N_CARROSSEL, 5, POS_CAR_GP, ESC_CAR_GP, travado=True),
            i(N_LIVEPIX, 6, POS_LIVEPIX_GP, ESC_LIVEPIX_GP),
            i(N_GRP_WEB, 12, POS_WEB, ESC_WEB),
            i(N_CONTADOR, 13, POS_TW, ESC_TW),
            i(N_ALERTAS, 14, POS_ALERTA, ESC_ALERTA), i(N_TICKER, 7, POS_TICKER),
            i(N_SPOTIFY, 15), i(N_DISCORD, 16), i(N_MIC, 17)], id_counter=17)
        self.cena("04 · BRB", [
            i(N_GAME, 1, travado=True), i(N_BRB, 2), i(N_CARROSSEL, 3, travado=True),
            i(N_TICKER, 4, POS_TICKER), i(N_ALERTAS, 10, POS_ALERTA, ESC_ALERTA),
            i(N_SPOTIFY, 11), i(N_MIC, 12), i(N_LIVEPIX, 13, POS_LIVEPIX_BRB)], id_counter=13)
        self.cena("05 · ENCERRAMENTO", [
            i(N_GAME, 1, travado=True), i(N_ENC, 2), i(N_CARROSSEL, 3, travado=True),
            i(N_TICKER, 4, POS_TICKER), i(N_SPOTIFY, 10)], id_counter=10)
        self.cena("06 · TELA", [
            i(N_MONITOR, 13), i(N_GAME, 3, POS_TIBIA_MINI, ESC_TIBIA_MINI),
            i(N_MOLD_JOGO, 5, POS_MOLD_JOGO, ESC_MOLD_JOGO), i(N_MOLD_MON, 4),
            i(N_ALERTAS, 6, POS_ALERTA, ESC_ALERTA), i(N_TICKER, 7, POS_TICKER),
            i(N_NAV, 14), i(N_SPOTIFY, 15), i(N_MIC, 16), i(N_DISCORD, 17)], id_counter=17)

    # ── coleção completa ────────────────────────────────────────────────────
    def montar(self):
        self.montar_fontes()
        n_base = len(self.fontes)          # as cenas ficam entre as fontes-base e as nativas
        self.montar_fontes_nativas()
        self.montar_cenas()
        todas = list(self.fontes.values())
        grupos = [c for n, c in self.cenas.items()
                  if c.get("private_settings", {}).get("is_group")]
        sources = todas[:n_base] + [self.cenas[n] for n in CENAS] + todas[n_base:] + grupos
        return {
            "name": "EXORISERVICE",
            "groups": [],
            "scene_order": [{"name": n} for n in ORDEM_NO_OBS],
            "current_scene": CENAS[0],
            "current_program_scene": CENAS[0],
            "canvases": [],
            "current_transition": "Limpar",
            "transition_duration": 1500,
            "transitions": [
                {"name": "Limpar", "id": "wipe_transition", "settings": {"luma_softness": 1.0}},
                # chaves que o OBS lê no stinger: path / tp_type (0 = ms) / transition_point (ms).
                # O vídeo tem 44 quadros a 60 fps; a tela fica 100% coberta nos quadros 16-27,
                # então a troca de cena ocorre no meio (quadro 22 = 367 ms). Decodificação por
                # software (hw_decode False) para preservar o canal alfa do WebM.
                {"name": "⚡ STINGER EXORI", "id": "obs_stinger_transition",
                 "settings": {"path": f"{self.A}/stinger/stinger-transicao.webm",
                              "hw_decode": False, "tp_type": 0, "transition_point": 367}},
            ],
            "quick_transitions": [],
            "saved_projectors": [],
            "preview_locked": False,
            "scaling_enabled": True,
            "scaling_level": -11,
            "scaling_off_x": 0.0,
            "scaling_off_y": 11.0,
            "virtual-camera": {"type2": 3},
            "modules": {
                "scripts-tool": [],
                "output-timer": {"streamTimerHours": 0, "streamTimerMinutes": 0,
                                 "streamTimerSeconds": 0, "recordTimerHours": 0,
                                 "recordTimerMinutes": 0, "recordTimerSeconds": 0,
                                 "autoStartStreamTimer": False, "autoStartRecordTimer": False,
                                 "pauseRecordTimer": False},
                "auto-scene-switcher": {"interval": 300, "non_matching_scene": "",
                                        "switch_if_not_matching": False, "active": False,
                                        "switches": []},
                "captions": {"source": "", "enabled": False, "lang_id": 1046,
                             "provider": "mssapi"},
            },
            "resolution": {"x": W, "y": H},
            "version": 2,
            "sources": sources,
        }


def validar(col):
    """Checagens estáticas (não há OBS aqui): referências, ids e hotkeys coerentes."""
    fontes = col["sources"]
    nomes = [s["name"] for s in fontes]
    uuids = [s["uuid"] for s in fontes] + [f["uuid"] for s in fontes for f in s.get("filters", [])]
    assert len(nomes) == len(set(nomes)), "nomes de fonte duplicados"
    assert len(uuids) == len(set(uuids)), "UUIDs duplicados"
    por_uuid = {s["uuid"]: s for s in fontes}
    cenas = [s for s in fontes if s["id"] == "scene"]
    # grupo do OBS tem id "scene" mas não é uma cena navegável: excluir do scene_order
    nomes_cenas = {c["name"] for c in cenas
                   if not c.get("private_settings", {}).get("is_group")}
    assert {o["name"] for o in col["scene_order"]} == nomes_cenas, "scene_order != cenas"
    assert col["current_scene"] in nomes_cenas and col["current_program_scene"] in nomes_cenas
    assert col["current_transition"] in {t["name"] for t in col["transitions"]} | {"Corte", "Fade"}
    avisos = []
    for c in cenas:
        its = c["settings"]["items"]
        ids = [it["id"] for it in its]
        assert len(ids) == len(set(ids)), f"{c['name']}: ids de item repetidos"
        assert c["settings"]["id_counter"] >= max(ids), f"{c['name']}: id_counter baixo"
        for it in its:
            src = por_uuid.get(it["source_uuid"])
            assert src is not None, f"{c['name']}: item órfão {it['name']}"
            assert src["name"] == it["name"], f"{c['name']}: nome do item != fonte"
        usados = [it["source_uuid"] for it in its]
        if len(usados) != len(set(usados)):
            avisos.append(f"{c['name']}: a mesma fonte aparece mais de uma vez na cena")
        if c.get("private_settings", {}).get("is_group"):
            # grupo não tem hotkeys de navegação (cena -> SelectScene, item -> show/hide)
            assert c["hotkeys"] == {}, f"{c['name']}: grupo não deve ter hotkeys"
            continue
        esperado = {"OBSBasic.SelectScene"} | {f"libobs.{a}_scene_item.{n}" for n in ids
                                               for a in ("show", "hide")}
        assert set(c["hotkeys"]) == esperado, f"{c['name']}: hotkeys incoerentes"
    for s in fontes:
        st = s["settings"]
        assert isinstance(st, dict), f"{s['name']}: settings deve ser objeto (era string?)"
        url = st.get("url")
        if url and url != URL_PENDENTE and not url.startswith("file:///"):
            avisos.append(f"{s['name']}: URL externa no arquivo; não versionar no repositório")
    return avisos


def main():
    ap = argparse.ArgumentParser(description="Gera a coleção de cenas do OBS (EXORISERVICE).")
    ap.add_argument("--base", default=BASE_PADRAO, help="pasta no PC com assets/ (padrão %(default)s)")
    ap.add_argument("--saida", default=str(AQUI / "exoriservice-cenas.json"), help="arquivo de saída")
    a = ap.parse_args()

    col = Colecao(a.base).montar()
    avisos = validar(col)
    saida = Path(a.saida)
    saida.parent.mkdir(parents=True, exist_ok=True)
    with open(saida, "w", encoding="utf-8", newline="\n") as f:
        json.dump(col, f, ensure_ascii=False, indent=4)
        f.write("\n")
    with open(saida, encoding="utf-8") as f:       # relê para garantir JSON válido
        data = json.load(f)
    cenas = [s for s in data["sources"] if s["id"] == "scene"]
    itens = sum(len(c["settings"]["items"]) for c in cenas)
    print(f"OK - JSON valido: {len(cenas)} cenas, {len(data['sources']) - len(cenas)} fontes, {itens} itens")
    for av in avisos:
        print("AVISO:", av)
    print("arquivo:", saida)


if __name__ == "__main__":
    main()
