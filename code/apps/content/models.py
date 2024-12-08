from django.db import models
from django.utils import timezone
# Create your models here.

class Customer(models.Model):
    username = models.CharField(max_length=100, verbose_name="იუზერნეიმი")
    first_name = models.CharField(max_length=100, verbose_name="სახელი", default="")
    email = models.EmailField("ელ.ფოსტის მისამართი", unique=False)
    is_active = models.BooleanField("აქტიურია", default=False)

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return f"{self.first_name} ".strip() or self.email

    class Meta:
        ordering = ("-id",)
        verbose_name = "მომხმარებელი"
        verbose_name_plural = "მომხმარებლები"

class Category(models.Model):
    title = models.CharField(max_length=20, verbose_name="დასახელება")

    def __str__(self) -> str:
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name="დასახელება")
    description = models.TextField(verbose_name="აღწერა")
    seller = models.ForeignKey(Customer, null=False, blank=False, related_name="product", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    listing_date = models.DateField(null=False, blank=False, default=timezone.now())
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ("listing_date",)
        verbose_name = "პროდუქტი"
        verbose_name_plural = "პროდუქტები"

class Cart(models.Model):
    customer = models.ForeignKey(Customer, null=False, blank=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self) -> str:
        return f"{self.customer} - {self.created_at}"
    

    def add_product(self, product, quantity=1):
        cart_item, created = CartItem.objects.get_or_create(
            product=product,
            cart=self,
            defaults={"quantity": quantity}
        )

        if not created:
            cart_item.quantity += 1
            cart_item.save()
        
        return cart_item
    
    def get_total_price(self):
        return sum(item.total_price() for item in self.items.all())

class CartItem(models.Model):
    product = models.ForeignKey(
        Product, 
        blank=True, 
        null=False, 
        related_name="items",
        on_delete=models.CASCADE,
    )

    cart = models.ForeignKey(
        Cart,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.product} - {self.cart}"
    
    def total_price(self):
        return self.quantity * self.product.price
