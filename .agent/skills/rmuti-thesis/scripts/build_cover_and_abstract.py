# -*- coding: utf-8 -*-
"""
Script to generate:
1. output/Asset_ปก.docx (ปกนอก, ปกในภาษาไทย, ปกในภาษาอังกฤษ, ใบรับรองปริญญานิพนธ์)
2. output/Asset_บทคัดย่อ.docx (บทคัดย่อภาษาไทย, Abstract ภาษาอังกฤษ)

Compliant with RMUTI Thesis Guideline (พ.ศ. 2566)
"""

import os
import sys
import docx
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
TEMPLATE = os.path.join(ROOT, "input", "reference", "rmuti_thesis_template.docx")
OUTPUT_DIR = os.path.join(ROOT, "output")


def mark_thai(run, font_name="TH SarabunPSK", size_pt=16, bold=False, italic=False):
    """Ensure font, size, and complex script tags are strictly compliant with Word's Thai Uniscribe engine."""
    run.font.name = font_name
    run.font.size = Pt(size_pt)
    run.bold = bold
    run.italic = italic

    rPr = run._r.get_or_add_rPr()

    # Clear previous rFonts, cs, lang if any
    for tag in ("w:rFonts", "w:cs", "w:lang", "w:szCs", "w:bCs", "w:iCs"):
        for old in rPr.findall(qn(tag)):
            rPr.remove(old)

    fonts = OxmlElement("w:rFonts")
    fonts.set(qn("w:ascii"), font_name)
    fonts.set(qn("w:hAnsi"), font_name)
    fonts.set(qn("w:cs"), font_name)
    fonts.set(qn("w:hint"), "cs")
    rPr.insert(0, fonts)

    szCs = OxmlElement("w:szCs")
    szCs.set(qn("w:val"), str(int(size_pt * 2)))
    rPr.append(szCs)

    if bold:
        rPr.append(OxmlElement("w:bCs"))
    if italic:
        rPr.append(OxmlElement("w:iCs"))

    lang = OxmlElement("w:lang")
    lang.set(qn("w:val"), "en-US")
    lang.set(qn("w:eastAsia"), "en-US")
    lang.set(qn("w:bidi"), "th-TH")
    rPr.append(OxmlElement("w:cs"))
    rPr.append(lang)


def set_p_thai_distribute(p):
    """Set paragraph alignment to thaiDistribute."""
    pPr = p._p.get_or_add_pPr()
    jc = pPr.find(qn("w:jc"))
    if jc is not None:
        pPr.remove(jc)
    new_jc = OxmlElement("w:jc")
    new_jc.set(qn("w:val"), "thaiDistribute")
    pPr.append(new_jc)


def set_p_format(p, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=0, space_after=0, line_spacing=1.0, first_line_indent_cm=0.0):
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    if first_line_indent_cm > 0:
        p.paragraph_format.first_line_indent = Cm(first_line_indent_cm)


def remove_table_borders(table):
    tblPr = table._tbl.tblPr
    tblBorders = tblPr.find(qn("w:tblBorders"))
    if tblBorders is not None:
        tblPr.remove(tblBorders)
    new_borders = OxmlElement("w:tblBorders")
    for b_name in ("top", "left", "bottom", "right", "insideH", "insideV"):
        b = OxmlElement(f"w:{b_name}")
        b.set(qn("w:val"), "none")
        b.set(qn("w:sz"), "0")
        b.set(qn("w:space"), "0")
        b.set(qn("w:color"), "auto")
        new_borders.append(b)
    tblPr.append(new_borders)


def add_tab_run(p):
    r = p.add_run()
    rPr = r._r.get_or_add_rPr()
    rPr.append(OxmlElement("w:tab"))


def add_blank_lines(doc, count=1, size_pt=16):
    for _ in range(count):
        p = doc.add_paragraph()
        set_p_format(p, space_before=0, space_after=0, line_spacing=1.0)
        r = p.add_run()
        mark_thai(r, size_pt=size_pt)


def create_cover_docx():
    print("Creating Asset_ปก.docx...")
    doc = docx.Document(TEMPLATE)
    for el in list(doc.element.body):
        if el.tag != qn("w:sectPr"):
            doc.element.body.remove(el)

    # ==========================================
    # SECTION 1: ปกนอก (Outer Cover)
    # Margins: Top 2.54, Left 2.54, Right 2.54, Bottom 2.54 cm
    # ==========================================
    sec0 = doc.sections[0]
    sec0.top_margin = Cm(2.54)
    sec0.bottom_margin = Cm(2.54)
    sec0.left_margin = Cm(2.54)
    sec0.right_margin = Cm(2.54)
    sec0.different_first_page_header_footer = False
    sec0.header.is_linked_to_previous = False
    for hp in sec0.header.paragraphs:
        hp.text = ""

    # ชื่อเรื่องภาษาไทย (20pt Bold Center)
    p_title_th = doc.add_paragraph()
    set_p_format(p_title_th, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=12, space_after=0)
    r1 = p_title_th.add_run("ระบบบริหารจัดการสินทรัพย์")
    mark_thai(r1, size_pt=20, bold=True)

    # ชื่อเรื่องภาษาอังกฤษ (20pt Bold Center)
    p_title_en = doc.add_paragraph()
    set_p_format(p_title_en, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=6, space_after=0)
    r2 = p_title_en.add_run("ASSET MANAGEMENT WEB APPLICATION")
    mark_thai(r2, size_pt=20, bold=True)

    # เว้นระยะห่างก่อนชื่อผู้เขียน
    add_blank_lines(doc, count=7, size_pt=16)

    # ผู้เขียนปริญญานิพนธ์ (18pt Bold Center) - จัดตาราง 2 คอลัมน์ไม่มีขอบ ชิดกึ่งกลาง
    table_authors = doc.add_table(rows=3, cols=2)
    table_authors.alignment = WD_TABLE_ALIGNMENT.CENTER
    remove_table_borders(table_authors)

    authors_data = [
        ("นายอดิเทพ", "สิทธิโสภา"),
        ("นายนครินทร์", "มานิล"),
        ("นายวีระพล", "สังข์ทอง")
    ]
    for row_idx, (fname, sname) in enumerate(authors_data):
        cell_f = table_authors.rows[row_idx].cells[0]
        cell_s = table_authors.rows[row_idx].cells[1]
        cell_f.width = Cm(5.0)
        cell_s.width = Cm(5.0)
        
        pf = cell_f.paragraphs[0]
        set_p_format(pf, align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=2, space_after=2)
        rf = pf.add_run(fname)
        mark_thai(rf, size_pt=18, bold=True)

        ps = cell_s.paragraphs[0]
        set_p_format(ps, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=2, space_after=2)
        rs = ps.add_run("   " + sname)
        mark_thai(rs, size_pt=18, bold=True)

    # เว้นระยะห่างก่อนส่วนท้ายปก
    add_blank_lines(doc, count=8, size_pt=16)

    # ส่วนท้ายปกนอก (16pt Bold Center)
    footer_texts = [
        "ปริญญานิพนธ์นี้เป็นส่วนหนึ่งของการศึกษาตามหลักสูตรปริญญาวิศวกรรมศาสตรบัณฑิต",
        "สาขาวิชาวิศวกรรมคอมพิวเตอร์",
        "คณะวิศวกรรมศาสตร์ มหาวิทยาลัยเทคโนโลยีราชมงคลอีสาน วิทยาเขตขอนแก่น",
        "พ.ศ. 2568",
        "ลิขสิทธิ์ของคณะวิศวกรรมศาสตร์ มหาวิทยาลัยเทคโนโลยีราชมงคลอีสาน"
    ]
    for ftxt in footer_texts:
        p_ft = doc.add_paragraph()
        set_p_format(p_ft, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=1, space_after=1)
        r = p_ft.add_run(ftxt)
        mark_thai(r, size_pt=16, bold=True)

    # ==========================================
    # SECTION 2: ปกในภาษาไทย (Inner Cover TH)
    # Margins: Top 2.54, Left 3.81, Right 2.54, Bottom 2.54 cm
    # ==========================================
    sec1 = doc.add_section(docx.enum.section.WD_SECTION.NEW_PAGE)
    sec1.top_margin = Cm(2.54)
    sec1.bottom_margin = Cm(2.54)
    sec1.left_margin = Cm(3.81)
    sec1.right_margin = Cm(2.54)
    sec1.header.is_linked_to_previous = False
    for hp in sec1.header.paragraphs:
        hp.text = ""

    p_in_th = doc.add_paragraph()
    set_p_format(p_in_th, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=14, space_after=0)
    r = p_in_th.add_run("ระบบบริหารจัดการสินทรัพย์")
    mark_thai(r, size_pt=18, bold=True)

    add_blank_lines(doc, count=8, size_pt=16)

    t_in_th = doc.add_table(rows=3, cols=2)
    t_in_th.alignment = WD_TABLE_ALIGNMENT.CENTER
    remove_table_borders(t_in_th)
    for row_idx, (fname, sname) in enumerate(authors_data):
        cell_f = t_in_th.rows[row_idx].cells[0]
        cell_s = t_in_th.rows[row_idx].cells[1]
        cell_f.width = Cm(4.5)
        cell_s.width = Cm(4.5)
        
        pf = cell_f.paragraphs[0]
        set_p_format(pf, align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=2, space_after=2)
        rf = pf.add_run(fname)
        mark_thai(rf, size_pt=16, bold=False)

        ps = cell_s.paragraphs[0]
        set_p_format(ps, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=2, space_after=2)
        rs = ps.add_run("   " + sname)
        mark_thai(rs, size_pt=16, bold=False)

    add_blank_lines(doc, count=9, size_pt=16)

    for ftxt in footer_texts:
        p_ft = doc.add_paragraph()
        set_p_format(p_ft, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=1, space_after=1)
        r = p_ft.add_run(ftxt)
        mark_thai(r, size_pt=16, bold=False)

    # ==========================================
    # SECTION 3: ปกในภาษาอังกฤษ (Inner Cover EN)
    # Margins: Top 2.54, Left 3.81, Right 2.54, Bottom 2.54 cm
    # ==========================================
    sec2 = doc.add_section(docx.enum.section.WD_SECTION.NEW_PAGE)
    sec2.top_margin = Cm(2.54)
    sec2.bottom_margin = Cm(2.54)
    sec2.left_margin = Cm(3.81)
    sec2.right_margin = Cm(2.54)
    sec2.header.is_linked_to_previous = False
    for hp in sec2.header.paragraphs:
        hp.text = ""

    p_in_en = doc.add_paragraph()
    set_p_format(p_in_en, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=14, space_after=0)
    r = p_in_en.add_run("Asset Management Web Application")
    mark_thai(r, size_pt=18, bold=True)

    add_blank_lines(doc, count=8, size_pt=16)

    t_in_en = doc.add_table(rows=3, cols=2)
    t_in_en.alignment = WD_TABLE_ALIGNMENT.CENTER
    remove_table_borders(t_in_en)
    authors_en = [
        ("Mr. Adithep", "Sitthisopa"),
        ("Mr. Nakharin", "Manin"),
        ("Mr. Weeraphon", "Sangthong")
    ]
    for row_idx, (fname, sname) in enumerate(authors_en):
        cell_f = t_in_en.rows[row_idx].cells[0]
        cell_s = t_in_en.rows[row_idx].cells[1]
        cell_f.width = Cm(4.5)
        cell_s.width = Cm(4.5)
        
        pf = cell_f.paragraphs[0]
        set_p_format(pf, align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=2, space_after=2)
        rf = pf.add_run(fname)
        mark_thai(rf, size_pt=16, bold=False)

        ps = cell_s.paragraphs[0]
        set_p_format(ps, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=2, space_after=2)
        rs = ps.add_run("   " + sname)
        mark_thai(rs, size_pt=16, bold=False)

    add_blank_lines(doc, count=8, size_pt=16)

    en_footer_texts = [
        "A Report Submitted in Partial Fulfillment of the Requirements for",
        "the Degree of Bachelor of Engineering",
        "Department of Computer Engineering, Faculty of Engineering",
        "Rajamangala University of Technology Isan, Khon Kaen Campus",
        "2025",
        "© Faculty of Engineering, Rajamangala University of Technology Isan"
    ]
    for ftxt in en_footer_texts:
        p_ft = doc.add_paragraph()
        set_p_format(p_ft, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=1, space_after=1)
        r = p_ft.add_run(ftxt)
        mark_thai(r, size_pt=16, bold=False)

    # ==========================================
    # SECTION 4: ใบรับรองปริญญานิพนธ์ (Certification Page)
    # Margins: Top 8.00 cm, Left 3.81, Right 2.54, Bottom 2.54 cm
    # ==========================================
    sec3 = doc.add_section(docx.enum.section.WD_SECTION.NEW_PAGE)
    sec3.top_margin = Cm(8.00)
    sec3.bottom_margin = Cm(2.54)
    sec3.left_margin = Cm(3.81)
    sec3.right_margin = Cm(2.54)
    sec3.header.is_linked_to_previous = False
    for hp in sec3.header.paragraphs:
        hp.text = ""

    cert_info = [
        ("หัวข้อปริญญานิพนธ์", "ระบบบริหารจัดการสินทรัพย์"),
        ("จัดทำโดย", "นายอดิเทพ  สิทธิโสภา,  นายนครินทร์  มานิล  และนายวีระพล  สังข์ทอง"),
        ("สาขาวิชา", "วิศวกรรมคอมพิวเตอร์"),
        ("ประธานที่ปรึกษา", "ผู้ช่วยศาสตราจารย์ ดร.อติราช สุขสวัสดิ์")
    ]
    for label, val in cert_info:
        p = doc.add_paragraph()
        set_p_format(p, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=0, space_after=0)
        r_lbl = p.add_run(f"{label} \t:\t")
        mark_thai(r_lbl, size_pt=16, bold=False)
        r_val = p.add_run(val)
        mark_thai(r_val, size_pt=16, bold=False)

    add_blank_lines(doc, count=1, size_pt=16)

    p_approve = doc.add_paragraph()
    set_p_format(p_approve, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=4, space_after=0)
    p_approve.paragraph_format.first_line_indent = Cm(1.8)
    r_app = p_approve.add_run("ได้รับอนุมัติให้เป็นส่วนหนึ่งของการศึกษาตามหลักสูตรปริญญาวิศวกรรมศาสตรบัณฑิต คณะวิศวกรรมศาสตร์ มหาวิทยาลัยเทคโนโลยีราชมงคลอีสาน วิทยาเขตขอนแก่น")
    mark_thai(r_app, size_pt=16, bold=False)
    set_p_thai_distribute(p_approve)

    add_blank_lines(doc, count=1, size_pt=16)

    p_dean1 = doc.add_paragraph()
    set_p_format(p_dean1, align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=0)
    r_d1 = p_dean1.add_run("…………………………………………………… คณบดีคณะวิศวกรรมศาสตร์")
    mark_thai(r_d1, size_pt=16, bold=False)

    p_dean2 = doc.add_paragraph()
    set_p_format(p_dean2, align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=0)
    r_d2 = p_dean2.add_run("(ผู้ช่วยศาสตราจารย์ ดร.ศุภฤกษ์  ชามงคลประดิษฐ์) วันที่.........เดือน....................พ.ศ. ..........")
    mark_thai(r_d2, size_pt=16, bold=False)

    add_blank_lines(doc, count=1, size_pt=16)

    p_comm_title = doc.add_paragraph()
    set_p_format(p_comm_title, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=2, space_after=2)
    r_ct = p_comm_title.add_run("คณะกรรมการสอบปริญญานิพนธ์")
    mark_thai(r_ct, size_pt=16, bold=True)

    # คณะกรรมการสอบ: 2 คอลัมน์
    t_comm = doc.add_table(rows=4, cols=2)
    t_comm.alignment = WD_TABLE_ALIGNMENT.CENTER
    remove_table_borders(t_comm)

    comm_data = [
        ("................................................ ประธานกรรมการสอบ", "................................................ ประธานที่ปรึกษา"),
        ("(อาจารย์ ดร.ปิยะนุช ตั้งกิตติพล)", "(ผู้ช่วยศาสตราจารย์ ดร.อติราช สุขสวัสดิ์)"),
        ("................................................ กรรมการสอบ", "................................................ กรรมการสอบ"),
        ("(อาจารย์ ดร.ประภาส ผ่องสนาม)", "(ผู้ช่วยศาสตราจารย์ ดร.อติราช สุขสวัสดิ์)")
    ]

    for row_idx, (col1_txt, col2_txt) in enumerate(comm_data):
        c1 = t_comm.rows[row_idx].cells[0]
        c2 = t_comm.rows[row_idx].cells[1]
        c1.width = Cm(7.2)
        c2.width = Cm(7.2)
        
        p1 = c1.paragraphs[0]
        set_p_format(p1, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=1, space_after=1)
        r1 = p1.add_run(col1_txt)
        mark_thai(r1, size_pt=15, bold=False)

        p2 = c2.paragraphs[0]
        set_p_format(p2, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=1, space_after=1)
        r2 = p2.add_run(col2_txt)
        mark_thai(r2, size_pt=15, bold=False)

    out_file = os.path.join(OUTPUT_DIR, "Asset_ปก.docx")
    doc.save(out_file)
    print("Saved:", out_file)


def create_abstract_docx():
    print("Creating Asset_บทคัดย่อ.docx...")
    doc = docx.Document(TEMPLATE)
    for el in list(doc.element.body):
        if el.tag != qn("w:sectPr"):
            doc.element.body.remove(el)

    # ==========================================
    # SECTION 1: บทคัดย่อภาษาไทย
    # Margins: Top 3.81, Left 3.81, Right 2.54, Bottom 2.54 cm
    # Header: "ง" at top-right (2.54 cm from top)
    # ==========================================
    sec0 = doc.sections[0]
    sec0.top_margin = Cm(3.81)
    sec0.bottom_margin = Cm(2.54)
    sec0.left_margin = Cm(3.81)
    sec0.right_margin = Cm(2.54)
    sec0.header_distance = Cm(2.54)
    sec0.different_first_page_header_footer = False
    sec0.header.is_linked_to_previous = False
    
    hp0 = sec0.header.paragraphs[0]
    set_p_format(hp0, align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=0)
    r_num_th = hp0.add_run("ง")
    mark_thai(r_num_th, size_pt=16, bold=False)

    # ข้อมูลโครงงาน
    info_th = [
        ("หัวข้อปริญญานิพนธ์", "\tระบบบริหารจัดการสินทรัพย์"),
        ("จัดทำโดย", "\t\t\tนายอดิเทพ สิทธิโสภา, นายนครินทร์ มานิล และนายวีระพล สังข์ทอง"),
        ("ปีที่ปริญญานิพนธ์สำเร็จ", "\tพ.ศ. 2568"),
        ("สาขาวิชา", "\t\t\tวิศวกรรมคอมพิวเตอร์"),
        ("ประธานที่ปรึกษา", "\t\tผู้ช่วยศาสตราจารย์ ดร.อติราช สุขสวัสดิ์")
    ]
    for lbl, val in info_th:
        p = doc.add_paragraph()
        set_p_format(p, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=0, space_after=0)
        r_lbl = p.add_run(lbl)
        mark_thai(r_lbl, size_pt=16, bold=False)
        r_val = p.add_run(val)
        mark_thai(r_val, size_pt=16, bold=False)

    add_blank_lines(doc, count=2, size_pt=16)

    p_ab_th = doc.add_paragraph()
    set_p_format(p_ab_th, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=0)
    r_ab_th = p_ab_th.add_run("บทคัดย่อ")
    mark_thai(r_ab_th, size_pt=16, bold=True)

    add_blank_lines(doc, count=1, size_pt=16)

    # 3 ย่อหน้า (ย่อหน้า 1.8 ซม. / 1 tab, thaiDistribute, กระชับ จบใน 1 หน้าพอดี)
    p1_text = (
        "\tโครงงานนี้มีวัตถุประสงค์เพื่อพัฒนาระบบบริหารจัดการสินทรัพย์ (Asset Management) ในรูปแบบเว็บแอปพลิเคชัน สำหรับคณะแพทยศาสตร์ โรงพยาบาลศรีนครินทร์ มหาวิทยาลัยขอนแก่น เพื่อแก้ไขปัญหาข้อจำกัดของระบบเดิมที่จำกัดสิทธิ์การสืบค้นข้อมูลครุภัณฑ์เฉพาะแผนกพัสดุส่วนกลาง ทำให้บุคลากรแต่ละหน่วยงานไม่สามารถตรวจสอบสถานะครุภัณฑ์ในความดูแลได้โดยตรง เกิดความล่าช้าและขาดความคล่องตัวในการปฏิบัติงาน"
    )
    p1 = doc.add_paragraph()
    set_p_format(p1, space_before=0, space_after=0, line_spacing=1.0)
    set_p_thai_distribute(p1)
    r_p1 = p1.add_run(p1_text)
    mark_thai(r_p1, size_pt=16, bold=False)

    p2_text = (
        "\tระบบพัฒนาขึ้นบนสถาปัตยกรรมแบบจำลอง มุมมอง และตัวควบคุม (MVC) ร่วมกับการเรนเดอร์ฝั่งเซิร์ฟเวอร์ โดยใช้ Node.js, Express Framework, EJS และ Bootstrap 5 ผู้จัดทำรับผิดชอบพัฒนาส่วนต่อประสานผู้ใช้ (Frontend) รองรับการแสดงผลตารางครุภัณฑ์ขนาดใหญ่พร้อมระบบตรึงหัวตาราง (Sticky Header) ระบบนำเข้าและเปรียบเทียบผลต่างของข้อมูล Excel ระบบโอนย้ายครุภัณฑ์ระหว่างแผนกแบบกลุ่ม การสร้างและจัดพิมพ์ป้ายสติกเกอร์รหัสคิวอาร์ขนาด 70×24 มิลลิเมตร และรองรับโหมดกลางคืน (Dark Mode)"
    )
    p2 = doc.add_paragraph()
    set_p_format(p2, space_before=0, space_after=0, line_spacing=1.0)
    set_p_thai_distribute(p2)
    r_p2 = p2.add_run(p2_text)
    mark_thai(r_p2, size_pt=16, bold=False)

    p3_text = (
        "\tผลการดำเนินงานพบว่า ระบบเว็บแอปพลิเคชันทำงานได้อย่างมีเสถียรภาพและมีความพร้อมสำหรับการนำไปติดตั้งใช้งานจริง ผ่านการทดสอบฟังก์ชันการทำงานครบถ้วนทั้ง 80 กรณีทดสอบ (ร้อยละ 100) ส่วนต่อประสานผู้ใช้ตอบสนองได้อย่างราบรื่น การแสดงผลตารางขนาดใหญ่และการเปรียบเทียบข้อมูลมีความแม่นยำ และจัดพิมพ์ป้ายรหัสคิวอาร์ได้ตรงตามขนาดจริง ช่วยลดภาระงานของเจ้าหน้าที่พัสดุและเพิ่มความโปร่งใสในการตรวจสอบสินทรัพย์ของหน่วยงานได้อย่างเป็นรูปธรรม"
    )
    p3 = doc.add_paragraph()
    set_p_format(p3, space_before=0, space_after=0, line_spacing=1.0)
    set_p_thai_distribute(p3)
    r_p3 = p3.add_run(p3_text)
    mark_thai(r_p3, size_pt=16, bold=False)

    add_blank_lines(doc, count=1, size_pt=16)

    p_kw_th = doc.add_paragraph()
    set_p_format(p_kw_th, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=0, space_after=0)
    r_kwt = p_kw_th.add_run("คำสำคัญ\t\t:  ")
    mark_thai(r_kwt, size_pt=16, bold=True)
    r_kwv = p_kw_th.add_run("ระบบบริหารจัดการสินทรัพย์, ครุภัณฑ์, ส่วนต่อประสานผู้ใช้, รหัสคิวอาร์, โรงพยาบาลศรีนครินทร์")
    mark_thai(r_kwv, size_pt=16, bold=False)

    # ==========================================
    # SECTION 2: Abstract ภาษาอังกฤษ
    # Margins: Top 3.81, Left 3.81, Right 2.54, Bottom 2.54 cm
    # Header: "จ" at top-right (2.54 cm from top)
    # ==========================================
    sec1 = doc.add_section(docx.enum.section.WD_SECTION.NEW_PAGE)
    sec1.top_margin = Cm(3.81)
    sec1.bottom_margin = Cm(2.54)
    sec1.left_margin = Cm(3.81)
    sec1.right_margin = Cm(2.54)
    sec1.header_distance = Cm(2.54)
    sec1.header.is_linked_to_previous = False

    hp1 = sec1.header.paragraphs[0]
    set_p_format(hp1, align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=0)
    r_num_en = hp1.add_run("จ")
    mark_thai(r_num_en, size_pt=16, bold=False)

    info_en = [
        ("Project Title", "\tAsset Management Web Application"),
        ("Proposed by", "\tMr. Adithep Sitthisopa, Mr. Nakharin Manin, and Mr. Weeraphon Sangthong"),
        ("Year", "\t\t2025"),
        ("Department", "\tComputer Engineering"),
        ("Advisor", "\t\tAssistant Professor Atirarj Suksawad, D.Eng.")
    ]
    for lbl, val in info_en:
        p = doc.add_paragraph()
        set_p_format(p, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=0, space_after=0)
        r_lbl = p.add_run(lbl)
        mark_thai(r_lbl, size_pt=16, bold=False)
        r_val = p.add_run(val)
        mark_thai(r_val, size_pt=16, bold=False)

    add_blank_lines(doc, count=2, size_pt=16)

    p_ab_en = doc.add_paragraph()
    set_p_format(p_ab_en, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=0)
    r_ab_en = p_ab_en.add_run("Abstract")
    mark_thai(r_ab_en, size_pt=16, bold=True)

    add_blank_lines(doc, count=1, size_pt=16)

    p1_en_text = (
        "\tThis project aims to develop a Web-Based Asset Management System for the Faculty of Medicine, Srinagarind Hospital, Khon Kaen University. The system resolves operational bottlenecks in the existing workflow, where asset inquiry was restricted exclusively to central procurement personnel, preventing departmental staff from directly accessing real-time equipment status and causing unnecessary operational delays."
    )
    p1_en = doc.add_paragraph()
    set_p_format(p1_en, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=0, space_after=0, line_spacing=1.0)
    r_p1_en = p1_en.add_run(p1_en_text)
    mark_thai(r_p1_en, size_pt=16, bold=False)

    p2_en_text = (
        "\tThe system was developed under the Model-View-Controller (MVC) architecture with Server-Side Rendering (SSR) utilizing Node.js, Express Framework, EJS, and Bootstrap 5. The implementation specifically focused on the Frontend User Interface, featuring a 25-column asset table with sticky header pinning, an Excel data update and difference comparison preview, a bulk inter-departmental asset transfer modal, dynamic QR code generation with standard 70×24 mm sticker label printing, and seamless dark mode support."
    )
    p2_en = doc.add_paragraph()
    set_p_format(p2_en, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=0, space_after=0, line_spacing=1.0)
    r_p2_en = p2_en.add_run(p2_en_text)
    mark_thai(r_p2_en, size_pt=16, bold=False)

    p3_en_text = (
        "\tThe evaluation results demonstrate that the web application operates stably and is production-ready, successfully achieving a 100% pass rate across all 80 functional test cases. The user interface delivers smooth responsiveness, high data precision in large-scale table rendering, and accurate label formatting. The system significantly alleviates the workload of procurement staff and provides tangible efficiency improvements for institutional asset tracking."
    )
    p3_en = doc.add_paragraph()
    set_p_format(p3_en, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=0, space_after=0, line_spacing=1.0)
    r_p3_en = p3_en.add_run(p3_en_text)
    mark_thai(r_p3_en, size_pt=16, bold=False)

    add_blank_lines(doc, count=1, size_pt=16)

    p_kw_en = doc.add_paragraph()
    set_p_format(p_kw_en, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=0, space_after=0)
    r_kwe = p_kw_en.add_run("Keywords\t:  ")
    mark_thai(r_kwe, size_pt=16, bold=True)
    r_kwe_val = p_kw_en.add_run("Asset Management System, Medical Equipment, Frontend User Interface, QR Code, Srinagarind Hospital")
    mark_thai(r_kwe_val, size_pt=16, bold=False)

    out_file = os.path.join(OUTPUT_DIR, "Asset_บทคัดย่อ.docx")
    doc.save(out_file)
    print("Saved:", out_file)


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    create_cover_docx()
    create_abstract_docx()
