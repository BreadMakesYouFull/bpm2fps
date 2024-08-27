import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import Qt.labs.platform


ApplicationWindow {
    id: main
    width: 400
    height: 400
    minimumWidth: 300
    minimumHeight: 150
    visible: true
    title: "bpm2fps"
    property bool is_windows: Qt.platform.os == "windows" // Just use light mode on windows for simplicity
    property bool darkMode: is_windows ? false : (Application.styleHints.colorScheme === Qt.ColorScheme.Dark)
    font: Qt.font({
                underline: false,
                pixelSize: Math.max(12, (main.height > main.width) ? (main.width / 25) : (main.height / 25)) ,
                family: "monospace"
        })
    property var fontSmall: Qt.font({
                underline: false,
                pixelSize: main.font.pixelSize * 0.75,
                family: "monospace"
        })
    ColumnLayout {
        id: mainLayout
        anchors.fill: parent
        RowLayout {
            Label {
                id: bpm_text
                text: " bpm "
                horizontalAlignment: Qt.AlignRight
            }
            SpinBox {
                id: bpm_spin
                from: 10
                value: 120
                to: 220
                stepSize: 1
                editable: true
                onValueChanged: {
                    bpm.value = bpm_spin.value
                    backend.input_changed(bpm.value, fps.value);
                }
            }
            Slider {
                id: bpm
                Layout.fillWidth: true
                Layout.columnSpan: 1
                from: 10
                value: 120
                to: 220
                stepSize: 10
                onValueChanged: {
                    bpm_spin.value = bpm.value
                    backend.input_changed(bpm.value, fps.value);
                }
                handle.implicitWidth: fps_text.height
                handle.implicitHeight: fps_text.height
            }
        }
        RowLayout {
            Label {
                id: fps_text
                text: " fps "
                horizontalAlignment: Qt.AlignRight
            }
            SpinBox {
                id: fps_spin
                from: 2
                value: 24
                to: 120
                stepSize: 1
                editable: true
                onValueChanged: {
                    fps.value = fps_spin.value
                    backend.input_changed(bpm.value, fps.value);
                }
            }
            Slider {
                id: fps
                Layout.fillWidth: true
                Layout.columnSpan: 1
                from: 2
                value: 24
                to: 120
                stepSize: 1
                onValueChanged: {
                    fps_spin.value = fps.value
                    backend.input_changed(bpm.value, fps.value);
                }
                handle.implicitWidth: fps_text.height
                handle.implicitHeight: fps_text.height
            }
        }
        TableView {
            id: tableView
            Layout.fillWidth: true
            Layout.fillHeight: true
                
            clip: true
            model: resultData

            columnSpacing: 0
            rowSpacing: 0

            delegate: Rectangle{
                implicitWidth: main.width / 3
                implicitHeight: main.fontSmall.pixelSize + 10
                color: "#fffed7"
                border.color: "#AAAAAA"
                border.width: 1
                TextInput {
                   width: parent.width
                   height: parent.height
                   horizontalAlignment: TextInput.AlignHCenter
                   verticalAlignment: TextInput.AlignVCenter
                   //leftPadding: 10
                   //topPadding: 10
                   text: model.display
                   font: main.fontSmall
                   readOnly: true
               }
            }
        }
        RowLayout {
            Label {
                text: " Save: "
                horizontalAlignment: Qt.AlignRight
            }
            Button {
                text: "csv"
                padding: 10
                Layout.fillWidth: true
                onClicked: {
                    fileDialogCsv.open()
                }
            }
            Button {
                text: "json"
                padding: 10
                Layout.fillWidth: true
                onClicked: {
                    fileDialogJson.open()
                }
            }
            Button {
                text: "usd"
                padding: 10
                Layout.fillWidth: true
                onClicked: {
                    fileDialogUsd.open()
                }
            }
            FileDialog {
                id: fileDialogCsv
                folder: StandardPaths.writableLocation(StandardPaths.DocumentsLocation)
                fileMode: FileDialog.SaveFile
                defaultSuffix: ".csv"
                nameFilters: ["json (*.csv)", "all (*)"]
                onAccepted: {
                    backend.save(file, "csv")
                }
            }
            FileDialog {
                id: fileDialogJson
                folder: StandardPaths.writableLocation(StandardPaths.DocumentsLocation)
                fileMode: FileDialog.SaveFile
                defaultSuffix: ".json"
                nameFilters: ["json (*.json)", "all (*)"]
                onAccepted: {
                    backend.save(file, "json")
                }
            }
            FileDialog {
                id: fileDialogUsd
                folder: StandardPaths.writableLocation(StandardPaths.DocumentsLocation)
                fileMode: FileDialog.SaveFile
                defaultSuffix: ".usda"
                nameFilters: ["usd (*.usd)", "usda (*.usda)", "all (*)"]
                onAccepted: {
                    backend.save(file, "usd")
                }
            }
        }
    }
}
