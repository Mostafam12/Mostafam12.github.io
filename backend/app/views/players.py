# -*- coding: utf-8 -*-
import logging
from functools import partial
import json
import os

from rest_framework.response import Response
from rest_framework.views import APIView, exception_handler
# from app.dbmodels import models
from app import models, serializers

LOGGER = logging.getLogger('django')


class PlayerSummary(APIView):
    logger = LOGGER

    def get(self, request, playerID):
        """Return player data"""
        print(playerID)
        # TODO: Complete API response, replace placeholder below with actual implementation that sources data from database
        # print(os.path.dirname(os.path.abspath(__file__)))
        # with open(os.path.dirname(os.path.abspath(__file__)) + '/sample_response/sample_response.json') as sample_response:
        #     data = json.load(sample_response)
        # return Response(data)
        player = models.AppPlayer.objects.get(id=playerID)
        player_serializer = serializers.PlayerSerializer(player)

        player_data = {
            "name": player_serializer.data["name"],
            "games": player_serializer.data["games"]
        }

        return Response(player_data)
