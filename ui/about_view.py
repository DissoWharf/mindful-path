from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QScrollArea, QFrame,
)
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication

PATH_ASPECTS = [
    ("Right View", "◉", "See clearly — understand how things truly are, without distortion or delusion. For students: approach your work and yourself with honesty and curiosity."),
    ("Right Intention", "◎", "Cultivate wholesome motivation. Study not to impress, but to genuinely understand. Act from kindness and compassion, not fear."),
    ("Right Speech", "◯", "Speak truthfully and kindly. In study groups, with professors, with yourself — words shape reality."),
    ("Right Action", "◈", "Act ethically and with care. Honor your body, your commitments, and those around you."),
    ("Right Livelihood", "◇", "Engage in work that doesn't harm others. Find meaning in what you study — connect your efforts to something larger."),
    ("Right Effort", "◆", "Cultivate consistent, balanced effort — not frantic bursts or lazy drifting. The Middle Way between burnout and avoidance."),
    ("Right Mindfulness", "✦", "Bring full, non-judgmental awareness to each moment — while studying, eating, resting. The mind that is present learns deeply."),
    ("Right Concentration", "☸", "Develop the capacity for sustained, deep focus. A calm, steady mind is the ground of all wisdom."),
]

PRINCIPLES = [
    ("Impermanence (Anicca)", "◦",
     "Everything changes — including your struggles, your grades, your mood. A missed day is not a broken self. Each morning is a fresh beginning."),
    ("The Middle Way", "〜",
     "Avoid extremes. Neither punishing perfectionism nor aimless drift — but a balanced, sustainable path of gentle consistency."),
    ("Non-Attachment", "◌",
     "Do the practice for its own sake, not for the outcome. Effort without clinging to results frees you from anxiety and deepens your learning."),
    ("Self-Compassion (Metta)", "♡",
     "Offer yourself the same kindness you would offer a dear friend. Criticism and guilt are poor teachers. Warmth and honesty are better ones."),
    ("Mindfulness", "☯",
     "The quality of full presence — awake to this moment, this breath, this page. It is both a practice and a way of being."),
    ("Interconnection", "∞",
     "You are not separate from those around you. Your growth ripples outward. Your struggles are shared by countless others on the same path."),
]

CATEGORIES = [
    ("Mind",  "◯", "#7c9cbf", "Meditation, awareness, and presence practices. The ground of clear seeing."),
    ("Body",  "◈", "#6ea87a", "Movement, nourishment, rest. The vessel must be cared for."),
    ("Study", "◎", "#c8790a", "Deep learning, focused effort, and the joy of understanding."),
    ("Heart", "♡", "#c86a7c", "Gratitude, kindness, connection. The practices that keep us human."),
    ("Path",  "☸", "#9c7cbc", "Intention, reflection, and alignment with your deepest values."),
]


class AboutView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._scroll = None
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        header = QWidget()
        header.setObjectName("view_header")
        h_layout = QHBoxLayout(header)
        h_layout.setContentsMargins(28, 20, 28, 20)
        title = QLabel("About")
        title.setObjectName("view_title")
        h_layout.addWidget(title)
        layout.addWidget(header)

        self._scroll = QScrollArea()
        self._scroll.setWidgetResizable(True)
        self._scroll.setFrameShape(QFrame.Shape.NoFrame)
        self._scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        layout.addWidget(self._scroll, 1)

        self._build_content()

    def refresh(self):
        self._build_content()

    def _build_content(self):
        dark = QApplication.palette().window().color().lightness() < 128

        title_col   = "#e8d8b8" if dark else "#2c2416"
        body_col    = "#c0a880" if dark else "#4a3a2a"
        muted_col   = "#7a6a52" if dark else "#7a6a5a"
        card_name   = "#d8c8a8" if dark else "#2c2416"
        card_desc   = "#907860" if dark else "#5a4a3a"
        section_col = "#6a5a42" if dark else "#9a8a78"

        content = QWidget()
        cl = QVBoxLayout(content)
        cl.setContentsMargins(28, 20, 28, 40)
        cl.setSpacing(20)
        self._scroll.setWidget(content)

        # ── Intro card ──────────────────────────────
        intro = QFrame()
        intro.setObjectName("reflect_card")
        il = QVBoxLayout(intro)
        il.setContentsMargins(24, 24, 24, 24)
        il.setSpacing(10)

        wheel = QLabel("☸")
        wheel.setStyleSheet("font-size: 34px; color: #c8790a;")
        wheel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        il.addWidget(wheel)

        app_name = QLabel("Mindful Path")
        app_name.setStyleSheet(f"font-size: 21px; font-weight: bold; color: {title_col};")
        app_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        il.addWidget(app_name)

        tagline = QLabel("A Daily Practice Tracker for Students")
        tagline.setStyleSheet(f"font-size: 12px; color: {muted_col};")
        tagline.setAlignment(Qt.AlignmentFlag.AlignCenter)
        il.addWidget(tagline)

        desc = QLabel(
            "Mindful Path helps you build a daily practice rooted in balance, "
            "awareness, and compassion. Inspired by Buddhist wisdom — without dogma "
            "or religion — it offers a gentle framework for the habits that support "
            "a student's deepest flourishing: mind, body, study, and heart.\n\n"
            "There are no penalties for missed days. Impermanence is built in. "
            "Each morning, the path begins again."
        )
        desc.setWordWrap(True)
        desc.setStyleSheet(f"color: {body_col}; font-size: 13px;")
        desc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        il.addWidget(desc)

        cl.addWidget(intro)

        # ── Eightfold Path ──────────────────────────
        self._section(cl, "THE NOBLE EIGHTFOLD PATH", section_col)

        sub = QLabel(
            "The Eightfold Path is not a checklist — it is eight facets of a single "
            "jewel, developed together. Each practice in Mindful Path is linked to one "
            "of these aspects as a gentle reminder of the deeper intention behind your habits."
        )
        sub.setWordWrap(True)
        sub.setStyleSheet(f"color: {muted_col}; font-size: 12px;")
        cl.addWidget(sub)

        for name, icon, desc_text in PATH_ASPECTS:
            cl.addWidget(self._card(icon, "#c8790a", name, desc_text,
                                    card_name, card_desc))

        # ── Core Principles ─────────────────────────
        self._section(cl, "CORE PRINCIPLES", section_col)

        for name, icon, desc_text in PRINCIPLES:
            cl.addWidget(self._card(icon, "#9c7cbc", name, desc_text,
                                    card_name, card_desc))

        # ── Categories ──────────────────────────────
        self._section(cl, "PRACTICE CATEGORIES", section_col)

        for cat, icon, color, desc_text in CATEGORIES:
            card = QFrame()
            card.setObjectName("habit_row")
            c_layout = QHBoxLayout(card)
            c_layout.setContentsMargins(14, 10, 14, 10)
            c_layout.setSpacing(12)

            bar = QFrame()
            bar.setFixedWidth(3)
            bar.setStyleSheet(f"background: {color}; border-radius: 2px;")
            c_layout.addWidget(bar)

            icon_lbl = QLabel(icon)
            icon_lbl.setStyleSheet(f"color: {color}; font-size: 15px;")
            icon_lbl.setFixedWidth(22)
            icon_lbl.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignCenter)
            c_layout.addWidget(icon_lbl)

            name_lbl = QLabel(f"<b>{cat}</b> — {desc_text}")
            name_lbl.setStyleSheet(f"color: {body_col}; font-size: 12px;")
            name_lbl.setWordWrap(True)
            c_layout.addWidget(name_lbl, 1)

            cl.addWidget(card)

        cl.addStretch()

    def _section(self, layout, text: str, color: str):
        lbl = QLabel(text)
        lbl.setStyleSheet(
            f"color: {color}; font-size: 11px; font-weight: bold; letter-spacing: 2px;"
        )
        lbl.setContentsMargins(0, 6, 0, 0)
        layout.addWidget(lbl)

    def _card(self, icon: str, icon_color: str, name: str, desc: str,
              name_col: str, desc_col: str) -> QFrame:
        card = QFrame()
        card.setObjectName("habit_row")
        c_layout = QHBoxLayout(card)
        c_layout.setContentsMargins(14, 12, 14, 12)
        c_layout.setSpacing(14)

        bar = QFrame()
        bar.setFixedWidth(3)
        bar.setStyleSheet(f"background: {icon_color}80; border-radius: 2px;")
        c_layout.addWidget(bar)

        icon_lbl = QLabel(icon)
        icon_lbl.setStyleSheet(f"color: {icon_color}; font-size: 16px;")
        icon_lbl.setFixedWidth(22)
        icon_lbl.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignCenter)
        c_layout.addWidget(icon_lbl)

        text_col = QVBoxLayout()
        text_col.setSpacing(3)

        name_lbl = QLabel(name)
        name_lbl.setStyleSheet(f"font-weight: bold; font-size: 13px; color: {name_col};")
        text_col.addWidget(name_lbl)

        desc_lbl = QLabel(desc)
        desc_lbl.setWordWrap(True)
        desc_lbl.setStyleSheet(f"color: {desc_col}; font-size: 12px;")
        text_col.addWidget(desc_lbl)

        c_layout.addLayout(text_col, 1)
        return card
