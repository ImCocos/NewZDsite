from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponse, JsonResponse
import json

from .models import StationStats, Ticket


def index(request):

    context = {
        'stations': StationStats.objects.all().values_list('pk', 'name')
    }

    if request.method == 'POST':
        submit = request.POST.get('submit')

        match submit:
            case 'show-info':
                return redirect('show-info', request.POST.get('stations[]'))

    return render(request, template_name='index.html', context=context)


def show_info(request, station_pk):
    st = get_object_or_404(StationStats, pk=station_pk)

    context = {
        'st': st,
    }
    return render(request, template_name='show-info.html', context=context)


def buy_ticket(request):

    context = {
        'stations': StationStats.objects.all().values_list('pk', 'name')
    }

    if request.method == 'POST':
        submit = request.POST.get('submit')

        match submit:
            case 'buy-ticket':
                st_from = get_object_or_404(StationStats, pk=int(request.POST.get('stations-from[]')))
                st_to = get_object_or_404(StationStats, pk=int(request.POST.get('stations-to[]')))

                ticket = Ticket(st_from=st_from.pk, st_to=st_to.pk)
                ticket.save()

                st_to.tickets.add(ticket)
                st_to.people += 1
                st_to.save()

                return redirect('home')

    return render(request, template_name='buy-ticket.html', context=context)


@csrf_exempt 
def data_getter(request, station_pk):
    key = 'zsrgdragae5hrbzdhnsrtWQA354'

    if request.method == 'GET':
        raise Http404
    if request.method == 'POST':
        data = dict(json.loads(str(request.body, encoding='utf-8')))
        try:
            if data['key'] == key:
                print(data)
                st = get_object_or_404(StationStats, pk=station_pk)
                st.people += int(data['input']) - int(data['output'])
                st.save()

        except KeyError:
            pass
        return HttpResponse()


def data_sender(request, station_pk):
    st = get_object_or_404(StationStats, pk=station_pk)
    data = {
        'people': st.people,
        'recirculers': [
                {
                    'id': r.pk,
                    'power': r.power,
                }
                for r in st.recirculers.all()
        ],
    }

    response = {
        'data': data
    }
    return JsonResponse(response)
