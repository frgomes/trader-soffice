import uno
import unohelper

def read_cell_from_libreoffice(file_path, sheet_name, cell_address):
    """
    Reads a cell value from a LibreOffice spreadsheet using UNO API.

    Args:
        file_path (str): The path to the LibreOffice spreadsheet file.
        sheet_name (str): The name of the sheet to read from.
        cell_address (str): The address of the cell to read (e.g., "A1").

    Returns:
        The value of the specified cell.
    """

    context = uno.getComponentContext()
    print("@@@@@@ 1")
    ## desktop = context.getServiceManager().createInstanceWithContext("com.sun.star.frame.Desktop", context)
    ## print("@@@@@@ 2")
    # Connect to the listening LibreOffice instance
    resolver = context.getServiceManager().createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", context)
    print("@@@@@@ 3")

    ctx = resolver.resolve("uno:socket,host=localhost,port=2002;urp;")
    print("@@@@@@ 4")

    localContext = ctx.getServiceManager()
    print("@@@@@@ 5")

    doc = desktop.loadComponentFromURL(uno.systemPathToFileUrl(file_path), "_blank", 0, ())
    print("@@@@@@ 6")

    sheets = doc.getSheets()
    print("@@@@@@ 7")

    sheet = sheets.getByIndex(0)  ##TODO: sheet_name
    print("@@@@@@ 8")

    cell = sheet.getCellRangeByName(cell_address)
    print("@@@@@@ 9")

    cell_value = cell.getValue()
    print("@@@@@@ 10")

    doc.close(True)

    return cell_value


ticker = read_cell_from_libreoffice("BESST.ods", "BESST", "A3")
print(ticker)
