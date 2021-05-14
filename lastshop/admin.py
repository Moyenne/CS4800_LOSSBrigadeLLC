from django.contrib import admin
from users.models import Profile
from .models import cart, driver, favorite, grocerylist, groceryorder, item, paymentinfo, store, suborder, tag, webuser

admin.site.register(cart)
admin.site.register(driver)
admin.site.register(favorite)
admin.site.register(grocerylist)
admin.site.register(groceryorder)
admin.site.register(item)
admin.site.register(paymentinfo)
admin.site.register(store)
admin.site.register(suborder)
admin.site.register(tag)
admin.site.register(Profile)
admin.site.register(webuser)

