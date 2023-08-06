from django.shortcuts import render
from django.http import HttpResponse
from tablib import Dataset
from .resources import BookResource
from .models import Book

# Create your views here.
def Import_Excel(request):
    if request.method == 'POST':
        book_resource = BookResource()
        dataset = Dataset()
        new_book = request.FILES['myfile']
        data_import = dataset.load(new_book.read())
        result = book_resource.import_data(dataset=dataset, dry_run=True)
        if not result.has_errors():
            book_resource.import_data(dataset, dry_run=False)
            print("Success")
    return render(request, 'import_excel_db.html', {})