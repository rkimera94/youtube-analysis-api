import imp
from flask import Blueprint
from flask_restful import Api
from resources.video_details import VideoDetailsResource
from resources.videos import VideoResource


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(VideoResource, '/videos')
api.add_resource(VideoDetailsResource, '/video-details')
