import encrypt
from toPDF import genPDF
from getQuote import getQuotes

genPDF(encrypt.encryptArray(getQuotes()))