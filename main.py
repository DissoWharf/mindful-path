import sys
import os
import json
import time

from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon

from database import Database
from ui.main_window import MainWindow

LOG_PATH = "/home/justin/Documents/Claude/mindful_path/.cursor/debug-96e8b9.log"
SESSION_ID = "96e8b9"
RUN_ID = "close_pre"


def _log_ndjson(*, hypothesis_id: str, location: str, message: str, data: dict | None = None):
    payload = {
        "sessionId": SESSION_ID,
        "runId": RUN_ID,
        "hypothesisId": hypothesis_id,
        "location": location,
        "message": message,
        "data": data or {},
        "timestamp": int(time.time() * 1000),
    }
    # Best-effort logging; do not affect app behavior if logging fails.
    try:
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(payload, ensure_ascii=True) + "\n")
    except Exception:
        pass


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Mindful Path")
    app.setOrganizationName("MindfulPath")
    app.setStyle("Fusion")

    try:
        _qotlwc = app.quitOnLastWindowClosed()
    except Exception:
        # Some PyQt versions expose this differently; best-effort only.
        _qotlwc = None

    # #region agent log
    _log_ndjson(
        hypothesis_id="H5",
        location="main.py:startup",
        message="quit_on_last_window_closed_value",
        data={"quitOnLastWindowClosed": _qotlwc},
    )
    # #endregion

    # Load stylesheet
    style_path = os.path.join(os.path.dirname(__file__), "resources", "style.qss")
    if os.path.exists(style_path):
        with open(style_path, "r") as f:
            app.setStyleSheet(f.read())

    db = Database()
    db.initialize()

    window = MainWindow(db)
    window.show()

    # #region agent log
    app.lastWindowClosed.connect(
        lambda: _log_ndjson(
            hypothesis_id="H3",
            location="main.py:lastWindowClosed",
            message="last_window_closed_signal",
        )
    )
    # #endregion

    # #region agent log
    app.aboutToQuit.connect(
        lambda: _log_ndjson(
            hypothesis_id="H2",
            location="main.py:aboutToQuit",
            message="about_to_quit_signal",
        )
    )
    # #endregion

    rc = app.exec()
    # #region agent log
    _log_ndjson(
        hypothesis_id="H2",
        location="main.py:app_exec_return",
        message="app_exec_return",
        data={"rc": rc},
    )
    # #endregion
    sys.exit(rc)


if __name__ == "__main__":
    main()
