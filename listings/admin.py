from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
  prepopulated_fields = { 
    'slug': ['title']
  }
  list_display = ['id', 'title', 'is_published', 'price', 'list_date', 'realtor', 'property_type']
  list_display_links = ['id', 'title']
  list_filter = ['realtor', 'property_type']
  list_editable = ['is_published']
  search_fields = ['title', 'description', 'address', 'city','zipcode', 'price'] 
  list_per_page = 25
  
  


admin.site.register(Listing, ListingAdmin)
