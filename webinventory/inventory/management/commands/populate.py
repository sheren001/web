from django.core.management.base import BaseCommand
from inventory.models import Equipment
from datetime import date







class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        equipment_data = [
            {"name": "Laptop w/ 2070 GPU", "quantity": 1, "type": "PC/Laptop", "on_site": False, "borrowable": False, "warranty": date(2022, 4, 25)},
            {"name": "Laptop w/ 2070 GPU", "quantity": 3, "type": "PC/Laptop", "on_site": True, "borrowable": False, "warranty": date(2022, 4, 23)},
            {"name": "Valve Index", "quantity": 3, "type": "VR headset", "on_site": True, "borrowable": False, "warranty": date(2022, 3, 27)},
            {"name": "Vive Pro Eye", "quantity": 1, "type": "VR headset", "on_site": False, "borrowable": False, "warranty": date(2025, 4, 23)},
            {"name": "Base Station 2", "quantity": 6, "type": "Camera/sensors", "on_site": False, "borrowable": True, "warranty": date(2025, 4, 25)},
            {"name": "PC w/ 1080", "quantity": 4, "type": "PC/laptop", "on_site": True, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "PC w/ 1060", "quantity": 1, "type": "PC/Laptop", "on_site": False, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Windows AIO PC", "quantity": 1, "type": "PC/Laptop", "on_site": True, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Mac Mini (Intel)", "quantity": 1, "type": "PC/laptop", "on_site": True, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "HP Omen Ultrawide ", "quantity": 4, "type": "PC Peripherals", "on_site": False, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Monitor 16:9", "quantity": 1, "type": "PC Peripherals", "on_site": False, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Keyboard", "quantity": 7, "type": "PC Peripherals", "on_site": False, "borrowable": True, "warranty": date(2025, 4, 25)},
            {"name": "Mouse", "quantity": 7, "type": "PC Peripherals", "on_site": True, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Samsung smart TV 55 Inch", "quantity": 3, "type": "PC Peripherals", "on_site": False, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Movable TVs ", "quantity": 1, "type": "PC Peripherals", "on_site": True, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Clevertouch Screen", "quantity": 1, "type": "PC Peripherals", "on_site": True, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Desk", "quantity": 5, "type": "Furniture", "on_site": False, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Lectern", "quantity": 1, "type": "Furniture", "on_site": False, "borrowable": True, "warranty": date(2025, 4, 25)},
            {"name": "Chair ", "quantity": 6, "type": "Furniture", "on_site": True, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Chair w/ Armrest", "quantity": 5, "type": "Furniture", "on_site": False, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Stool", "quantity": 1, "type": "Furniture", "on_site": True, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Table", "quantity": 1, "type": "Furniture", "on_site": True, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "chair w/o backrest", "quantity": 2, "type": "Furniture", "on_site": False, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Leap motion Mount", "quantity": 1, "type": "Camera/Sensors", "on_site": False, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "VRGo Egg Chair", "quantity": 1, "type": "PC Peripherals", "on_site": False, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Generic Tripod", "quantity": 1, "type": "Tripods", "on_site": False, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Manfroto Tripod", "quantity": 2, "type": "Tripods", "on_site": False, "borrowable": True, "warranty": date(2025, 4, 25)},
            {"name": "Green screen", "quantity": 1, "type": "other", "on_site": True, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Linx Vision Gaming Tablet", "quantity": 1, "type": "PC/Laptop", "on_site": False, "borrowable": True, "warranty": date(2025, 4, 25)},
            {"name": "Insta 360 Pro", "quantity": 1, "type": "Camera/Sensors", "on_site": True, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Insta 360 Pro 2", "quantity": 1, "type": "Camera/Sensors", "on_site": False, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Samsung Gear 360 Camera", "quantity": 1, "type": "Camera/Sensors", "on_site": True, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Insta 360 Pro Battery", "quantity": 2, "type": "Power/Cable", "on_site": True, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Insta 360 Pro Charger x 1", "quantity": 2, "type": "Power/cable", "on_site": False, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Structure sensor", "quantity": 1, "type": "Camera/Sensors", "on_site": False, "borrowable": True, "warranty": date(2025, 4, 25)},
            {"name": "Leap Motion", "quantity": 2, "type": "Camera/sensors", "on_site": True, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Laptop w/ 1070", "quantity": 1, "type": "PC/Laptop", "on_site": False, "borrowable": True, "warranty": date(2025, 4, 25)},
            {"name": "Pico 4", "quantity": 2, "type": "VR Headset", "on_site": True, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Pico 4 Enterprise", "quantity": 1, "type": "VR Headset", "on_site": False, "borrowable": True, "warranty": date(2025, 4, 25)},
            {"name": "Oculus Quest w/ Controllers", "quantity": 3, "type": "VR Headset", "on_site": False, "borrowable": True, "warranty": date(2025, 4, 25)},
            {"name": "Hololens 1", "quantity": 1, "type": "VR Headset", "on_site": True, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Hololens 2", "quantity": 1, "type": "VR Headset", "on_site": False, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Vive Pro Controller Pair", "quantity": 1, "type": "VR Controller", "on_site": True, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Valve Knuckles Controller Pair", "quantity": 3, "type": "VR Controller", "on_site": True, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Emotiv EEG", "quantity": 1, "type": "Other", "on_site": False, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Neewer 480 LED Lights", "quantity": 1, "type": "Other", "on_site": False, "borrowable": True, "warranty": date(2025, 4, 25)},
            {"name": "BeBox Router", "quantity": 1, "type": "Other", "on_site": True, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Generic Tripod", "quantity": 1, "type": "Camera/sensors", "on_site": False, "borrowable": True, "warranty": date(2025, 4, 25)},
            {"name": "GearVR Headset", "quantity": 2, "type": "PC/laptop", "on_site": True, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "GearVR Controller", "quantity": 2, "type": "PC/Laptop", "on_site": False, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "IPad Air Gen3 2019", "quantity": 1, "type": "PC/Laptop", "on_site": True, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Anker 10 port USB charger", "quantity": 2, "type": "PC/laptop", "on_site": True, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Anker Power Bank 10000MAH", "quantity": 2, "type": "PC Peripherals", "on_site": False, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "HTC Power Bank 5700MAH", "quantity": 2, "type": "PC Peripherals", "on_site": False, "borrowable": True, "warranty": date(2025, 4, 25)},
            {"name": "Vive Wireless Adapter", "quantity": 1, "type": "PC Peripherals", "on_site": True, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Vive Trackers & Dongles", "quantity": 4, "type": "PC Peripherals", "on_site": False, "borrowable": True, "warranty": date(2025, 4, 25)},
            {"name": "Samsung Galaxy S6", "quantity": 1, "type": "PC Peripherals", "on_site": True, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Google Pixel 2", "quantity": 1, "type": "Camera/sensors", "on_site": False, "borrowable": True, "warranty": date(2025, 4, 25)},
            {"name": "Xbox One Dongle", "quantity": 5, "type": "PC/laptop", "on_site": True, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "DJI Osmo Mobile 3", "quantity": 1, "type": "Camera/sensors", "on_site": False, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Elgato Streamdeck", "quantity": 1, "type": "PC Peripherals", "on_site": True, "borrowable": True, "warranty": date(2025, 4, 25)},
            {"name": "Elgato CamLink 4k", "quantity": 1, "type": "Camera/Sensors", "on_site": False, "borrowable": True, "warranty": date(2025, 4, 25)},
            {"name": "Raspberry Pi 4", "quantity": 2, "type": "PC Peripherals", "on_site": True, "borrowable": False, "warranty": date(2025, 4, 25)},
            {"name": "Raspberry Pi 4", "quantity": 1, "type": "PC Peripherals", "on_site": False, "borrowable": False, "warranty": date(2025, 4, 25)},
        ]

       
            

        for item in equipment_data:
    
            Equipment.objects.create(
                equip_name=item["name"],
                quantity=item["quantity"],
                equip_type=item["type"],
                on_site=item["on_site"],
                borrowable=item["borrowable"],
                warranty=item["warranty"],
                
            
                
            )

            



            

        self.stdout.write(self.style.SUCCESS('population sucessful'))

