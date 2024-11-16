import barcode
from barcode.writer import ImageWriter

txtfile = open("codes_for_bcode.txt", "r")
barcodes = txtfile.readlines()
# Strip whitespace and newline characters
barcodes = [code.strip() for code in barcodes]

for i, code in enumerate(barcodes):
    ean = barcode.get('ean13', code, writer=ImageWriter())
    filename = ean.save(f'Barcodes_all\\{code}')  

    