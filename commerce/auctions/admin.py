from django.contrib import admin
from .models import User, Category, AuctionListing, Watchlist, Comment, Bid, Notification

# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(AuctionListing)
admin.site.register(Watchlist)
admin.site.register(Comment)
admin.site.register(Bid)
admin.site.register(Notification)