from django.core.management.base import BaseCommand, CommandError
from deshonnati_app.models import *
from rest_framework.decorators import api_view
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status
import os
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from PyPDF2 import PdfFileWriter, PdfFileReader
from pdf2image import convert_from_path

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        dailyfeed = DailyFeed.objects.filter(date=timezone.now().date())
        for val in dailyfeed:
            inputpdf = PdfFileReader(open(val.page1.path, "rb"))
            for i in range(inputpdf.numPages):
                output = PdfFileWriter()
                output.addPage(inputpdf.getPage(i))
                dailyfeed_path = val.date.strftime("%Y/%m/%d")
                os.mkdir(os.path.join(settings.MEDIA_ROOT+"image/{0}/{1}".format(val.city,dailyfeed_path), "page%s.pdf" % i))
                outputFilename = os.path.join(settings.MEDIA_ROOT+"image/{0}/{1}".format(val.city,dailyfeed_path), "page%s.pdf" % i)
                with open(outputFilename, "wb") as outputStream:
                    output.write(outputStream)
                pages1 = convert_from_path('{}'.format(os.path.join(settings.MEDIA_ROOT+"image/{0}/{1}".format(val.city,dailyfeed_path), "page%s.pdf" % i)), 100)
                for page1 in pages1:
                    page1.save('{}'.format(outputFilename)[:-4] +".jpg", 'JPEG')

                os.remove(outputFilename)

                self.stdout.write(self.style.SUCCESS('Successfully closed task' ))