from datetime import datetime
import os

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import RGBColor

from dotenv import load_dotenv
import emailer


load_dotenv()

document = Document(os.getenv('TEMPLATE_FILE'))

# INVOICE NO:
first_table = document.tables[0]
invoice_no_obj = first_table.cell(0, 1)
current_date = datetime.now().strftime('%m%y')
invoice_no_obj.paragraphs[0].text = None
invoice_no = f'ENG64730{current_date}'
run = invoice_no_obj.paragraphs[0].add_run(invoice_no)
run.font.color.rgb = RGBColor.from_string('9E9E9E')

# INVOICE DATE:
second_table = document.tables[1]
invoice_date_obj = second_table.cell(0, 2)
current_date = datetime.now().strftime('%d %b %Y')
invoice_date_obj.paragraphs[1].text = None
invoice_date_obj.paragraphs[1].add_run(current_date).bold = True

# INVOICE ITEM:
third_table = document.tables[2]
invoice_item_obj = third_table.cell(1, 0)
current_date = datetime.now().strftime('%b %Y')
invoice_item_obj.text = invoice_item_obj.text.replace('[mm] [yyyy]', current_date)

filename = 'Invoice_' + datetime.now().strftime('%b_%Y') + '.docx'
document.save(f'./generated/{filename}')

emailer.send_email(
    invoice_no=invoice_no, 
    month=current_date, 
    filename=filename, 
    to=os.getenv('EMAIL_TO'),
    sender_name=os.getenv('EMAIL_SENDER_NAME')
)