from django.shortcuts import render
from datetime import date
from .models import Equipment, Booking, Inventory
from django.utils import timezone



def equipment_search(request):
    search_result = request.GET.get('q', '') #search bar and filter and sort options
    sort_choice= request.GET.get('sort', '')  
    filter_choice= request.GET.get('filter_by', '')  

    name_retrieval = Equipment.objects.filter( #search bar retrieves equipment names
        equip_name__icontains=search_result
    )

    
    if search_result.isdigit():
        id_number = Equipment.objects.filter( #if it does not, it retrieves id number 
            equipment_id=search_result
        )
        total = list(id_number)
    else:
        total = list(name_retrieval) #else just retrieves name from list 

    
    if not total:
        type_search = Equipment.objects.filter(
            equip_type__icontains=search_result
        )
        total = list(type_search)  #if it is not able to retrive id, it provides equipment type 

    
    if sort_choice == 'warranty':
        total.sort(key=lambda x: x.warranty)  
    elif sort_choice == 'borrowable':              #filter and sort options based on model and populate file 
        total.sort(key=lambda x: x.borrowable) 
    elif sort_choice == 'on_site':
        total.sort(key=lambda x: x.on_site)  

    
    name_results = []
    listed_names = set()

    for equipment in total:
        if equipment.equip_name not in listed_names:  #stops duplicates from appearing in the equipment list 
            name_results.append(equipment)
            listed_names.add(equipment.equip_name)

    context = {
        'results': name_results,
        'search_bar': search_result,
        'sort_by': sort_choice, 
        'filter_by': filter_choice,  
    }

    return render(request, 'equipment-search.html', context)

def update_equipment(request):
    if request.method == 'POST':
        equip_name = request.POST.get('equip_name')
        quantity = int(request.POST.get('quantity', 0))
        equip_type = request.POST.get('equip_type')
        on_site = bool(request.POST.get('on_site'))           #retrieves data from the form.
        borrowable = bool(request.POST.get('borrowable'))
        warranty_str = request.POST.get('warranty')
        date_added=timezone.now()

        try:
            warranty = date.fromisoformat(warranty_str)
        except ValueError:
            return render(request, 'update-equipment.html', {'error_message': 'Invalid warranty date'}) #item does not get added, if the warranty is in the past

        
        existing_equipment = Equipment.objects.filter(equip_name=equip_name, equip_type=equip_type).first()
        if existing_equipment:
            return render(request, 'update-equipment.html', {'equipment_already_exists': True})  #if the equipment has the same name and type, the page views a message

    
        update_equipment_equipment = Equipment.objects.create(
            equip_name=equip_name,
            quantity=quantity,
            equip_type=equip_type,
            on_site=on_site,
            borrowable=borrowable,
            warranty=warranty,
            date_added=date.today()   # these attributes are to add the new equipment 
        )

     
        if update_equipment_equipment.quantity > 0:
            inventory = Inventory.objects.first()  #item gets added to inventory and os viewed in equipment search page 
            if inventory:
                inventory.quantity += update_equipment_equipment.quantity
                inventory.save()

        previous_booking = []
        previous_booking = Booking.objects.filter(equipment_list=update_equipment_equipment).first()
        for booking in previous_booking:
            previous_booking.append(booking.booking_nums) #gives previous booking number if any 

          

        return render(request, 'update-equipment.html', {'equipment': update_equipment_equipment, 'previous_booking': previous_booking})
    else:
        return render(request, 'update-equipment.html')





