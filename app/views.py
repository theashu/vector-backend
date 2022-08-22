import json
from rest_framework import mixins
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

from .models import PicturesModel
from .serializer import PictureSerializer


class PictureListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = PicturesModel.objects.all()
    serializer_class = PictureSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PictureDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, 
    generics.GenericAPIView
):
    queryset = PicturesModel.objects.all()
    serializer_class = PictureSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@api_view(['PATCH'])
@permission_classes([permissions.IsAuthenticated])
def reordering_cats(request):
    data = request.data
    pictures_count = PicturesModel.objects.count()
    updated_picture_detail = PicturesModel.objects.get(pk=data.get("cat_id"))
    sorted_order = data.get("moves")
    if not updated_picture_detail:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Cat not found"})
    position_list = [updated_picture_detail.position]
    if sorted_order < 0:
        if updated_picture_detail.position + sorted_order < 0:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Moves value is not correct."})
        while sorted_order < 0:
           position_list.append(updated_picture_detail.position+sorted_order)
           sorted_order +=1 
    elif sorted_order == 0:
        return Response(status=status.HTTP_200_OK, data={"message": "Reorder not performed"})
    else:
        if updated_picture_detail.position + sorted_order > pictures_count:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Moves value is not correct."})
        while sorted_order > 0:
            position_list.append(updated_picture_detail.position+sorted_order)
            sorted_order-=1
    print(f"Positions List: {position_list}, Requested Id: {data.get('cat_id')}, Sorting Order: {data.get('moves')}\n")
    update_dict = {}
    if data.get("moves") < 0:
        update_dict[updated_picture_detail.id] = min(position_list)
        position_list.remove(max(position_list))
        for postion_data in position_list:
            filter_data = PicturesModel.objects.get(position=postion_data)
            update_dict[filter_data.id] = filter_data.position+1
    else:
        update_dict[updated_picture_detail.id] = max(position_list)
        position_list.remove(min(position_list))
        for postion_data in position_list:
            filter_data = PicturesModel.objects.get(position=postion_data)
            update_dict[filter_data.id] = filter_data.position-1
    print(f"Updated Dictionary with and Position: {json.dumps(update_dict)}\n")
    with transaction.atomic():
        if not transaction.get_connection().in_atomic_block:
            raise RuntimeError("Needs to be run inside an atomic transaction")
        for key, value in update_dict.items():
            PicturesModel.objects.filter(id=key).update(position=value)
    return Response(status=status.HTTP_200_OK, data={"message": "Reorder done successfully."})