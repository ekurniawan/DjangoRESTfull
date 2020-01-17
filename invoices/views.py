from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from invoices.models import Invoice
from invoices.serializers import InvoiceSerializer

# Create your views here.

@api_view(['GET'])
def invoice_list(request):
    if request.method == 'GET':
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def invoice_detail(request,pk):
    try:
        invoice = Invoice.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = InvoiceSerializer(invoice)
    return Response(serializer.data)