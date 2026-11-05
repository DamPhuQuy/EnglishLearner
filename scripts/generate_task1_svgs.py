#!/usr/bin/env python3
"""
Generates high-definition, authentic IELTS Academic Task 1 vector SVG graphics:
1. task1_bar_chart_renewables.svg
2. task1_line_graph_smartphones.svg
3. task1_pie_chart_energy.svg
4. task1_table_university.svg
5. task1_proc_battery_recycling.svg
6. task1_map_port_haven.svg
7. task1_proc_pumped_storage.svg
8. task1_multi_farmland_deforestation.svg
"""

import math
import os

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend", "public", "images", "writing")
os.makedirs(OUT_DIR, exist_ok=True)

def generate_svg_1_bar_chart():
    # Solar PV, Wind Energy, Hydroelectric (2010, 2014, 2018, 2023)
    # Solar: 85, 130, 180, 320
    # Wind: 110, 135, 160, 215
    # Hydro: 55, 65, 45, 38
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 420" width="100%" height="100%" style="background:#0f172a; font-family:system-ui,-apple-system,sans-serif;">
  <defs>
    <linearGradient id="solarGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f59e0b"/><stop offset="100%" stop-color="#d97706"/></linearGradient>
    <linearGradient id="windGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#06b6d4"/><stop offset="100%" stop-color="#0891b2"/></linearGradient>
    <linearGradient id="hydroGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#3b82f6"/><stop offset="100%" stop-color="#2563eb"/></linearGradient>
  </defs>

  <!-- Title & Subtitle -->
  <text x="380" y="32" text-anchor="middle" fill="#f8fafc" font-size="16" font-weight="700">Global Renewable Energy Investment by Technology (2010–2023)</text>
  <text x="380" y="52" text-anchor="middle" fill="#94a3b8" font-size="12">Annual Capital Deployment in Billions of US Dollars ($bn)</text>

  <!-- Y-Axis Gridlines & Labels (Max 350, step 50) -->
  <!-- Y=330 at 0, Y=70 at 350 -> scale: (330-70)/350 = 260/350 = 0.7428 px per bn -->
  <!-- 0: 330, 50: 293, 100: 256, 150: 219, 200: 181, 250: 144, 300: 107, 350: 70 -->
  <g stroke="#334155" stroke-width="1" stroke-dasharray="4,4">
    <line x1="90" y1="70" x2="710" y2="70" />
    <line x1="90" y1="107" x2="710" y2="107" />
    <line x1="90" y1="144" x2="710" y2="144" />
    <line x1="90" y1="181" x2="710" y2="181" />
    <line x1="90" y1="219" x2="710" y2="219" />
    <line x1="90" y1="256" x2="710" y2="256" />
    <line x1="90" y1="293" x2="710" y2="293" />
  </g>
  <line x1="90" y1="330" x2="710" y2="330" stroke="#64748b" stroke-width="1.5" />

  <!-- Y-axis labels -->
  <g fill="#94a3b8" font-size="11" text-anchor="end">
    <text x="80" y="74">350</text>
    <text x="80" y="111">300</text>
    <text x="80" y="148">250</text>
    <text x="80" y="185">200</text>
    <text x="80" y="223">150</text>
    <text x="80" y="260">100</text>
    <text x="80" y="297">50</text>
    <text x="80" y="334">0</text>
  </g>

  <!-- Group 1: 2010 (Center ~ 170) -->
  <!-- Solar 85: h = 85*0.743 = 63, y = 330-63 = 267 -->
  <rect x="130" y="267" width="28" height="63" rx="3" fill="url(#solarGrad)" />
  <text x="144" y="261" fill="#fef08a" font-size="10" font-weight="600" text-anchor="middle">85</text>
  <!-- Wind 110: h = 110*0.743 = 82, y = 330-82 = 248 -->
  <rect x="162" y="248" width="28" height="82" rx="3" fill="url(#windGrad)" />
  <text x="176" y="242" fill="#a5f3fc" font-size="10" font-weight="600" text-anchor="middle">110</text>
  <!-- Hydro 55: h = 55*0.743 = 41, y = 330-41 = 289 -->
  <rect x="194" y="289" width="28" height="41" rx="3" fill="url(#hydroGrad)" />
  <text x="208" y="283" fill="#bfdbfe" font-size="10" font-weight="600" text-anchor="middle">55</text>
  <text x="176" y="352" fill="#e2e8f0" font-size="13" font-weight="600" text-anchor="middle">2010</text>

  <!-- Group 2: 2014 (Center ~ 320) -->
  <!-- Solar 130: h = 97, y = 233 -->
  <rect x="280" y="233" width="28" height="97" rx="3" fill="url(#solarGrad)" />
  <text x="294" y="227" fill="#fef08a" font-size="10" font-weight="600" text-anchor="middle">130</text>
  <!-- Wind 135: h = 100, y = 230 -->
  <rect x="312" y="230" width="28" height="100" rx="3" fill="url(#windGrad)" />
  <text x="326" y="224" fill="#a5f3fc" font-size="10" font-weight="600" text-anchor="middle">135</text>
  <!-- Hydro 65: h = 48, y = 282 -->
  <rect x="344" y="282" width="28" height="48" rx="3" fill="url(#hydroGrad)" />
  <text x="358" y="276" fill="#bfdbfe" font-size="10" font-weight="600" text-anchor="middle">65</text>
  <text x="326" y="352" fill="#e2e8f0" font-size="13" font-weight="600" text-anchor="middle">2014</text>

  <!-- Group 3: 2018 (Center ~ 470) -->
  <!-- Solar 180: h = 134, y = 196 -->
  <rect x="430" y="196" width="28" height="134" rx="3" fill="url(#solarGrad)" />
  <text x="444" y="190" fill="#fef08a" font-size="10" font-weight="600" text-anchor="middle">180</text>
  <!-- Wind 160: h = 119, y = 211 -->
  <rect x="462" y="211" width="28" height="119" rx="3" fill="url(#windGrad)" />
  <text x="476" y="205" fill="#a5f3fc" font-size="10" font-weight="600" text-anchor="middle">160</text>
  <!-- Hydro 45: h = 33, y = 297 -->
  <rect x="494" y="297" width="28" height="33" rx="3" fill="url(#hydroGrad)" />
  <text x="508" y="291" fill="#bfdbfe" font-size="10" font-weight="600" text-anchor="middle">45</text>
  <text x="476" y="352" fill="#e2e8f0" font-size="13" font-weight="600" text-anchor="middle">2018</text>

  <!-- Group 4: 2023 (Center ~ 620) -->
  <!-- Solar 320: h = 238, y = 92 -->
  <rect x="580" y="92" width="28" height="238" rx="3" fill="url(#solarGrad)" />
  <text x="594" y="86" fill="#fef08a" font-size="10" font-weight="700" text-anchor="middle">320</text>
  <!-- Wind 215: h = 160, y = 170 -->
  <rect x="612" y="170" width="28" height="160" rx="3" fill="url(#windGrad)" />
  <text x="626" y="164" fill="#a5f3fc" font-size="10" font-weight="600" text-anchor="middle">215</text>
  <!-- Hydro 38: h = 28, y = 302 -->
  <rect x="644" y="302" width="28" height="28" rx="3" fill="url(#hydroGrad)" />
  <text x="658" y="296" fill="#bfdbfe" font-size="10" font-weight="600" text-anchor="middle">38</text>
  <text x="626" y="352" fill="#e2e8f0" font-size="13" font-weight="600" text-anchor="middle">2023</text>

  <!-- Legend -->
  <g transform="translate(180, 385)">
    <rect x="0" y="0" width="16" height="12" rx="2" fill="url(#solarGrad)" />
    <text x="24" y="10" fill="#cbd5e1" font-size="12">Solar Photovoltaic</text>

    <rect x="150" y="0" width="16" height="12" rx="2" fill="url(#windGrad)" />
    <text x="174" y="10" fill="#cbd5e1" font-size="12">Wind Power</text>

    <rect x="270" y="0" width="16" height="12" rx="2" fill="url(#hydroGrad)" />
    <text x="294" y="10" fill="#cbd5e1" font-size="12">Hydroelectric Power</text>
  </g>
</svg>"""
    with open(os.path.join(OUT_DIR, "task1_bar_chart_renewables.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

def generate_svg_2_line_graph():
    # Smartphone Adoption: 2012, 2014, 2016, 2018, 2020, 2022
    # 18–29: 72 -> 81 -> 87 -> 91 -> 95 -> 98
    # 30–49: 54 -> 63 -> 73 -> 81 -> 88 -> 92
    # 50–64: 31 -> 42 -> 60 -> 68 -> 74 -> 80
    # 65+:   14 -> 22 -> 33 -> 43 -> 50 -> 58
    # X points: 2012=140, 2014=250, 2016=360, 2018=470, 2020=580, 2022=690
    # Y range: 0% = 330, 100% = 70. Height = 260. Y = 330 - (val * 2.6)
    xs = [140, 250, 360, 470, 580, 690]
    p18 = [72, 81, 87, 91, 95, 98]
    p30 = [54, 63, 73, 81, 88, 92]
    p50 = [31, 42, 60, 68, 74, 80]
    p65 = [14, 22, 33, 43, 50, 58]

    def line_path(pts):
        coords = [f"{xs[i]},{330 - int(pts[i] * 2.6)}" for i in range(len(pts))]
        return "M " + " L ".join(coords)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 420" width="100%" height="100%" style="background:#0f172a; font-family:system-ui,-apple-system,sans-serif;">
  <!-- Title -->
  <text x="380" y="32" text-anchor="middle" fill="#f8fafc" font-size="16" font-weight="700">Smartphone Adoption Across Age Demographics (2012–2022)</text>
  <text x="380" y="52" text-anchor="middle" fill="#94a3b8" font-size="12">Percentage of European Population Utilizing Smartphones Daily (%)</text>

  <!-- Gridlines -->
  <g stroke="#334155" stroke-width="1" stroke-dasharray="4,4">
    <line x1="90" y1="70" x2="710" y2="70" />
    <line x1="90" y1="122" x2="710" y2="122" />
    <line x1="90" y1="174" x2="710" y2="174" />
    <line x1="90" y1="226" x2="710" y2="226" />
    <line x1="90" y1="278" x2="710" y2="278" />
  </g>
  <line x1="90" y1="330" x2="710" y2="330" stroke="#64748b" stroke-width="1.5" />

  <!-- Y labels -->
  <g fill="#94a3b8" font-size="11" text-anchor="end">
    <text x="80" y="74">100%</text>
    <text x="80" y="126">80%</text>
    <text x="80" y="178">60%</text>
    <text x="80" y="230">40%</text>
    <text x="80" y="282">20%</text>
    <text x="80" y="334">0%</text>
  </g>

  <!-- X axis labels & vertical guidelines -->
  <g fill="#e2e8f0" font-size="12" font-weight="600" text-anchor="middle">
    <text x="140" y="352">2012</text>
    <text x="250" y="352">2014</text>
    <text x="360" y="352">2016</text>
    <text x="470" y="352">2018</text>
    <text x="580" y="352">2020</text>
    <text x="690" y="352">2022</text>
  </g>

  <!-- Lines -->
  <!-- 18-29 -->
  <path d="{line_path(p18)}" fill="none" stroke="#a855f7" stroke-width="3" stroke-linecap="round" />
  <!-- 30-49 -->
  <path d="{line_path(p30)}" fill="none" stroke="#10b981" stroke-width="3" stroke-linecap="round" />
  <!-- 50-64 -->
  <path d="{line_path(p50)}" fill="none" stroke="#06b6d4" stroke-width="3" stroke-linecap="round" />
  <!-- 65+ -->
  <path d="{line_path(p65)}" fill="none" stroke="#f43f5e" stroke-width="3" stroke-linecap="round" />

  <!-- Dots & Values for Line 1 (18-29) -->
  {"".join([f'<circle cx="{xs[i]}" cy="{330 - int(p18[i]*2.6)}" r="4.5" fill="#c084fc" stroke="#581c87" stroke-width="2"/>' for i in range(len(xs))])}
  <!-- Dots for Line 2 (30-49) -->
  {"".join([f'<circle cx="{xs[i]}" cy="{330 - int(p30[i]*2.6)}" r="4.5" fill="#34d399" stroke="#064e3b" stroke-width="2"/>' for i in range(len(xs))])}
  <!-- Dots for Line 3 (50-64) -->
  {"".join([f'<circle cx="{xs[i]}" cy="{330 - int(p50[i]*2.6)}" r="4.5" fill="#22d3ee" stroke="#164e63" stroke-width="2"/>' for i in range(len(xs))])}
  <!-- Dots for Line 4 (65+) -->
  {"".join([f'<circle cx="{xs[i]}" cy="{330 - int(p65[i]*2.6)}" r="4.5" fill="#fb7185" stroke="#881337" stroke-width="2"/>' for i in range(len(xs))])}

  <!-- Final labels on 2022 endpoint -->
  <text x="702" y="{330 - int(98*2.6) + 4}" fill="#c084fc" font-size="11" font-weight="700">98%</text>
  <text x="702" y="{330 - int(92*2.6) + 4}" fill="#34d399" font-size="11" font-weight="700">92%</text>
  <text x="702" y="{330 - int(80*2.6) + 4}" fill="#22d3ee" font-size="11" font-weight="700">80%</text>
  <text x="702" y="{330 - int(58*2.6) + 4}" fill="#fb7185" font-size="11" font-weight="700">58%</text>

  <!-- Legend -->
  <g transform="translate(130, 385)">
    <line x1="0" y1="8" x2="20" y2="8" stroke="#a855f7" stroke-width="3" />
    <circle cx="10" cy="8" r="4" fill="#c084fc" />
    <text x="26" y="12" fill="#cbd5e1" font-size="12">18–29 yrs</text>

    <line x1="120" y1="8" x2="140" y2="8" stroke="#10b981" stroke-width="3" />
    <circle cx="130" cy="8" r="4" fill="#34d399" />
    <text x="146" y="12" fill="#cbd5e1" font-size="12">30–49 yrs</text>

    <line x1="240" y1="8" x2="260" y2="8" stroke="#06b6d4" stroke-width="3" />
    <circle cx="250" cy="8" r="4" fill="#22d3ee" />
    <text x="266" y="12" fill="#cbd5e1" font-size="12">50–64 yrs</text>

    <line x1="360" y1="8" x2="380" y2="8" stroke="#f43f5e" stroke-width="3" />
    <circle cx="370" cy="8" r="4" fill="#fb7185" />
    <text x="386" y="12" fill="#cbd5e1" font-size="12">65+ yrs</text>
  </g>
</svg>"""
    with open(os.path.join(OUT_DIR, "task1_line_graph_smartphones.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

def make_pie_path(cx, cy, r, start_pct, end_pct):
    s_ang = start_pct * 2 * math.pi - math.pi / 2
    e_ang = end_pct * 2 * math.pi - math.pi / 2
    x1 = cx + r * math.cos(s_ang)
    y1 = cy + r * math.sin(s_ang)
    x2 = cx + r * math.cos(e_ang)
    y2 = cy + r * math.sin(e_ang)
    large = 1 if (end_pct - start_pct) > 0.5 else 0
    return f"M {cx},{cy} L {x1:.2f},{y1:.2f} A {r},{r} 0 {large},1 {x2:.2f},{y2:.2f} Z"

def generate_svg_3_pie_chart():
    # 1990: Space 52%, Water 24%, Appliances 13%, Cooking 7%, Lighting 4%
    # 2020: Space 46%, Water 17%, Appliances 26%, Cooking 6%, Lighting 5%
    c1 = (220, 200, 105)
    c2 = (540, 200, 105)
    slices_1990 = [
        (0.00, 0.52, "#e11d48", "52%"), # Space heating
        (0.52, 0.76, "#2563eb", "24%"), # Water heating
        (0.76, 0.89, "#10b981", "13%"), # Appliances
        (0.89, 0.96, "#f59e0b", "7%"),  # Cooking
        (0.96, 1.00, "#a855f7", "4%")   # Lighting
    ]
    slices_2020 = [
        (0.00, 0.46, "#e11d48", "46%"),
        (0.46, 0.63, "#2563eb", "17%"),
        (0.63, 0.89, "#10b981", "26%"),
        (0.89, 0.95, "#f59e0b", "6%"),
        (0.95, 1.00, "#a855f7", "5%")
    ]

    p1990_paths = []
    for s, e, col, txt in slices_1990:
        d = make_pie_path(c1[0], c1[1], c1[2], s, e)
        mid_ang = (s + e) * math.pi - math.pi / 2
        lx = c1[0] + (c1[2] * 0.65) * math.cos(mid_ang)
        ly = c1[1] + (c1[2] * 0.65) * math.sin(mid_ang)
        p1990_paths.append(f'<path d="{d}" fill="{col}" stroke="#0f172a" stroke-width="2" />')
        p1990_paths.append(f'<text x="{lx:.1f}" y="{ly:.1f}" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle" dominant-baseline="central">{txt}</text>')

    p2020_paths = []
    for s, e, col, txt in slices_2020:
        d = make_pie_path(c2[0], c2[1], c2[2], s, e)
        mid_ang = (s + e) * math.pi - math.pi / 2
        lx = c2[0] + (c2[2] * 0.65) * math.cos(mid_ang)
        ly = c2[1] + (c2[2] * 0.65) * math.sin(mid_ang)
        p2020_paths.append(f'<path d="{d}" fill="{col}" stroke="#0f172a" stroke-width="2" />')
        p2020_paths.append(f'<text x="{lx:.1f}" y="{ly:.1f}" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle" dominant-baseline="central">{txt}</text>')

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 420" width="100%" height="100%" style="background:#0f172a; font-family:system-ui,-apple-system,sans-serif;">
  <text x="380" y="32" text-anchor="middle" fill="#f8fafc" font-size="16" font-weight="700">Household Energy Consumption Breakdown in the UK</text>
  <text x="380" y="52" text-anchor="middle" fill="#94a3b8" font-size="12">Comparison of Proportional End-Use Demands (1990 vs 2020)</text>

  <!-- 1990 Chart -->
  <text x="{c1[0]}" y="75" text-anchor="middle" fill="#38bdf8" font-size="14" font-weight="700">Year 1990</text>
  {"".join(p1990_paths)}

  <!-- 2020 Chart -->
  <text x="{c2[0]}" y="75" text-anchor="middle" fill="#38bdf8" font-size="14" font-weight="700">Year 2020</text>
  {"".join(p2020_paths)}

  <!-- Legend -->
  <g transform="translate(60, 360)">
    <rect x="0" y="0" width="14" height="14" rx="2" fill="#e11d48" />
    <text x="20" y="12" fill="#cbd5e1" font-size="12">Space Heating</text>

    <rect x="130" y="0" width="14" height="14" rx="2" fill="#2563eb" />
    <text x="150" y="12" fill="#cbd5e1" font-size="12">Water Heating</text>

    <rect x="260" y="0" width="14" height="14" rx="2" fill="#10b981" />
    <text x="280" y="12" fill="#cbd5e1" font-size="12">Electronic Appliances</text>

    <rect x="430" y="0" width="14" height="14" rx="2" fill="#f59e0b" />
    <text x="450" y="12" fill="#cbd5e1" font-size="12">Cooking</text>

    <rect x="530" y="0" width="14" height="14" rx="2" fill="#a855f7" />
    <text x="550" y="12" fill="#cbd5e1" font-size="12">Lighting</text>
  </g>
</svg>"""
    with open(os.path.join(OUT_DIR, "task1_pie_chart_energy.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

def generate_svg_4_table():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 420" width="100%" height="100%" style="background:#0f172a; font-family:system-ui,-apple-system,sans-serif;">
  <text x="380" y="32" text-anchor="middle" fill="#f8fafc" font-size="16" font-weight="700">International Tertiary Student Enrolment Across Five Academic Disciplines</text>
  <text x="380" y="52" text-anchor="middle" fill="#94a3b8" font-size="12">Admissions Volume, 8-Year Growth, and Student Retention Metrics (Australian University)</text>

  <!-- Table Container -->
  <g transform="translate(30, 75)">
    <!-- Header Row -->
    <rect x="0" y="0" width="700" height="42" rx="6" fill="#1e293b" />
    <text x="20" y="26" fill="#f1f5f9" font-size="12" font-weight="700">Academic Department</text>
    <text x="215" y="26" fill="#f1f5f9" font-size="12" font-weight="700" text-anchor="middle">2015 Enrolment</text>
    <text x="345" y="26" fill="#f1f5f9" font-size="12" font-weight="700" text-anchor="middle">2023 Enrolment</text>
    <text x="465" y="26" fill="#f1f5f9" font-size="12" font-weight="700" text-anchor="middle">Growth Rate (%)</text>
    <text x="575" y="26" fill="#f1f5f9" font-size="12" font-weight="700" text-anchor="middle">Retention</text>
    <text x="655" y="26" fill="#f1f5f9" font-size="12" font-weight="700" text-anchor="middle">Completion</text>

    <!-- Row 1: Computer Science -->
    <rect x="0" y="46" width="700" height="46" rx="4" fill="#0f172a" stroke="#334155" stroke-width="0.8" />
    <text x="20" y="74" fill="#38bdf8" font-size="13" font-weight="600">Computer Science</text>
    <text x="215" y="74" fill="#cbd5e1" font-size="13" text-anchor="middle">1,240</text>
    <text x="345" y="74" fill="#cbd5e1" font-size="13" font-weight="600" text-anchor="middle">3,850</text>
    <text x="465" y="74" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">+210.5%</text>
    <text x="575" y="74" fill="#e2e8f0" font-size="13" text-anchor="middle">93%</text>
    <text x="655" y="74" fill="#e2e8f0" font-size="13" text-anchor="middle">91%</text>

    <!-- Row 2: Business & Finance -->
    <rect x="0" y="96" width="700" height="46" rx="4" fill="#1e293b" fill-opacity="0.5" stroke="#334155" stroke-width="0.8" />
    <text x="20" y="124" fill="#f8fafc" font-size="13" font-weight="600">Business &amp; Finance</text>
    <text x="215" y="124" fill="#cbd5e1" font-size="13" text-anchor="middle">4,200</text>
    <text x="345" y="124" fill="#cbd5e1" font-size="13" font-weight="600" text-anchor="middle">5,600</text>
    <text x="465" y="124" fill="#34d399" font-size="13" font-weight="600" text-anchor="middle">+33.3%</text>
    <text x="575" y="124" fill="#e2e8f0" font-size="13" text-anchor="middle">88%</text>
    <text x="655" y="124" fill="#e2e8f0" font-size="13" text-anchor="middle">86%</text>

    <!-- Row 3: Engineering -->
    <rect x="0" y="146" width="700" height="46" rx="4" fill="#0f172a" stroke="#334155" stroke-width="0.8" />
    <text x="20" y="174" fill="#f8fafc" font-size="13" font-weight="600">Engineering &amp; Technology</text>
    <text x="215" y="174" fill="#cbd5e1" font-size="13" text-anchor="middle">2,100</text>
    <text x="345" y="174" fill="#cbd5e1" font-size="13" font-weight="600" text-anchor="middle">3,150</text>
    <text x="465" y="174" fill="#34d399" font-size="13" font-weight="600" text-anchor="middle">+50.0%</text>
    <text x="575" y="174" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">95%</text>
    <text x="655" y="174" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">94%</text>

    <!-- Row 4: Humanities & Social Sciences -->
    <rect x="0" y="196" width="700" height="46" rx="4" fill="#1e293b" fill-opacity="0.5" stroke="#334155" stroke-width="0.8" />
    <text x="20" y="224" fill="#f8fafc" font-size="13" font-weight="600">Humanities &amp; Social Sciences</text>
    <text x="215" y="224" fill="#cbd5e1" font-size="13" text-anchor="middle">1,850</text>
    <text x="345" y="224" fill="#cbd5e1" font-size="13" font-weight="600" text-anchor="middle">1,200</text>
    <text x="465" y="224" fill="#f43f5e" font-size="13" font-weight="700" text-anchor="middle">-35.1%</text>
    <text x="575" y="224" fill="#fca5a5" font-size="13" text-anchor="middle">74%</text>
    <text x="655" y="224" fill="#fca5a5" font-size="13" text-anchor="middle">71%</text>

    <!-- Row 5: Medicine & Health Sciences -->
    <rect x="0" y="246" width="700" height="46" rx="4" fill="#0f172a" stroke="#334155" stroke-width="0.8" />
    <text x="20" y="274" fill="#f8fafc" font-size="13" font-weight="600">Medicine &amp; Health Sciences</text>
    <text x="215" y="274" fill="#cbd5e1" font-size="13" text-anchor="middle">950</text>
    <text x="345" y="274" fill="#cbd5e1" font-size="13" font-weight="600" text-anchor="middle">1,120</text>
    <text x="465" y="274" fill="#34d399" font-size="13" font-weight="600" text-anchor="middle">+17.9%</text>
    <text x="575" y="274" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">96%</text>
    <text x="655" y="274" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">93%</text>
  </g>
</svg>"""
    with open(os.path.join(OUT_DIR, "task1_table_university.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

def generate_svg_5_process_diagram():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 420" width="100%" height="100%" style="background:#0f172a; font-family:system-ui,-apple-system,sans-serif;">
  <text x="380" y="30" text-anchor="middle" fill="#f8fafc" font-size="16" font-weight="700">Industrial Lithium-Ion Battery Recycling Procedure</text>
  <text x="380" y="48" text-anchor="middle" fill="#94a3b8" font-size="12">Hydrometallurgical Closed-Loop Material Recovery Flowchart</text>

  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#38bdf8" />
    </marker>
  </defs>

  <!-- Stage 1 Box -->
  <g transform="translate(30, 80)">
    <rect x="0" y="0" width="200" height="110" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
    <rect x="0" y="0" width="200" height="26" rx="8" fill="#0284c7" />
    <text x="100" y="18" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">STAGE 1: DISMANTLING</text>
    <text x="15" y="48" fill="#e2e8f0" font-size="11" font-weight="600">• EV Battery Modules</text>
    <text x="15" y="66" fill="#94a3b8" font-size="11">• Automated Discharge</text>
    <text x="15" y="84" fill="#94a3b8" font-size="11">• Cryogenic Shredder</text>
    <text x="15" y="100" fill="#f59e0b" font-size="10" font-weight="600">(Inert Argon Atmosphere)</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <line x1="230" y1="135" x2="275" y2="135" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Stage 2 Box -->
  <g transform="translate(280, 80)">
    <rect x="0" y="0" width="200" height="110" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
    <rect x="0" y="0" width="200" height="26" rx="8" fill="#0284c7" />
    <text x="100" y="18" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">STAGE 2: SEPARATION</text>
    <text x="15" y="48" fill="#e2e8f0" font-size="11" font-weight="600">• Density &amp; Air Sieving</text>
    <text x="15" y="66" fill="#94a3b8" font-size="11">• Copper / Aluminum Foils</text>
    <text x="15" y="84" fill="#94a3b8" font-size="11">• Plastic Casings Removed</text>
    <text x="15" y="100" fill="#a855f7" font-size="11" font-weight="700">Yield: Pure "Black Mass"</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <line x1="480" y1="135" x2="525" y2="135" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Stage 3 Box -->
  <g transform="translate(530, 80)">
    <rect x="0" y="0" width="200" height="110" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
    <rect x="0" y="0" width="200" height="26" rx="8" fill="#0284c7" />
    <text x="100" y="18" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">STAGE 3: ACID LEACHING</text>
    <text x="15" y="48" fill="#e2e8f0" font-size="11" font-weight="600">• Hydrometallurgical Tank</text>
    <text x="15" y="66" fill="#94a3b8" font-size="11">• Sulfuric Acid (H2SO4)</text>
    <text x="15" y="84" fill="#94a3b8" font-size="11">• Hydrogen Peroxide (H2O2)</text>
    <text x="15" y="100" fill="#f59e0b" font-size="10">Heated Dissolution 80°C</text>
  </g>

  <!-- Downward arrow from 3 to 4 -->
  <path d="M 630 190 L 630 235 L 535 235" fill="none" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Stage 4 Box -->
  <g transform="translate(280, 220)">
    <rect x="0" y="0" width="240" height="110" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5" />
    <rect x="0" y="0" width="240" height="26" rx="8" fill="#059669" />
    <text x="120" y="18" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">STAGE 4: PRECIPITATION &amp; CALCINATION</text>
    <text x="15" y="48" fill="#e2e8f0" font-size="11" font-weight="600">• Multi-stage pH Neutralization</text>
    <text x="15" y="68" fill="#94a3b8" font-size="11">• Selective Reagent Dosing</text>
    <text x="15" y="88" fill="#94a3b8" font-size="11">• Thermal Calcination Furnaces</text>
    <text x="15" y="102" fill="#34d399" font-size="10" font-weight="600">Precipitates Salt Crystals</text>
  </g>

  <!-- Arrow 4 -> 5 -->
  <line x1="280" y1="275" x2="235" y2="275" stroke="#10b981" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Final Product Box -->
  <g transform="translate(20, 220)">
    <rect x="0" y="0" width="210" height="110" rx="8" fill="#1e293b" stroke="#e11d48" stroke-width="2" />
    <rect x="0" y="0" width="210" height="26" rx="8" fill="#be123c" />
    <text x="105" y="18" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">RECOVERED PRODUCTS (98.5%)</text>
    <text x="15" y="48" fill="#fb7185" font-size="11" font-weight="700">• Lithium Carbonate (Li2CO3)</text>
    <text x="15" y="68" fill="#38bdf8" font-size="11" font-weight="700">• Nickel Hydroxide (Ni(OH)2)</text>
    <text x="15" y="88" fill="#f59e0b" font-size="11" font-weight="700">• Cobalt Sulfate (CoSO4)</text>
    <text x="15" y="103" fill="#34d399" font-size="10">Direct Battery Re-entry</text>
  </g>

  <!-- Cycle back arrow indicator -->
  <g transform="translate(180, 360)">
    <text x="200" y="20" fill="#94a3b8" font-size="11" text-anchor="middle">Closed-loop cycle: 95% of active cathode minerals diverted from landfill back to cell manufacturing.</text>
  </g>
</svg>"""
    with open(os.path.join(OUT_DIR, "task1_proc_battery_recycling.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

def generate_svg_6_map_plan():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 420" width="100%" height="100%" style="background:#0f172a; font-family:system-ui,-apple-system,sans-serif;">
  <text x="380" y="28" text-anchor="middle" fill="#f8fafc" font-size="16" font-weight="700">Port Haven Waterfront Redevelopment: 2000 vs Present</text>
  <text x="380" y="46" text-anchor="middle" fill="#94a3b8" font-size="12">Structural Transformation from Heavy Industrial Port to Commercial &amp; Residential Precinct</text>

  <!-- Compass Rose -->
  <g transform="translate(710, 45)">
    <circle cx="0" cy="0" r="18" fill="#1e293b" stroke="#475569" stroke-width="1" />
    <line x1="0" y1="12" x2="0" y2="-12" stroke="#38bdf8" stroke-width="1.5" />
    <line x1="-12" y1="0" x2="12" y2="0" stroke="#475569" stroke-width="1.5" />
    <polygon points="0,-12 3,-4 -3,-4" fill="#38bdf8" />
    <text x="0" y="-14" fill="#38bdf8" font-size="10" font-weight="700" text-anchor="middle">N</text>
  </g>

  <!-- LEFT MAP: YEAR 2000 -->
  <g transform="translate(25, 70)">
    <rect x="0" y="0" width="345" height="315" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1" />
    <rect x="0" y="0" width="345" height="26" rx="8" fill="#334155" />
    <text x="172" y="18" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">YEAR 2000 (Industrial Cargo Port)</text>

    <!-- Northern Cargo Docks & Warehouses -->
    <rect x="25" y="40" width="295" height="65" rx="4" fill="#475569" stroke="#64748b" />
    <text x="172" y="65" fill="#f8fafc" font-size="12" font-weight="700" text-anchor="middle">HEAVY CARGO DOCKS</text>
    <text x="172" y="85" fill="#cbd5e1" font-size="10" text-anchor="middle">Disused Timber Warehouses &amp; Freight Cranes</text>

    <!-- Central Shipping Canal -->
    <rect x="25" y="120" width="295" height="60" rx="4" fill="#0369a1" stroke="#0284c7" />
    <text x="172" y="145" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">CONTAINER SHIPPING CANAL</text>
    <text x="172" y="163" fill="#bae6fd" font-size="10" text-anchor="middle">Deep-water Bulk Cargo Berth</text>

    <!-- South Railyard & East Farmland -->
    <rect x="25" y="195" width="170" height="95" rx="4" fill="#334155" stroke="#475569" />
    <text x="110" y="235" fill="#f8fafc" font-size="11" font-weight="700" text-anchor="middle">INDUSTRIAL</text>
    <text x="110" y="250" fill="#f8fafc" font-size="11" font-weight="700" text-anchor="middle">RAILYARD</text>
    <text x="110" y="268" fill="#94a3b8" font-size="9" text-anchor="middle">Freight Sidings</text>

    <rect x="210" y="195" width="110" height="95" rx="4" fill="#365314" stroke="#4d7c0f" />
    <text x="265" y="240" fill="#f8fafc" font-size="11" font-weight="700" text-anchor="middle">AGRICULTURAL</text>
    <text x="265" y="255" fill="#f8fafc" font-size="11" font-weight="700" text-anchor="middle">FARMLAND</text>
    <text x="265" y="270" fill="#bef264" font-size="9" text-anchor="middle">Pasture Ground</text>
  </g>

  <!-- RIGHT MAP: PRESENT DAY -->
  <g transform="translate(390, 70)">
    <rect x="0" y="0" width="345" height="315" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
    <rect x="0" y="0" width="345" height="26" rx="8" fill="#0284c7" />
    <text x="172" y="18" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">PRESENT DAY (Waterfront Precinct)</text>

    <!-- Northern Residential & Museum -->
    <rect x="25" y="40" width="190" height="65" rx="4" fill="#0f766e" stroke="#14b8a6" />
    <text x="120" y="65" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">LUXURY APARTMENTS</text>
    <text x="120" y="85" fill="#99f6e4" font-size="10" text-anchor="middle">Multi-storey Living (400 Units)</text>

    <rect x="225" y="40" width="95" height="65" rx="4" fill="#7e22ce" stroke="#a855f7" />
    <text x="272" y="68" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">PUBLIC</text>
    <text x="272" y="82" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">ART MUSEUM</text>

    <!-- Central Yacht Marina & Promenade -->
    <rect x="25" y="120" width="295" height="60" rx="4" fill="#0284c7" stroke="#38bdf8" />
    <text x="172" y="145" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">RECREATIONAL YACHT MARINA</text>
    <text x="172" y="163" fill="#bae6fd" font-size="10" text-anchor="middle">Boardwalk Promenade &amp; Waterfront Cafes</text>

    <!-- South Transit & East Wetland -->
    <rect x="25" y="195" width="170" height="95" rx="4" fill="#b45309" stroke="#f59e0b" />
    <text x="110" y="235" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">LIGHT RAIL TERMINUS</text>
    <text x="110" y="255" fill="#fef3c7" font-size="10" text-anchor="middle">Direct Electrified Tram</text>
    <text x="110" y="270" fill="#fef3c7" font-size="9" text-anchor="middle">Connection to CBD (15 min)</text>

    <rect x="210" y="195" width="110" height="95" rx="4" fill="#15803d" stroke="#22c55e" />
    <text x="265" y="235" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">NATURE RESERVE</text>
    <text x="265" y="250" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">WETLAND</text>
    <text x="265" y="270" fill="#bbf7d0" font-size="9" text-anchor="middle">Public Walking Trails</text>
  </g>
</svg>"""
    with open(os.path.join(OUT_DIR, "task1_map_port_haven.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

def generate_svg_7_pumped_storage():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 420" width="100%" height="100%" style="background:#0f172a; font-family:system-ui,-apple-system,sans-serif;">
  <text x="380" y="30" text-anchor="middle" fill="#f8fafc" font-size="16" font-weight="700">Closed-Loop Hydroelectric Pumped Storage Power Station</text>
  <text x="380" y="48" text-anchor="middle" fill="#94a3b8" font-size="12">Daytime Power Generation vs Nighttime Water Replenishment Cycle</text>

  <!-- Mountain Slope -->
  <path d="M 40 180 L 260 120 L 520 280 L 720 280 L 720 380 L 40 380 Z" fill="#1e293b" stroke="#334155" stroke-width="1.5" />

  <!-- Upper Reservoir (Mountain) -->
  <rect x="60" y="90" width="180" height="60" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5" />
  <text x="150" y="118" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">UPPER RESERVOIR</text>
  <text x="150" y="136" fill="#bae6fd" font-size="10" text-anchor="middle">Elevated Mountain Basin</text>

  <!-- Lower Reservoir (Catchment) -->
  <rect x="520" y="260" width="180" height="60" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5" />
  <text x="610" y="288" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">LOWER RESERVOIR</text>
  <text x="610" y="306" fill="#bae6fd" font-size="10" text-anchor="middle">Catchment Basin</text>

  <!-- Underground Penstock (Pipe connecting reservoirs) -->
  <path d="M 240 135 L 370 210 L 420 300 L 520 290" fill="none" stroke="#64748b" stroke-width="16" stroke-linecap="round" stroke-linejoin="round" />
  <path d="M 240 135 L 370 210 L 420 300 L 520 290" fill="none" stroke="#38bdf8" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" />

  <!-- Underground Powerhouse -->
  <rect x="360" y="265" width="110" height="70" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="2" />
  <text x="415" y="288" fill="#f59e0b" font-size="11" font-weight="700" text-anchor="middle">POWERHOUSE</text>
  <text x="415" y="306" fill="#e2e8f0" font-size="10" text-anchor="middle">Reversible Turbine</text>
  <text x="415" y="322" fill="#e2e8f0" font-size="10" text-anchor="middle">&amp; Generator / Pump</text>

  <!-- Cycle Modes Indicators -->
  <!-- Daytime Mode -->
  <g transform="translate(60, 210)">
    <rect x="0" y="0" width="210" height="90" rx="6" fill="#0f172a" stroke="#e11d48" stroke-width="1.5" />
    <text x="15" y="22" fill="#fb7185" font-size="11" font-weight="700">☀️ DAYTIME PEAK MODE</text>
    <text x="15" y="42" fill="#cbd5e1" font-size="10">• High electricity grid demand</text>
    <text x="15" y="60" fill="#cbd5e1" font-size="10">• Water cascades DOWN penstock</text>
    <text x="15" y="78" fill="#34d399" font-size="10" font-weight="700">• Supplies 500 MW to Power Grid</text>
  </g>

  <!-- Nighttime Mode -->
  <g transform="translate(490, 90)">
    <rect x="0" y="0" width="220" height="90" rx="6" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.5" />
    <text x="15" y="22" fill="#c084fc" font-size="11" font-weight="700">🌙 NIGHTTIME OFF-PEAK MODE</text>
    <text x="15" y="42" fill="#cbd5e1" font-size="10">• Cheap surplus grid electricity</text>
    <text x="15" y="60" fill="#cbd5e1" font-size="10">• Turbines reverse as pumps</text>
    <text x="15" y="78" fill="#38bdf8" font-size="10" font-weight="700">• Forces water UP to refill reservoir</text>
  </g>

  <!-- Closed-loop footer banner -->
  <rect x="180" y="365" width="400" height="30" rx="4" fill="#1e293b" stroke="#475569" stroke-width="1" />
  <text x="380" y="385" fill="#38bdf8" font-size="11" font-weight="600" text-anchor="middle">Closed-Loop System: 100% Water Recycled With Near-Zero Consumptive Depletion</text>
</svg>"""
    with open(os.path.join(OUT_DIR, "task1_proc_pumped_storage.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

def generate_svg_8_multi_chart():
    # Left: Farmland Area (1980: 42M, 1990: 43.2M, 2000: 44.5M, 2010: 46.1M, 2020: 48.0M)
    # Right: Deforestation drivers: Cattle 41%, Commercial crops 32%, Subsistence 18%, Logging/Infra 9%
    c2 = (560, 205, 95)
    slices = [
        (0.00, 0.41, "#e11d48", "41%"), # Cattle
        (0.41, 0.73, "#f59e0b", "32%"), # Commercial crops
        (0.73, 0.91, "#10b981", "18%"), # Subsistence
        (0.91, 1.00, "#6366f1", "9%")   # Logging
    ]

    p_slices = []
    for s, e, col, txt in slices:
        d = make_pie_path(c2[0], c2[1], c2[2], s, e)
        mid_ang = (s + e) * math.pi - math.pi / 2
        lx = c2[0] + (c2[2] * 0.65) * math.cos(mid_ang)
        ly = c2[1] + (c2[2] * 0.65) * math.sin(mid_ang)
        p_slices.append(f'<path d="{d}" fill="{col}" stroke="#0f172a" stroke-width="2" />')
        p_slices.append(f'<text x="{lx:.1f}" y="{ly:.1f}" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle" dominant-baseline="central">{txt}</text>')

    # Left Bar chart:
    # Y-axis 30 to 50M sq km. Base at y=320 (30M), top at y=90 (50M). Range=230px for 20M -> 11.5px per M.
    # 1980 (42): h = 12 * 11.5 = 138, y = 320 - 138 = 182
    # 1990 (43.2): h = 13.2 * 11.5 = 152, y = 168
    # 2000 (44.5): h = 14.5 * 11.5 = 167, y = 153
    # 2010 (46.1): h = 16.1 * 11.5 = 185, y = 135
    # 2020 (48.0): h = 18.0 * 11.5 = 207, y = 113

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 420" width="100%" height="100%" style="background:#0f172a; font-family:system-ui,-apple-system,sans-serif;">
  <text x="380" y="28" text-anchor="middle" fill="#f8fafc" font-size="16" font-weight="700">Worldwide Agricultural Land Use and Deforestation Drivers</text>
  <text x="380" y="46" text-anchor="middle" fill="#94a3b8" font-size="12">Farmland Area Expansion (1980–2020) &amp; Primary Catalysts of Tropical Forest Clearance</text>

  <!-- Left Section: Bar Chart -->
  <g transform="translate(10, 20)">
    <text x="180" y="48" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">Total Farmland Area (Million km²)</text>

    <!-- Gridlines & Y-axis labels -->
    <line x1="50" y1="90" x2="330" y2="90" stroke="#334155" stroke-dasharray="3,3" />
    <text x="42" y="94" fill="#94a3b8" font-size="10" text-anchor="end">50M</text>

    <line x1="50" y1="147" x2="330" y2="147" stroke="#334155" stroke-dasharray="3,3" />
    <text x="42" y="151" fill="#94a3b8" font-size="10" text-anchor="end">45M</text>

    <line x1="50" y1="205" x2="330" y2="205" stroke="#334155" stroke-dasharray="3,3" />
    <text x="42" y="209" fill="#94a3b8" font-size="10" text-anchor="end">40M</text>

    <line x1="50" y1="262" x2="330" y2="262" stroke="#334155" stroke-dasharray="3,3" />
    <text x="42" y="266" fill="#94a3b8" font-size="10" text-anchor="end">35M</text>

    <line x1="50" y1="320" x2="330" y2="320" stroke="#64748b" stroke-width="1.5" />
    <text x="42" y="324" fill="#94a3b8" font-size="10" text-anchor="end">30M</text>

    <!-- Bars -->
    <rect x="65" y="182" width="36" height="138" rx="3" fill="#10b981" />
    <text x="83" y="174" fill="#6ee7b7" font-size="10" font-weight="700" text-anchor="middle">42.0</text>
    <text x="83" y="338" fill="#e2e8f0" font-size="11" text-anchor="middle">1980</text>

    <rect x="120" y="168" width="36" height="152" rx="3" fill="#10b981" />
    <text x="138" y="160" fill="#6ee7b7" font-size="10" font-weight="700" text-anchor="middle">43.2</text>
    <text x="138" y="338" fill="#e2e8f0" font-size="11" text-anchor="middle">1990</text>

    <rect x="175" y="153" width="36" height="167" rx="3" fill="#10b981" />
    <text x="193" y="145" fill="#6ee7b7" font-size="10" font-weight="700" text-anchor="middle">44.5</text>
    <text x="193" y="338" fill="#e2e8f0" font-size="11" text-anchor="middle">2000</text>

    <rect x="230" y="135" width="36" height="185" rx="3" fill="#10b981" />
    <text x="248" y="127" fill="#6ee7b7" font-size="10" font-weight="700" text-anchor="middle">46.1</text>
    <text x="248" y="338" fill="#e2e8f0" font-size="11" text-anchor="middle">2010</text>

    <rect x="285" y="113" width="36" height="207" rx="3" fill="#059669" stroke="#34d399" stroke-width="1.5" />
    <text x="303" y="105" fill="#a7f3d0" font-size="10" font-weight="700" text-anchor="middle">48.0</text>
    <text x="303" y="338" fill="#e2e8f0" font-size="11" font-weight="700" text-anchor="middle">2020</text>
  </g>

  <!-- Right Section: Pie Chart -->
  <g transform="translate(390, 20)">
    <text x="170" y="48" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">Drivers of Tropical Deforestation</text>
    {"".join(p_slices)}

    <!-- Pie Legend -->
    <g transform="translate(20, 315)">
      <rect x="0" y="0" width="12" height="12" rx="2" fill="#e11d48" />
      <text x="18" y="10" fill="#cbd5e1" font-size="11">Cattle Ranching (41%)</text>

      <rect x="170" y="0" width="12" height="12" rx="2" fill="#f59e0b" />
      <text x="188" y="10" fill="#cbd5e1" font-size="11">Commercial Crops (32%)</text>

      <rect x="0" y="24" width="12" height="12" rx="2" fill="#10b981" />
      <text x="18" y="34" fill="#cbd5e1" font-size="11">Subsistence Farming (18%)</text>

      <rect x="170" y="24" width="12" height="12" rx="2" fill="#6366f1" />
      <text x="188" y="34" fill="#cbd5e1" font-size="11">Logging &amp; Infra (9%)</text>
    </g>
  </g>
</svg>"""
    with open(os.path.join(OUT_DIR, "task1_multi_farmland_deforestation.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == "__main__":
    generate_svg_1_bar_chart()
    generate_svg_2_line_graph()
    generate_svg_3_pie_chart()
    generate_svg_4_table()
    generate_svg_5_process_diagram()
    generate_svg_6_map_plan()
    generate_svg_7_pumped_storage()
    generate_svg_8_multi_chart()
    print("Successfully generated all 8 Academic Task 1 vector SVG graphics in:", OUT_DIR)
