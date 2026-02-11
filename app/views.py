from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Content
from .serializers import ContentSerializer



@api_view(['GET', 'POST'])
def content_list(request):
    if request.method == 'GET':
        category = request.query_params.get('category')
        contents = Content.objects.all()
        
        if category:
            contents = contents.filter(category=category)
        
        serializer = ContentSerializer(contents, many=True)
        return Response({
            'count': contents.count(),
            'results': serializer.data
        })
    
    elif request.method == 'POST':
        serializer = ContentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def content_detail(request, pk):
    try:
        content = Content.objects.get(pk=pk)
    except Content.DoesNotExist:
        return Response({'error': 'Content not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ContentSerializer(content)
        return Response(serializer.data)
    

    elif request.method == 'PUT':
        serializer = ContentSerializer(content, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    elif request.method == 'DELETE':
        content.delete()
        return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)