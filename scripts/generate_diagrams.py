# -*- coding: utf-8 -*-
"""Generate high-resolution diagram figures for Chapter 3.
Renders SVG/HTML via headless Edge to PNG in output/figures/ and input/figures/.
"""
import os
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
HTML_DIR = os.path.join(ROOT, "input", "figures", "html")
INPUT_FIG_DIR = os.path.join(ROOT, "input", "figures")
OUTPUT_FIG_DIR = os.path.join(ROOT, "output", "figures")

os.makedirs(HTML_DIR, exist_ok=True)
os.makedirs(INPUT_FIG_DIR, exist_ok=True)
os.makedirs(OUTPUT_FIG_DIR, exist_ok=True)

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(EDGE_PATH):
    EDGE_PATH = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(EDGE_PATH):
    EDGE_PATH = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

COMMON_CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    background-color: #ffffff;
    font-family: 'TH Sarabun New', 'TH SarabunPSK', 'Sarabun', 'Segoe UI', Tahoma, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
}
.diagram-container {
    background: #ffffff;
    padding: 10px;
    display: inline-block;
}
svg {
    font-family: 'TH Sarabun New', 'TH SarabunPSK', 'Sarabun', 'Segoe UI', Tahoma, sans-serif;
    overflow: visible;
}
.title { font-size: 20px; font-weight: bold; fill: #1e293b; text-anchor: middle; }
.subtitle { font-size: 15px; fill: #64748b; text-anchor: middle; }
.box-title { font-size: 16px; font-weight: bold; fill: #0f172a; text-anchor: middle; }
.box-desc { font-size: 13.5px; fill: #334155; text-anchor: middle; }
.badge { font-size: 12px; font-weight: bold; fill: #ffffff; }
.label { font-size: 13px; font-weight: bold; fill: #475569; }
.decision-text { font-size: 14.5px; font-weight: bold; fill: #1e293b; text-anchor: middle; }
.tag-pk { fill: #dc2626; font-weight: bold; font-size: 12px; }
.tag-fk { fill: #2563eb; font-weight: bold; font-size: 12px; }
.col-name { font-size: 13.5px; fill: #1e293b; font-family: monospace; }
.col-type { font-size: 12.5px; fill: #64748b; }
"""

# -------------------------------------------------------------
# Figure 3.1: ผังงานขั้นตอนการวางแผนและดำเนินงานของโครงการ
# -------------------------------------------------------------
FIG_3_1_HTML = f"""<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<style>
{COMMON_CSS}
</style>
</head>
<body>
<div class="diagram-container">
<svg width="780" height="920" viewBox="0 0 780 920" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#3b82f6" />
    </marker>
    <marker id="arrow-loop" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#ef4444" />
    </marker>
  </defs>

  <!-- Title -->
  <text x="390" y="32" class="title">รูปที่ 3.1 ขั้นตอนการวางแผนและดำเนินงานของโครงการ</text>
  <text x="390" y="54" class="subtitle">ระเบียบวิธีพัฒนาซอฟต์แวร์แบบวนซ้ำและเพิ่มพูน (Iterative and Incremental Development)</text>

  <!-- Start -->
  <rect x="290" y="75" width="200" height="42" rx="21" fill="#1e3a8a" filter="url(#shadow)" />
  <text x="390" y="102" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle">เริ่มต้นโครงการ</text>
  <line x1="390" y1="117" x2="390" y2="145" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 1 -->
  <rect x="150" y="145" width="480" height="74" rx="8" fill="#f8fafc" stroke="#3b82f6" stroke-width="2" filter="url(#shadow)" />
  <rect x="160" y="153" width="24" height="24" rx="12" fill="#3b82f6" />
  <text x="172" y="170" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">1</text>
  <text x="390" y="171" class="box-title">การศึกษาและรวบรวมความต้องการ (Requirement Gathering)</text>
  <text x="390" y="196" class="box-desc">ศึกษาระบบงานเดิมของคณะแพทยศาสตร์ วิเคราะห์ปัญหา และกำหนดความต้องการ 2 ส่วนหลัก</text>
  <line x1="390" y1="219" x2="390" y2="247" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 2 -->
  <rect x="150" y="247" width="480" height="74" rx="8" fill="#f8fafc" stroke="#3b82f6" stroke-width="2" filter="url(#shadow)" />
  <rect x="160" y="255" width="24" height="24" rx="12" fill="#3b82f6" />
  <text x="172" y="272" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">2</text>
  <text x="390" y="273" class="box-title">การออกแบบระบบและฐานข้อมูล (System & Database Design)</text>
  <text x="390" y="298" class="box-desc">ออกแบบสถาปัตยกรรมระบบ ฐานข้อมูล MySQL 7 ตารางหลัก แผนภาพ ERD และ Use Case</text>
  <line x1="390" y1="321" x2="390" y2="349" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 3 -->
  <rect x="150" y="349" width="480" height="74" rx="8" fill="#f8fafc" stroke="#3b82f6" stroke-width="2" filter="url(#shadow)" />
  <rect x="160" y="357" width="24" height="24" rx="12" fill="#3b82f6" />
  <text x="172" y="374" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">3</text>
  <text x="390" y="375" class="box-title">การออกแบบส่วนต่อประสานผู้ใช้ (UI/UX Design)</text>
  <text x="390" y="400" class="box-desc">ออกแบบโครงสร้าง Partials ตารางแสดงผล 25 คอลัมน์ ธีมสีสว่าง/มืด และระบบสองภาษา</text>
  <line x1="390" y1="423" x2="390" y2="451" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 4 -->
  <rect x="150" y="451" width="480" height="74" rx="8" fill="#f8fafc" stroke="#3b82f6" stroke-width="2" filter="url(#shadow)" />
  <rect x="160" y="459" width="24" height="24" rx="12" fill="#3b82f6" />
  <text x="172" y="476" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">4</text>
  <text x="390" y="477" class="box-title">การพัฒนาระบบ (System Implementation)</text>
  <text x="390" y="502" class="box-desc">พัฒนาส่วนติดต่อผู้ใช้ด้วย EJS, CSS, JS จัดการ Data Diff, โอนย้ายสินทรัพย์, QR Code และความปลอดภัย</text>
  <line x1="390" y1="525" x2="390" y2="553" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 5 -->
  <rect x="150" y="553" width="480" height="74" rx="8" fill="#f8fafc" stroke="#3b82f6" stroke-width="2" filter="url(#shadow)" />
  <rect x="160" y="561" width="24" height="24" rx="12" fill="#3b82f6" />
  <text x="172" y="578" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">5</text>
  <text x="390" y="579" class="box-title">การทดสอบระบบ (System Testing)</text>
  <text x="390" y="604" class="box-desc">ทดสอบความถูกต้องของฟังก์ชันการทำงาน ทดสอบการตอบสนองทุกขนาดหน้าจอ และการป้องกัน FOUC</text>
  <line x1="390" y1="627" x2="390" y2="655" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Decision -->
  <polygon points="390,655 520,705 390,755 260,705" fill="#fef3c7" stroke="#d97706" stroke-width="2" filter="url(#shadow)" />
  <text x="390" y="700" class="decision-text">ผลการทดสอบ</text>
  <text x="390" y="718" class="decision-text">ผ่านเกณฑ์หรือไม่?</text>

  <!-- Pass branch (Down) -->
  <text x="405" y="775" fill="#059669" font-size="14" font-weight="bold">ผ่าน (Yes)</text>
  <line x1="390" y1="755" x2="390" y2="785" stroke="#059669" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Fail branch (Loop Left) -->
  <text x="180" y="695" fill="#ef4444" font-size="14" font-weight="bold">ไม่ผ่าน (No): ปรับปรุงแก้ไข</text>
  <polyline points="260,705 90,705 90,488 145,488" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="6,4" marker-end="url(#arrow-loop)" />

  <!-- Step 6 -->
  <rect x="150" y="785" width="480" height="66" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="2" filter="url(#shadow)" />
  <rect x="160" y="793" width="24" height="24" rx="12" fill="#16a34a" />
  <text x="172" y="810" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">6</text>
  <text x="390" y="811" class="box-title">การปรับปรุงแก้ไขข้อบกพร่องและจัดทำเอกสาร (Refinement & Documentation)</text>
  <text x="390" y="834" class="box-desc">ปรับปรุงแก้ไขข้อบกพร่อง จัดทำคู่มือการใช้งาน และสรุปผลการดำเนินงานของโครงการ</text>
  <line x1="390" y1="851" x2="390" y2="875" stroke="#16a34a" stroke-width="2" marker-end="url(#arrow)" />

  <!-- End -->
  <rect x="290" y="875" width="200" height="40" rx="20" fill="#1e3a8a" filter="url(#shadow)" />
  <text x="390" y="901" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle">สิ้นสุดโครงการ</text>
</svg>
</div>
</body>
</html>
"""

# -------------------------------------------------------------
# Figure 3.2: ผังงานกระบวนการนำเข้าข้อมูลสินทรัพย์ด้วยไฟล์ Excel
# -------------------------------------------------------------
FIG_3_2_HTML = f"""<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<style>
{COMMON_CSS}
</style>
</head>
<body>
<div class="diagram-container">
<svg width="780" height="880" viewBox="0 0 780 880" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#2563eb" />
    </marker>
    <marker id="arrow-red" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#ef4444" />
    </marker>
  </defs>

  <!-- Title -->
  <text x="390" y="32" class="title">รูปที่ 3.2 ผังงานกระบวนการนำเข้าข้อมูลสินทรัพย์ด้วยไฟล์ Excel</text>
  <text x="390" y="54" class="subtitle">กระบวนการตรวจสอบโครงสร้างไฟล์ ตรวจสอบความถูกต้อง และบันทึกลงฐานข้อมูล</text>

  <!-- Start -->
  <rect x="300" y="75" width="180" height="38" rx="19" fill="#1e3a8a" filter="url(#shadow)" />
  <text x="390" y="100" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle">เริ่มต้น</text>
  <line x1="390" y1="113" x2="390" y2="135" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 1 -->
  <rect x="180" y="135" width="420" height="50" rx="8" fill="#f8fafc" stroke="#2563eb" stroke-width="1.8" filter="url(#shadow)" />
  <text x="390" y="157" class="box-title">ผู้ดูแลระบบเข้าสู่เมนู "นำเข้าสินทรัพย์"</text>
  <text x="390" y="174" class="box-desc">เข้าถึงหน้าจออัปโหลดไฟล์ตารางทำการผ่านแถบเมนูด้านข้าง</text>
  <line x1="390" y1="185" x2="390" y2="207" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 2 -->
  <polygon points="200,207 600,207 580,257 180,257" fill="#eff6ff" stroke="#2563eb" stroke-width="1.8" filter="url(#shadow)" />
  <text x="390" y="229" class="box-title">เลือกและอัปโหลดไฟล์ Excel (.xlsx)</text>
  <text x="390" y="246" class="box-desc">ไฟล์ตารางทำการข้อมูลครุภัณฑ์จากแผนกพัสดุ</text>
  <line x1="390" y1="257" x2="390" y2="279" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 3 -->
  <rect x="180" y="279" width="420" height="50" rx="8" fill="#f8fafc" stroke="#2563eb" stroke-width="1.8" filter="url(#shadow)" />
  <text x="390" y="301" class="box-title">ระบบอ่านข้อมูลและแปลงโครงสร้างไฟล์ (Parse Excel Data)</text>
  <text x="390" y="318" class="box-desc">สกัดข้อมูลหัวคอลัมน์และแถวข้อมูลในสเปรดชีต</text>
  <line x1="390" y1="329" x2="390" y2="351" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Decision 1 -->
  <polygon points="390,351 530,396 390,441 250,396" fill="#fef3c7" stroke="#d97706" stroke-width="1.8" filter="url(#shadow)" />
  <text x="390" y="392" class="decision-text">ชนิดไฟล์และหัวตาราง</text>
  <text x="390" y="410" class="decision-text">ถูกต้องครบถ้วนหรือไม่?</text>

  <!-- Decision 1 Fail (Right) -->
  <text x="540" y="390" fill="#ef4444" font-size="13.5" font-weight="bold">ไม่ถูกต้อง</text>
  <polyline points="530,396 660,396 660,232 605,232" fill="none" stroke="#ef4444" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arrow-red)" />
  <rect x="580" y="340" width="150" height="40" rx="6" fill="#fef2f2" stroke="#ef4444" stroke-width="1.5" />
  <text x="655" y="357" fill="#b91c1c" font-size="12.5" font-weight="bold" text-anchor="middle">แจ้งเตือนข้อผิดพลาด</text>
  <text x="655" y="372" fill="#b91c1c" font-size="11.5" text-anchor="middle">โครงสร้างหัวตารางไม่ตรง</text>

  <!-- Decision 1 Pass (Down) -->
  <text x="405" y="460" fill="#059669" font-size="13.5" font-weight="bold">ถูกต้อง</text>
  <line x1="390" y1="441" x2="390" y2="475" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 4 -->
  <rect x="180" y="475" width="420" height="50" rx="8" fill="#f8fafc" stroke="#2563eb" stroke-width="1.8" filter="url(#shadow)" />
  <text x="390" y="497" class="box-title">ระบบตรวจสอบความถูกต้องของข้อมูลแต่ละแถว (Validation)</text>
  <text x="390" y="514" class="box-desc">ตรวจสอบรหัสสินทรัพย์ วันที่ รูปแบบข้อความ และค่าว่างที่ไม่อนุญาต</text>
  <line x1="390" y1="525" x2="390" y2="547" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Decision 2 -->
  <polygon points="390,547 530,592 390,637 250,592" fill="#fef3c7" stroke="#d97706" stroke-width="1.8" filter="url(#shadow)" />
  <text x="390" y="588" class="decision-text">ข้อมูลในแถว</text>
  <text x="390" y="606" class="decision-text">ผ่านเกณฑ์ทั้งหมดหรือไม่?</text>

  <!-- Decision 2 Fail (Right) -->
  <text x="540" y="586" fill="#ef4444" font-size="13.5" font-weight="bold">พบข้อผิดพลาด</text>
  <polyline points="530,592 660,592 660,650" fill="none" stroke="#ef4444" stroke-width="1.8" />
  <rect x="580" y="650" width="160" height="45" rx="6" fill="#fef2f2" stroke="#ef4444" stroke-width="1.5" />
  <text x="660" y="669" fill="#b91c1c" font-size="12.5" font-weight="bold" text-anchor="middle">แสดงรายการแถวที่ผิดพลาด</text>
  <text x="660" y="684" fill="#b91c1c" font-size="11.5" text-anchor="middle">ยกเลิกการนำเข้าแถวนั้น</text>
  <polyline points="660,695 660,780 485,780" fill="none" stroke="#64748b" stroke-width="1.8" marker-end="url(#arrow)" />

  <!-- Decision 2 Pass (Down) -->
  <text x="405" y="656" fill="#059669" font-size="13.5" font-weight="bold">ถูกต้อง</text>
  <line x1="390" y1="637" x2="390" y2="667" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 5 -->
  <rect x="180" y="667" width="420" height="48" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8" filter="url(#shadow)" />
  <text x="390" y="688" class="box-title">บันทึกข้อมูลสินทรัพย์ลงฐานข้อมูล MySQL (ตาราง assets)</text>
  <text x="390" y="704" class="box-desc">แทรกข้อมูลสินทรัพย์ใหม่หรืออัปเดตข้อมูลที่มีอยู่เดิม</text>
  <line x1="390" y1="715" x2="390" y2="735" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 6 -->
  <rect x="180" y="735" width="420" height="46" rx="8" fill="#f8fafc" stroke="#2563eb" stroke-width="1.8" filter="url(#shadow)" />
  <text x="390" y="754" class="box-title">บันทึกประวัติลงตาราง activity_logs</text>
  <text x="390" y="770" class="box-desc">ระบุรหัสผู้ใช้งาน โมดูล Assets การกระทำ Import และรายละเอียด</text>
  <line x1="390" y1="781" x2="390" y2="801" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 7 -->
  <polygon points="200,801 600,801 580,839 180,839" fill="#eff6ff" stroke="#2563eb" stroke-width="1.8" filter="url(#shadow)" />
  <text x="390" y="821" class="box-title">แสดงผลสรุปยอดนำเข้าสำเร็จ และรีเฟรชตารางสินทรัพย์</text>
  <line x1="390" y1="839" x2="390" y2="855" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)" />

  <!-- End -->
  <rect x="300" y="855" width="180" height="34" rx="17" fill="#1e3a8a" filter="url(#shadow)" />
  <text x="390" y="877" fill="#ffffff" font-size="15" font-weight="bold" text-anchor="middle">สิ้นสุด</text>
</svg>
</div>
</body>
</html>
"""

# -------------------------------------------------------------
# Figure 3.3: ผังงานกระบวนการอัปเดตข้อมูลสินทรัพย์แบบเทียบผลต่าง
# -------------------------------------------------------------
FIG_3_3_HTML = f"""<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<style>
{COMMON_CSS}
</style>
</head>
<body>
<div class="diagram-container">
<svg width="780" height="950" viewBox="0 0 780 950" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0284c7" />
    </marker>
    <marker id="arrow-cancel" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#ef4444" />
    </marker>
  </defs>

  <!-- Title -->
  <text x="390" y="32" class="title">รูปที่ 3.3 ผังงานกระบวนการอัปเดตข้อมูลสินทรัพย์แบบเทียบผลต่าง</text>
  <text x="390" y="54" class="subtitle">ระบบวิเคราะห์ความแตกต่างของข้อมูล (Data Diff Preview) ก่อนบันทึกปรับปรุงจริง</text>

  <!-- Start -->
  <rect x="300" y="75" width="180" height="36" rx="18" fill="#1e3a8a" filter="url(#shadow)" />
  <text x="390" y="99" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle">เริ่มต้น</text>
  <line x1="390" y1="111" x2="390" y2="133" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 1 -->
  <polygon points="200,133 600,133 580,181 180,181" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.8" filter="url(#shadow)" />
  <text x="390" y="153" class="box-title">อัปโหลดไฟล์ Excel เพื่ออัปเดตข้อมูลสินทรัพย์</text>
  <text x="390" y="170" class="box-desc">ผู้ดูแลระบบเลือกไฟล์ข้อมูลชุดใหม่ที่ต้องการนำมาปรับปรุง</text>
  <line x1="390" y1="181" x2="390" y2="203" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 2 -->
  <rect x="180" y="203" width="420" height="50" rx="8" fill="#f8fafc" stroke="#0284c7" stroke-width="1.8" filter="url(#shadow)" />
  <text x="390" y="224" class="box-title">ระบบค้นหาข้อมูลเดิมในฐานข้อมูล (Lookup Existing Assets)</text>
  <text x="390" y="242" class="box-desc">จับคู่รายการข้อมูลโดยใช้ Asset ID และ Tag Number</text>
  <line x1="390" y1="253" x2="390" y2="275" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 3 -->
  <rect x="180" y="275" width="420" height="52" rx="8" fill="#f8fafc" stroke="#0284c7" stroke-width="1.8" filter="url(#shadow)" />
  <text x="390" y="296" class="box-title">ประมวลผลเปรียบเทียบข้อมูล (Data Diff Engine)</text>
  <text x="390" y="315" class="box-desc">ตรวจสอบค่าของฟิลด์ข้อมูลเดิมเปรียบเทียบกับค่าของฟิลด์ข้อมูลใหม่ทีละคอลัมน์</text>
  <line x1="390" y1="327" x2="390" y2="349" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 4: Classification Cards -->
  <rect x="120" y="349" width="540" height="96" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" filter="url(#shadow)" />
  <text x="390" y="371" class="box-title">จำแนกรายการข้อมูลออกเป็น 3 กลุ่ม</text>
  <!-- Card 1 -->
  <rect x="135" y="383" width="160" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.2" />
  <text x="215" y="403" fill="#92400e" font-size="13" font-weight="bold" text-anchor="middle">1. ข้อมูลที่มีการเปลี่ยนแปลง</text>
  <text x="215" y="420" fill="#78350f" font-size="11.5" text-anchor="middle">(Modified Records)</text>
  <!-- Card 2 -->
  <rect x="310" y="383" width="160" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.2" />
  <text x="390" y="403" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">2. ข้อมูลรายการใหม่</text>
  <text x="390" y="420" fill="#14532d" font-size="11.5" text-anchor="middle">(New Records)</text>
  <!-- Card 3 -->
  <rect x="485" y="383" width="160" height="50" rx="6" fill="#f1f5f9" stroke="#64748b" stroke-width="1.2" />
  <text x="565" y="403" fill="#334155" font-size="13" font-weight="bold" text-anchor="middle">3. ข้อมูลเดิมไม่เปลี่ยนแปลง</text>
  <text x="565" y="420" fill="#475569" font-size="11.5" text-anchor="middle">(Unchanged Records)</text>
  <line x1="390" y1="445" x2="390" y2="467" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 5 -->
  <polygon points="170,467 630,467 610,519 150,519" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.8" filter="url(#shadow)" />
  <text x="390" y="489" class="box-title">แสดงผลหน้าจอตรวจสอบผลต่าง (Data Diff Preview)</text>
  <text x="390" y="507" class="box-desc">แสดงตารางเปรียบเทียบค่าเดิมและค่าใหม่พร้อมไฮไลต์สีชัดเจน</text>
  <line x1="390" y1="519" x2="390" y2="541" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 6 -->
  <rect x="180" y="541" width="420" height="52" rx="8" fill="#f8fafc" stroke="#0284c7" stroke-width="1.8" filter="url(#shadow)" />
  <text x="390" y="563" class="box-title">ผู้ใช้เลือกคอลัมน์และแถวที่ต้องการปรับใช้ (Column Selection)</text>
  <text x="390" y="581" class="box-desc">สามารถเลือกเฉพาะบางคอลัมน์ที่ต้องการอัปเดต หรือเลือกทั้งหมดได้</text>
  <line x1="390" y1="593" x2="390" y2="615" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Decision -->
  <polygon points="390,615 530,660 390,705 250,660" fill="#fef3c7" stroke="#d97706" stroke-width="1.8" filter="url(#shadow)" />
  <text x="390" y="656" class="decision-text">ผู้ใช้กดยืนยัน</text>
  <text x="390" y="674" class="decision-text">การปรับปรุงข้อมูลหรือไม่?</text>

  <!-- Cancel branch (Right) -->
  <text x="540" y="654" fill="#ef4444" font-size="13.5" font-weight="bold">ยกเลิก (Cancel)</text>
  <polyline points="530,660 670,660 670,890 490,890" fill="none" stroke="#ef4444" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arrow-cancel)" />
  <rect x="590" y="700" width="140" height="38" rx="6" fill="#fef2f2" stroke="#ef4444" stroke-width="1.2" />
  <text x="660" y="724" fill="#b91c1c" font-size="12.5" font-weight="bold" text-anchor="middle">ยกเลิกรายการ</text>

  <!-- Confirm branch (Down) -->
  <text x="405" y="725" fill="#059669" font-size="13.5" font-weight="bold">ยืนยัน (Confirm)</text>
  <line x1="390" y1="705" x2="390" y2="735" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 7 -->
  <rect x="180" y="735" width="420" height="50" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8" filter="url(#shadow)" />
  <text x="390" y="756" class="box-title">ปรับปรุงข้อมูลลงตาราง assets เฉพาะคอลัมน์ที่เลือก</text>
  <text x="390" y="773" class="box-desc">อัปเดตเฉพาะฟิลด์ที่ได้รับอนุมัติ และบันทึกเวลา updated_at</text>
  <line x1="390" y1="785" x2="390" y2="805" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 8 -->
  <rect x="180" y="805" width="420" height="46" rx="8" fill="#f8fafc" stroke="#0284c7" stroke-width="1.8" filter="url(#shadow)" />
  <text x="390" y="824" class="box-title">บันทึกประวัติการปรับปรุงลงตาราง activity_logs</text>
  <text x="390" y="841" class="box-desc">บันทึกรายละเอียดรายการที่มีการเปลี่ยนแปลงเพื่อการตรวจสอบย้อนหลัง</text>
  <line x1="390" y1="851" x2="390" y2="871" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow)" />

  <!-- End -->
  <rect x="300" y="871" width="180" height="38" rx="19" fill="#1e3a8a" filter="url(#shadow)" />
  <text x="390" y="895" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle">สิ้นสุด (แจ้งเตือนสำเร็จ)</text>
</svg>
</div>
</body>
</html>
"""

# -------------------------------------------------------------
# Figure 3.4: ผังงานกระบวนการโอนย้ายสินทรัพย์ระหว่างแผนกแบบกลุ่ม
# -------------------------------------------------------------
FIG_3_4_HTML = f"""<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<style>
{COMMON_CSS}
</style>
</head>
<body>
<div class="diagram-container">
<svg width="780" height="920" viewBox="0 0 780 920" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#4f46e5" />
    </marker>
    <marker id="arrow-warn" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#ef4444" />
    </marker>
  </defs>

  <!-- Title -->
  <text x="390" y="32" class="title">รูปที่ 3.4 ผังงานกระบวนการโอนย้ายสินทรัพย์ระหว่างแผนกแบบกลุ่ม</text>
  <text x="390" y="54" class="subtitle">ระบบโอนย้ายสินทรัพย์ (Batch Department Transfer) พร้อมช่องค้นหาแผนกและบันทึกประวัติ</text>

  <!-- Start -->
  <rect x="300" y="75" width="180" height="36" rx="18" fill="#1e3a8a" filter="url(#shadow)" />
  <text x="390" y="99" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle">เริ่มต้น</text>
  <line x1="390" y1="111" x2="390" y2="133" stroke="#4f46e5" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 1 -->
  <polygon points="180,133 600,133 580,181 160,181" fill="#eef2ff" stroke="#4f46e5" stroke-width="1.8" filter="url(#shadow)" />
  <text x="390" y="153" class="box-title">ผู้ใช้เลือกรายการสินทรัพย์ที่ต้องการโอนย้าย (Batch Selection)</text>
  <text x="390" y="170" class="box-desc">ทำเครื่องหมายเลือกรายการครุภัณฑ์หลายรายการพร้อมกันจากตารางแดชบอร์ด</text>
  <line x1="390" y1="181" x2="390" y2="203" stroke="#4f46e5" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 2 -->
  <rect x="170" y="203" width="440" height="50" rx="8" fill="#f8fafc" stroke="#4f46e5" stroke-width="1.8" filter="url(#shadow)" />
  <text x="390" y="224" class="box-title">คลิกปุ่ม "โอนย้ายแผนก" เพื่อเปิด Transfer Modal</text>
  <text x="390" y="242" class="box-desc">ระบบดึงชื่อแผนกต้นทาง (from_dept) มาแสดงผลเป็นป้ายกำกับอัตโนมัติ</text>
  <line x1="390" y1="253" x2="390" y2="275" stroke="#4f46e5" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 3 -->
  <polygon points="180,275 600,275 580,323 160,323" fill="#eef2ff" stroke="#4f46e5" stroke-width="1.8" filter="url(#shadow)" />
  <text x="390" y="295" class="box-title">พิมพ์ค้นหาและเลือกแผนกปลายทาง (Department Combobox)</text>
  <text x="390" y="312" class="box-desc">รองรับการพิมพ์แล้วกรองข้อมูลทันที เลื่อนเลือกด้วยปุ่มลูกศร และกด Enter</text>
  <line x1="390" y1="323" x2="390" y2="345" stroke="#4f46e5" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 4 -->
  <polygon points="180,345 600,345 580,393 160,393" fill="#eef2ff" stroke="#4f46e5" stroke-width="1.8" filter="url(#shadow)" />
  <text x="390" y="365" class="box-title">ระบุหมายเหตุ/เหตุผลการโอนย้าย และคลิก "ยืนยันการโอนย้าย"</text>
  <text x="390" y="382" class="box-desc">บันทึกเหตุผลของการย้ายสถานที่ เช่น ส่งซ่อม ย้ายประจำห้องตรวจใหม่</text>
  <line x1="390" y1="393" x2="390" y2="415" stroke="#4f46e5" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Decision 1 -->
  <polygon points="390,415 530,460 390,505 250,460" fill="#fef3c7" stroke="#d97706" stroke-width="1.8" filter="url(#shadow)" />
  <text x="390" y="456" class="decision-text">เลือกแผนกปลายทาง</text>
  <text x="390" y="474" class="decision-text">ถูกต้องหรือไม่?</text>

  <!-- Decision 1 Fail (Right) -->
  <text x="540" y="454" fill="#ef4444" font-size="13.5" font-weight="bold">ไม่ถูกต้อง / ค่าว่าง</text>
  <polyline points="530,460 660,460 660,299 605,299" fill="none" stroke="#ef4444" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arrow-warn)" />
  <rect x="580" y="370" width="150" height="40" rx="6" fill="#fef2f2" stroke="#ef4444" stroke-width="1.2" />
  <text x="655" y="388" fill="#b91c1c" font-size="12" font-weight="bold" text-anchor="middle">แจ้งเตือนให้ระบุแผนก</text>
  <text x="655" y="402" fill="#b91c1c" font-size="11" text-anchor="middle">ปลายทางให้ถูกต้อง</text>

  <!-- Decision 1 Pass (Down) -->
  <text x="405" y="525" fill="#059669" font-size="13.5" font-weight="bold">ถูกต้อง</text>
  <line x1="390" y1="505" x2="390" y2="535" stroke="#4f46e5" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Decision 2: Permission Check -->
  <polygon points="390,535 530,580 390,625 250,580" fill="#fef3c7" stroke="#d97706" stroke-width="1.8" filter="url(#shadow)" />
  <text x="390" y="576" class="decision-text">ตรวจสอบสิทธิ์ผู้ใช้งาน</text>
  <text x="390" y="594" class="decision-text">(Admin / Super Admin)?</text>

  <!-- Permission Denied -->
  <text x="540" y="574" fill="#ef4444" font-size="13.5" font-weight="bold">ไม่มีสิทธิ์</text>
  <polyline points="530,580 660,580 660,865 485,865" fill="none" stroke="#ef4444" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arrow-warn)" />
  <rect x="580" y="630" width="150" height="40" rx="6" fill="#fef2f2" stroke="#ef4444" stroke-width="1.2" />
  <text x="655" y="648" fill="#b91c1c" font-size="12" font-weight="bold" text-anchor="middle">ปฏิเสธการเข้าถึง</text>
  <text x="655" y="662" fill="#b91c1c" font-size="11" text-anchor="middle">สิทธิ์ไม่เพียงพอ</text>

  <!-- Permission Granted -->
  <text x="405" y="645" fill="#059669" font-size="13.5" font-weight="bold">มีสิทธิ์ดำเนินการ</text>
  <line x1="390" y1="625" x2="390" y2="655" stroke="#4f46e5" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 5 -->
  <rect x="170" y="655" width="440" height="50" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8" filter="url(#shadow)" />
  <text x="390" y="676" class="box-title">อัปเดตชื่อแผนกปัจจุบัน (dept_name) ในตาราง assets</text>
  <text x="390" y="694" class="box-desc">ปรับปรุงข้อมูลแผนกครอบครองใหม่สำหรับทุกรายการสินทรัพย์ที่เลือก</text>
  <line x1="390" y1="705" x2="390" y2="725" stroke="#4f46e5" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 6 -->
  <rect x="170" y="725" width="440" height="50" rx="8" fill="#f8fafc" stroke="#4f46e5" stroke-width="1.8" filter="url(#shadow)" />
  <text x="390" y="746" class="box-title">บันทึกประวัติการโอนย้ายลงตาราง asset_transfers</text>
  <text x="390" y="763" class="box-desc">บันทึก asset_id, from_dept, to_dept, note, ผู้ทำรายการ และเวลา</text>
  <line x1="390" y1="775" x2="390" y2="795" stroke="#4f46e5" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 7 -->
  <rect x="170" y="795" width="440" height="46" rx="8" fill="#f8fafc" stroke="#4f46e5" stroke-width="1.8" filter="url(#shadow)" />
  <text x="390" y="815" class="box-title">บันทึกประวัติกิจกรรมลงตาราง activity_logs</text>
  <text x="390" y="831" class="box-desc">ระบุโมดูล Transfers บันทึกรายการโอนย้ายแบบกลุ่มเพื่อความโปร่งใส</text>
  <line x1="390" y1="841" x2="390" y2="855" stroke="#4f46e5" stroke-width="2" marker-end="url(#arrow)" />

  <!-- End -->
  <rect x="300" y="855" width="180" height="38" rx="19" fill="#1e3a8a" filter="url(#shadow)" />
  <text x="390" y="879" fill="#ffffff" font-size="15" font-weight="bold" text-anchor="middle">สิ้นสุด (แจ้งเตือนสำเร็จ)</text>
</svg>
</div>
</body>
</html>
"""

# -------------------------------------------------------------
# Figure 3.5: แผนภาพความสัมพันธ์ของข้อมูลในระบบบริหารจัดการสินทรัพย์ (ER Diagram)
# -------------------------------------------------------------
FIG_3_5_HTML = f"""<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<style>
{COMMON_CSS}
.erd-header {{ font-size: 15px; font-weight: bold; fill: #ffffff; text-anchor: middle; }}
.erd-row {{ font-size: 12.5px; fill: #1e293b; }}
.cardinality {{ font-size: 12px; font-weight: bold; fill: #1e3a8a; }}
</style>
</head>
<body>
<div class="diagram-container">
<svg width="1120" height="820" viewBox="0 0 1120 820" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
  </defs>

  <!-- Title -->
  <text x="560" y="32" class="title">รูปที่ 3.5 แผนภาพความสัมพันธ์ของข้อมูลในระบบบริหารจัดการสินทรัพย์ (Entity Relationship Diagram)</text>
  <text x="560" y="52" class="subtitle">สถาปัตยกรรมฐานข้อมูลเชิงสัมพันธ์ MySQL แสดงตารางหลัก คีย์หลัก (PK) คีย์นอก (FK) และความสัมพันธ์ 1:N</text>

  <!-- ==================== TABLE 1: users ==================== -->
  <g transform="translate(60, 80)">
    <rect x="0" y="0" width="230" height="235" rx="6" fill="#ffffff" stroke="#1e3a8a" stroke-width="1.8" filter="url(#shadow)" />
    <path d="M 0 6 Q 0 0 6 0 L 224 0 Q 230 0 230 6 L 230 30 L 0 30 Z" fill="#1e3a8a" />
    <text x="115" y="21" class="erd-header">users (ตารางผู้ใช้)</text>
    
    <text x="10" y="50" class="tag-pk">PK</text>
    <text x="35" y="50" class="col-name">id</text>
    <text x="150" y="50" class="col-type">INT (AUTO)</text>
    
    <text x="35" y="71" class="col-name">username</text>
    <text x="150" y="71" class="col-type">VARCHAR(50)</text>
    
    <text x="35" y="92" class="col-name">email</text>
    <text x="150" y="92" class="col-type">VARCHAR(100)</text>
    
    <text x="35" y="113" class="col-name">password</text>
    <text x="150" y="113" class="col-type">VARCHAR(255)</text>
    
    <text x="35" y="134" class="col-name">full_name</text>
    <text x="150" y="134" class="col-type">VARCHAR(100)</text>
    
    <text x="35" y="155" class="col-name">role</text>
    <text x="150" y="155" class="col-type">VARCHAR(20)</text>
    
    <text x="35" y="176" class="col-name">department</text>
    <text x="150" y="176" class="col-type">VARCHAR(100)</text>
    
    <text x="35" y="197" class="col-name">email_verified</text>
    <text x="150" y="197" class="col-type">TINYINT(1)</text>
    
    <text x="35" y="218" class="col-name">created_at</text>
    <text x="150" y="218" class="col-type">DATETIME</text>
  </g>

  <!-- ==================== TABLE 2: assets ==================== -->
  <g transform="translate(430, 80)">
    <rect x="0" y="0" width="290" height="285" rx="6" fill="#ffffff" stroke="#0284c7" stroke-width="1.8" filter="url(#shadow)" />
    <path d="M 0 6 Q 0 0 6 0 L 284 0 Q 290 0 290 6 L 290 30 L 0 30 Z" fill="#0284c7" />
    <text x="145" y="21" class="erd-header">assets (ตารางสินทรัพย์และครุภัณฑ์)</text>
    
    <text x="10" y="50" class="tag-pk">PK</text>
    <text x="35" y="50" class="col-name">asset_id</text>
    <text x="195" y="50" class="col-type">VARCHAR(100)</text>
    
    <text x="35" y="71" class="col-name">tag_number</text>
    <text x="195" y="71" class="col-type">VARCHAR(100)</text>
    
    <text x="35" y="92" class="col-name">serial_number_asset</text>
    <text x="195" y="92" class="col-type">VARCHAR(100)</text>
    
    <text x="35" y="113" class="col-name">descr</text>
    <text x="195" y="113" class="col-type">VARCHAR(255)</text>
    
    <text x="35" y="134" class="col-name">model</text>
    <text x="195" y="134" class="col-type">VARCHAR(100)</text>
    
    <text x="35" y="155" class="col-name">dept_name</text>
    <text x="195" y="155" class="col-type">VARCHAR(255)</text>
    
    <text x="35" y="176" class="col-name">category_name</text>
    <text x="195" y="176" class="col-type">VARCHAR(100)</text>
    
    <text x="35" y="197" class="col-name">asset_status</text>
    <text x="195" y="197" class="col-type">VARCHAR(100)</text>
    
    <text x="35" y="218" class="col-name">x_agreement_id</text>
    <text x="195" y="218" class="col-type">VARCHAR(100)</text>
    
    <text x="35" y="239" class="col-name">expire_date</text>
    <text x="195" y="239" class="col-type">DATE</text>
    
    <text x="10" y="260" class="tag-fk">FK</text>
    <text x="35" y="260" class="col-name">uploaded_by</text>
    <text x="195" y="260" class="col-type">INT</text>
    
    <text x="35" y="278" class="col-name">updated_at</text>
    <text x="195" y="278" class="col-type">DATETIME</text>
  </g>

  <!-- ==================== TABLE 3: departments ==================== -->
  <g transform="translate(830, 80)">
    <rect x="0" y="0" width="240" height="110" rx="6" fill="#ffffff" stroke="#475569" stroke-width="1.8" filter="url(#shadow)" />
    <path d="M 0 6 Q 0 0 6 0 L 234 0 Q 240 0 240 6 L 240 30 L 0 30 Z" fill="#475569" />
    <text x="120" y="21" class="erd-header">departments (ตารางแผนก)</text>
    
    <text x="10" y="52" class="tag-pk">PK</text>
    <text x="35" y="52" class="col-name">id</text>
    <text x="155" y="52" class="col-type">INT (AUTO)</text>
    
    <text x="35" y="75" class="col-name">name</text>
    <text x="155" y="75" class="col-type">VARCHAR(255)</text>
    
    <text x="35" y="98" class="col-name">costcenter</text>
    <text x="155" y="98" class="col-type">VARCHAR(50)</text>
  </g>

  <!-- ==================== TABLE 4: categories ==================== -->
  <g transform="translate(830, 230)">
    <rect x="0" y="0" width="240" height="110" rx="6" fill="#ffffff" stroke="#475569" stroke-width="1.8" filter="url(#shadow)" />
    <path d="M 0 6 Q 0 0 6 0 L 234 0 Q 240 0 240 6 L 240 30 L 0 30 Z" fill="#475569" />
    <text x="120" y="21" class="erd-header">categories (ตารางหมวดหมู่)</text>
    
    <text x="10" y="52" class="tag-pk">PK</text>
    <text x="35" y="52" class="col-name">id</text>
    <text x="155" y="52" class="col-type">INT (AUTO)</text>
    
    <text x="35" y="75" class="col-name">code</text>
    <text x="155" y="75" class="col-type">VARCHAR(50)</text>
    
    <text x="35" y="98" class="col-name">name</text>
    <text x="155" y="98" class="col-type">VARCHAR(100)</text>
  </g>

  <!-- ==================== TABLE 5: asset_transfers ==================== -->
  <g transform="translate(430, 440)">
    <rect x="0" y="0" width="290" height="195" rx="6" fill="#ffffff" stroke="#4f46e5" stroke-width="1.8" filter="url(#shadow)" />
    <path d="M 0 6 Q 0 0 6 0 L 284 0 Q 290 0 290 6 L 290 30 L 0 30 Z" fill="#4f46e5" />
    <text x="145" y="21" class="erd-header">asset_transfers (ประวัติโอนย้าย)</text>
    
    <text x="10" y="52" class="tag-pk">PK</text>
    <text x="35" y="52" class="col-name">id</text>
    <text x="185" y="52" class="col-type">INT (AUTO)</text>
    
    <text x="10" y="75" class="tag-fk">FK</text>
    <text x="35" y="75" class="col-name">asset_id</text>
    <text x="185" y="75" class="col-type">VARCHAR(100)</text>
    
    <text x="35" y="98" class="col-name">from_dept</text>
    <text x="185" y="98" class="col-type">VARCHAR(255)</text>
    
    <text x="35" y="121" class="col-name">to_dept</text>
    <text x="185" y="121" class="col-type">VARCHAR(255)</text>
    
    <text x="35" y="144" class="col-name">note</text>
    <text x="185" y="144" class="col-type">TEXT</text>
    
    <text x="10" y="167" class="tag-fk">FK</text>
    <text x="35" y="167" class="col-name">transferred_by</text>
    <text x="185" y="167" class="col-type">INT</text>
    
    <text x="35" y="188" class="col-name">created_at</text>
    <text x="185" y="188" class="col-type">DATETIME</text>
  </g>

  <!-- ==================== TABLE 6: documents ==================== -->
  <g transform="translate(60, 360)">
    <rect x="0" y="0" width="230" height="175" rx="6" fill="#ffffff" stroke="#059669" stroke-width="1.8" filter="url(#shadow)" />
    <path d="M 0 6 Q 0 0 6 0 L 224 0 Q 230 0 230 6 L 230 30 L 0 30 Z" fill="#059669" />
    <text x="115" y="21" class="erd-header">documents (เอกสาร PDF)</text>
    
    <text x="10" y="52" class="tag-pk">PK</text>
    <text x="35" y="52" class="col-name">id</text>
    <text x="150" y="52" class="col-type">INT (AUTO)</text>
    
    <text x="35" y="75" class="col-name">filename</text>
    <text x="150" y="75" class="col-type">VARCHAR(255)</text>
    
    <text x="35" y="98" class="col-name">original_name</text>
    <text x="150" y="98" class="col-type">VARCHAR(255)</text>
    
    <text x="35" y="121" class="col-name">department</text>
    <text x="150" y="121" class="col-type">VARCHAR(255)</text>
    
    <text x="10" y="144" class="tag-fk">FK</text>
    <text x="35" y="144" class="col-name">uploaded_by</text>
    <text x="150" y="144" class="col-type">INT</text>
    
    <text x="35" y="165" class="col-name">created_at</text>
    <text x="150" y="165" class="col-type">DATETIME</text>
  </g>

  <!-- ==================== TABLE 7: activity_logs ==================== -->
  <g transform="translate(60, 580)">
    <rect x="0" y="0" width="230" height="195" rx="6" fill="#ffffff" stroke="#d97706" stroke-width="1.8" filter="url(#shadow)" />
    <path d="M 0 6 Q 0 0 6 0 L 224 0 Q 230 0 230 6 L 230 30 L 0 30 Z" fill="#d97706" />
    <text x="115" y="21" class="erd-header">activity_logs (ประวัติกิจกรรม)</text>
    
    <text x="10" y="52" class="tag-pk">PK</text>
    <text x="35" y="52" class="col-name">id</text>
    <text x="150" y="52" class="col-type">INT (AUTO)</text>
    
    <text x="10" y="75" class="tag-fk">FK</text>
    <text x="35" y="75" class="col-name">user_id</text>
    <text x="150" y="75" class="col-type">INT</text>
    
    <text x="35" y="98" class="col-name">module</text>
    <text x="150" y="98" class="col-type">VARCHAR(50)</text>
    
    <text x="35" y="121" class="col-name">action</text>
    <text x="150" y="121" class="col-type">VARCHAR(50)</text>
    
    <text x="35" y="144" class="col-name">target</text>
    <text x="150" y="144" class="col-type">VARCHAR(100)</text>
    
    <text x="35" y="167" class="col-name">details</text>
    <text x="150" y="167" class="col-type">TEXT</text>
    
    <text x="35" y="188" class="col-name">created_at</text>
    <text x="150" y="188" class="col-type">DATETIME</text>
  </g>

  <!-- ==================== TABLE 8: sessions ==================== -->
  <g transform="translate(830, 440)">
    <rect x="0" y="0" width="240" height="110" rx="6" fill="#ffffff" stroke="#64748b" stroke-width="1.8" filter="url(#shadow)" />
    <path d="M 0 6 Q 0 0 6 0 L 234 0 Q 240 0 240 6 L 240 30 L 0 30 Z" fill="#64748b" />
    <text x="120" y="21" class="erd-header">sessions (ตารางเซสชันระบบ)</text>
    
    <text x="10" y="52" class="tag-pk">PK</text>
    <text x="35" y="52" class="col-name">session_id</text>
    <text x="145" y="52" class="col-type">VARCHAR(128)</text>
    
    <text x="35" y="75" class="col-name">expires</text>
    <text x="145" y="75" class="col-type">INT(11)</text>
    
    <text x="35" y="98" class="col-name">data</text>
    <text x="145" y="98" class="col-type">MEDIUMTEXT</text>
  </g>

  <!-- ==================== RELATIONSHIP LINES ==================== -->
  <!-- users (1) to assets (N) [uploaded_by] -->
  <path d="M 290 130 L 360 130 L 360 340 L 430 340" fill="none" stroke="#2563eb" stroke-width="2" />
  <circle cx="295" cy="130" r="4" fill="#2563eb" />
  <text x="305" y="125" class="cardinality">1</text>
  <polyline points="420,333 430,340 420,347" fill="none" stroke="#2563eb" stroke-width="2" />
  <text x="405" y="335" class="cardinality">N</text>

  <!-- assets (1) to asset_transfers (N) [asset_id] -->
  <path d="M 575 365 L 575 440" fill="none" stroke="#4f46e5" stroke-width="2" />
  <circle cx="575" cy="370" r="4" fill="#4f46e5" />
  <text x="585" y="380" class="cardinality">1</text>
  <polyline points="568,430 575,440 582,430" fill="none" stroke="#4f46e5" stroke-width="2" />
  <text x="585" y="435" class="cardinality">N</text>

  <!-- users (1) to asset_transfers (N) [transferred_by] -->
  <path d="M 290 220 L 340 220 L 340 605 L 430 605" fill="none" stroke="#4f46e5" stroke-width="1.8" stroke-dasharray="4,3" />
  <circle cx="295" cy="220" r="4" fill="#4f46e5" />
  <text x="305" y="215" class="cardinality">1</text>
  <polyline points="420,598 430,605 420,612" fill="none" stroke="#4f46e5" stroke-width="2" />
  <text x="405" y="600" class="cardinality">N</text>

  <!-- users (1) to documents (N) [uploaded_by] -->
  <path d="M 175 315 L 175 360" fill="none" stroke="#059669" stroke-width="2" />
  <circle cx="175" cy="320" r="4" fill="#059669" />
  <text x="185" y="330" class="cardinality">1</text>
  <polyline points="168,350 175,360 182,350" fill="none" stroke="#059669" stroke-width="2" />
  <text x="185" y="355" class="cardinality">N</text>

  <!-- users (1) to activity_logs (N) [user_id] (routes around left side) -->
  <path d="M 60 130 L 30 130 L 30 650 L 60 650" fill="none" stroke="#d97706" stroke-width="2" stroke-dasharray="5,3" />
  <circle cx="55" cy="130" r="4" fill="#d97706" />
  <text x="40" y="125" class="cardinality">1</text>
  <polyline points="50,643 60,650 50,657" fill="none" stroke="#d97706" stroke-width="2" />
  <text x="40" y="665" class="cardinality">N</text>

  <!-- departments (1) to assets (N) [dept_name] -->
  <path d="M 830 135 L 720 135" fill="none" stroke="#475569" stroke-width="1.8" />
  <circle cx="825" cy="135" r="4" fill="#475569" />
  <text x="810" y="130" class="cardinality">1</text>
  <polyline points="730,128 720,135 730,142" fill="none" stroke="#475569" stroke-width="2" />
  <text x="735" y="130" class="cardinality">N</text>

  <!-- categories (1) to assets (N) [category_name] -->
  <path d="M 830 285 L 720 285" fill="none" stroke="#475569" stroke-width="1.8" />
  <circle cx="825" cy="285" r="4" fill="#475569" />
  <text x="810" y="280" class="cardinality">1</text>
  <polyline points="730,278 720,285 730,292" fill="none" stroke="#475569" stroke-width="2" />
  <text x="735" y="280" class="cardinality">N</text>

</svg>
</div>
</body>
</html>
"""

# -------------------------------------------------------------
# Figure 3.6: แผนภาพกรณีการใช้งานของระบบบริหารจัดการสินทรัพย์ (Use Case Diagram)
# -------------------------------------------------------------
FIG_3_6_HTML = f"""<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<style>
{COMMON_CSS}
.actor-text {{ font-size: 14.5px; font-weight: bold; fill: #1e293b; text-anchor: middle; }}
.actor-sub {{ font-size: 12.5px; fill: #64748b; text-anchor: middle; }}
.uc-text {{ font-size: 13px; fill: #0f172a; text-anchor: middle; font-weight: 500; }}
.sys-boundary-title {{ font-size: 16px; font-weight: bold; fill: #1e3a8a; text-anchor: middle; }}
.group-header {{ font-size: 14px; font-weight: bold; fill: #334155; text-anchor: middle; }}
</style>
</head>
<body>
<div class="diagram-container">
<svg width="1120" height="780" viewBox="0 0 1120 780" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
    <marker id="generalize" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <polygon points="0,0 10,6 0,12" fill="#ffffff" stroke="#475569" stroke-width="1.8" />
    </marker>
  </defs>

  <!-- Title -->
  <text x="560" y="32" class="title">รูปที่ 3.6 แผนภาพกรณีการใช้งานของระบบบริหารจัดการสินทรัพย์ (Use Case Diagram)</text>
  <text x="560" y="52" class="subtitle">การควบคุมสิทธิ์ตามบทบาท (Role-Based Access Control: RBAC) ครอบคลุม 3 บทบาทหลัก</text>

  <!-- System Boundary -->
  <rect x="180" y="75" width="760" height="685" rx="10" fill="#f8fafc" stroke="#3b82f6" stroke-width="2" filter="url(#shadow)" />
  <text x="560" y="104" class="sys-boundary-title">ระบบบริหารจัดการสินทรัพย์ (Asset Management System)</text>

  <!-- ==================== ACTOR LEFT: User ==================== -->
  <g transform="translate(45, 270)">
    <circle cx="45" cy="20" r="15" fill="#ffffff" stroke="#1e3a8a" stroke-width="2.2" />
    <line x1="45" y1="35" x2="45" y2="80" stroke="#1e3a8a" stroke-width="2.2" />
    <line x1="15" y1="52" x2="75" y2="52" stroke="#1e3a8a" stroke-width="2.2" />
    <line x1="45" y1="80" x2="22" y2="120" stroke="#1e3a8a" stroke-width="2.2" />
    <line x1="45" y1="80" x2="68" y2="120" stroke="#1e3a8a" stroke-width="2.2" />
    <text x="45" y="145" class="actor-text">ผู้ใช้งานทั่วไป</text>
    <text x="45" y="163" class="actor-sub">(User)</text>
  </g>

  <!-- ==================== ACTORS RIGHT: Admin & Super Admin ==================== -->
  <!-- Admin -->
  <g transform="translate(980, 160)">
    <circle cx="45" cy="20" r="15" fill="#ffffff" stroke="#0284c7" stroke-width="2.2" />
    <line x1="45" y1="35" x2="45" y2="80" stroke="#0284c7" stroke-width="2.2" />
    <line x1="15" y1="52" x2="75" y2="52" stroke="#0284c7" stroke-width="2.2" />
    <line x1="45" y1="80" x2="22" y2="120" stroke="#0284c7" stroke-width="2.2" />
    <line x1="45" y1="80" x2="68" y2="120" stroke="#0284c7" stroke-width="2.2" />
    <text x="45" y="145" class="actor-text">ผู้ดูแลระบบ</text>
    <text x="45" y="163" class="actor-sub">(Admin)</text>
  </g>

  <!-- Super Admin -->
  <g transform="translate(980, 500)">
    <circle cx="45" cy="20" r="15" fill="#ffffff" stroke="#7c3aed" stroke-width="2.2" />
    <line x1="45" y1="35" x2="45" y2="80" stroke="#7c3aed" stroke-width="2.2" />
    <line x1="15" y1="52" x2="75" y2="52" stroke="#7c3aed" stroke-width="2.2" />
    <line x1="45" y1="80" x2="22" y2="120" stroke="#7c3aed" stroke-width="2.2" />
    <line x1="45" y1="80" x2="68" y2="120" stroke="#7c3aed" stroke-width="2.2" />
    <text x="45" y="145" class="actor-text">ผู้ดูแลระบบสูงสุด</text>
    <text x="45" y="163" class="actor-sub">(Super Admin)</text>
  </g>

  <!-- Generalization Arrow (Super Admin -> Admin) -->
  <line x1="1025" y1="500" x2="1025" y2="340" stroke="#475569" stroke-width="2" marker-end="url(#generalize)" />

  <!-- ==================== COLUMN 1 (LEFT): USER USE CASES ==================== -->
  <text x="360" y="138" class="group-header">ฟังก์ชันสำหรับผู้ใช้งานทั่วไป (User)</text>
  <line x1="230" y1="146" x2="490" y2="146" stroke="#cbd5e1" stroke-width="1" />

  <!-- UC 1 -->
  <ellipse cx="360" cy="180" rx="135" ry="22" fill="#ffffff" stroke="#2563eb" stroke-width="1.5" filter="url(#shadow)" />
  <text x="360" y="185" class="uc-text">เข้าสู่ระบบ (Sign In)</text>

  <!-- UC 2 -->
  <ellipse cx="360" cy="245" rx="135" ry="22" fill="#ffffff" stroke="#2563eb" stroke-width="1.5" filter="url(#shadow)" />
  <text x="360" y="250" class="uc-text">ดูแดชบอร์ดสรุปยอดสินทรัพย์</text>

  <!-- UC 3 -->
  <ellipse cx="360" cy="310" rx="135" ry="22" fill="#ffffff" stroke="#2563eb" stroke-width="1.5" filter="url(#shadow)" />
  <text x="360" y="315" class="uc-text">ค้นหาและคัดกรองข้อมูลสินทรัพย์</text>

  <!-- UC 4 -->
  <ellipse cx="360" cy="375" rx="135" ry="22" fill="#ffffff" stroke="#2563eb" stroke-width="1.5" filter="url(#shadow)" />
  <text x="360" y="380" class="uc-text">ดูรายละเอียดและประวัติสินทรัพย์</text>

  <!-- UC 5 -->
  <ellipse cx="360" cy="440" rx="135" ry="22" fill="#ffffff" stroke="#2563eb" stroke-width="1.5" filter="url(#shadow)" />
  <text x="360" y="445" class="uc-text">ส่งออกข้อมูลเป็นไฟล์ CSV</text>

  <!-- UC 6 -->
  <ellipse cx="360" cy="505" rx="135" ry="22" fill="#ffffff" stroke="#2563eb" stroke-width="1.5" filter="url(#shadow)" />
  <text x="360" y="510" class="uc-text">แสดงรหัสคิวอาร์และพิมพ์ป้ายสติกเกอร์</text>

  <!-- UC 7 -->
  <ellipse cx="360" cy="570" rx="135" ry="22" fill="#ffffff" stroke="#2563eb" stroke-width="1.5" filter="url(#shadow)" />
  <text x="360" y="575" class="uc-text">เปิดดูและดาวน์โหลดเอกสาร PDF</text>

  <!-- UC 8 -->
  <ellipse cx="360" cy="635" rx="135" ry="22" fill="#ffffff" stroke="#2563eb" stroke-width="1.5" filter="url(#shadow)" />
  <text x="360" y="640" class="uc-text">แก้ไขข้อมูลโปรไฟล์ส่วนตัว</text>

  <!-- ==================== COLUMN 2 (RIGHT): ADMIN & SUPER ADMIN USE CASES ==================== -->
  <text x="740" y="138" class="group-header">ฟังก์ชันเฉพาะผู้ดูแลระบบและระดับสูง</text>
  <line x1="600" y1="146" x2="880" y2="146" stroke="#cbd5e1" stroke-width="1" />

  <!-- UC 9 (Admin) -->
  <ellipse cx="740" cy="180" rx="145" ry="22" fill="#ffffff" stroke="#0284c7" stroke-width="1.5" filter="url(#shadow)" />
  <text x="740" y="185" class="uc-text">นำเข้าข้อมูลสินทรัพย์ผ่านไฟล์ Excel</text>

  <!-- UC 10 (Admin) -->
  <ellipse cx="740" cy="240" rx="145" ry="22" fill="#ffffff" stroke="#0284c7" stroke-width="1.5" filter="url(#shadow)" />
  <text x="740" y="245" class="uc-text">อัปเดตข้อมูลพร้อมตรวจผลต่าง (Diff)</text>

  <!-- UC 11 (Admin) -->
  <ellipse cx="740" cy="300" rx="145" ry="22" fill="#ffffff" stroke="#0284c7" stroke-width="1.5" filter="url(#shadow)" />
  <text x="740" y="305" class="uc-text">โอนย้ายสินทรัพย์ระหว่างแผนกแบบกลุ่ม</text>

  <!-- UC 12 (Admin) -->
  <ellipse cx="740" cy="360" rx="145" ry="22" fill="#ffffff" stroke="#0284c7" stroke-width="1.5" filter="url(#shadow)" />
  <text x="740" y="365" class="uc-text">แก้ไขและปรับปรุงสถานะสินทรัพย์</text>

  <!-- UC 13 (Admin) -->
  <ellipse cx="740" cy="420" rx="145" ry="22" fill="#ffffff" stroke="#0284c7" stroke-width="1.5" filter="url(#shadow)" />
  <text x="740" y="425" class="uc-text">จัดการไฟล์เอกสาร PDF (อัปโหลด/ลบ)</text>

  <!-- UC 14 (Admin) -->
  <ellipse cx="740" cy="480" rx="145" ry="22" fill="#ffffff" stroke="#0284c7" stroke-width="1.5" filter="url(#shadow)" />
  <text x="740" y="485" class="uc-text">ตรวจสอบบันทึกกิจกรรม (Activity Logs)</text>

  <!-- UC 15 (Super Admin) -->
  <ellipse cx="740" cy="555" rx="145" ry="22" fill="#faf5ff" stroke="#7c3aed" stroke-width="1.8" filter="url(#shadow)" />
  <text x="740" y="560" class="uc-text" font-weight="bold" fill="#6b21a8">จัดการบัญชีผู้ใช้และกำหนดสิทธิ์</text>

  <!-- UC 16 (Super Admin) -->
  <ellipse cx="740" cy="615" rx="145" ry="22" fill="#faf5ff" stroke="#7c3aed" stroke-width="1.8" filter="url(#shadow)" />
  <text x="740" y="620" class="uc-text" font-weight="bold" fill="#6b21a8">จัดการข้อมูลแผนกและศูนย์ต้นทุน</text>

  <!-- UC 17 (Super Admin) -->
  <ellipse cx="740" cy="675" rx="145" ry="22" fill="#faf5ff" stroke="#7c3aed" stroke-width="1.8" filter="url(#shadow)" />
  <text x="740" y="680" class="uc-text" font-weight="bold" fill="#6b21a8">จัดการหมวดหมู่สินทรัพย์</text>

  <!-- ==================== ASSOCIATIONS (Solid Lines) ==================== -->
  <!-- User lines (from Actor on Left at x=120, y=320 to Left Column at x=225) -->
  <line x1="120" y1="320" x2="225" y2="180" stroke="#2563eb" stroke-width="1.3" />
  <line x1="120" y1="320" x2="225" y2="245" stroke="#2563eb" stroke-width="1.3" />
  <line x1="120" y1="320" x2="225" y2="310" stroke="#2563eb" stroke-width="1.3" />
  <line x1="120" y1="320" x2="225" y2="375" stroke="#2563eb" stroke-width="1.3" />
  <line x1="120" y1="320" x2="225" y2="440" stroke="#2563eb" stroke-width="1.3" />
  <line x1="120" y1="320" x2="225" y2="505" stroke="#2563eb" stroke-width="1.3" />
  <line x1="120" y1="320" x2="225" y2="570" stroke="#2563eb" stroke-width="1.3" />
  <line x1="120" y1="320" x2="225" y2="635" stroke="#2563eb" stroke-width="1.3" />

  <!-- Admin lines (from Actor on Right at x=980, y=210 to Right Column at x=885) -->
  <line x1="980" y1="210" x2="885" y2="180" stroke="#0284c7" stroke-width="1.5" />
  <line x1="980" y1="210" x2="885" y2="240" stroke="#0284c7" stroke-width="1.5" />
  <line x1="980" y1="210" x2="885" y2="300" stroke="#0284c7" stroke-width="1.5" />
  <line x1="980" y1="210" x2="885" y2="360" stroke="#0284c7" stroke-width="1.5" />
  <line x1="980" y1="210" x2="885" y2="420" stroke="#0284c7" stroke-width="1.5" />
  <line x1="980" y1="210" x2="885" y2="480" stroke="#0284c7" stroke-width="1.5" />

  <!-- Super Admin lines (from Actor on Right at x=980, y=550 to Super Admin use cases at x=885) -->
  <line x1="980" y1="550" x2="885" y2="555" stroke="#7c3aed" stroke-width="1.8" />
  <line x1="980" y1="550" x2="885" y2="615" stroke="#7c3aed" stroke-width="1.8" />
  <line x1="980" y1="550" x2="885" y2="675" stroke="#7c3aed" stroke-width="1.8" />

  <!-- Inherited Note -->
  <rect x="945" y="380" width="160" height="42" rx="4" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1" />
  <text x="1025" y="398" fill="#475569" font-size="11.5" text-anchor="middle">* ได้รับสิทธิ์ครอบคลุม</text>
  <text x="1025" y="413" fill="#475569" font-size="11.5" text-anchor="middle">ทุกฟังก์ชันของระดับก่อนหน้า</text>

</svg>
</div>
</body>
</html>
"""



ALL_DIAGRAMS = [
    ("fig_3_1", FIG_3_1_HTML, 840, 980),
    ("fig_3_2", FIG_3_2_HTML, 840, 940),
    ("fig_3_3", FIG_3_3_HTML, 840, 1010),
    ("fig_3_4", FIG_3_4_HTML, 840, 980),
    ("fig_3_5", FIG_3_5_HTML, 1140, 860),
    ("fig_3_6", FIG_3_6_HTML, 1110, 980),
]

def render_diagrams():
    print("Generating diagrams...")
    for name, html_content, w, h in ALL_DIAGRAMS:
        html_file = os.path.join(HTML_DIR, f"{name}.html")
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        
        in_png_file = os.path.join(INPUT_FIG_DIR, f"{name}.png")
        out_png_file = os.path.join(OUTPUT_FIG_DIR, f"{name}.png")
        
        file_url = f"file:///{html_file.replace(os.sep, '/')}"
        
        # Render with Edge headless
        cmd = [
            EDGE_PATH,
            "--headless=new",
            "--disable-gpu",
            "--force-device-scale-factor=2",
            f"--window-size={w},{h}",
            f"--screenshot={out_png_file}",
            file_url
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"Error rendering {name}: {res.stderr}")
        else:
            # Also copy to input/figures/
            if os.path.exists(out_png_file):
                import shutil
                shutil.copy2(out_png_file, in_png_file)
                print(f"Rendered: {name}.png ({os.path.getsize(out_png_file)} bytes)")
            else:
                print(f"Warning: {name}.png was not created.")

if __name__ == "__main__":
    render_diagrams()
