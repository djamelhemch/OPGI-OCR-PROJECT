import subprocess
import time

class PDFPrinter:
    def __init__(self, acrobat_path):
        self.acrobat_path = acrobat_path

    def print_pdf_with_acrobat(self, pdffile, printer_name):
        cmd = '"{}" /N /T "{}" "{}"'.format(self.acrobat_path, pdffile, printer_name)

        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        exit_code = proc.wait()

        if exit_code == 0:
            print("Printing successful")
        else:
            print("Printing failed. Error:", stderr.decode('utf-8'))

def print_pdf(pdf_content, output_file="output.pdf"):
    with open(output_file, "wb") as pdf_file:
        pdf_file.write(pdf_content)

    # Set the path to your PDF viewer executable (e.g., Adobe Acrobat Reader)
    pdf_viewer_path = r'C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe'

    # Open the PDF file with the default PDF viewer
    subprocess.run([pdf_viewer_path, output_file], shell=True)

    # Introduce a delay before starting the printing process
    time.sleep(1)  # Adjust the delay time as needed

    # Start the printing process with Adobe Acrobat
    acrobat_path = r'C:\Program Files (x86)\Adobe\Acrobat 11.0\Acrobat\Acrobat.exe'  # Adjust the path as needed
    pdf_printer = PDFPrinter(acrobat_path)
    pdf_printer.print_pdf_with_acrobat(output_file, 'Your_Printer_Name')  # Replace 'Your_Printer_Name' with your printer name

if __name__ == "__main__":
    # For testing the print_pdf function independently
    sample_pdf_content = b"Sample PDF Content"
    print_pdf(sample_pdf_content)
