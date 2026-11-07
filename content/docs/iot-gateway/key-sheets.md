+++
title = "Key sheets"
description = "Edit many gateway data keys at once in a spreadsheet: keyboard editing, import from CSV or Excel, export, and resizable columns."
weight = 225

[extra]
status = "checked"
checked = "4.3.0.57"
+++
A connector device can have hundreds of keys: time series, attributes, RPC methods and attribute updates. The **key sheet** shows them as a spreadsheet, so you can type, copy and check many keys at once instead of opening each one.

## Open the key sheet

1. In SENTIENT, open the gateway, then **Connectors**, and open the connector.
2. Open the device in the connector's configuration and click the keys you want to edit, for example **Time series**.
3. In the keys panel, click the full-screen button at the top right. The panel opens as a sheet that fills the screen.

Click the button again, now **Exit fullscreen**, to go back to the list. Click **Apply** to keep your changes, or **Cancel** to drop them.

The columns depend on the connector: a Modbus sheet has the function code, address, data type and byte order; an OPC UA sheet has the node path. Red cells hold a value that is not valid; hover over the warning sign to see why.

## Edit with the keyboard

Click a cell, then:

| Key | Does |
|---|---|
| Arrows, **Tab**, **Shift+Tab** | Move between cells |
| **Enter** or **F2** | Edit the cell; **Enter** again moves down. At the last row it adds a new one |
| **Ctrl+Enter** | Add a row below |
| **Escape** | Leave the cell without leaving the sheet |
| **Delete**, **Backspace** | Clear the cell |
| **Space** | Tick or clear a checkbox cell |
| **Home**, **End** | First or last column |

### Select rows

Click a row number to select the row. **Shift**+click selects a range and **Ctrl**+click adds or removes one row. **Ctrl+A** selects all rows. **Delete** then deletes the selected rows.

With rows selected, **Add to RPC write** and **Add to attribute updates** turn them into write keys. See [Write values to devices](/docs/iot-gateway/rpc-write/).

## Search, import and export

- The **Search keys...** box filters the rows. The line under it says how many keys match.
- **Import keys** reads a CSV, XLSX, XLS or ODS file. The first row must hold the column names as the sheet shows them; columns that do not match are ignored. The imported rows are added to the sheet for you to check, and are only saved when you click **Apply**.
- **Export as CSV** downloads the rows that are shown, with the same column names, so you can edit them in a spreadsheet program and import them again.

## Resize columns

With a cell selected, **Ctrl+Shift+←** and **Ctrl+Shift+→** make its column narrower or wider, and **Ctrl+Shift+0** resets it.

From the release after 4.3.0.57, you can also drag the right edge of a column header, and double-click the edge to reset it.

## Related

- [Write values to devices](/docs/iot-gateway/rpc-write/)
- [General configuration](/docs/iot-gateway/configuration/)
