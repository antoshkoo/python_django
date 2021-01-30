from django.test import TestCase

from app_shops.models import Shop, Good, Promotion, Sale, Order

LOAD_DATA = ['initial_data.json']


class TestShopModel(TestCase):
    fixtures = LOAD_DATA

    def test_shop_model(self):
        shop = Shop.objects.first()

        name_label = shop._meta.get_field('name').verbose_name
        self.assertEquals(name_label, 'Shop name')

        name_max_length = shop._meta.get_field('name').max_length
        self.assertEquals(name_max_length, 100)

        self.assertEquals(f'{shop.name}', str(shop))

    def test_shop_get_good_sales(self):
        shop = Shop.objects.first()
        self.assertEquals(shop.get_goods_sales().count(), 1)

    def test_shop_get_good_no_sales(self):
        shop = Shop.objects.first()
        self.assertEquals(shop.get_goods_no_sales().count(), 1)


class TestGoodModel(TestCase):
    fixtures = LOAD_DATA

    def test_good_model(self):
        good = Good.objects.first()

        name_label = good._meta.get_field('name').verbose_name
        self.assertEquals(name_label, 'name')

        name_max_length = good._meta.get_field('name').max_length
        self.assertEquals(name_max_length, 100)

        self.assertEquals(f'{good.name} ({good.shop})', str(good))


class TestSaleModel(TestCase):
    fixtures = LOAD_DATA

    def test_sale_model(self):
        sale = Sale.objects.first()

        sale_price_label = sale._meta.get_field('sale_price').verbose_name
        self.assertEquals(sale_price_label, 'Sale price')

        self.assertEquals(f'{sale.good.name} - {sale.good.price} ({sale.sale_price})', str(sale))


class TestPromotionModel(TestCase):
    fixtures = LOAD_DATA

    def test_promotion_model(self):
        promotion = Promotion.objects.first()

        title_label = promotion._meta.get_field('title').verbose_name
        self.assertEquals(title_label, 'Title')

        title_max_length = promotion._meta.get_field('title').max_length
        self.assertEquals(title_max_length, 150)

        self.assertEquals(f'{promotion.shop} - ({promotion.title})', str(promotion))


class TestOrderModel(TestCase):
    fixtures = LOAD_DATA

    def test_order_model(self):
        order = Order.objects.first()
        time = order.date.strftime('%d.%m.%Y')

        self.assertEquals(f'{order.user}, {order.good.name}, {order.price_order} - {time}', str(order))
