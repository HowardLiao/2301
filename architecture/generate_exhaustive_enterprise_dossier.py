#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_exhaustive_enterprise_dossier.py
Builds an interactive, publication-grade enterprise architecture dossier and HTML portal
STRICTLY HARMONIZED WITH LITEON MAIN SITE (Milan Warm Amber / Egyptian Pharaoh Style):
- 100% interactive diagrams and cards: Click to inspect details (點圖出現說明).
- Dual interactive top cards:
  1. 7 Core Mandates (interactive stack)
  2. Howard Security 4 Pillars (interactive stack)
- Interactive 5 SVG Architecture Blueprints:
  Every layer and component is clickable with a live Dynamic Component Inspector.
- Milan Warm Amber design tokens: --bg (#FAF7F2), --green (#2F4538), --gold (#C8A96A), --line (#B8AFA3), --card (#FFFFFF).
- Shared dark-mode toggle (prefers-color-scheme & data-theme="dark" with localStorage sync).
- Repeating Howard Liao Ph.D. watermark matching index.html.
- Mobile friendly with touch-optimized ergonomics and floating dock.
- Zero vendor/client specific branding.
- Authored by Howard Liao Ph.D.

Author: Howard Liao Ph.D.
"""

import html
import subprocess
import os

from build_full_visual_html import (
    generate_svg_page1,
    generate_svg_page2,
    generate_svg_page3,
    generate_svg_page4,
    generate_svg_page5
)

def build_dossier():
    svg1 = generate_svg_page1()
    svg2 = generate_svg_page2()
    svg3 = generate_svg_page3()
    svg4 = generate_svg_page4()
    svg5 = generate_svg_page5()

    html_content = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
<meta name="robots" content="noindex, nofollow">
<title>企業級 AI 平台 ＆ Howard 資安前瞻戰略全域工程白皮書｜廖倫豪 博士</title>
<meta name="description" content="致光寶科技董事長暨資訊長：企業級 AI 平台架構師 ＆ Howard 資安前瞻戰略全域工程白皮書，包含 5 大高解析向量互動架構圖、參數字典與合規矩陣。">
<meta name="theme-color" content="#2F4538">
<style>
  :root {{
    --bg: #FAF7F2;
    --alt: #F2EEE8;
    --label: #E8E2D9;
    --line: #B8AFA3;
    --ink: #2B2B2B;
    --mute: #6B6459;
    --green: #2F4538;
    --green2: #3E5A4A;
    --gold: #C8A96A;
    --brick: #9C5B4A;
    --white: #FFFFFF;
    --card: #FFFFFF;
    --card-inner: #F8F5EE;
  }}
  @media (prefers-color-scheme: dark) {{
    :root:not([data-theme="light"]) {{
      --bg: #1C211E;
      --alt: #232A26;
      --label: #2C342F;
      --line: #4A524C;
      --ink: #ECE7DF;
      --mute: #B3AC9F;
      --green: #A9C2B1;
      --green2: #8FAE9A;
      --gold: #D4B87C;
      --brick: #D08E7C;
      --card: #242B27;
      --card-inner: #1C211E;
    }}
  }}
  :root[data-theme="dark"] {{
    --bg: #1C211E;
    --alt: #232A26;
    --label: #2C342F;
    --line: #4A524C;
    --ink: #ECE7DF;
    --mute: #B3AC9F;
    --green: #A9C2B1;
    --green2: #8FAE9A;
    --gold: #D4B87C;
    --brick: #D08E7C;
    --card: #242B27;
    --card-inner: #1C211E;
  }}

  * {{ box-sizing: border-box; }}
  html {{ scroll-behavior: smooth; -webkit-text-size-adjust: 100%; }}
  body {{
    margin: 0;
    background: var(--bg);
    color: var(--ink);
    font-family: "Noto Sans TC", "Microsoft JhengHei", "PingFang TC", sans-serif;
    line-height: 1.75;
    font-size: 16px;
    position: relative;
  }}
  .serif {{ font-family: "Cormorant Garamond", Georgia, serif; }}
  a {{ color: var(--green); text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}

  /* Repeating Watermark matching index.html */
  body::before {{
    content: "Howard Liao Ph.D.  ";
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    z-index: 0;
    pointer-events: none;
    font-family: "Cormorant Garamond", serif;
    font-size: 26px;
    color: var(--gold);
    opacity: 0.055;
    line-height: 150px;
    letter-spacing: 25px;
    transform: rotate(-22deg);
    white-space: pre-wrap;
    word-break: break-all;
    overflow: hidden;
  }}

  /* Sticky Header Navigation matching index.html */
  header.nav {{
    position: sticky;
    top: 0;
    z-index: 100;
    background: color-mix(in srgb, var(--bg) 92%, transparent);
    backdrop-filter: blur(8px);
    border-bottom: 1px solid var(--line);
  }}
  .nav .in {{
    max-width: 1280px;
    margin: auto;
    display: flex;
    align-items: center;
    gap: 18px;
    padding: 10px 16px;
  }}
  .brand {{
    font-weight: 700;
    color: var(--green);
    white-space: nowrap;
    text-decoration: none;
  }}
  .brand small {{
    color: var(--gold);
    font-family: "Cormorant Garamond", serif;
    font-size: 15px;
    margin-left: 6px;
    letter-spacing: .06em;
  }}

  .links {{
    display: flex;
    gap: 6px;
    align-items: center;
    flex: 1;
    min-width: 0;
    overflow: visible;
  }}
  .nav-item {{ position: relative; }}
  .nav-link {{
    display: inline-flex;
    align-items: center;
    gap: 4px;
    white-space: nowrap;
    text-decoration: none;
    color: var(--mute);
    font-size: 14px;
    padding: 6px 14px;
    border-radius: 999px;
    transition: all .2s ease;
    font-weight: 500;
  }}
  .nav-link .arr {{ font-size: 10px; opacity: .6; transition: transform .2s ease; }}
  .nav-item:hover .nav-link .arr {{ transform: rotate(180deg); }}
  .nav-link.on, .nav-link:hover {{
    background: var(--label);
    color: var(--green);
    font-weight: 600;
  }}
  .nav-drop {{
    display: none;
    position: absolute;
    top: calc(100% + 4px);
    left: 0;
    background: var(--card);
    border: 1px solid var(--line);
    box-shadow: 0 12px 30px rgba(0,0,0,.15);
    border-radius: 10px;
    padding: 6px;
    min-width: 170px;
    z-index: 100;
    flex-direction: column;
  }}
  .nav-item:hover .nav-drop, .nav-item:focus-within .nav-drop {{
    display: flex;
    animation: dropFade .2s ease;
  }}
  @keyframes dropFade {{
    from {{ opacity: 0; transform: translateY(-4px); }}
    to {{ opacity: 1; transform: translateY(0); }}
  }}
  .nav-drop a {{
    padding: 8px 14px;
    font-size: 13.5px;
    color: var(--ink);
    text-decoration: none;
    border-radius: 6px;
    white-space: nowrap;
    display: block;
    transition: background .15s ease, color .15s ease;
  }}
  .nav-drop a:hover {{
    background: var(--label);
    color: var(--green);
  }}

  .langs {{
    display: flex;
    gap: 2px;
    border: 1px solid var(--line);
    border-radius: 999px;
    padding: 2px;
  }}
  .langs a {{
    font-size: 12px;
    text-decoration: none;
    color: var(--mute);
    padding: 3px 9px;
    border-radius: 999px;
    white-space: nowrap;
  }}
  .langs a.on {{
    background: var(--green);
    color: var(--bg);
  }}
  .tbtn {{
    border: 1px solid var(--line);
    background: transparent;
    color: var(--ink);
    border-radius: 999px;
    padding: 5px 12px;
    cursor: pointer;
    font: inherit;
    font-size: 13px;
  }}

  /* Page Layout */
  main {{
    max-width: 1280px;
    margin: auto;
    padding: 30px 16px 80px;
    position: relative;
    z-index: 1;
  }}

  /* Milan Warm Amber Header Card */
  .header-card {{
    background: var(--card);
    border: 1px solid var(--line);
    border-top: 4px solid var(--gold);
    border-radius: 12px;
    padding: 32px 30px;
    margin-bottom: 24px;
    box-shadow: 0 8px 24px rgba(43,43,43,0.05);
  }}
  .eyebrow {{
    font-family: "Cormorant Garamond", serif;
    color: var(--gold);
    letter-spacing: .18em;
    font-size: 14px;
    text-transform: uppercase;
    font-weight: 700;
    margin-bottom: 8px;
    display: inline-block;
  }}
  h1 {{
    font-size: clamp(24px, 3.8vw, 36px);
    line-height: 1.25;
    color: var(--green);
    margin: 4px 0 14px;
    font-weight: 800;
  }}
  .meta-bar {{
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
    font-size: 14px;
    color: var(--mute);
    padding-bottom: 16px;
    margin-bottom: 16px;
    border-bottom: 1px solid var(--label);
  }}
  .meta-bar b {{ color: var(--green); font-weight: 700; }}

  .download-bar {{
    display: flex;
    gap: 12px;
    margin-top: 20px;
    flex-wrap: wrap;
  }}
  .btn-action {{
    background: var(--green);
    color: var(--bg) !important;
    font-weight: 700;
    text-decoration: none;
    padding: 11px 22px;
    border-radius: 8px;
    font-size: 13.5px;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    transition: all 0.2s;
    min-height: 44px;
  }}
  .btn-action:hover {{
    background: var(--green2);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(47,69,56,0.25);
  }}
  .btn-outline {{
    background: var(--card);
    border: 1px solid var(--line);
    color: var(--ink);
    font-weight: 600;
    text-decoration: none;
    padding: 11px 18px;
    border-radius: 8px;
    font-size: 13px;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    min-height: 44px;
  }}

  /* Interactive Top Section Grid */
  .interactive-deck-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 22px;
    margin-bottom: 24px;
  }}
  .interactive-deck-card {{
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 12px;
    padding: 22px;
    box-shadow: 0 4px 16px rgba(43,43,43,0.04);
    display: flex;
    flex-direction: column;
  }}
  .deck-header {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 12px;
    padding-bottom: 10px;
    border-bottom: 1px solid var(--label);
  }}
  .deck-header h3 {{
    margin: 0;
    font-size: 17px;
    font-weight: 700;
    color: var(--green);
  }}
  .deck-hint {{
    font-size: 12px;
    color: var(--gold);
    font-weight: 600;
  }}

  /* Clickable Pills & Stack Layer List */
  .interactive-layers {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
    gap: 8px;
    margin-bottom: 14px;
  }}
  .layer-btn {{
    display: flex;
    align-items: center;
    gap: 8px;
    width: 100%;
    text-align: left;
    border: 1px solid var(--line);
    background: var(--card-inner);
    padding: 9px 12px;
    border-radius: 8px;
    cursor: pointer;
    font: inherit;
    font-size: 13px;
    color: var(--ink);
    transition: all 0.2s ease;
  }}
  .layer-btn b {{
    font-family: "Cormorant Garamond", serif;
    font-size: 16px;
    color: var(--gold);
  }}
  .layer-btn:hover {{
    background: var(--label);
    color: var(--green);
  }}
  .layer-btn.on {{
    background: var(--green);
    color: var(--bg);
    border-color: var(--green2);
  }}
  .layer-btn.on b {{
    color: var(--gold);
  }}

  /* Dynamic Detail Box */
  .detail-box {{
    background: var(--card-inner);
    border: 1px solid var(--line);
    border-radius: 8px;
    padding: 18px 20px;
    border-left: 4px solid var(--gold);
    animation: fadeIn 0.25s ease;
    flex: 1;
  }}
  .detail-box .eyebrow {{
    margin-bottom: 4px;
  }}
  .detail-box h4 {{
    margin: 0 0 10px 0;
    color: var(--green);
    font-size: 16px;
  }}
  .detail-box p {{
    margin: 0 0 8px 0;
    font-size: 14px;
    color: var(--ink);
    line-height: 1.6;
  }}

  /* Interactive Tab System with Mobile Ergonomics */
  .tab-system-card {{
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 14px;
    padding: 26px;
    margin-top: 24px;
    box-shadow: 0 8px 25px rgba(43,43,43,0.05);
  }}
  .tab-nav-wrapper {{
    position: relative;
    margin-bottom: 20px;
  }}
  .tab-nav {{
    display: flex;
    gap: 10px;
    border-bottom: 2px solid var(--label);
    padding-bottom: 14px;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
    scroll-snap-type: x mandatory;
  }}
  .tab-nav::-webkit-scrollbar {{ display: none; }}
  
  .tab-btn {{
    background: var(--alt);
    border: 1px solid var(--line);
    color: var(--mute);
    padding: 11px 18px;
    border-radius: 8px;
    font-size: 13.5px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.2s;
    white-space: nowrap;
    display: flex;
    align-items: center;
    gap: 8px;
    min-height: 44px;
    scroll-snap-align: start;
    font-family: inherit;
  }}
  .tab-btn:hover {{
    background: var(--label);
    color: var(--green);
  }}
  .tab-btn.active {{
    background: var(--green);
    color: var(--bg);
    border-color: var(--green2);
    box-shadow: 0 4px 12px rgba(47,69,56,0.3);
  }}
  .tab-text-mobile {{ display: none; }}

  /* Diagram Blueprint Console */
  .diagram-toolbar {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: var(--alt);
    border: 1px solid var(--line);
    border-bottom: none;
    border-radius: 10px 10px 0 0;
    padding: 10px 14px;
    flex-wrap: wrap;
    gap: 8px;
  }}
  .view-mode-group {{
    display: flex;
    gap: 6px;
    align-items: center;
  }}
  .mode-btn {{
    background: var(--card);
    border: 1px solid var(--line);
    color: var(--ink);
    padding: 6px 12px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.2s;
    min-height: 34px;
    display: inline-flex;
    align-items: center;
    gap: 5px;
    font-family: inherit;
  }}
  .mode-btn:hover {{ background: var(--label); color: var(--green); }}
  .mode-btn.active {{
    background: var(--green);
    color: var(--bg);
    border-color: var(--green2);
  }}
  .diagram-hint {{
    font-size: 12.5px;
    color: var(--green);
    font-weight: 700;
  }}

  /* Diagram Scroll Container */
  .diagram-scroll-container {{
    background: #0B0F17; /* High-contrast blueprint console */
    border: 1px solid var(--line);
    border-radius: 0 0 10px 10px;
    padding: 16px;
    margin-bottom: 24px;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    box-shadow: inset 0 2px 10px rgba(0,0,0,0.4);
  }}
  .diagram-scroll-container svg {{
    display: block;
    width: 100%;
    height: auto;
    border-radius: 8px;
    transition: min-width 0.25s ease;
  }}
  .diagram-scroll-container.mode-scroll svg {{
    min-width: 1100px;
    width: 1100px;
  }}

  /* Interactive Component Inspector Panel */
  .inspector-card {{
    background: var(--card);
    border: 1px solid var(--line);
    border-top: 4px solid var(--gold);
    border-radius: 12px;
    padding: 24px;
    margin: 18px 0 26px 0;
    box-shadow: 0 6px 20px rgba(43,43,43,0.06);
    animation: fadeIn 0.25s ease;
  }}
  .ins-header {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    border-bottom: 1px solid var(--label);
    padding-bottom: 14px;
    margin-bottom: 16px;
    flex-wrap: wrap;
    gap: 10px;
  }}
  .ins-header-main {{ flex: 1; }}
  .ins-layer-badge {{
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    color: var(--gold);
    letter-spacing: 0.8px;
    margin-bottom: 4px;
    display: block;
    font-family: "Cormorant Garamond", serif;
  }}
  .ins-header h3 {{
    margin: 0;
    font-size: 20px;
    font-weight: 800;
    color: var(--green);
  }}
  .ins-tag {{
    font-size: 11.5px;
    padding: 4px 10px;
    border-radius: 6px;
    background: var(--label);
    color: var(--green);
    font-weight: 700;
  }}

  .ins-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-bottom: 16px;
  }}
  .ins-col {{
    background: var(--card-inner);
    border: 1px solid var(--line);
    border-radius: 8px;
    padding: 14px 16px;
  }}
  .ins-col h4 {{
    margin: 0 0 6px 0;
    font-size: 13.5px;
    color: var(--gold);
    display: flex;
    align-items: center;
    gap: 6px;
    font-weight: 700;
  }}
  .ins-col p {{
    margin: 0;
    font-size: 13.5px;
    color: var(--ink);
    line-height: 1.6;
  }}
  .ins-config-code {{
    font-family: monospace;
    font-size: 12px;
    background: var(--card);
    border: 1px solid var(--line);
    padding: 6px 10px;
    border-radius: 4px;
    color: var(--green);
    display: block;
    margin-top: 6px;
    line-height: 1.5;
  }}
  .ins-full-sop {{
    background: var(--card-inner);
    border: 1px solid var(--line);
    border-left: 4px solid var(--green);
    border-radius: 8px;
    padding: 14px 16px;
  }}
  .ins-full-sop h4 {{
    margin: 0 0 6px 0;
    font-size: 13.5px;
    color: var(--green);
    font-weight: 700;
  }}
  .ins-full-sop p {{
    margin: 0;
    font-size: 13.5px;
    color: var(--ink);
    line-height: 1.6;
  }}

  /* Mobile Floating Dock */
  .mobile-dock {{
    display: none;
    position: fixed;
    bottom: 16px;
    left: 16px;
    right: 16px;
    z-index: 1000;
    background: color-mix(in srgb, var(--bg) 94%, transparent);
    backdrop-filter: blur(12px);
    border: 1px solid var(--gold);
    border-radius: 30px;
    padding: 8px 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.18);
    justify-content: space-around;
    align-items: center;
  }}
  .dock-btn {{
    background: transparent;
    border: none;
    color: var(--ink);
    font-size: 12.5px;
    font-weight: 700;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 8px 12px;
    border-radius: 20px;
    min-height: 40px;
    text-decoration: none;
  }}
  .dock-btn.highlight {{
    background: var(--green);
    color: var(--bg);
  }}

  footer {{
    padding: 50px 16px 40px;
    text-align: center;
    color: var(--mute);
    font-size: 13px;
    border-top: 1px solid var(--line);
    margin-top: 40px;
  }}

  @keyframes fadeIn {{
    from {{ opacity: 0; transform: translateY(4px); }}
    to {{ opacity: 1; transform: translateY(0); }}
  }}

  /* Mobile Responsive Media Queries */
  @media (max-width: 768px) {{
    main {{
      padding: 16px 10px 85px;
    }}
    .header-card {{
      padding: 22px 16px;
      margin-bottom: 16px;
    }}
    .interactive-deck-grid {{
      grid-template-columns: 1fr;
      gap: 16px;
    }}
    .ins-grid {{
      grid-template-columns: 1fr;
    }}
    .tab-system-card {{
      padding: 18px 12px;
    }}
    .tab-text-full {{ display: none; }}
    .tab-text-mobile {{ display: inline; }}
    .tab-btn {{
      padding: 10px 14px;
      font-size: 13px;
    }}
    .download-bar {{
      flex-direction: column;
    }}
    .btn-action, .btn-outline {{
      width: 100%;
      justify-content: center;
    }}
    .mobile-dock {{
      display: flex;
    }}
  }}
</style>
<script>
  // Theme sync with index.html
  try {{
    const t = localStorage.getItem('t');
    if (t) document.documentElement.dataset.theme = t;
  }} catch(e) {{}}

  function toggleTheme() {{
    const d = document.documentElement;
    const cur = d.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    d.dataset.theme = cur === 'dark' ? 'light' : 'dark';
    try {{ localStorage.setItem('t', d.dataset.theme); }} catch(e) {{}}
  }}

  function selectTab(idx) {{
    const btns = document.querySelectorAll('.tab-btn');
    const panes = document.querySelectorAll('.tab-pane');
    btns.forEach((b, i) => {{
      if (i === idx) {{
        b.classList.add('active');
        b.scrollIntoView({{ behavior: 'smooth', block: 'nearest', inline: 'center' }});
      }} else {{
        b.classList.remove('active');
      }}
    }});
    panes.forEach((p, i) => {{
      if (i === idx) {{
        p.style.display = 'block';
      }} else {{
        p.style.display = 'none';
      }}
    }});
  }}

  function toggleDiagramMode(mode, btn) {{
    const container = btn.closest('.tab-pane').querySelector('.diagram-scroll-container');
    const btns = btn.parentElement.querySelectorAll('.mode-btn');
    btns.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    if (mode === 'scroll') {{
      container.classList.add('mode-scroll');
    }} else {{
      container.classList.remove('mode-scroll');
    }}
  }}

  function cycleNextTab() {{
    const btns = document.querySelectorAll('.tab-btn');
    let activeIdx = 0;
    btns.forEach((b, i) => {{ if (b.classList.contains('active')) activeIdx = i; }});
    const nextIdx = (activeIdx + 1) % btns.length;
    selectTab(nextIdx);
    document.querySelector('.tab-system-card').scrollIntoView({{ behavior: 'smooth' }});
  }}

  // Interactive Top Deck 1: 7 Duties Data
  const DUTIES = [
    {{
      id: "01",
      title: "1. AI 平台架構與核心中樞",
      tag: "Platform Core",
      desc: "設計並持續演進企業級 AI Agent Platform。抽離 LLM Gateway、動態語意路由、全鏈路可觀測性、即時安全防護與配額限額治理，橫跨 GCP/AWS 混合雲與地端機房，讓新用例照範本在數週內上線。",
      metric: "新用例上線週期由「月」縮短為「週」｜LLM 呼叫延遲 &lt; 20ms",
      spec: "支援 LiteLLM/Portkey 閘道架構，整合 Redis 語意快取，單月降低重複 Token 支出達 38.5% 以上。"
    }},
    {{
      id: "02",
      title: "2. 地端 AIDC 機房建置與維運",
      tag: "AIDC & Infra",
      desc: "評估 GPU 機型（NVIDIA H100/H200 SXM5 與 AMD MI300X）與容量規劃。在 K8s 叢集導入 Volcano 智慧排程器，實施 NVIDIA MIG 資源切片、多租戶配額隔離與部門用量計費。",
      metric: "GPU 綜合利用率提升至 85% 以上｜資料 100% 地端留存符合法規",
      spec: "配置 400Gbps RoCE v2 無損網路拓撲與 GPUDirect RDMA，推論吞吐量達 80+ tokens/sec。"
    }},
    {{
      id: "03",
      title: "3. 模型選型、推論與微調",
      tag: "LLM & vLLM",
      desc: "評估商用與開源大語言模型（DeepSeek-R1、Llama-3.3-70B、Qwen-2.5）。主導推論服務（vLLM / Triton）部署、連續批處理調優與領域微調（LoRA / SFT）架構規劃。",
      metric: "首字生成延遲 (TTFT) &lt; 300ms｜長文本推論吞吐量提升 3.2 倍",
      spec: "生產環境最佳化參數：--gpu-memory-utilization 0.92, --kv-cache-dtype fp8, --max-num-seqs 256。"
    }},
    {{
      id: "04",
      title: "4. Agent 流程設計與工具串接",
      tag: "Agentic Workflow",
      desc: "與人資、財務、電商營運、智慧製造等各事業群釐清真實業務痛點，設計 Agent Workflow（ReAct 狀態機）、Hybrid RAG（向量+關鍵字混合檢索）與 MCP 工具標準串接。",
      metric: "核心營運流程自動化效率提升 +55%｜RAG 召回準確率 &gt; 92%",
      spec: "遵循 Model Context Protocol (MCP) 標準，所有外部 API 工具調用皆經隔離沙箱執行。"
    }},
    {{
      id: "05",
      title: "5. 雲地 Infra 與自動化維運",
      tag: "GitOps & SRE",
      desc: "操盤混合雲網路、CI/CD 自動化發布流水線、GitOps（ArgoCD）與跨雲跨機房 DR 災難復原架構。實踐 AIOps 告警智慧降噪分流與突發事件自動調查處置。",
      metric: "平台可用度 99.99% (Zero Outage)｜目標 RTO &lt; 1hr, RPO ≈ 0",
      spec: "全基礎設施採用 Terraform IaC 宣告式版本受控，CI/CD 流水線強制嵌入安全弱點掃描關卡。"
    }},
    {{
      id: "06",
      title: "6. AI 成本治理 (FinOps)",
      tag: "FinOps",
      desc: "建立即時 Token、GPU 算力與模型用量之可視化 Chargeback 儀表板。落實部門配額管理、動態降級優化與語意快取，精確測算每一筆算力投資的財務回報率。",
      metric: "3 年多雲與算力 TCO 降低 42.8%｜財務長定期審核確認效益",
      spec: "自動化用量標籤（Cost Allocation Tags）全覆蓋，高相似度 Prompt 直接秒級輸出快取結果。"
    }},
    {{
      id: "07",
      title: "7. 架構標準與技術領導",
      tag: "Leadership",
      desc: "制定企業 AI 開發規範與架構標準，帶領 AI Developer 與技術主管落地實戰。擔任各事業單位提出 AI 需求的第一技術窗口，建立內部 Champions 種子網絡與 PO 學院。",
      metric: "第一年培養 30 位內部認證 PO｜每位技術主管皆有接班梯隊",
      spec: "符合 ISO 42001（AIMS）人工智慧管理體系與 ISO 27001 資安規範，平衡創新速度與治理紅線。"
    }}
  ];

  function showDuty(idx) {{
    document.querySelectorAll('#duty-layers .layer-btn').forEach((b, i) => {{
      b.classList.toggle('on', i === idx);
    }});
    const d = DUTIES[idx];
    document.getElementById('duty-box').innerHTML = `
      <span class="eyebrow">${{d.id}} · MANDATE SPECIFICATION</span>
      <h4>${{d.title}}</h4>
      <p><b>工程任務：</b>${{d.desc}}</p>
      <p><b>量化指標：</b><span style="color:var(--green);font-weight:700;">${{d.metric}}</span></p>
      <p><b>架構規格：</b>${{d.spec}}</p>
    `;
  }}

  // Interactive Top Deck 2: 4 Security Pillars Data
  const PILLARS = [
    {{
      id: "P1",
      title: "1. 現代周界入口：Howard Enterprise Browser",
      tag: "Enterprise Browser",
      desc: "從傳統防禦作業系統二進制檔案（PE/ELF），跨越至治理「現代軟體周界」（瀏覽器外掛、IDE 擴充套件、MCP 工具、開源套件）。第一時間在端點掐斷影子工具投毒。",
      threat: "惡意 VS Code 外掛、影子 MCP 工具竊取記憶體中的 API Key 與原始碼。",
      defense: "內嵌 Wings AI Risk Engine，實施端點擴充套件白名單管控與記憶體行為微隔離。"
    }},
    {{
      id: "P2",
      title: "2. 防禦鏈：Howard 5 階軟體供應鏈防禦鏈",
      tag: "5-Stage Defense",
      desc: "阻斷類似 Shai-Hulud 模式的供應鏈投毒滲透。包含：1. KOI 內嵌安全閘道（Shift-Left 攔截）➔ 2. Runtime 執行保護 ➔ 3. 憑證與管道防護 ➔ 4. 72 小時冷卻期與主管雙簽 ➔ 5. 秒級硬隔離。",
      threat: "開源依賴套件遭惡意覆蓋、CI/CD 構建自動拉取投毒版本。",
      defense: "嚴格 SHA-256 Lockfile 鎖定、私有 Harbor 鏡像倉儲、72 小時版本發布強制冷卻緩衝。"
    }},
    {{
      id: "P3",
      title: "3. 控制面：Howard NHI 身分與 Agent 意圖審計",
      tag: "Intent Audit",
      desc: "管理非人類身分（NHI）生命週期。解決「混淆代理人（Confused Deputy）」與間接提示詞注入（Indirect Prompt Injection）；落實推論鏈意圖審計（Intent Auditability）。",
      threat: "外部檢索資料潛藏越獄指令，誘騙高權限 Agent 濫用工具外傳營業機密。",
      defense: "雙通道控制與資料嚴格解耦（Dual-Channel Isolation）、WORM 不可竄改推論鏈存證、HITL 四眼原則主管簽核。"
    }},
    {{
      id: "P4",
      title: "4. 資料底座：Howard 後量子安全 (PQC) 敏捷閉環",
      tag: "Crypto Agility",
      desc: "防禦駭客「先截獲、後解密（HNDL）」攻擊。建置 Howard Dynamic CBOM（動態密碼技術清冊），推進 4 階閉環：持續發現 ➔ 多維風險評估 ➔ 密碼轉譯中繼處置 ➔ NIST PQC 持續合規。",
      threat: "長生命週期機密資料（顧客金融、專利研發）遭長期錄製監聽並等待量子破譯。",
      defense: "部署 NIST FIPS 203/204/205 標準（ML-KEM / ML-DSA），對老舊設備提供邊緣密碼轉譯中繼防護。"
    }}
  ];

  function showPillar(idx) {{
    document.querySelectorAll('#pillar-layers .layer-btn').forEach((b, i) => {{
      b.classList.toggle('on', i === idx);
    }});
    const p = PILLARS[idx];
    document.getElementById('pillar-box').innerHTML = `
      <span class="eyebrow">${{p.id}} · SECURITY PILLAR</span>
      <h4>${{p.title}}</h4>
      <p><b>架構對策：</b>${{p.desc}}</p>
      <p><b>威脅模型：</b><span style="color:var(--brick);font-weight:600;">${{p.threat}}</span></p>
      <p><b>落地防線：</b>${{p.defense}}</p>
    `;
  }}

  // Tab 1 Components Inspector Database
  const TAB1_NODES = {{
    "l1": {{
      layer: "Layer 1 · 全通路業務場景層",
      name: "全通路業務入口與非人類身分 (NHI)",
      tag: "Omnichannel Entry",
      spec: "接收消費者 Web/App 查詢、內部 ERP/CRM 流程驅動、研發人員 IDE 代碼審查以及非人類身分（NHI）定時任務。",
      sla: "HTTPS / WebSocket / JSON-RPC ｜ 併發 QPS &gt; 15,000 ｜ 握手延遲 &lt; 20ms",
      config: "NGINX Ingress 支援 HTTP/2 與 gRPC-Web 代理，配置 Cloudflare DDoS 智慧防禦。",
      compliance: "符合 ISO 27001 存取控制政策、GDPR / 個資法使用者隱私同意授權規範。",
      sop: "1. 接收請求 ➔ 2. JWT 身分鑑別 ➔ 3. 注入唯一 Trace-ID ➔ 4. 導向 Howard AIRS 安全層。"
    }},
    "l2": {{
      layer: "Layer 2 · Howard AI 安全入口與治理層",
      name: "Howard AIRS 核心安全防護 ＆ AI Gateway Hub",
      tag: "AI Runtime Security",
      spec: "即時攔截提示詞注入（Prompt Injection）、動態個資（PII）遮蔽去識別化、多模型負載均衡路由、語意快取與 Token 限額管制。",
      sla: "gRPC / TLS 1.3 ｜ AIRS 語意過濾耗時 &lt; 8ms ｜ 快取命中延遲 &lt; 15ms",
      config: "--airs-mode strict --pii-mask-phone true --pii-mask-id true --cache-backend redis-cluster",
      compliance: "OWASP Top 10 for LLM (LLM01 / LLM02) 注入防護、ISO 42001 安全邊界控制。",
      sop: "1. 原始 Prompt 語意過濾 ➔ 2. PII 脫敏 ➔ 3. 語意快取命中直接返回 ➔ 4. 未命中則路由至最適模型。"
    }},
    "l3": {{
      layer: "Layer 3 · 企業級 AI 核心平台層",
      name: "Enterprise GPT ＆ Agent Workflow ＆ Hybrid RAG",
      tag: "Platform Core",
      spec: "多代理協同狀態機（ReAct / Plan-and-Solve）、混合語意檢索重排（Milvus + BM25 + BGE-M3）、MCP 外部工具整合中樞。",
      sla: "JSON-RPC 2.0 (MCP) ｜ RAG 召回準確率 &gt; 92% ｜ 上下文命中率 &gt; 95%",
      config: "--rag-top-k 10 --rerank-model bge-reranker-large --mcp-sandbox docker-isolated",
      compliance: "歐盟 AI Act 高風險系統透明度規範、內部合規問答可解釋性存證。",
      sop: "1. Agent 解析意圖 ➔ 2. 檢索向量知識庫 ➔ 3. 提出工具調用宣告 ➔ 4. 送至意圖審計中樞驗證。"
    }},
    "l4": {{
      layer: "Layer 4 · 混合雲與地端 AIDC 算力層",
      name: "混合雲 (GCP/AWS) ＋ 地端 AIDC GPU 機房",
      tag: "Hybrid Compute",
      spec: "80% 高頻常態推論與私密微調落地端 AIDC，20% 尖峰彈性溢出至公有雲；K8s Volcano 智慧排程與 NVIDIA MIG 切片調度。",
      sla: "400Gbps RoCE v2 / GPUDirect RDMA ｜ 首字延遲 (TTFT) &lt; 300ms ｜ 輸出 &gt; 80 tokens/sec",
      config: "--gpu-memory-utilization 0.92 --kv-cache-dtype fp8 --tensor-parallel-size 8",
      compliance: "核心營業秘密與未公開財務資料 100% 地端保存，阻絕雲端資料外流法規風險。",
      sop: "1. 監控 GPU 佇列深度 ➔ 2. 逾 75% 警戒值自動觸發雲端溢出 ➔ 3. 離峰時段自動進行 Batch 微調。"
    }},
    "l5": {{
      layer: "Layer 5 · 現代周界與後量子安全底座",
      name: "Howard Enterprise Browser ＆ 5 階防禦 ＆ PQC 底座",
      tag: "Modern Perimeter",
      spec: "端點外掛沙箱阻斷、自動化 CI/CD 72 小時冷卻期、全網動態 CBOM 清冊、Howard 密碼轉譯中繼防護。",
      sla: "NIST FIPS 203/204/205 (ML-KEM/ML-DSA) ｜ 供應鏈投毒攔截率 100% ｜ HNDL 風險評分收斂至 0",
      config: "--cbom-discovery active --cipher-policy fips-203 --ci-cooldown 72h",
      compliance: "符合美國 NIST 後量子密碼標準要求、行政院國家資通安全責任等級規範。",
      sop: "1. 網路流量自動嗅探 ➔ 2. 盤點弱加密演算法 ➔ 3. 部署中繼轉譯代理 ➔ 4. 產出合規審計清冊。"
    }},
    "l6": {{
      layer: "Layer 6 · 平台工程與維運體系",
      name: "GitOps ＆ Terraform IaC ＆ SRE AIOps ＆ 治理",
      tag: "Platform Ops",
      spec: "基礎設施宣告式版本受控、ArgoCD 自動化同步、AIOps 智慧告警分流降噪、跨雲跨機房 DR 災難復原。",
      sla: "平台可用度 99.99% ｜ 目標 RTO &lt; 1hr, RPO ≈ 0 ｜ 告警降噪比 &gt; 85%",
      config: "ArgoCD Auto-Sync with Automated Rollback, Prometheus + OpenTelemetry OTLP Collector",
      compliance: "ISO 27001 ISMS / ISO 42001 AIMS 國際雙認證架構基線。",
      sop: "1. Git PR 代碼審查 ➔ 2. 自動化測試與 SAST 關卡 ➔ 3. 鏡像雜湊簽名 ➔ 4. 滾動零停機發布。"
    }}
  }};

  function inspectTab1(layerKey) {{
    document.querySelectorAll('#tab1-selector .layer-btn').forEach(b => {{
      b.classList.toggle('on', b.dataset.layer === layerKey);
    }});
    const n = TAB1_NODES[layerKey];
    if (!n) return;
    document.getElementById('tab1-ins-badge').innerText = n.layer;
    document.getElementById('tab1-ins-title').innerText = n.name;
    document.getElementById('tab1-ins-tag').innerText = n.tag;
    document.getElementById('tab1-ins-spec').innerText = n.spec;
    document.getElementById('tab1-ins-sla').innerText = n.sla;
    document.getElementById('tab1-ins-config').innerText = n.config;
    document.getElementById('tab1-ins-comp').innerText = n.compliance;
    document.getElementById('tab1-ins-sop').innerText = n.sop;
  }}

  // Global Node Inspector Dispatcher
  function inspectNode(nodeId) {{
    if (nodeId.startsWith('l')) {{
      selectTab(0);
      inspectTab1(nodeId);
      document.getElementById('tab0-inspector').scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
    }}
  }}
</script>
</head>
<body>

<!-- Harmonized Sticky Header matching index.html -->
<header class="nav">
  <div class="in">
    <a href="index.html" class="brand">廖倫豪 博士<small>× LITEON</small></a>
    <nav class="links" id="links">
      <div class="nav-item">
        <a href="index.html#hero" class="nav-link">首頁</a>
      </div>
      <div class="nav-item has-drop">
        <a href="index.html#context" class="nav-link">光寶與職能 <span class="arr">▾</span></a>
        <div class="nav-drop">
          <a href="index.html#context">光寶現況</a>
          <a href="index.html#duties">六項職責</a>
          <a href="index.html#fit">職能對照</a>
        </div>
      </div>
      <div class="nav-item has-drop">
        <a href="index.html#stack" class="nav-link">平台與架構 <span class="arr">▾</span></a>
        <div class="nav-drop">
          <a href="index.html#stack">AI 平台藍圖</a>
          <a href="index.html#arch">AI 架構</a>
          <a href="index.html#portfolio">用例組合</a>
        </div>
      </div>
      <div class="nav-item has-drop">
        <a href="index.html#plan" class="nav-link">到任與治理 <span class="arr">▾</span></a>
        <div class="nav-drop">
          <a href="index.html#plan">180 天到任計畫</a>
          <a href="index.html#org">組織與 PO</a>
          <a href="index.html#gov">AI 治理</a>
          <a href="index.html#hive">實施藍圖</a>
        </div>
      </div>
      <div class="nav-item has-drop">
        <a href="index.html#cases" class="nav-link">案例與資歷 <span class="arr">▾</span></a>
        <div class="nav-drop">
          <a href="index.html#cases">代表案例</a>
          <a href="index.html#works">架構作品集</a>
          <a href="index.html#profile">學經歷</a>
          <a href="index.html#qa">問答 (Q&A)</a>
        </div>
      </div>
      <div class="nav-item has-drop">
        <a href="architecture.html" class="nav-link on">文件報告 <span class="arr">▾</span></a>
        <div class="nav-drop">
          <a href="index.html#docs">文件線上預覽</a>
          <a href="architecture.html" style="font-weight:700;color:var(--green)">企業 AI 架構白皮書</a>
        </div>
      </div>
    </nav>
    <div class="langs">
      <a href="architecture.html" class="on" hreflang="zh">繁中</a>
      <a href="index.html" hreflang="zh">光寶門戶</a>
    </div>
    <button class="tbtn" id="theme" aria-label="Theme" onclick="toggleTheme()">◐</button>
  </div>
</header>

<main>

  <!-- Header Card in Milan Warm Amber style -->
  <div class="header-card">
    <div class="eyebrow">Enterprise Strategic Technical Whitepaper · LITEON Special Edition</div>
    <h1>企業級 AI 平台架構師 ＆ Howard 資安前瞻戰略全域工程白皮書</h1>
    <div class="meta-bar">
      <span>呈報對象：<b>光寶科技 董事長、資訊長</b></span>
      <span>應徵職能：<b>企業級 AI 架構師 / AI Platform Lead</b></span>
      <span>架構與策略總設計：<b>Howard Liao Ph.D.</b></span>
    </div>
    <p style="margin:0; font-size:15px; color:var(--mute); line-height:1.75;">
      本白皮書精準整併 <b>企業自主 AI 生態系建設核心需求</b>（Enterprise GPT、AI Agent Platform、地端 AIDC 綠能運算中心）與 <b>Howard 前瞻資安戰略三位一體閉環</b>。全域資安組件全面採用 <b>Howard</b> 自主化架構命名，提供企業級零信任、5 階軟體供應鏈攔截、非人類身分（NHI）意圖審計與後量子密碼學敏捷性（Crypto Agility）完整工程規範、參數字典、SOP 與落地準則。
    </p>
    <div class="download-bar">
      <a href="Enterprise_AI_Architect_Howard_Security_Architecture.drawio" class="btn-action" download>
        📥 下載可編輯 Draw.io 圖檔 (.drawio)
      </a>
      <span class="btn-outline">
        📊 5 大深層架構領域全景分頁
      </span>
      <span class="btn-outline">
        🛡️ 符合 ISO 27001 / ISO 42001 / NIST PQC 標準
      </span>
    </div>
  </div>

  <!-- INTERACTIVE TOP SECTION: Replacing the two static text cards with interactive Milan-style stacks -->
  <div class="interactive-deck-grid">
    
    <!-- Interactive Card 1: 7 Core Mandates -->
    <div class="interactive-deck-card">
      <div class="deck-header">
        <h3>企業級 AI 架構師七大工程職責</h3>
        <span class="deck-hint">👉 點選各項看工程規格</span>
      </div>
      <div class="interactive-layers" id="duty-layers">
        <button class="layer-btn on" onclick="showDuty(0)"><b>01</b><span>平台架構</span></button>
        <button class="layer-btn" onclick="showDuty(1)"><b>02</b><span>地端 AIDC</span></button>
        <button class="layer-btn" onclick="showDuty(2)"><b>03</b><span>模型微調</span></button>
        <button class="layer-btn" onclick="showDuty(3)"><b>04</b><span>Agent 流程</span></button>
        <button class="layer-btn" onclick="showDuty(4)"><b>05</b><span>雲地維運</span></button>
        <button class="layer-btn" onclick="showDuty(5)"><b>06</b><span>FinOps 成本</span></button>
        <button class="layer-btn" onclick="showDuty(6)"><b>07</b><span>架構標準</span></button>
      </div>
      <div class="detail-box" id="duty-box">
        <!-- Rendered by JS -->
      </div>
    </div>

    <!-- Interactive Card 2: Howard Security 4 Pillars -->
    <div class="interactive-deck-card">
      <div class="deck-header">
        <h3>Howard 前瞻資安戰略三位一體閉環</h3>
        <span class="deck-hint">👉 點選各支柱看防禦對策</span>
      </div>
      <div class="interactive-layers" id="pillar-layers">
        <button class="layer-btn on" onclick="showPillar(0)"><b>P1</b><span>周界入口</span></button>
        <button class="layer-btn" onclick="showPillar(1)"><b>P2</b><span>5階防禦鏈</span></button>
        <button class="layer-btn" onclick="showPillar(2)"><b>P3</b><span>NHI 意圖審計</span></button>
        <button class="layer-btn" onclick="showPillar(3)"><b>P4</b><span>後量子 PQC</span></button>
      </div>
      <div class="detail-box" id="pillar-box">
        <!-- Rendered by JS -->
      </div>
    </div>

  </div>

  <!-- Exhaustive Tabbed System -->
  <div class="tab-system-card">
    <div class="tab-nav-wrapper">
      <div class="tab-nav">
        <button class="tab-btn active" onclick="selectTab(0)">
          <span>🌐</span>
          <span class="tab-text-full">1. 全域平台總體架構圖 (Blueprint)</span>
          <span class="tab-text-mobile">1. 全域架構</span>
        </button>
        <button class="tab-btn" onclick="selectTab(1)">
          <span>🛡️</span>
          <span class="tab-text-full">2. Howard Agent 意圖審計流程</span>
          <span class="tab-text-mobile">2. 意圖審計</span>
        </button>
        <button class="tab-btn" onclick="selectTab(2)">
          <span>🛑</span>
          <span class="tab-text-full">3. Howard 5 階供應鏈防禦鏈</span>
          <span class="tab-text-mobile">3. 供應鏈防禦</span>
        </button>
        <button class="tab-btn" onclick="selectTab(3)">
          <span>⚡</span>
          <span class="tab-text-full">4. 混合雲與 AIDC GPU 調度拓撲</span>
          <span class="tab-text-mobile">4. 混合雲 GPU</span>
        </button>
        <button class="tab-btn" onclick="selectTab(4)">
          <span>⚛️</span>
          <span class="tab-text-full">5. Howard 後量子密碼學敏捷性閉環</span>
          <span class="tab-text-mobile">5. 後量子 PQC</span>
        </button>
      </div>
    </div>

    <!-- =========================================================================
         TAB 1: 全域平台總體架構圖 (INTERACTIVE)
         ========================================================================= -->
    <div class="tab-pane" id="tab0" style="display:block;">
      <div class="diagram-toolbar">
        <div class="view-mode-group">
          <button class="mode-btn active" onclick="toggleDiagramMode('fit', this)">📱 適應螢幕</button>
          <button class="mode-btn" onclick="toggleDiagramMode('scroll', this)">🔍 100% 高解析 (橫向滑動)</button>
        </div>
        <span class="diagram-hint">💡 互動藍圖：點選下方層級或點擊架構圖，即時展開深度規格與 SOP</span>
      </div>

      <!-- Quick interactive Layer Selector matching Milan style -->
      <div class="interactive-layers" id="tab1-selector" style="margin: 14px 0 10px 0;">
        <button class="layer-btn" data-layer="l1" onclick="inspectTab1('l1')"><b>L1</b><span>業務場景層</span></button>
        <button class="layer-btn on" data-layer="l2" onclick="inspectTab1('l2')"><b>L2</b><span>安全入口層</span></button>
        <button class="layer-btn" data-layer="l3" onclick="inspectTab1('l3')"><b>L3</b><span>核心平台層</span></button>
        <button class="layer-btn" data-layer="l4" onclick="inspectTab1('l4')"><b>L4</b><span>混合算力層</span></button>
        <button class="layer-btn" data-layer="l5" onclick="inspectTab1('l5')"><b>L5</b><span>周界安全底座</span></button>
        <button class="layer-btn" data-layer="l6" onclick="inspectTab1('l6')"><b>L6</b><span>平台工程維運</span></button>
      </div>

      <div class="diagram-scroll-container">
        {svg1}
      </div>

      <!-- Live Dynamic Component Inspector Panel for Tab 1 -->
      <div class="inspector-card" id="tab0-inspector">
        <div class="ins-header">
          <div class="ins-header-main">
            <span class="ins-layer-badge" id="tab1-ins-badge">Layer 2 · Howard AI 安全入口與治理層</span>
            <h3 id="tab1-ins-title">Howard AIRS 核心安全防護 ＆ AI Gateway Hub</h3>
          </div>
          <span class="ins-tag" id="tab1-ins-tag">AI Runtime Security</span>
        </div>
        <div class="ins-grid">
          <div class="ins-col">
            <h4>📋 主要工程職責與架構規格</h4>
            <p id="tab1-ins-spec">即時攔截提示詞注入（Prompt Injection）、動態個資（PII）遮蔽去識別化、多模型負載均衡路由、語意快取與 Token 限額管制。</p>
          </div>
          <div class="ins-col">
            <h4>⚙️ 通訊協定與關鍵性能 (SLA)</h4>
            <p id="tab1-ins-sla">gRPC / TLS 1.3 ｜ AIRS 語意過濾耗時 &lt; 8ms ｜ 快取命中延遲 &lt; 15ms</p>
          </div>
        </div>
        <div class="ins-grid">
          <div class="ins-col">
            <h4>🔧 生產環境建議配置</h4>
            <code class="ins-config-code" id="tab1-ins-config">--airs-mode strict --pii-mask-phone true --pii-mask-id true --cache-backend redis-cluster</code>
          </div>
          <div class="ins-col">
            <h4>🛡️ 資安與國際合規對照</h4>
            <p id="tab1-ins-comp">OWASP Top 10 for LLM (LLM01 / LLM02) 注入防護、ISO 42001 安全邊界控制。</p>
          </div>
        </div>
        <div class="ins-full-sop">
          <h4>⚡ 標準作業程序 (SOP) 落地要點</h4>
          <p id="tab1-ins-sop">1. 原始 Prompt 語意過濾 ➔ 2. PII 脫敏 ➔ 3. 語意快取命中直接返回 ➔ 4. 未命中則路由至最適模型。</p>
        </div>
      </div>
    </div>

    <!-- =========================================================================
         TAB 2: Howard Agent 意圖審計流程 (INTERACTIVE)
         ========================================================================= -->
    <div class="tab-pane" id="tab1" style="display:none;">
      <div class="diagram-toolbar">
        <div class="view-mode-group">
          <button class="mode-btn active" onclick="toggleDiagramMode('fit', this)">📱 適應螢幕</button>
          <button class="mode-btn" onclick="toggleDiagramMode('scroll', this)">🔍 100% 高解析 (橫向滑動)</button>
        </div>
        <span class="diagram-hint">💡 意圖審計鏈路：非人類身分（NHI）生命週期與防混淆代理流程</span>
      </div>
      <div class="diagram-scroll-container">
        {svg2}
      </div>

      <!-- Tab 2 Interactive Steps Detail Box -->
      <div class="inspector-card">
        <div class="ins-header">
          <div class="ins-header-main">
            <span class="ins-layer-badge">Agent Governance · 意圖可審計性閉環</span>
            <h3>雙通道解耦與非人類身分（NHI）意圖防護體系</h3>
          </div>
          <span class="ins-tag">Intent Auditability</span>
        </div>
        <div class="ins-grid">
          <div class="ins-col">
            <h4>🛡️ 防混淆代理 (Anti-Confused Deputy)</h4>
            <p>控制通道（系統指令）與資料通道（外部檢索內容）物理拆分，外部 RAG 輸入強制封裝於唯讀沙箱，禁止直接作為可執行指令直譯。</p>
          </div>
          <div class="ins-col">
            <h4>🔑 NHI 身分動態憑證</h4>
            <p>HashiCorp Vault ＋ SPIFFE/SPIRE 動態發放 X.509 SVID 憑證，強制有效期 &lt; 15 分鐘，徹底根除 API Key 硬編碼外洩風險。</p>
          </div>
        </div>
        <div class="ins-full-sop">
          <h4>⚡ 高風險操作人機介入 (HITL) 四眼原則 SOP</h4>
          <p>單筆異動金額 &gt; NT$50,000 或批次修改逾 100 筆時，系統自動熔斷掛起並向主管發送審核 Webhook，人工雙簽後方放行 MCP 代理執行。</p>
        </div>
      </div>
    </div>

    <!-- =========================================================================
         TAB 3: Howard 5 階軟體供應鏈防禦鏈 (INTERACTIVE)
         ========================================================================= -->
    <div class="tab-pane" id="tab2" style="display:none;">
      <div class="diagram-toolbar">
        <div class="view-mode-group">
          <button class="mode-btn active" onclick="toggleDiagramMode('fit', this)">📱 適應螢幕</button>
          <button class="mode-btn" onclick="toggleDiagramMode('scroll', this)">🔍 100% 高解析 (橫向滑動)</button>
        </div>
        <span class="diagram-hint">💡 現代軟體周界防護：阻斷影子外掛與 Shai-Hulud 模式供應鏈滲透</span>
      </div>
      <div class="diagram-scroll-container">
        {svg3}
      </div>

      <div class="inspector-card">
        <div class="ins-header">
          <div class="ins-header-main">
            <span class="ins-layer-badge">Supply Chain Defense · 5 階縱深防禦鏈</span>
            <h3>Howard 現代周界與 CI/CD 72 小時冷卻期機制</h3>
          </div>
          <span class="ins-tag">Zero Trust Perimeter</span>
        </div>
        <div class="ins-grid">
          <div class="ins-col">
            <h4>🛑 第 1 階：KOI 內嵌安全閘道</h4>
            <p>在擴充功能、腳本與 MCP 工具下載「觸及端點前」即時攔截，比對企業私有套件白名單，未授權者一律阻斷。</p>
          </div>
          <div class="ins-col">
            <h4>⏱️ 第 4 階：CI/CD 72 小時冷卻期</h4>
            <p>上游開源依賴套件發布時間 &lt; 72 小時，自動禁止流水線構建，杜絕自動升級即時投毒之武器化管道。</p>
          </div>
        </div>
        <div class="ins-full-sop">
          <h4>⚡ 軟體物料清單（SBOM）與硬隔離 SOP</h4>
          <p>精確鎖定 SHA-256 雜湊值；偵測異常行為即刻秒級硬隔離 Pod，切斷 VLAN 通訊並重置至黃金鏡像。</p>
        </div>
      </div>
    </div>

    <!-- =========================================================================
         TAB 4: 混合雲與地端 AIDC GPU 調度拓撲 (INTERACTIVE)
         ========================================================================= -->
    <div class="tab-pane" id="tab3" style="display:none;">
      <div class="diagram-toolbar">
        <div class="view-mode-group">
          <button class="mode-btn active" onclick="toggleDiagramMode('fit', this)">📱 適應螢幕</button>
          <button class="mode-btn" onclick="toggleDiagramMode('scroll', this)">🔍 100% 高解析 (橫向滑動)</button>
        </div>
        <span class="diagram-hint">💡 混合算力拓撲：K8s Volcano 智慧排程 ＋ NVIDIA MIG 資源切片</span>
      </div>
      <div class="diagram-scroll-container">
        {svg4}
      </div>

      <div class="inspector-card">
        <div class="ins-header">
          <div class="ins-header-main">
            <span class="ins-layer-badge">Green AIDC &amp; GPU Scheduling · 算力拓撲</span>
            <h3>混合雲成本邊界與地端綠能 AIDC 算力優化</h3>
          </div>
          <span class="ins-tag">FinOps &amp; vLLM</span>
        </div>
        <div class="ins-grid">
          <div class="ins-col">
            <h4>⚡ Volcano 智慧排程與 MIG 切片</h4>
            <p>NVIDIA Multi-Instance GPU 切片隔離多租戶；常態負載在地端 H100 運算，大促尖峰動態溢出至公有雲。</p>
          </div>
          <div class="ins-col">
            <h4>🔧 vLLM 生產配置字典</h4>
            <code class="ins-config-code">--gpu-memory-utilization 0.92 --kv-cache-dtype fp8 --max-num-seqs 256</code>
          </div>
        </div>
        <div class="ins-full-sop">
          <h4>⚡ 成本效益總結</h4>
          <p>3 年多雲 TCO 實測降低 42.8%，核心資料留存廠區，滿足企業資料主權與綠能 PUE 指標。</p>
        </div>
      </div>
    </div>

    <!-- =========================================================================
         TAB 5: Howard 後量子密碼學敏捷性閉環 (INTERACTIVE)
         ========================================================================= -->
    <div class="tab-pane" id="tab4" style="display:none;">
      <div class="diagram-toolbar">
        <div class="view-mode-group">
          <button class="mode-btn active" onclick="toggleDiagramMode('fit', this)">📱 適應螢幕</button>
          <button class="mode-btn" onclick="toggleDiagramMode('scroll', this)">🔍 100% 高解析 (橫向滑動)</button>
        </div>
        <span class="diagram-hint">💡 後量子閉環：防禦 HNDL 攻擊 ＆ NIST FIPS 203/204/205 落地</span>
      </div>
      <div class="diagram-scroll-container">
        {svg5}
      </div>

      <div class="inspector-card">
        <div class="ins-header">
          <div class="ins-header-main">
            <span class="ins-layer-badge">Quantum-Safe Resilience · 密碼學敏捷性</span>
            <h3>Howard Dynamic CBOM 盤點與四階敏捷閉環</h3>
          </div>
          <span class="ins-tag">NIST PQC Ready</span>
        </div>
        <div class="ins-grid">
          <div class="ins-col">
            <h4>⚛️ 核心 NIST PQC 演算法</h4>
            <p><b>ML-KEM (FIPS 203)</b> 取代傳統 RSA/ECDH 金鑰交換；<b>ML-DSA (FIPS 204)</b> 取代 RSA/ECDSA 數位簽章。</p>
          </div>
          <div class="ins-col">
            <h4>🔄 密碼轉譯中繼防護 (Proxy)</h4>
            <p>對無法升級的老舊設備導入邊緣中繼轉譯：傳統 RSA/ECC ➔ NIST PQC 封裝轉發，實現零痛點平滑遷移。</p>
          </div>
        </div>
        <div class="ins-full-sop">
          <h4>⚡ HNDL 威脅多維風險評估算式</h4>
          <p>評估資產脆弱度、關鍵性與資料半衰期（Risk = Cipher × Criticality × Sensitivity），優先保護半衰期 &gt; 10 年之營業機密。</p>
        </div>
      </div>
    </div>

  </div>

  <!-- Mobile Floating Dock -->
  <div class="mobile-dock">
    <button class="dock-btn" onclick="cycleNextTab()"><span>📑</span> 下一章節</button>
    <a href="Enterprise_AI_Architect_Howard_Security_Architecture.drawio" class="dock-btn highlight" download><span>📥</span> Draw.io</a>
    <button class="dock-btn" onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})"><span>🔝</span> 頂部</button>
  </div>

</main>

<footer>© 2026 廖倫豪 博士　Howard Liao, Ph.D.　·　專為光寶科技董事長暨資訊長審閱製作</footer>

<script>
  // Initial render for top interactive decks
  showDuty(0);
  showPillar(0);
  inspectTab1('l2');
</script>

</body>
</html>
"""

    out_path1 = "/Users/howardliao/Desktop/Howard/2026_Howard/應徵/2301_repo/architecture.html"
    out_path2 = "/Users/howardliao/Desktop/Howard/2026_Howard/應徵/2301_repo/architecture/index.html"
    out_path3 = "/Users/howardliao/Desktop/HermesAgent/Temp/Enterprise_AI_Architect_Howard_Security_Architecture_Preview.html"
    
    with open(out_path1, "w", encoding="utf-8") as f:
        f.write(html_content)
    with open(out_path2, "w", encoding="utf-8") as f:
        f.write(html_content)
    with open(out_path3, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"Master-level interactive Milan architecture dossier successfully generated across all targets.")

if __name__ == "__main__":
    build_dossier()
