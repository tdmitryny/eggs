# Egg Price Tracker - Django Project Structure

EggPrice/                  # Root directory
│
├── .gitignore             # Git ignore file
├── requirements.txt       # Project dependencies
├── manage.py              # Django management script
│
├── eggpricetracker/       # Main project directory
│   ├── __init__.py
│   ├── settings.py        # Project settings
│   ├── urls.py            # Main URL routing
│   ├── asgi.py            # ASGI configuration
│   └── wsgi.py            # WSGI configuration
│
├── api/                   # API application
│   ├── __init__.py
│   ├── admin.py           # Admin configuration for API models
│   ├── apps.py            # App configuration
│   ├── models.py          # API data models
│   ├── serializers.py     # DRF serializers for API
│   ├── urls.py            # API URL routing
│   ├── views.py           # API view logic
│   ├── tests.py           # Tests for API
│   └── migrations/        # Database migrations
│
├── core/                  # Core application for business logic
│   ├── __init__.py
│   ├── admin.py           # Admin configuration
│   ├── apps.py            # App configuration
│   ├── models.py          # Core data models (Egg, Price, etc.)
│   ├── forms.py           # Forms for data entry
│   ├── views.py           # View logic
│   ├── urls.py            # URL routing
│   ├── utils.py           # Utility functions
│   ├── tests.py           # Tests
│   └── migrations/        # Database migrations
│
├── templates/             # HTML templates
│   ├── base.html          # Base template with common elements
│   ├── home.html          # Homepage template
│   ├── core/              # Core app templates
│   │   ├── price_list.html
│   │   ├── price_detail.html
│   │   └── price_form.html
│   └── admin/             # Custom admin templates
│
├── static/                # Static files
│   ├── css/               # CSS files
│   ├── js/                # JavaScript files
│   └── images/            # Image files
│
└── media/                 # User-uploaded files

## Key Components

### Models
- **EggType**: Different types of eggs (e.g., organic, free-range, jumbo)
- **Supplier**: Information about egg suppliers
- **PriceRecord**: Historical price data with timestamps
- **Region**: Geographic regions for price differentiation

### API Endpoints
- `/api/eggtypes/` - List and create egg types
- `/api/eggtypes/<id>/` - Retrieve, update, delete egg type
- `/api/suppliers/` - List and create suppliers
- `/api/suppliers/<id>/` - Retrieve, update, delete supplier
- `/api/prices/` - List and create price records
- `/api/prices/<id>/` - Retrieve, update, delete price record
- `/api/prices/current/` - Get current prices
- `/api/prices/historical/` - Get historical price data
- `/api/regions/` - List and create regions
- `/api/regions/<id>/` - Retrieve, update, delete region

### Core Features
1. **Price tracking**: Record and display egg prices
2. **Historical data**: Track price changes over time
3. **Supplier management**: Keep track of different egg suppliers
4. **Region-based pricing**: Support for different prices by region
5. **Data visualization**: Charts and graphs for price trends
6. **API access**: Programmatic access to price data
7. **User authentication**: Secured access to API and admin functions