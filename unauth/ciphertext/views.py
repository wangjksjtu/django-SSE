from rest_framework import generics
#from django.contrib.auth.models import User
from ciphertext.serializers import CiphertextSerializer
from ciphertext.models import Ciphertext
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

class CiphertextList(generics.ListCreateAPIView):
    queryset = Ciphertext.objects.all()
    serializer_class = CiphertextSerializer

#    def perform_create(self, serializer):
#        serializer.save(owner=self.request.user)

class CiphertextDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ciphertext.objects.all()
    serializer_class = CiphertextSerializer
'''
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
#    def get_queryset(self):
#        user = self.request.user
#        return User.objects.filter(username=user.username)

#    def perform_create(self, serializer):
#        serializer.save(owner=self.request.user)

class UserDetail(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
'''
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
		#'users': reverse('user-list', request=request, format=format),
		'ciphertexts': reverse('ciphertext-list', request=request, format=format),
    })

