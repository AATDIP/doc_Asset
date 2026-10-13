# -*- coding: utf-8 -*-
import subprocess
import os
import shutil

ROOT = r"d:\inturn\doc\doc\doc"
HTML_DIR = os.path.join(ROOT, "input", "figures", "html")
os.makedirs(HTML_DIR, exist_ok=True)

HTML_CONTENT = """<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<title>Asset Management - Korat Circuit.pdf</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/font/bootstrap-icons.css">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background-color: #12141c;
    color: #e2e8f0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    min-height: 100vh;
    overflow: hidden;
  }
  .navbar-custom {
    background-color: #0f4b26;
    padding: 8px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255,255,255,0.1);
  }
  .brand {
    font-weight: 700;
    font-size: 1.25rem;
    color: #ffffff;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .sidebar {
    width: 200px;
    background-color: #161822;
    min-height: calc(100vh - 56px);
    padding: 16px 12px;
    border-right: 1px solid rgba(255,255,255,0.08);
  }
  .nav-item {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 10px 14px;
    color: #94a3b8;
    text-decoration: none;
    border-radius: 8px;
    margin-bottom: 6px;
    font-size: 0.95rem;
  }
  .nav-item.active {
    background-color: rgba(34, 197, 94, 0.15);
    color: #4ade80;
    font-weight: 600;
    border-left: 3px solid #22c55e;
  }
  .main-content {
    flex: 1;
    padding: 24px 32px;
    display: flex;
    flex-direction: column;
  }
  .doc-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
  }
  .pdf-viewer-card {
    background: #1e2230;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 8px 24px rgba(0,0,0,0.3);
    overflow: hidden;
    height: 720px;
    display: flex;
    flex-direction: column;
  }
  .pdf-toolbar {
    background: #2a2e40;
    padding: 8px 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid rgba(255,255,255,0.1);
    font-size: 0.85rem;
    color: #cbd5e1;
  }
  .pdf-canvas {
    flex: 1;
    background: #3a3f55;
    padding: 24px;
    display: flex;
    justify-content: center;
    overflow-y: auto;
  }
  .pdf-page {
    background: #ffffff;
    color: #1e293b;
    width: 600px;
    min-height: 800px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.4);
    padding: 48px;
    border-radius: 4px;
    font-family: 'TH Sarabun New', 'TH SarabunPSK', sans-serif;
  }
</style>
</head>
<body>
<div class="navbar-custom">
  <div class="brand"><i class="bi bi-boxes text-success"></i> Asset Management</div>
  <div class="d-flex align-items-center gap-3">
    <span class="badge bg-secondary"><i class="bi bi-globe me-1"></i>EN</span>
    <span class="text-white-50"><i class="bi bi-person-circle me-1 text-light"></i>admin</span>
    <span class="badge bg-success"><i class="bi bi-shield-check me-1"></i>Admin</span>
    <button class="btn btn-sm btn-outline-danger"><i class="bi bi-box-arrow-right me-1"></i>Logout</button>
  </div>
</div>
<div class="d-flex">
  <div class="sidebar">
    <div class="nav-item"><i class="bi bi-speedometer2"></i> Dashboard</div>
    <div class="nav-item"><i class="bi bi-cloud-upload"></i> Upload</div>
    <div class="nav-item"><i class="bi bi-pencil-square"></i> Update</div>
    <div class="nav-item"><i class="bi bi-clock-history"></i> Logs</div>
    <div class="nav-item"><i class="bi bi-arrow-left-right"></i> Transfer</div>
    <div class="nav-item active"><i class="bi bi-file-earmark-pdf"></i> Documents</div>
  </div>
  <div class="main-content">
    <div class="doc-header">
      <h5 class="mb-0 text-white"><i class="bi bi-file-earmark-pdf-fill text-danger me-2"></i>Korat Circuit.pdf <small class="text-white-50 fs-6 ms-2">(100.0 KB - งานสารสนเทศ)</small></h5>
      <div class="d-flex gap-2">
        <button class="btn btn-sm btn-outline-light"><i class="bi bi-arrow-left me-1"></i>ย้อนกลับ</button>
        <button class="btn btn-sm btn-success"><i class="bi bi-download me-1"></i>ดาวน์โหลด</button>
      </div>
    </div>
    <div class="pdf-viewer-card">
      <div class="pdf-toolbar">
        <div class="d-flex align-items-center gap-3">
          <span><i class="bi bi-layout-sidebar me-1"></i>สารบัญ</span>
          <span>หน้า 1 / 1</span>
          <span><i class="bi bi-zoom-out"></i> 100% <i class="bi bi-zoom-in"></i></span>
        </div>
        <div class="d-flex align-items-center gap-2">
          <span class="badge bg-primary">Content-Security-Policy: Validated</span>
          <i class="bi bi-printer text-white-50 ms-2"></i>
        </div>
      </div>
      <div class="pdf-canvas">
        <div class="pdf-page">
          <div style="text-align: center; border-bottom: 2px solid #0f4b26; padding-bottom: 12px; margin-bottom: 20px;">
            <h4 style="margin: 0; color: #0f4b26;">แบบฟอร์มบันทึกการตรวจสอบระบบเครือข่ายและสินทรัพย์</h4>
            <div style="font-size: 14px; color: #64748b;">ศูนย์นวัตกรรมและสารสนเทศ มหาวิทยาลัยเทคโนโลยีราชมงคลอีสาน</div>
          </div>
          <table style="width: 100%; border-collapse: collapse; font-size: 14px; margin-bottom: 16px;">
            <tr>
              <td style="padding: 6px; font-weight: bold; width: 30%;">รหัสเอกสาร:</td>
              <td style="padding: 6px;">DOC-2026-0818-002</td>
            </tr>
            <tr>
              <td style="padding: 6px; font-weight: bold;">ชื่อโครงการ:</td>
              <td style="padding: 6px;">Korat Circuit Network Maintenance</td>
            </tr>
            <tr>
              <td style="padding: 6px; font-weight: bold;">หน่วยงานรับผิดชอบ:</td>
              <td style="padding: 6px;">งานสารสนเทศ คณะแพทยศาสตร์</td>
            </tr>
            <tr>
              <td style="padding: 6px; font-weight: bold;">วันที่บันทึกข้อมูล:</td>
              <td style="padding: 6px;">18 สิงหาคม 2569</td>
            </tr>
          </table>
          <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 12px; font-size: 13px; line-height: 1.6; color: #334155;">
            <strong>รายละเอียดการตรวจสอบ:</strong><br>
            ดำเนินการตรวจสอบระบบอุปกรณ์เครือข่าย อาคารศูนย์นวัตกรรมและข้อมูลครุภัณฑ์ประจำห้องปฏิบัติการคอมพิวเตอร์ ระบบสามารถเชื่อมต่อและซิงค์ข้อมูลกับระบบ Asset Management ได้อย่างราบรื่น
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</body>
</html>
"""

html_file = os.path.join(HTML_DIR, "fig_4_9.html")
with open(html_file, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

out_fig = os.path.join(ROOT, "input", "figures", "fig_4_9.png")
out_fig_pub = os.path.join(ROOT, "output", "figures", "fig_4_9.png")

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(EDGE_PATH):
    EDGE_PATH = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

cmd = [
    EDGE_PATH,
    "--headless=new",
    "--disable-gpu",
    "--force-device-scale-factor=1",
    "--window-size=1280,820",
    f"--screenshot={out_fig}",
    f"file:///{html_file.replace(os.sep, '/')}"
]
subprocess.run(cmd, check=True)
shutil.copy2(out_fig, out_fig_pub)
print(f"Generated fig_4_9.png successfully: {os.path.getsize(out_fig)} bytes")
