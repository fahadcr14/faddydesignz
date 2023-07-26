
def inserting_responded(request):
    respond_id = request.GET.get('id')
    Contact.objects.filter(id=respond_id).update(responded='yes')
    
    responded_row = Contact.objects.filter(id=respond_id).values()
    responded_row_list = list(responded_row)
    
    print(responded_row_list)
    
    return JsonResponse(responded_row_list, safe=False)