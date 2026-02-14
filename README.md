# Content Management API

Django REST API for managing categorized content.

## Setup

1. Install dependencies:
   ```bash
   pip install django djangorestframework
   ```

2. Run migrations:
   ```bash
   python manage.py migrate
   ```

3. Start server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

- `GET /api/content` - List all content (optional: `?category=<name>`)
- `POST /api/content` - Create content
- `GET /api/content/<id>` - Get content by ID
- `PUT /api/content/<id>` - Update content
- `DELETE /api/content/<id>` - Delete content

## Categories

`sports`, `technology`, `entertainment`, `news`, `education`
