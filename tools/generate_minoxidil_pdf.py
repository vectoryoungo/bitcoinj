from pathlib import Path

from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


OUTPUT_PATH = Path("/workspace/minoxidil_report.pdf")
FONT_PATH = "/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf"


TITLE = "米诺地尔酊作用机理、毒性与头皮使用分析"

SECTIONS = [
    (
        "一、药物组成说明",
        [
            "你提供的成分里“磷酸二氢钾氢，氧化钠缓冲液”大概率是转述误差，常见写法通常是：米诺地尔、丙二醇、乙醇、磷酸二氢钾/氢氧化钠缓冲液。",
            "如果规格是 30 mL:1.5 g，则属于 5% 米诺地尔酊，也就是每 1 mL 含约 50 mg 米诺地尔。",
        ],
    ),
    (
        "二、作用机理",
        [
            "米诺地尔原本是降压药，外用于脱发时的主要作用包括：延长毛囊生长期、促进微小化毛囊增大、改善毛囊周围微循环，以及可能通过钾离子通道和 VEGF 等相关通路促进毛发生长。",
            "它更接近“维持和刺激毛发生长”，不是根治脱发。通常需要连续使用 3 到 6 个月才能评估效果，停药后数月可能再次脱落。",
        ],
    ),
    (
        "三、各成分作用与风险",
        [
            "米诺地尔：有效成分，负责促进毛发生长；局部可引起瘙痒、红斑、脱屑，吸收过多时可导致低血压、心悸、水肿。",
            "丙二醇：溶剂和助渗剂，帮助米诺地尔溶解并进入皮肤；较常见问题是刺激和接触性皮炎。",
            "乙醇：溶剂，帮助快速挥发；主要风险是刺激、干燥和易燃。",
            "磷酸二氢钾/氢氧化钠缓冲液：用于调节 pH 和提高稳定性；成品中通常不是主要毒性来源，但 pH 异常时会增加刺激性。",
        ],
    ),
    (
        "四、毒性重点",
        [
            "最需要警惕的成分是米诺地尔。正常外用在完整头皮上时，全身吸收通常较低；但如果头皮破损、发炎、晒伤，或与增强渗透的产品同用，吸收会增加。",
            "米诺地尔误服可引起低血压、反射性心动过速、头晕、乏力、水肿，严重时可致休克。",
            "5% 米诺地尔酊的换算方式为：1 mL 约含 50 mg 米诺地尔，2 mL 约 100 mg，10 mL 约 500 mg，30 mL 约 1500 mg。",
            "文献中的严重中毒多见于较大体积误服，例如 60 mL 的 5% 溶液约为 3000 mg，120 mL 的 5% 溶液约为 6000 mg，可导致严重循环抑制和休克。",
            "儿童对误服更敏感，不能套用成人耐受量。宠物尤其是猫狗对米诺地尔也非常敏感，应严格避免接触。",
        ],
    ),
    (
        "五、哪些成分更容易带来不良反应",
        [
            "米诺地尔：是临床意义上最重要的毒性成分，尤其在误服或吸收过量时。",
            "丙二醇：系统毒性通常较低，但更容易引发局部刺激、红斑和过敏样反应。",
            "乙醇：外用主要体现为干燥和刺激，误服时则另有酒精毒性风险。",
            "氢氧化钠：原料本身有腐蚀性，但在合格成品中通常仅用于调 pH，不是主要中毒来源。",
        ],
    ),
    (
        "六、与哪些成分或情况一起更容易“出问题”",
        [
            "与强氧化剂同用：如过氧化氢、漂发剂、某些染发氧化剂、过氧化苯甲酰等，可能增加降解和刺激。",
            "与强酸、强碱环境接触：可能改变配方 pH，影响稳定性并增强刺激。",
            "与维 A 酸、果酸、水杨酸、强去角质产品同用：会破坏角质层并增加米诺地尔经皮吸收和刺痛感。",
            "与微针、滚针、头皮磨砂同天使用：会显著增加吸收与系统副作用风险。",
            "在头皮破损、感染、晒伤、炎症活跃期使用：会明显增加局部刺激和全身吸收。",
            "与高酒精头皮液、刺激性精油、生发刺激液叠加：更容易诱发接触性皮炎。",
        ],
    ),
    (
        "七、是否适合用于头皮",
        [
            "结论是：适合，但前提是按说明用于完整头皮。",
            "适用条件包括：头皮没有破损、红肿、感染或明显疼痛；按规定剂量和频次使用；涂后洗手；避免流到面部和其他不希望长毛的部位。",
            "如果对丙二醇较敏感，可能会觉得酊剂刺激更明显，可考虑咨询医生是否改用泡沫剂型。",
        ],
    ),
    (
        "八、不太适合自行使用的人群",
        [
            "孕妇、哺乳期人群、18 岁以下、头皮存在明显炎症或感染者、有低血压或心律失常或心衰病史者，应先咨询医生。",
            "如果脱发类型并不典型，例如斑秃、瘢痕性脱发、突然短期大量脱发，也不建议只靠米诺地尔自行处理。",
        ],
    ),
    (
        "九、出现以下情况应立即停用并就医",
        [
            "胸闷、胸痛、明显心悸、头晕欲晕、手脚肿胀、短期体重异常增加、呼吸不适、头皮大面积红肿渗液或严重皮疹。",
            "若发生误服，尤其是儿童误服，应立即联系急救或中毒咨询中心处理。",
        ],
    ),
    (
        "十、简要结论",
        [
            "米诺地尔酊是标准的头皮外用脱发药，主要价值在于延长毛囊生长期和维持毛发生长。",
            "真正需要重点防范的是两类风险：一是局部刺激或过敏，常与丙二醇和乙醇有关；二是在破损头皮上吸收增加或误服时出现的米诺地尔系统毒性。",
            "如果按说明在完整头皮上使用，通常是可以应用于头皮的；但不应在受损头皮、微针后、强去角质后或儿童可能误触误服的环境中随意使用。",
        ],
    ),
]


def build_pdf() -> None:
    pdfmetrics.registerFont(TTFont("ChineseFont", FONT_PATH))

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "TitleCN",
        parent=styles["Title"],
        fontName="ChineseFont",
        fontSize=18,
        leading=24,
        alignment=TA_LEFT,
        spaceAfter=10,
    )
    heading_style = ParagraphStyle(
        "HeadingCN",
        parent=styles["Heading2"],
        fontName="ChineseFont",
        fontSize=13,
        leading=18,
        spaceBefore=8,
        spaceAfter=6,
    )
    body_style = ParagraphStyle(
        "BodyCN",
        parent=styles["BodyText"],
        fontName="ChineseFont",
        fontSize=10.5,
        leading=16,
        spaceAfter=4,
    )

    doc = SimpleDocTemplate(
        str(OUTPUT_PATH),
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
        title=TITLE,
        author="OpenAI",
    )

    story = [Paragraph(TITLE, title_style), Spacer(1, 4)]
    for heading, paragraphs in SECTIONS:
        story.append(Paragraph(heading, heading_style))
        for item in paragraphs:
            story.append(Paragraph(item, body_style))
        story.append(Spacer(1, 4))

    doc.build(story)


if __name__ == "__main__":
    build_pdf()
