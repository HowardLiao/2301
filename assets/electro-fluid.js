/* === LITEON 2301 Electro-Fluid Physics & Interactivity Engine === */
(function () {
  'use strict';

  const LANG = (document.documentElement.lang || 'zh').toLowerCase().startsWith('ja')
    ? 'ja'
    : (document.documentElement.lang || 'zh').toLowerCase().startsWith('en')
      ? 'en'
      : 'zh';

  const I18N = {
    zh: {
      searchBtn: '快速檢索',
      searchPh: '搜尋章節、AI 用例、800V DC、CDU、S/4HANA、治理… (Enter 跳轉)',
      searchEmpty: '找不到相符項目，請嘗試其他關鍵字。',
      laminar: '層流 Laminar',
      transitional: '過渡流 Transitional',
      turbulent: '紊流高效換熱 Turbulent',
      aiAutoOn: 'HowardPro AI 閉環調控中 · 自動抑溫',
      aiAutoOff: '手動模式 · 調整滑桿觀察電熱反應',
      aiWarn: '熱負載偏高 · 建議開啟 AI 調控或提升流速',
      aiAlert: '高溫預警 · 建議切換 800V DC 並提高 CDU 流速',
      lossSave: (pct) => `較 48V 降損 ${pct}%`,
      lossBase: '傳統 48V 基準（高銅損）',
      tempOk: '安全溫區（≤ 60°C）',
      tempWarn: '偏高溫區（60–72°C）',
      tempHot: '過熱警戒（> 72°C）',
      pueSub: (save) => `HowardRoute 省 ${save}% 算力`,
      zonePower: '800V DC 電源匯流排',
      zonePower48: '48V DC 傳統匯流排',
      zoneGpu: 'HowardAIDC GPU 推論機櫃',
      zoneCdu: '120kW 液冷 CDU 流體迴路',
      inlet: '冷液進水 28°C',
      outlet: (t) => `回水 ${t.toFixed(1)}°C`,
      surgeMsg: '已注入 18kW 瞬間熱點衝擊！觀察流體擾動與 AI 調控反應',
      eaDefault: '點選上方任一架構層級，檢視即時「資料流 × 電算力 × 治理邊界」互動摘要。',
      eaBriefs: [
        '【經營層】每季 AI 投資委員會直接對接 EBITDA、存貨周轉與 PUE 節能指標，所有 ROI 由財務長核定。',
        '【事業群】雲端物聯網（800V DC / CDU）、消費電子與光電三大事業群共用單一 AI 底座，按需複製用例。',
        '【價值鏈】從研發 NPI、採購、SMT 生產到品質出貨，AI Agent 串聯斷點並消除跨部門資訊落差。',
        '【應用系統】堅守 SAP S/4HANA Clean Core（2027.01.04 上線），AI 僅透過 API／CDC 讀取並以人員核可回寫。',
        '【AI 平台 L2–L5】HowardAIDC 地端推論結合 HowardRoute 智慧分流（省 30%+ Token）與 HowardPro 預測核心。',
        '【資料底座 L0–L1】蜂巢計畫雙環匯流排（IT Kafka CDC ＋ OT MQTT），湖倉 Bronze/Silver/Gold 統一全球 112 廠口徑。',
        '【基礎架構】內湖總部與光寶 800V DC 液冷 AIDC 機櫃深度耦合，112 座工廠依 IEC 62443 維持離線自治。'
      ]
    },
    en: {
      searchBtn: 'Quick Find',
      searchPh: 'Search chapters, AI use cases, 800V DC, CDU, S/4HANA, governance…',
      searchEmpty: 'No matching sections or items found.',
      laminar: 'Laminar Flow',
      transitional: 'Transitional Flow',
      turbulent: 'Turbulent High-Transfer',
      aiAutoOn: 'HowardPro AI Closed-Loop PID · Active',
      aiAutoOff: 'Manual Mode · Adjust sliders to inspect physics',
      aiWarn: 'Elevated Thermal Load · Increase CDU flow or enable AI',
      aiAlert: 'Thermal Alert · Switch to 800V DC & boost CDU flow',
      lossSave: (pct) => `-${pct}% copper loss vs 48V`,
      lossBase: 'Legacy 48V baseline (high I²R)',
      tempOk: 'Optimal Zone (≤ 60°C)',
      tempWarn: 'Warm Zone (60–72°C)',
      tempHot: 'Thermal Limit (> 72°C)',
      pueSub: (save) => `HowardRoute saves ${save}% compute`,
      zonePower: '800V DC Power Bus',
      zonePower48: '48V DC Legacy Bus',
      zoneGpu: 'HowardAIDC GPU Rack',
      zoneCdu: '120kW Liquid CDU Loop',
      inlet: 'Inlet 28°C',
      outlet: (t) => `Outlet ${t.toFixed(1)}°C`,
      surgeMsg: 'Injected +18kW thermal surge! Watch fluid wake & AI response.',
      eaDefault: 'Click any architecture tier above to inspect live Data × Power × Governance flow.',
      eaBriefs: [
        '[Executive] Quarterly AI Investment Committee governs EBITDA, inventory turns & PUE with CFO-verified ROI.',
        '[Business Groups] Cloud/AIoT (800V DC / CDU), IT/CE, and Optoelectronics share one reusable AI platform.',
        '[Value Chain] End-to-end Agent orchestration across R&D/NPI, Procurement, SMT Production, Quality, and Service.',
        '[Core Apps] Strict SAP S/4HANA Clean Core (2027.01.04); AI reads via API/CDC and writes back with Human-in-the-Loop.',
        '[AI Platform L2–L5] HowardAIDC on-prem vLLM + HowardRoute smart routing (-30%+ token cost) + HowardPro predictive core.',
        '[Data Foundation L0–L1] Beehive dual-ring bus (IT Kafka CDC + OT MQTT) & Medallion Lakehouse across 112 factories.',
        '[Infrastructure] Neihu HQ & LITEON 800V DC liquid-cooled AIDC racks; 112 plants retain IEC 62443 offline autonomy.'
      ]
    },
    ja: {
      searchBtn: 'クイック検索',
      searchPh: '章・AIユースケース・800V DC・CDU・S/4HANA・ガバナンスを検索…',
      searchEmpty: '一致する項目が見つかりません。',
      laminar: '層流 Laminar',
      transitional: '遷移流 Transitional',
      turbulent: '乱流高熱伝達 Turbulent',
      aiAutoOn: 'HowardPro AI 閉ループPID制御中 · 最適冷却',
      aiAutoOff: '手動モード · スライダーで電熱流体反応を検証',
      aiWarn: '熱負荷上昇 · AI制御ONまたはCDU流量増加を推奨',
      aiAlert: '高温警告 · 800V DC切替とCDU増流を推奨',
      lossSave: (pct) => `48V比 銅損 -${pct}%`,
      lossBase: '従来48V基準（高銅損）',
      tempOk: '安全温度域（≤ 60°C）',
      tempWarn: '注意温度域（60–72°C）',
      tempHot: '過熱警戒（> 72°C）',
      pueSub: (save) => `HowardRoute 計算負荷 -${save}%`,
      zonePower: '800V DC 給電バスバー',
      zonePower48: '48V DC 従来バスバー',
      zoneGpu: 'HowardAIDC GPU 推論ラック',
      zoneCdu: '120kW 液冷 CDU 流体ループ',
      inlet: '冷却水入口 28°C',
      outlet: (t) => `出口 ${t.toFixed(1)}°C`,
      surgeMsg: '+18kW 局所熱負荷を注入！流体渦とAI自動制御を確認してください',
      eaDefault: '上のアーキテクチャ層をクリックすると、データ流・電力計算・ガバナンス連携を表示します。',
      eaBriefs: [
        '【経営層】四半期AI投資委員会でEBITDA・在庫回転・PUEをCFO確認済みのROIで統治。',
        '【事業群】クラウド/AIoT（800V DC/CDU）・情報電子・光電の3事業群で共通AI基盤を再利用。',
        '【バリューチェーン】設計NPI・調達・SMT製造・品質保証を横断し、部門間の分断を解消。',
        '【基幹システム】SAP S/4HANA Clean Core（2027.01.04）を厳守し、API/CDC読取＋人手承認書戻し。',
        '【AI基盤 L2–L5】HowardAIDC推論＋HowardRoute最適ルーティング（トークン-30%）＋HowardPro予測中核。',
        '【データ基盤 L0–L1】ビーハイブ計画の二重バス（IT Kafka＋OT MQTT）で世界112工場の指標を統一。',
        '【インフラ】内湖本社とLITEON 800V DC液冷AIDCを統合し、112工場はIEC 62443で自律稼働。'
      ]
    }
  }[LANG];

  const reducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function isDark() {
    const t = document.documentElement.dataset.theme;
    if (t === 'dark') return true;
    if (t === 'light') return false;
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  }

  /* =========================================================================
   * 1. HERO AMBIENT ELECTRO-FLUID PHYSICS CANVAS
   * ========================================================================= */
  function initHeroField() {
    const hero = document.getElementById('hero');
    const canvas = document.getElementById('ef-hero-canvas');
    if (!hero || !canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    let mode = reducedMotion ? 'off' : 'coupled'; // 'coupled' | 'electric' | 'fluid' | 'off'
    let w = 0, h = 0, dpr = 1;
    let visible = true;
    let rafId = null;
    let lastFrame = 0;

    const pointer = { x: -999, y: -999, vx: 0, vy: 0, active: false };
    const ripples = [];

    // Fluid streamline particles (capped <= 48 for smooth 30fps)
    const FLUID_N = 44;
    const fluidPts = [];

    // Electric current busbar packets (capped <= 22)
    const ELEC_N = 22;
    const elecPts = [];

    function resize() {
      const rect = hero.getBoundingClientRect();
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      w = Math.max(320, Math.floor(rect.width));
      h = Math.max(260, Math.floor(rect.height));
      canvas.width = Math.floor(w * dpr);
      canvas.height = Math.floor(h * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      seedParticles();
    }

    function seedParticles() {
      fluidPts.length = 0;
      for (let i = 0; i < FLUID_N; i++) {
        fluidPts.push({
          x: Math.random() * w,
          y: Math.random() * h,
          px: 0,
          py: 0,
          life: Math.random() * 140 + 60,
          speed: 0.9 + Math.random() * 1.1,
          temp: Math.random()
        });
      }
      elecPts.length = 0;
      const grid = 48;
      for (let i = 0; i < ELEC_N; i++) {
        const horiz = Math.random() > 0.35;
        elecPts.push({
          x: Math.floor((Math.random() * w) / grid) * grid,
          y: Math.floor((Math.random() * h) / grid) * grid,
          dir: horiz ? (Math.random() > 0.5 ? 0 : 2) : (Math.random() > 0.5 ? 1 : 3),
          speed: 2.2 + Math.random() * 1.8,
          steps: 0,
          trail: []
        });
      }
    }

    // Divergence-free curl-like velocity field + interactive pointer vortex
    function fluidVelocity(x, y, t) {
      const nx = x * 0.0042;
      const ny = y * 0.0042;
      let vx = 1.15 + Math.cos(ny * 2.4 + t * 0.7) * 0.85 + Math.sin((nx + ny) * 1.7 - t * 0.45) * 0.45;
      let vy = Math.sin(nx * 2.6 - t * 0.65) * 0.75 + Math.cos((nx - ny) * 1.5 + t * 0.5) * 0.4;

      if (pointer.active) {
        const dx = x - pointer.x;
        const dy = y - pointer.y;
        const dist2 = dx * dx + dy * dy + 900;
        if (dist2 < 45000) {
          const inf = 9000 / dist2;
          // Vortex swirl + pointer drag momentum
          vx += (-dy / Math.sqrt(dist2)) * inf * 1.1 + pointer.vx * inf * 0.06;
          vy += (dx / Math.sqrt(dist2)) * inf * 1.1 + pointer.vy * inf * 0.06;
        }
      }
      return [vx, vy];
    }

    function drawFrame(now) {
      rafId = requestAnimationFrame(drawFrame);
      if (!visible || document.hidden || mode === 'off') return;
      if (now - lastFrame < 32) return; // ~30fps cap
      lastFrame = now;

      const t = now * 0.001;
      const dark = isDark();

      // Gentle trail decay matching active theme
      ctx.fillStyle = dark ? 'rgba(20, 25, 23, 0.16)' : 'rgba(250, 247, 242, 0.18)';
      ctx.fillRect(0, 0, w, h);

      // Subtle orthogonal PCB / 800V busbar grid
      if (mode === 'electric' || mode === 'coupled') {
        ctx.strokeStyle = dark ? 'rgba(222, 192, 130, 0.045)' : 'rgba(47, 69, 56, 0.045)';
        ctx.lineWidth = 1;
        const step = 48;
        ctx.beginPath();
        for (let gx = step; gx < w; gx += step) {
          ctx.moveTo(gx, 0);
          ctx.lineTo(gx, h);
        }
        for (let gy = step; gy < h; gy += step) {
          ctx.moveTo(0, gy);
          ctx.lineTo(w, gy);
        }
        ctx.stroke();
      }

      // FLUID DYNAMICS STREAMLINES
      if (mode === 'fluid' || mode === 'coupled') {
        for (let i = 0; i < fluidPts.length; i++) {
          const p = fluidPts[i];
          p.px = p.x;
          p.py = p.y;
          const [vx, vy] = fluidVelocity(p.x, p.y, t);
          p.x += vx * p.speed * 1.45;
          p.y += vy * p.speed * 1.45;
          p.life -= 1;

          // Color transitions cool teal (inlet) -> warm gold (thermal exchange)
          const heat = Math.min(1, Math.max(0, p.x / w));
          if (dark) {
            ctx.strokeStyle = heat < 0.55
              ? `rgba(56, 189, 248, ${0.26 + heat * 0.14})`
              : `rgba(222, 192, 130, ${0.32 - (heat - 0.55) * 0.16})`;
          } else {
            ctx.strokeStyle = heat < 0.55
              ? `rgba(14, 116, 144, ${0.22 + heat * 0.1})`
              : `rgba(200, 169, 106, ${0.34 - (heat - 0.55) * 0.12})`;
          }
          ctx.lineWidth = 1.6;
          ctx.beginPath();
          ctx.moveTo(p.px, p.py);
          ctx.lineTo(p.x, p.y);
          ctx.stroke();

          if (p.life <= 0 || p.x < -10 || p.x > w + 10 || p.y < -10 || p.y > h + 10) {
            p.x = Math.random() * w * 0.25;
            p.y = Math.random() * h;
            p.life = 90 + Math.random() * 110;
          }
        }
      }

      // ELECTRIC CURRENT 800V DC BUS PACKETS & MICRO-ARCS
      if (mode === 'electric' || mode === 'coupled') {
        const dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]];
        const grid = 48;
        for (let i = 0; i < elecPts.length; i++) {
          const e = elecPts[i];
          const [dx, dy] = dirs[e.dir];
          e.x += dx * e.speed;
          e.y += dy * e.speed;
          e.steps += e.speed;
          e.trail.push([e.x, e.y]);
          if (e.trail.length > 12) e.trail.shift();

          // Orthogonal turn at busbar intersections
          if (e.steps >= grid) {
            e.steps = 0;
            e.x = Math.round(e.x / grid) * grid;
            e.y = Math.round(e.y / grid) * grid;
            if (Math.random() < 0.42) {
              e.dir = (e.dir + (Math.random() > 0.5 ? 1 : 3)) % 4;
            }
          }

          if (e.x < -grid || e.x > w + grid || e.y < -grid || e.y > h + grid) {
            e.x = Math.floor((Math.random() * w) / grid) * grid;
            e.y = Math.floor((Math.random() * h) / grid) * grid;
            e.trail.length = 0;
          }

          if (e.trail.length > 1) {
            ctx.beginPath();
            ctx.moveTo(e.trail[0][0], e.trail[0][1]);
            for (let k = 1; k < e.trail.length; k++) {
              ctx.lineTo(e.trail[k][0], e.trail[k][1]);
            }
            ctx.strokeStyle = dark ? 'rgba(222, 192, 130, 0.55)' : 'rgba(47, 69, 56, 0.35)';
            ctx.lineWidth = 1.8;
            ctx.stroke();

            // Glowing charge carrier head
            ctx.fillStyle = dark ? '#FDE68A' : '#C8A96A';
            ctx.beginPath();
            ctx.arc(e.x, e.y, 2.3, 0, Math.PI * 2);
            ctx.fill();
          }

          // Interactive cursor electric micro-arc when pointer is near
          if (pointer.active) {
            const pdx = pointer.x - e.x;
            const pdy = pointer.y - e.y;
            const dist = Math.hypot(pdx, pdy);
            if (dist < 115 && Math.random() < 0.28) {
              ctx.beginPath();
              ctx.moveTo(e.x, e.y);
              const mx = (e.x + pointer.x) * 0.5 + (Math.random() - 0.5) * 16;
              const my = (e.y + pointer.y) * 0.5 + (Math.random() - 0.5) * 16;
              ctx.lineTo(mx, my);
              ctx.lineTo(pointer.x, pointer.y);
              ctx.strokeStyle = dark ? 'rgba(56, 189, 248, 0.55)' : 'rgba(200, 169, 106, 0.55)';
              ctx.lineWidth = 1.1;
              ctx.stroke();
            }
          }
        }
      }

      // Interactive click shockwave ripples
      for (let i = ripples.length - 1; i >= 0; i--) {
        const rp = ripples[i];
        rp.r += 4.5;
        rp.a *= 0.92;
        ctx.beginPath();
        ctx.arc(rp.x, rp.y, rp.r, 0, Math.PI * 2);
        ctx.strokeStyle = dark
          ? `rgba(222, 192, 130, ${rp.a.toFixed(3)})`
          : `rgba(47, 69, 56, ${rp.a.toFixed(3)})`;
        ctx.lineWidth = 1.6;
        ctx.stroke();
        if (rp.a < 0.03) ripples.splice(i, 1);
      }

      pointer.vx *= 0.85;
      pointer.vy *= 0.85;
    }

    // Pointer tracking on Hero section
    hero.addEventListener('pointermove', (ev) => {
      const r = hero.getBoundingClientRect();
      const nx = ev.clientX - r.left;
      const ny = ev.clientY - r.top;
      pointer.vx = nx - pointer.x;
      pointer.vy = ny - pointer.y;
      pointer.x = nx;
      pointer.y = ny;
      pointer.active = true;
    }, { passive: true });
    hero.addEventListener('pointerleave', () => { pointer.active = false; });
    hero.addEventListener('pointerdown', (ev) => {
      if (ev.target.closest('a,button')) return;
      const r = hero.getBoundingClientRect();
      ripples.push({ x: ev.clientX - r.left, y: ev.clientY - r.top, r: 8, a: 0.75 });
    });

    // Mode buttons
    const ctrl = document.getElementById('efHeroCtrl');
    if (ctrl) {
      ctrl.addEventListener('click', (ev) => {
        const b = ev.target.closest('.ef-mode-btn');
        if (!b) return;
        mode = b.dataset.mode;
        ctrl.querySelectorAll('.ef-mode-btn').forEach(x => x.classList.toggle('on', x === b));
        if (mode === 'off') {
          ctx.clearRect(0, 0, w, h);
        }
      });
      if (reducedMotion) {
        ctrl.querySelectorAll('.ef-mode-btn').forEach(x => x.classList.toggle('on', x.dataset.mode === 'off'));
      }
    }

    const io = new IntersectionObserver(entries => {
      entries.forEach(en => { visible = en.isIntersecting; });
    }, { threshold: 0.02 });
    io.observe(hero);

    window.addEventListener('resize', resize, { passive: true });
    resize();
    rafId = requestAnimationFrame(drawFrame);
  }

  /* =========================================================================
   * 2. INTERACTIVE 800V DC × 120kW CDU ELECTRO-FLUID DIGITAL TWIN LAB
   * ========================================================================= */
  function initTwinLab() {
    const canvas = document.getElementById('ef-twin-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    const elLoad = document.getElementById('efLoad');
    const elFlow = document.getElementById('efFlow');
    const elLoadVal = document.getElementById('efLoadVal');
    const elFlowVal = document.getElementById('efFlowVal');
    const btn800 = document.getElementById('efV800');
    const btn48 = document.getElementById('efV48');
    const btnAi = document.getElementById('efAiAuto');
    const aiPill = document.getElementById('efAiPill');

    const outCurrent = document.getElementById('efOutCurrent');
    const outCurrentSub = document.getElementById('efOutCurrentSub');
    const outLoss = document.getElementById('efOutLoss');
    const outLossSub = document.getElementById('efOutLossSub');
    const outRe = document.getElementById('efOutRe');
    const outReSub = document.getElementById('efOutReSub');
    const outTemp = document.getElementById('efOutTemp');
    const outTempSub = document.getElementById('efOutTempSub');
    const outPue = document.getElementById('efOutPue');
    const outPueSub = document.getElementById('efOutPueSub');

    const state = {
      loadKw: 110,      // 30 - 130 kW
      voltage: 800,     // 800 or 48 V DC
      flowLpm: 115,     // 40 - 180 LPM
      aiAuto: true,
      surgeKw: 0,       // temporary interactive hotspot injection
      vortexX: -1,
      vortexY: -1,
      vortexPower: 0,
      tj: 54.0,
      outletTemp: 39.5,
      visible: false
    };

    let w = 800, h = 350, dpr = 1;
    let lastFrame = 0;

    // Fluid tracer particles inside the 120kW CDU cold-plate channels
    const N_FLUID = 145;
    const fluid = [];
    // Electric charge carriers on the DC busbars
    const N_ELEC = 44;
    const charges = [];
    // Interactive ripples
    const sparks = [];

    function initParticles() {
      fluid.length = 0;
      for (let i = 0; i < N_FLUID; i++) {
        fluid.push({
          u: Math.random(),          // normalized x along cooling loop [0..1]
          lane: i % 4,               // 4 cold-plate micro-channels
          offset: (Math.random() - 0.5) * 0.72,
          phase: Math.random() * Math.PI * 2,
          size: 1.6 + Math.random() * 1.4
        });
      }
      charges.length = 0;
      for (let i = 0; i < N_ELEC; i++) {
        charges.push({
          u: Math.random(),
          bus: i % 4,
          jitter: Math.random() * Math.PI * 2
        });
      }
    }

    function resize() {
      const wrap = canvas.parentElement;
      const rect = wrap.getBoundingClientRect();
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      w = Math.max(300, Math.floor(rect.width));
      h = Math.max(250, Math.floor(rect.height));
      canvas.width = Math.floor(w * dpr);
      canvas.height = Math.floor(h * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }

    // Real electro-thermal fluid physics step
    function computePhysics(dt) {
      // Decay interactive surge & vortex
      if (state.surgeKw > 0.05) state.surgeKw *= Math.pow(0.55, dt);
      else state.surgeKw = 0;
      if (state.vortexPower > 0.02) state.vortexPower *= Math.pow(0.35, dt);
      else state.vortexPower = 0;

      // HowardRoute AI smart offload saves 12% peak compute power when AI Auto is ON
      const aiOffloadPct = state.aiAuto ? 12 : 0;
      const effectiveKw = (state.loadKw + state.surgeKw) * (1 - aiOffloadPct * 0.008);

      // Electric Current Physics: I = P / V
      const currentA = (effectiveKw * 1000) / state.voltage;
      // Busbar Resistance R_eq ≈ 0.0022 Ω (typical rack busbar + connectors)
      const R_bus = 0.0022;
      const lossKw = (currentA * currentA * R_bus) / 1000;
      const loss48Kw = Math.pow((effectiveKw * 1000) / 48, 2) * R_bus / 1000;
      const lossSavePct = state.voltage === 800 ? ((1 - lossKw / Math.max(0.01, loss48Kw)) * 100).toFixed(1) : '0.0';

      // Fluid Dynamics: Reynolds number Re = (rho * v * D) / mu
      // Calibrated to 120kW CDU cold-plate micro-channels: 40 LPM -> Re ~ 1,650 (Laminar), 180 LPM -> Re ~ 7,420 (Turbulent)
      const re = Math.round(state.flowLpm * 41.2);
      let regime = I18N.laminar;
      let nusseltBoost = 1.0;
      if (re >= 4000) {
        regime = I18N.turbulent;
        nusseltBoost = 1.38 + Math.min(0.28, (re - 4000) / 14000);
      } else if (re >= 2300) {
        regime = I18N.transitional;
        nusseltBoost = 1.0 + ((re - 2300) / 1700) * 0.38;
      }

      // Thermal energy balance: Q = m_dot * c_p * dT  (Water-glycol c_p ≈ 3.85 kJ/kg·K)
      const mDot = state.flowLpm / 60; // kg/s approx
      const tIn = 28.0;
      const deltaTFluid = (effectiveKw + lossKw * 0.4) / Math.max(0.4, mDot * 3.85);
      const targetOutlet = tIn + deltaTFluid;
      const filmDeltaT = (effectiveKw * 0.19) / nusseltBoost + (state.surgeKw * 0.45);
      const targetTj = targetOutlet + filmDeltaT;

      // Smooth thermal inertia
      state.outletTemp += (targetOutlet - state.outletTemp) * Math.min(1, dt * 3.2);
      state.tj += (targetTj - state.tj) * Math.min(1, dt * 2.8);

      // HowardPro AI Closed-Loop PID Controller
      if (state.aiAuto) {
        const targetOptimalTj = 55.5;
        const err = state.tj - targetOptimalTj;
        const desiredFlow = Math.min(180, Math.max(55, state.flowLpm + err * dt * 4.2));
        state.flowLpm += (desiredFlow - state.flowLpm) * Math.min(1, dt * 3.0);
        if (elFlow) elFlow.value = Math.round(state.flowLpm);
        if (elFlowVal) elFlowVal.textContent = Math.round(state.flowLpm) + ' LPM';
      }

      // Pump power scales cubically with flow (Affinity Law: P_pump ~ Q^3)
      const pumpKw = 0.6 + 2.4 * Math.pow(state.flowLpm / 180, 3);
      const pue = 1 + (pumpKw + lossKw + 3.2) / Math.max(20, effectiveKw);

      // Update DOM telemetry
      if (outCurrent) outCurrent.textContent = currentA >= 1000 ? (currentA / 1000).toFixed(2) + ' kA' : currentA.toFixed(1) + ' A';
      if (outCurrentSub) outCurrentSub.textContent = state.voltage + 'V DC · ' + effectiveKw.toFixed(1) + ' kW';
      if (outLoss) outLoss.textContent = lossKw.toFixed(2) + ' kW';
      if (outLossSub) outLossSub.textContent = state.voltage === 800 ? I18N.lossSave(lossSavePct) : I18N.lossBase;
      if (outRe) outRe.textContent = 'Re ' + re.toLocaleString();
      if (outReSub) outReSub.textContent = regime;
      if (outTemp) outTemp.textContent = state.tj.toFixed(1) + ' °C';
      if (outTempSub) outTempSub.textContent = state.tj > 72 ? I18N.tempHot : (state.tj > 60 ? I18N.tempWarn : I18N.tempOk);
      if (outPue) outPue.textContent = pue.toFixed(2);
      if (outPueSub) outPueSub.textContent = I18N.pueSub(state.aiAuto ? 31 : 18);

      if (aiPill) {
        aiPill.classList.remove('warn', 'alert');
        if (state.tj > 72) {
          aiPill.classList.add('alert');
          aiPill.textContent = '⚠ ' + I18N.aiAlert;
        } else if (state.tj > 62) {
          aiPill.classList.add('warn');
          aiPill.textContent = '⚡ ' + I18N.aiWarn;
        } else {
          aiPill.textContent = (state.aiAuto ? '● ' + I18N.aiAutoOn : '○ ' + I18N.aiAutoOff);
        }
      }

      return { currentA, lossKw, re, effectiveKw };
    }

    function lerpColor(t) {
      // 0 = cool cyan (#38BDF8), 0.5 = emerald/gold (#DEC082), 1 = hot brick (#EF4444)
      const c = Math.max(0, Math.min(1, t));
      if (c < 0.5) {
        const k = c * 2;
        const r = Math.round(56 + (222 - 56) * k);
        const g = Math.round(189 + (192 - 189) * k);
        const b = Math.round(248 + (130 - 248) * k);
        return `rgb(${r},${g},${b})`;
      } else {
        const k = (c - 0.5) * 2;
        const r = Math.round(222 + (239 - 222) * k);
        const g = Math.round(192 + (68 - 192) * k);
        const b = Math.round(130 + (68 - 130) * k);
        return `rgb(${r},${g},${b})`;
      }
    }

    function drawTwin(now) {
      requestAnimationFrame(drawTwin);
      if (!state.visible || document.hidden) return;
      if (now - lastFrame < 30) return;
      const dt = Math.min(0.08, (now - lastFrame) / 1000 || 0.033);
      lastFrame = now;
      const t = now * 0.001;

      const phys = computePhysics(dt);

      // Deep dark laboratory backdrop
      ctx.fillStyle = '#0F1714';
      ctx.fillRect(0, 0, w, h);

      // Subtle engineering grid
      ctx.strokeStyle = 'rgba(169, 200, 181, 0.06)';
      ctx.lineWidth = 1;
      for (let x = 32; x < w; x += 32) {
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke();
      }
      for (let y = 32; y < h; y += 32) {
        ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke();
      }

      // Layout geometry
      const pad = Math.max(14, w * 0.025);
      const topY = 38;
      const botY = h - 34;
      const innerH = botY - topY;

      const pwrX = pad;
      const pwrW = w * 0.22;
      const gpuX = pwrX + pwrW + w * 0.08;
      const gpuW = w * 0.34;
      const cduX = gpuX + gpuW + w * 0.08;
      const cduW = w - cduX - pad;

      // Zone Headers (responsive compact labels on mobile < 540px)
      const compact = w < 540;
      ctx.font = compact
        ? '600 10px "Inter", "Noto Sans TC", sans-serif'
        : '600 11.5px "Inter", "Noto Sans TC", sans-serif';
      ctx.fillStyle = state.voltage === 800 ? '#DEC082' : '#F87171';
      ctx.fillText(compact ? (state.voltage === 800 ? '⚡ 800V' : '⚡ 48V!') : (state.voltage === 800 ? '⚡ ' + I18N.zonePower : '⚡ ' + I18N.zonePower48), pwrX, 22);
      ctx.fillStyle = '#A9C8B5';
      ctx.fillText(compact ? '🖥 AIDC GPU' : '🖥 ' + I18N.zoneGpu, gpuX, 22);
      ctx.fillStyle = '#38BDF8';
      ctx.fillText(compact ? '💧 120kW CDU' : '💧 ' + I18N.zoneCdu, cduX, 22);

      // 4 Horizontal Blade Lanes
      const laneH = innerH / 4;

      // --- ZONE A: POWER SHELF ---
      ctx.fillStyle = 'rgba(27, 34, 30, 0.9)';
      ctx.strokeStyle = state.voltage === 800 ? 'rgba(222, 192, 130, 0.45)' : 'rgba(239, 68, 68, 0.65)';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.roundRect(pwrX, topY, pwrW, innerH, 6);
      ctx.fill();
      ctx.stroke();

      // Draw Power Busbars from Power Shelf -> GPU Rack
      const busStartX = pwrX + pwrW;
      const busEndX = gpuX;
      for (let i = 0; i < 4; i++) {
        const ly = topY + laneH * (i + 0.5);
        // Internal power module bar
        ctx.fillStyle = state.voltage === 800 ? 'rgba(222, 192, 130, 0.14)' : 'rgba(239, 68, 68, 0.22)';
        ctx.fillRect(pwrX + 8, topY + i * laneH + 7, pwrW - 16, laneH - 14);
        ctx.fillStyle = '#EFECE6';
        ctx.font = compact ? '600 9.5px ui-monospace, monospace' : '600 10.5px ui-monospace, monospace';
        ctx.fillText(compact ? `P0${i + 1}·${state.voltage}V` : (state.voltage === 800 ? `PSU-0${i + 1} · 800V` : `PSU-0${i + 1} · 48V!`), pwrX + (compact ? 6 : 14), ly + 4);

        // Busbar conduit
        ctx.strokeStyle = state.voltage === 800 ? 'rgba(222, 192, 130, 0.35)' : 'rgba(239, 68, 68, 0.5)';
        ctx.lineWidth = state.voltage === 800 ? 3 : 5;
        ctx.beginPath();
        ctx.moveTo(busStartX, ly);
        ctx.lineTo(busEndX, ly);
        ctx.stroke();
      }

      // Animated Electric Current Charge Carriers (I = P / V)
      const elecSpeed = state.voltage === 800
        ? 0.35 + (phys.effectiveKw / 130) * 0.65
        : 1.15 + (phys.effectiveKw / 130) * 1.45;
      for (let i = 0; i < charges.length; i++) {
        const c = charges[i];
        c.u = (c.u + dt * elecSpeed) % 1;
        const ly = topY + laneH * (c.bus + 0.5);
        const cx = busStartX + c.u * (busEndX - busStartX);
        // 48V high-current exhibits resistive jitter & heat sparks
        const jy = state.voltage === 48 ? Math.sin(t * 28 + c.jitter) * 4.5 : Math.sin(t * 8 + c.jitter) * 0.8;

        ctx.beginPath();
        ctx.arc(cx, ly + jy, state.voltage === 48 ? 3.1 : 2.3, 0, Math.PI * 2);
        ctx.fillStyle = state.voltage === 800 ? '#FDE68A' : '#FCA5A5';
        ctx.fill();

        // Electric arc pulse along bus
        if (state.voltage === 48 && Math.random() < 0.08) {
          ctx.strokeStyle = 'rgba(248, 113, 113, 0.75)';
          ctx.lineWidth = 1.2;
          ctx.beginPath();
          ctx.moveTo(cx - 8, ly);
          ctx.lineTo(cx, ly + (Math.random() - 0.5) * 14);
          ctx.lineTo(cx + 8, ly);
          ctx.stroke();
        }
      }

      // --- ZONE B: HOWARD AIDC GPU RACK ---
      const heatNorm = Math.min(1, Math.max(0, (state.tj - 38) / 42));
      ctx.fillStyle = 'rgba(22, 29, 25, 0.94)';
      ctx.strokeStyle = lerpColor(heatNorm);
      ctx.lineWidth = 1.6;
      ctx.beginPath();
      ctx.roundRect(gpuX, topY, gpuW, innerH, 6);
      ctx.fill();
      ctx.stroke();

      for (let i = 0; i < 4; i++) {
        const by = topY + i * laneH + 6;
        const bh = laneH - 12;
        const bladeHeat = Math.min(1, Math.max(0, heatNorm + (i === 1 && state.surgeKw > 1 ? 0.25 : 0)));
        const grad = ctx.createLinearGradient(gpuX + 8, by, gpuX + gpuW - 8, by);
        grad.addColorStop(0, 'rgba(56, 189, 248, 0.14)');
        grad.addColorStop(0.55, `rgba(222, 192, 130, ${(0.12 + bladeHeat * 0.22).toFixed(2)})`);
        grad.addColorStop(1, `rgba(239, 68, 68, ${(0.08 + bladeHeat * 0.34).toFixed(2)})`);
        ctx.fillStyle = grad;
        ctx.beginPath();
        ctx.roundRect(gpuX + 8, by, gpuW - 16, bh, 4);
        ctx.fill();

        ctx.fillStyle = 'rgba(239, 236, 230, 0.85)';
        ctx.font = '600 10.5px ui-monospace, monospace';
        ctx.fillText(`MIG-0${i + 1} · vLLM`, gpuX + 14, by + 15);
      }

      // --- ZONE C: 120kW LIQUID COOLING CDU ---
      ctx.fillStyle = 'rgba(14, 34, 42, 0.86)';
      ctx.strokeStyle = 'rgba(56, 189, 248, 0.55)';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.roundRect(cduX, topY, cduW, innerH, 6);
      ctx.fill();
      ctx.stroke();

      // CDU Pump Impeller Rotation (angular speed scales with LPM)
      const pumpCx = cduX + cduW * 0.5;
      const pumpCy = topY + innerH * 0.5;
      const pumpR = Math.min(cduW, innerH) * 0.26;
      ctx.save();
      ctx.translate(pumpCx, pumpCy);
      ctx.rotate(t * (1.2 + (state.flowLpm / 180) * 6.5));
      ctx.strokeStyle = 'rgba(56, 189, 248, 0.75)';
      ctx.lineWidth = 2;
      for (let b = 0; b < 6; b++) {
        ctx.rotate(Math.PI / 3);
        ctx.beginPath();
        ctx.moveTo(0, 0);
        ctx.quadraticCurveTo(pumpR * 0.55, pumpR * 0.35, pumpR, 0);
        ctx.stroke();
      }
      ctx.restore();
      ctx.beginPath();
      ctx.arc(pumpCx, pumpCy, pumpR + 5, 0, Math.PI * 2);
      ctx.strokeStyle = 'rgba(56, 189, 248, 0.35)';
      ctx.lineWidth = 1.5;
      ctx.stroke();

      ctx.fillStyle = '#BAE6FD';
      ctx.font = '600 10.5px ui-monospace, monospace';
      ctx.textAlign = 'center';
      ctx.fillText(`${Math.round(state.flowLpm)} LPM`, pumpCx, topY + 20);
      ctx.fillText(I18N.inlet, pumpCx, botY - 22);
      ctx.fillStyle = lerpColor(heatNorm);
      ctx.fillText(I18N.outlet(state.outletTemp), pumpCx, botY - 8);
      ctx.textAlign = 'left';

      // --- FLUID DYNAMICS STREAMLINES ACROSS GPU COLD-PLATES <-> CDU ---
      const chStartX = gpuX + 8;
      const chEndX = cduX;
      const chSpan = chEndX - chStartX;
      const flowSpeed = 0.22 + (state.flowLpm / 180) * 0.78;
      const turbAmp = phys.re >= 4000 ? 7.5 : (phys.re >= 2300 ? 3.6 : 0.7);
      const turbFreq = phys.re >= 4000 ? 11 : 5;

      for (let i = 0; i < fluid.length; i++) {
        const f = fluid[i];
        // Poiseuille parabolic profile: faster at channel centerline (offset ≈ 0), slower near walls
        const poiseuille = 1.15 - 0.65 * (f.offset * f.offset);
        f.u = (f.u + dt * flowSpeed * poiseuille) % 1;

        const baseY = topY + laneH * (f.lane + 0.5) + f.offset * (laneH * 0.32);
        let px = chStartX + f.u * chSpan;
        let py = baseY + Math.sin(f.u * turbFreq + t * 5 + f.phase) * turbAmp;

        // Interactive pointer vortex deflection
        if (state.vortexPower > 0.05) {
          const dx = px - state.vortexX;
          const dy = py - state.vortexY;
          const d2 = dx * dx + dy * dy + 600;
          if (d2 < 18000) {
            const kick = (state.vortexPower * 3400) / d2;
            py += Math.sin(t * 14 + f.phase) * kick * 8;
          }
        }

        // Local temperature color: cold at left inlet, heats up across GPU cold plate
        const localHeat = Math.min(1, Math.max(0, f.u * (0.45 + heatNorm * 0.65)));
        ctx.fillStyle = lerpColor(localHeat);
        ctx.beginPath();
        ctx.ellipse(px, py, f.size * (1.8 + flowSpeed * 1.4), f.size * 0.78, 0, 0, Math.PI * 2);
        ctx.fill();
      }

      // Interactive thermal surge ripples on canvas
      for (let i = sparks.length - 1; i >= 0; i--) {
        const sp = sparks[i];
        sp.r += 2.8;
        sp.a *= 0.93;
        ctx.beginPath();
        ctx.arc(sp.x, sp.y, sp.r, 0, Math.PI * 2);
        ctx.strokeStyle = `rgba(251, 146, 60, ${sp.a.toFixed(3)})`;
        ctx.lineWidth = 2;
        ctx.stroke();
        if (sp.a < 0.04) sparks.splice(i, 1);
      }
    }

    // Bind sliders & toggles
    if (elLoad) {
      elLoad.addEventListener('input', () => {
        state.loadKw = +elLoad.value;
        if (elLoadVal) elLoadVal.textContent = state.loadKw + ' kW';
      });
    }
    if (elFlow) {
      elFlow.addEventListener('input', () => {
        state.flowLpm = +elFlow.value;
        if (elFlowVal) elFlowVal.textContent = state.flowLpm + ' LPM';
        if (state.aiAuto) {
          state.aiAuto = false;
          if (btnAi) { btnAi.classList.remove('on'); btnAi.textContent = 'OFF'; }
        }
      });
    }
    if (btn800 && btn48) {
      btn800.addEventListener('click', () => {
        state.voltage = 800;
        btn800.classList.add('on');
        btn48.classList.remove('on', 'v48');
      });
      btn48.addEventListener('click', () => {
        state.voltage = 48;
        btn48.classList.add('on', 'v48');
        btn800.classList.remove('on');
      });
    }
    if (btnAi) {
      btnAi.addEventListener('click', () => {
        state.aiAuto = !state.aiAuto;
        btnAi.classList.toggle('on', state.aiAuto);
        btnAi.textContent = state.aiAuto ? 'ON' : 'OFF';
      });
    }

    // Scenario presets
    const presetWrap = document.getElementById('efPresets');
    if (presetWrap) {
      presetWrap.addEventListener('click', (ev) => {
        const b = ev.target.closest('.ef-pbtn');
        if (!b) return;
        if (b.dataset.surge) {
          state.surgeKw = Math.min(35, state.surgeKw + 18);
          state.vortexX = w * 0.48;
          state.vortexY = h * 0.5;
          state.vortexPower = 1.6;
          sparks.push({ x: w * 0.48, y: h * 0.5, r: 10, a: 0.95 });
          const toast = document.getElementById('toast');
          if (toast) {
            toast.textContent = I18N.surgeMsg;
            toast.classList.add('on');
            setTimeout(() => toast.classList.remove('on'), 2600);
          }
          return;
        }
        presetWrap.querySelectorAll('.ef-pbtn:not(.surge)').forEach(x => x.classList.toggle('on', x === b));
        state.loadKw = +b.dataset.kw;
        if (elLoad) elLoad.value = state.loadKw;
        if (elLoadVal) elLoadVal.textContent = state.loadKw + ' kW';
      });
    }

    // Direct canvas click / drag injects localized thermal hotspot + fluid vortex
    function injectAt(ev) {
      const r = canvas.getBoundingClientRect();
      const x = ev.clientX - r.left;
      const y = ev.clientY - r.top;
      state.vortexX = x;
      state.vortexY = y;
      state.vortexPower = 1.4;
      state.surgeKw = Math.min(28, state.surgeKw + 9);
      sparks.push({ x, y, r: 8, a: 0.9 });
    }
    canvas.addEventListener('pointerdown', injectAt);
    canvas.addEventListener('pointermove', (ev) => {
      if (ev.buttons === 1) injectAt(ev);
    });

    const io = new IntersectionObserver(entries => {
      entries.forEach(en => { state.visible = en.isIntersecting; });
    }, { threshold: 0.05 });
    io.observe(canvas);

    window.addEventListener('resize', resize, { passive: true });
    initParticles();
    resize();
    requestAnimationFrame(drawTwin);
  }

  /* =========================================================================
   * 3. INTERACTIVE ENTERPRISE ARCHITECTURE FLOW (Section 05 .la-ea)
   * ========================================================================= */
  function initInteractiveEA() {
    const ea = document.querySelector('#arch .la-ea');
    if (!ea) return;
    const rows = Array.from(ea.querySelectorAll('.la-row'));
    if (!rows.length) return;

    const brief = document.createElement('div');
    brief.className = 'ef-ea-brief';
    brief.setAttribute('aria-live', 'polite');
    brief.innerHTML = '<span>⚡ ' + I18N.eaDefault + '</span>';
    ea.insertAdjacentElement('afterend', brief);

    rows.forEach((row, idx) => {
      row.setAttribute('tabindex', '0');
      row.setAttribute('role', 'button');
      const activate = () => {
        rows.forEach(r => r.classList.remove('ef-active'));
        row.classList.add('ef-active');
        const msg = I18N.eaBriefs[idx] || I18N.eaDefault;
        brief.innerHTML = '<span>⚡ <b>' + msg.split('】')[0].replace('[', '').replace('【', '') + '</b> ' +
          (msg.includes('】') ? msg.split('】')[1] : msg.replace(/^\[[^\]]+\]\s*/, '')) + '</span>';
      };
      row.addEventListener('click', activate);
      row.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          activate();
        }
      });
    });
  }

  /* =========================================================================
   * 4. QUICK SPOTLIGHT SEARCH (Cmd+K / '/')
   * ========================================================================= */
  function initSpotlight() {
    const navIn = document.querySelector('header.nav .in');
    if (!navIn) return;

    // Insert compact search button before theme button
    const tbtn = document.getElementById('theme');
    const sbtn = document.createElement('button');
    sbtn.type = 'button';
    sbtn.className = 'ef-search-btn';
    sbtn.id = 'efSearchBtn';
    sbtn.setAttribute('aria-label', I18N.searchBtn);
    sbtn.innerHTML = '<span>🔍</span><kbd>/</kbd>';
    if (tbtn && tbtn.parentNode === navIn) {
      navIn.insertBefore(sbtn, tbtn);
    } else {
      navIn.appendChild(sbtn);
    }

    // Build index from live DOM sections & interactive labs
    const items = [];
    document.querySelectorAll('main > section[id]').forEach(sec => {
      const h = sec.querySelector('h2, h1');
      const ey = sec.querySelector('.eyebrow');
      const sub = sec.querySelector('.sub, .lead');
      if (h) {
        items.push({
          id: '#' + sec.id,
          title: (ey ? ey.textContent.trim() + ' · ' : '') + h.textContent.trim(),
          desc: sub ? sub.textContent.trim().slice(0, 90) : '',
          hay: (sec.textContent || '').toLowerCase()
        });
      }
    });
    const twin = document.getElementById('ef-twin-lab');
    if (twin) {
      const th = twin.querySelector('h3');
      items.unshift({
        id: '#ef-twin-lab',
        title: '⚡💧 ' + (th ? th.textContent.trim() : '800V DC × 120kW CDU Lab'),
        desc: '800V DC Electric Current × 120kW Liquid Cooling CDU Fluid Dynamics Interactive Simulator',
        hay: '800v dc 48v cdu fluid dynamics electric current 電流 流體力學 模擬 液冷 雷諾數 pue ' + (twin.textContent || '').toLowerCase()
      });
    }

    // Create modal
    const back = document.createElement('div');
    back.className = 'ef-spot-back';
    back.hidden = true;
    back.setAttribute('role', 'dialog');
    back.setAttribute('aria-modal', 'true');
    back.innerHTML =
      '<div class="ef-spot">' +
        '<div class="ef-spot-hd"><span>🔍</span><input type="search" id="efSpotIn" placeholder="' + I18N.searchPh + '" autocomplete="off"><button type="button" id="efSpotClose">ESC</button></div>' +
        '<div class="ef-spot-list" id="efSpotList"></div>' +
      '</div>';
    document.body.appendChild(back);

    const inp = document.getElementById('efSpotIn');
    const list = document.getElementById('efSpotList');
    const btnClose = document.getElementById('efSpotClose');

    function render(q) {
      const needle = (q || '').trim().toLowerCase();
      const matched = needle
        ? items.filter(it => it.title.toLowerCase().includes(needle) || it.hay.includes(needle)).slice(0, 10)
        : items.slice(0, 8);
      if (!matched.length) {
        list.innerHTML = '<div style="padding:14px;color:var(--mute);font-size:13.5px">' + I18N.searchEmpty + '</div>';
        return;
      }
      list.innerHTML = matched.map((it, idx) =>
        '<a class="ef-spot-item' + (idx === 0 ? ' sel' : '') + '" href="' + it.id + '"><b>' +
        it.title.replace(/</g, '&lt;') + '</b><span>' + it.desc.replace(/</g, '&lt;') + '</span></a>'
      ).join('');
    }

    function open() {
      back.hidden = false;
      inp.value = '';
      render('');
      setTimeout(() => inp.focus(), 20);
    }
    function close() {
      back.hidden = true;
    }

    sbtn.addEventListener('click', open);
    btnClose.addEventListener('click', close);
    back.addEventListener('click', (e) => { if (e.target === back) close(); });
    inp.addEventListener('input', () => render(inp.value));
    inp.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        const first = list.querySelector('.ef-spot-item');
        if (first) {
          close();
          const target = document.querySelector(first.getAttribute('href'));
          if (target) target.scrollIntoView({ behavior: reducedMotion ? 'auto' : 'smooth' });
        }
      }
    });
    list.addEventListener('click', (e) => {
      if (e.target.closest('.ef-spot-item')) close();
    });

    document.addEventListener('keydown', (e) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        back.hidden ? open() : close();
      } else if (e.key === '/' && !['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName) && back.hidden) {
        e.preventDefault();
        open();
      } else if (e.key === 'Escape' && !back.hidden) {
        close();
      }
    });
  }

  // Boot cleanly
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      initHeroField();
      initTwinLab();
      initInteractiveEA();
      initSpotlight();
    });
  } else {
    initHeroField();
    initTwinLab();
    initInteractiveEA();
    initSpotlight();
  }
})();
