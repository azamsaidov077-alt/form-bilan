from django.db  import models
class Category(models.Model):

    category_name = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    image = models.ImageField(upload_to='categories/',blank=True,null=True)
    def __str__(self):
        return self.category_name

class Products(models.Model):
    product_name = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted = models.BooleanField(default=False)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.product_name


class Suppliers(models.Model):
    company_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class Orders(models.Model):
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    order_date = models.DateField()
    required_date = models.DateField()
    shipped_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.id)
