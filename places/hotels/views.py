from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Hotels

class HotelsView(APIView):

    def get(self, request):
        all_hotels = Hotels.objects.all()
        print(all_hotels)
        hotel_list = []
        for hotel in all_hotels:
            list_hotel = {
                "id": hotel.id,
                "city": hotel.city,
                "state": hotel.state
            }
            hotel_list.append(list_hotel)
        return Response(hotel_list)

    def post(self, request):
        new_hotel = Hotels(city=request.data["city"], state=request.data["state"])
        new_hotel.save()
        return Response("Data Saved")
