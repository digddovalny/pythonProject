from django.shortcuts import render


def catalog(request):
    context = {
        'title': 'Home - Каталог',
        'products': [
            {
                'image': 'deps/images/products/Ghost basters.jpeg',
                'name': 'Ghost basters car',
                'description': 'Конструктор LEGO Creator Expert Автомобиль Охотников за привидениями ECTO-1 2352 детали.',
                'price': 25000.00
            },

            {
                'image': 'deps/images/products/Proshce 911.jpg',
                'name': 'Technic Porsche 911',
                'description': 'Конструктор LEGO Technic Porsche 911 RSR 42096.',
                'price': 35000.00
            },

            {
                'image': 'deps/images/products/minecraft tree.jpg',
                'name': 'Minecraft домик на дереве',
                'description': 'Конструктор LEGO Minecraft Современный домик на дереве.',
                'price': 11000.00
            },

            {
                'image': 'deps/images/products/Sport car.jpg',
                'name': 'Гоночный болид 1:16',
                'description': 'Машинка гоночный болид на радиоуправлении M.i.F. Super Car 1:16.',
                'price': 7990.00
            },

            {
                'image': 'deps/images/products/6 hotwheels.webp',
                'name': '6 машинок HotWheels',
                'description': 'Набор из 6 игрушечных машинок Hot Wheels коллекция Европейские автомобили масштаб 1:64.',
                'price': 3999.00
            },

            {
                'image': 'deps/images/products/disonter1.webp',
                'name': 'Игрушка Dinoster',
                'description': 'Игрушка Dinoster Стего Бласт Винг Трансформер 2в1.',
                'price': 5000.00
            },

            {
                'image': 'deps/images/products/barbie bed.jpg',
                'name': 'Набор Barbie Кровать',
                'description': 'Игровой набор Barbie Кровать с аксессуарами.',
                'price': 13200.00
            },

            {
                'image': 'deps/images/products/barbie rusal.jpg',
                'name': 'Набор Barbie Русалка',
                'description': 'Игровой набор Barbie Малибу Русалка.',
                'price': 4600.00
            },

            {
                'image': 'deps/images/products/box of kosmetic.jpeg',
                'name': 'Набор косметики',
                'description': 'Набор косметики Yummy Martinelia в чемоданичке голубой',
                'price': 6000.00
            },

            {
                'image': 'deps/images/products/chemical tools.jpg',
                'name': 'Набор химических элементов',
                'description': 'Набор химических элементов для детей Пламя ароматов Трюки Науки.',
                'price': 1500.00
            },

            {
                'image': 'deps/images/products/minecraft album.jpg',
                'name': 'Альбом для наклеек Minecraft',
                'description': 'Альбом для наклеек Panini Minecraft.',
                'price': 1499.00
            },

            {
                'image': 'deps/images/products/batbinton.jpg',
                'name': 'Бадминтон',
                'description': 'Бадминтон Junfa Sport в сумке. 2 Ракетки.',
                'price': 1399.00
            },
        ]
    }
    return render(request, 'products/catalog.html', context)


def product(request):
    return render(request, 'products/product.html')
