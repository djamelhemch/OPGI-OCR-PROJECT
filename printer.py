import subprocess
import time
import win32print

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
    def kill_print_process(self):
        if self.print_process and self.print_process.poll() is None:
            print("Killing print process")
            self.print_process.terminate()
            time.sleep(1)  # Allow time for termination
            if self.print_process.poll() is None:
                self.print_process.kill()

def get_default_printer():
    default_printer_info = win32print.GetDefaultPrinter()
    default_printer_name = default_printer_info.split(',')[0]
    return default_printer_name

def close_adobe_acrobat():
    # Specify the name of the process to be terminated
    process_name = "Acrobat.exe"  # Adjust this based on your Adobe Acrobat version

    try:
        # Use taskkill to terminate the process
        subprocess.run(['taskkill', '/F', '/IM', process_name], check=True)
        print(f"Adobe Acrobat process '{process_name}' terminated successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to terminate Adobe Acrobat process '{process_name}'.")

def print_pdf(pdf_content, output_file="output.pdf"):
    with open(output_file, "wb") as pdf_file:
        pdf_file.write(pdf_content)

    default_printer = get_default_printer()
    # Start the printing process with Adobe Acrobat
    acrobat_path = r'C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe'  # Adjust the path as needed
    pdf_printer = PDFPrinter(acrobat_path)
    pdf_printer.print_pdf_with_acrobat(output_file, default_printer)  # Replace with your printer name
    # Allow time for printing
    time.sleep(10)

    # Kill the print process
    close_adobe_acrobat()

if __name__ == "__main__":
    # For testing the print_pdf function independently
    sample_pdf_content = b"Sample PDF Content"
    print_pdf(sample_pdf_content)
