from pathlib import Path

import xlwings as xw
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse
from app.utils.file import save_temp_file

router = APIRouter()


@router.post("/excel/topdf")
async def upload_file(file: UploadFile = File(...)):
    suffix = Path(file.filename).suffix
    # 检查文件类型
    if suffix.lower() != ".xlsx":
        return {"error": "File type is not supported"}
    # 保存文件
    excel_filename = save_temp_file(file)
    excel_filename_str = str(excel_filename)
    pdf_filename_str = excel_filename_str.replace(".xlsx", ".pdf")

    # 转换为pdf
    app = xw.App(visible=False)
    # Initialize new excel workbook
    wb = app.books.open(excel_filename_str)
    sheet = wb.sheets[0]
    # Construct path for pdf file
    sheet.to_pdf(pdf_filename_str, show=False)
    # Close workbook
    wb.close()
    return FileResponse(
        pdf_filename_str,
        media_type="application/octet-stream",
        filename=Path(pdf_filename_str).name,
    )
