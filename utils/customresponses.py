from rest_framework.response import Response


class CustomResponse:
    def created(message):
        return Response({
            # "status" : "status.HTTP_201_CREATED",
            "status": "success",
            "message" : message
        })


    def successful(message):
        return Response({
            # "status" : status.HTTP_200_OK,
            "status": "success",
            "message" : message,
        })


    def accepted(message):
        return Response({
            # "status" : status.HTTP_202_ACCEPTED,
            "status": "success",
            "message" : message
        })

    def not_found(obj_name):
        return Response({
            # "status" : status.HTTP_404_NOT_FOUND,
            "status": "failure",
            "message" : f"{obj_name} not found"
        })

    def failed(message):
        return Response({
            "status": "failure",
            "message" : message
        })
