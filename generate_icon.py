"""Generates the Mindful Path app icon as a PNG."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPainter, QColor, QFont, QPixmap, QRadialGradient, QPen
from PyQt6.QtCore import Qt, QRectF

app = QApplication.instance() or QApplication(sys.argv)

def draw_icon(size: int) -> QPixmap:
    px = QPixmap(size, size)
    px.fill(Qt.GlobalColor.transparent)

    p = QPainter(px)
    p.setRenderHint(QPainter.RenderHint.Antialiasing)

    # Soft warm background — deep brown to muted saffron
    grad = QRadialGradient(size * 0.42, size * 0.38, size * 0.62)
    grad.setColorAt(0.0, QColor("#c87808"))
    grad.setColorAt(0.6, QColor("#9a5c06"))
    grad.setColorAt(1.0, QColor("#6e3e04"))
    p.setBrush(grad)
    p.setPen(Qt.PenStyle.NoPen)
    p.drawEllipse(1, 1, size - 2, size - 2)

    # Very subtle dark rim
    pen = QPen(QColor(0, 0, 0, 30))
    pen.setWidth(max(1, size // 48))
    p.setPen(pen)
    p.setBrush(Qt.BrushStyle.NoBrush)
    p.drawEllipse(1, 1, size - 2, size - 2)

    # Dharma wheel — slightly warm white, not pure white
    p.setPen(Qt.PenStyle.NoPen)
    font = QFont("Noto Sans", max(8, int(size * 0.56)))
    p.setFont(font)
    p.setPen(QColor(255, 240, 210, 210))
    p.drawText(QRectF(0, 0, size, size * 1.05), Qt.AlignmentFlag.AlignCenter, "☸")

    p.end()
    return px

for size in (16, 32, 48, 64, 128, 256):
    px = draw_icon(size)
    out_dir = os.path.expanduser("~/.local/share/icons/hicolor")
    icon_dir = os.path.join(out_dir, f"{size}x{size}", "apps")
    os.makedirs(icon_dir, exist_ok=True)
    path = os.path.join(icon_dir, "mindful-path.png")
    px.save(path, "PNG")
    print(f"  Saved {size}x{size} → {path}")

# Project copy
project_icon = os.path.join(os.path.dirname(__file__), "resources", "icon.png")
draw_icon(256).save(project_icon, "PNG")
print(f"  Saved project icon → {project_icon}")
print("Done.")
