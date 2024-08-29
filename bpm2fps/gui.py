import json
import os
import pkg_resources
import re
import sys

from PySide6.QtCore import QObject, Slot, QAbstractTableModel, Qt, Signal, Property
from PySide6.QtGui import QGuiApplication, QClipboard
from PySide6.QtQml import QQmlApplicationEngine

from . import beats_to_frames_data
from . import usd


class TableModel(QAbstractTableModel):
    def __init__(self, data=None):
        super().__init__()
        self._data = data or []

    def columnCount(self, parent) -> int:
        try:
            return len(self._data[0])
        except IndexError:
            return 0

    def rowCount(self, parent):
        return len(self._data)

    def data(self, index, role: int):
        if index.isValid() and role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        return None


class Backend(QObject):

    updateResult = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        resultJson = beats_to_frames_data(0, 60, 120, 24)[1:]
        self._resultJson = json.dumps(resultJson, indent=4)
        self.result = TableModel(
            data=[
                ["beat", "frame", "second"],
            ]
            + [[round(v, 3) for v in frame.values()] for frame in resultJson]
        )
        self._bpm = 120
        self._fps = 24

    @Slot(int, int)
    def input_changed(self, bpm, fps):
        self._bpm = bpm
        self._fps = fps
        resultJson = beats_to_frames_data(0, 60, bpm, fps)[1:]
        self._resultJson = json.dumps(resultJson, indent=4)
        self.updateResult.emit()
        self.result.beginResetModel()  # Start model reset
        self.result._data = [
            ["beat", "frame", "second"],
        ] + [[round(v, 3) for v in frame.values()] for frame in resultJson]
        self.result.endResetModel()  # End model reset

    @Property(str, notify=updateResult)
    def resultJson(self):
        return self._resultJson

    @Slot()
    def copy(self):
        clipboard = QClipboard()
        clipboard.setText(self._resultJson)

    @Slot(str, str)
    def save(self, filepath, extension):
        filepath = filepath.replace("file://", "")
        if extension == "json":
            data = self._resultJson
        elif extension == "csv":
            data = "\n".join([",".join(map(str, row)) for row in self.result._data])
        else:
            # Else assume usd / usda
            data = usd.generate(self._bpm, self._fps)
        try:
            with open(filepath, "w") as file:  # Open the file for writing
                file.write(data)
            if os.path.exists(filepath):
                print(f"File saved: {filepath}")
        except Exception as e:
            print(f"Error on save: {e}")


def main():
    backend = Backend()
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("backend", backend)
    engine.rootContext().setContextProperty("resultData", backend.result)
    engine.load(pkg_resources.resource_filename(__name__, "app.qml"))
    if not engine.rootObjects():
        sys.exit(-1)
    exit_code = app.exec()
    del engine
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
