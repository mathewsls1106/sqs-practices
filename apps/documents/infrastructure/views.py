from apps.documents.infrastructure.services.sqs_client import SQSClient
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class SendTaskView(View):
    def __init__(self):
        self.sqs_client = SQSClient()

    def post(self, request, *args, **kwargs):
        queue_identifier = 'procesamiento-tareas'
        payload = {
            'nombre': "mateo"
        }
        attributes = {}
        delay_seconds = 0

        try:
            self.sqs_client.send_task(queue_identifier, payload, attributes, delay_seconds)
            return JsonResponse({'status': 'success', 'queue_identifier': f'tarea enviada a la cola: {queue_identifier}'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
