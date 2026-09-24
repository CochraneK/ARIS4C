# PDF build output

This directory is generated from the frozen bilingual Markdown manuscripts and SVG figures by `.github/workflows/publish-023-pdfs.yml`.

Expected durable public artifacts:
- `ARIS4C-023_EN.pdf`
- `ARIS4C-023_ZH.pdf`

The workflow installs Pandoc, LibreOffice Writer, Noto CJK fonts and Poppler; builds DOCX intermediates; converts them to PDF; verifies file size, page count, searchable text and key terms; records SHA-256 in the workflow log; and commits only the final PDFs.

Do not hand-edit generated PDFs. Change the canonical manuscript/figures, then rebuild.
