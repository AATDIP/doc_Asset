# Project Fact Sheet: Asset Management (ระบบบริหารจัดการสินทรัพย์)

> กฎการจัดหน้า/พิมพ์ไทยทั้งหมดอยู่ที่ skill `.agent/skills/rmuti-thesis/SKILL.md` ที่เดียว ไฟล์นี้เก็บ **ข้อเท็จจริงของโปรเจกต์** เท่านั้น
> ข้อมูลทั้งหมดสอดคล้องกับโค้ดจริงใน `https://github.com/yonitsu45/assetmanage` และเอกสารอธิบายระบบ (2026-10-02)

## ชื่อโปรเจกต์ (ใช้ชื่อนี้ชื่อเดียวทั้งเล่ม)
- **TH**: ระบบบริหารจัดการสินทรัพย์ (Asset Management)
- **EN**: Asset Management System
- **สถานประกอบการ/หน่วยงานผู้ใช้งาน**: คณะแพทยศาสตร์ โรงพยาบาลศรีนครินทร์ มหาวิทยาลัยขอนแก่น (ฝ่ายเทคโนโลยีสารสนเทศ / แผนกงานสารสนเทศ)

## ขอบเขตและบทบาทหน้าที่ของผู้จัดทำ
- **บทบาทหลัก**: ผู้พัฒนาส่วนต่อประสานผู้ใช้ (**Frontend Developer**)
- **เทคโนโลยีฝั่ง Frontend ที่ผู้จัดทำพัฒนา**:
  - **Template Engine**: EJS (Embedded JavaScript Templates) บนสถาปัตยกรรม Server-Side Rendering (SSR)
  - **CSS Framework & Styling**: Bootstrap 5.3.3, Bootstrap Icons, และ Custom CSS (`public/css/style.css`)
  - **Theming & Dark Mode**: ออกแบบด้วย CSS Variables (`--bg`, `--card`, `--text` ฯลฯ) พร้อมสคริปต์ป้องกันการกระพริบของหน้าจอ (Anti-FOUC) ใน `header.ejs`
  - **Client-Side JavaScript**:
    - `public/js/sidebar.js`: จัดการย่อ/ขยาย Sidebar บนเดสก์ท็อปและ Drawer บนอุปกรณ์พกพา ซิงค์สถานะกับ `localStorage`
    - `public/js/dept-combo.js`: ระบบกล่องค้นหาเลือกแผนกแบบ Search-as-you-type และการนำทางด้วยแป้นพิมพ์
    - `public/js/qr.js`: การเรนเดอร์ QR Code ผ่านไลบรารี `qrcode.js` และจัดรูปแบบการพิมพ์ป้ายกำกับสินทรัพย์ (Print Label) ขนาด 70×24 มิลลิเมตร
  - **Partials Architecture**: โครงสร้างคอมโพเนนต์ย่อยแยกเป็น `header.ejs`, `navbar.ejs`, `sidebar.ejs`, และ `footer.ejs`
  - **หน้าจอและการโต้ตอบหลัก (Views)**:
    - `dashboard.ejs`: การ์ดสรุปยอดสินทรัพย์, แถบค้นหาและตัวกรองหลายมิติ, กล่องเลือกจำนวนต่อหน้า (`#limitSelect`), ตารางสินทรัพย์ขนาดใหญ่พร้อม `.table-scroll-wrapper` และ Sticky Header, Modals ดู/แก้ไข/QR/ยืนยัน
    - `upload.ejs` & `update.ejs`: หน้าจอนำเข้าไฟล์ Excel และหน้าจอเปรียบเทียบข้อมูลก่อนบันทึก (Data Diff Preview)
    - `partials/transfer-modal.ejs`: หน้าต่างโต้ตอบโอนย้ายสินทรัพย์ข้ามแผนกแบบกลุ่ม รองรับการเปิดจากทั้งแดชบอร์ดและหน้าโอนย้าย พร้อมป้าย Badge แผนกต้นทาง
    - `documents.ejs` & `document-view.ejs`: หน้าจอจัดการเอกสาร PDF รองรับการสลับมุมมอง Grid/List (บันทึกใน `localStorage`) และการฝังเอกสารผ่าน `<iframe>` ตามนโยบาย CSP
    - `admin-users.ejs`: หน้าจอจัดการผู้ใช้ แผนก และหมวดหมู่สินทรัพย์
  - **Internationalization (i18n)**: รองรับสองภาษา (ไทยและอังกฤษ) ผ่านฟังก์ชัน `__('key')` และไฟล์ `locales/th.json`, `en.json`
  - **Global Form Confirmation**: ตรวจจับการกดส่งแบบฟอร์มที่มีแอตทริบิวต์ `data-confirm` เพื่อเปิดหน้าต่างยืนยันผ่าน SweetAlert2 ก่อนบันทึกจริง

## สถาปัตยกรรมระบบโดยรวม (System Architecture)
- **สถาปัตยกรรม**: Web-based Multi-tier Architecture (MVC ร่วมกับ SSR)
- **ระบบเซิร์ฟเวอร์หลังบ้าน (Backend)**: Node.js ร่วมกับ Express Framework 5.2.1
- **ฐานข้อมูล**: MySQL ผ่านไดรเวอร์ `mysql2` (Connection Pool)
- **การจัดการ Session**: `express-session` ร่วมกับ `express-mysql-session` บันทึกลงตาราง `sessions` ใน MySQL
- **การรักษาความปลอดภัย (Security)**:
  - `bcrypt` สำหรับเข้ารหัสผ่าน
  - `helmet` กำหนด Content Security Policy (CSP) อนุญาตเฉพาะสคริปต์ที่กำหนด (`frameSrc: ["'self'"]`, `objectSrc: ["'none'"]`)
  - Custom CSRF Token (`csrf.js`) สำหรับคำขอแบบ POST/PUT/DELETE
  - Rate Limiting สำหรับป้องกัน Brute Force ในหน้าเข้าสู่ระบบ
  - reCAPTCHA v3 ในขั้นตอนลงทะเบียน
  - Magic Bytes Verification (`%PDF-`) ตรวจสอบความถูกต้องของไฟล์ PDF ก่อนบันทึก
- **บทบาทและสิทธิ์ผู้ใช้งาน (Role-Based Access Control)**:
  - `user`: ตรวจสอบสินทรัพย์, ดูรายละเอียด, Export CSV, พิมพ์ป้าย QR, ดู/ดาวน์โหลดเอกสาร PDF, แก้ไขโปรไฟล์
  - `admin`: เพิ่มสิทธิ์ Upload Excel, Update Excel (เทียบ Diff), โอนย้ายสินทรัพย์ (Transfer), อัปโหลด/ลบเอกสาร PDF, ดู Activity Logs
  - `super_admin`: เพิ่มสิทธิ์จัดการผู้ใช้งาน (Users), จัดการแผนก (Departments), จัดการหมวดหมู่ (Categories)
