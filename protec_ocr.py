import cv2
import pytesseract
from printer import print_pdf
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from arabic_reshaper import reshape
from reportlab.lib.units import inch
from reportlab.platypus import Image
from bidi.algorithm import get_display

# Register an Arabic font
# Register the Arabic font

class PDFGenerator:
    def __init__(self):
        self.buffer = BytesIO()
        self.pdf_document = SimpleDocTemplate(self.buffer, pagesize=letter)
        self.styles = getSampleStyleSheet()

        pdfmetrics.registerFont(TTFont('Scheherazade', 'fonts/ScheherazadeNew-Regular.ttf'))
        pdfmetrics.registerFont(TTFont('Amiri', 'fonts/Amiri-Regular.ttf'))

        self.styles.add(ParagraphStyle(name='ArabicTitle', parent=self.styles['Title'], fontName='Amiri', fontSize=42, underline=True, ))
        self.styles.add(ParagraphStyle(name='ArabicHeading2', parent=self.styles['Heading2'], fontName='Amiri'))
        
        self.story = []

    def add_text(self, text, style=None, spacing=0, x=None, y=None):
        if not style:
            style = self.styles['Normal']

        # Reshape and get display for Arabic text
        reshaped_text = reshape(text)
        reshaped_text_display = get_display(reshaped_text)

        # Add reshaped text to the story 
        self.story.append(Paragraph(reshaped_text_display, style))

    def add_datetime(self, client_name, date_of_purchase, total_ttc):
        # Add a centered title using the existing 'Title' style
        title = "قسيمة معالجة صك الملكية"
        title_style = self.styles['ArabicTitle']

        # Reshape Arabic title and get display
        reshaped_title = reshape(title)
        reshaped_title_display = get_display(reshaped_title)

        # Add reshaped title to the story
        title_paragraph = Paragraph(reshaped_title_display, title_style)
        title_paragraph.spaceAfter = 80  # Adjust this value as needed
        self.story.append(title_paragraph)
        
        # Add your logo to the top-left corner (adjust as needed)
        logo_path = 'imgs/opgi_oran.jpg'
        logo_width = 100  # Adjust the width of the logo as needed
        logo_height = 50  # Adjust the height of the logo as needed
        my_canvas = canvas.Canvas('pdf_file.pdf')
        logo_width = 100  # Adjust the width of the logo as needed
        logo_height = 50
        x = 10.25 * inch
        y = 0.5 * inch      
        my_canvas.drawImage(logo_path, x, y, width=logo_width, height=logo_height, mask=None)
        # Add the other text to the story
        self.add_text("اسم الزبون: " + client_name, style=self.styles['ArabicHeading2'])
        self.add_text("تاريخ الشراء: " + date_of_purchase, style=self.styles['ArabicHeading2'])
        self.add_text("الثمن إجمالي: " + total_ttc, style=self.styles['ArabicHeading2'])

        # Add the current date and time
        now = datetime.now()
        formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

        # Reshape and get display for Arabic formatted_datetime
        reshaped_datetime = reshape(formatted_datetime)
        reshaped_datetime_display = get_display(reshaped_datetime)

        self.add_text("وردت في: " + reshaped_datetime_display, style=self.styles['ArabicHeading2'])

    def generate_pdf(self):
        # Build the entire document
        self.pdf_document.build(self.story)

        # Reset the BytesIO buffer to the beginning
        self.buffer.seek(0)

        return self.buffer.getvalue()
    
def process_document(img_path):
    img = cv2.imread(img_path)
    
    # Check if the image was loaded successfully
    if img is None:
        print(f"Error: Unable to load the image at {img_path}")
        return
    
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    height, width, channels = img.shape
    data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
    
    # Initialize variables to store extracted information
    client_name = ""
    address = ""
    client_number = ""
    order_id = ""
    date_of_purchase = ""
    salesperson_name = ""
    purchased_item = ""
    total_ttc = ""

    for i, (left, top, width, height) in enumerate(zip(data["left"], data["top"], data["width"], data["height"])):
        if int(data["conf"][i]) > 30:
            x, y, w, h = left, top, width, height
            roi = img[y:y+h, x:x+w]
            text = data["text"][i]

            # Check if the box index matches the specified ones
            if i in [47, 48]:
                client_name +=  text + " "
            elif i in [51, 52, 53]:
                address += text
            elif i in [56,57]:
                client_number += text
            elif i in[61,62] :
                order_id += text
            elif i in [69]:
                date_of_purchase += text
            elif i in [71, 72]:
                salesperson_name += text
            elif i in [85]:
                purchased_item += text
            elif i in [129]:
                total_ttc += text

            # Draw bounding box and text on the image
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            img = cv2.putText(img, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # Print the extracted information
    print("Client Name:", client_name)
    print("Address:", address)
    print("Client Number:", client_number)
    print("Order ID:", order_id)
    print("Date of Purchase:", date_of_purchase)
    print("Salesperson Name:", salesperson_name)
    print("Purchased Item(s):", purchased_item)
    print("Total TTC:", total_ttc)

    # Create a PDF in memory
    pdf_generator = PDFGenerator()
    pdf_generator.add_datetime(client_name, date_of_purchase, total_ttc)
    
    # Generate and print the PDF
    pdf_content = pdf_generator.generate_pdf()
    
    print("PDF generated and saved to 'output.pdf'.")
    print_pdf(pdf_content)
    print("Waiting for printing process...")
    # Display the image
    #cv2.imshow("img", img)
    cv2.waitKey(0)

if __name__ == "__main__":
    img_path = 'imgs/invoice_abd.png'
    process_document(img_path)
