from django.http import JsonResponse

def payment_list(request):
    return JsonResponse({"status": "ok", "message": "Payment API v1"})