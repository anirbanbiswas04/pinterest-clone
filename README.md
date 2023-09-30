# Pinterest Clone
A Django Photo Sharing app (+ HTMX & Bulma CSS)

This is a Django Photo Sharing webapp that uses HTMX and the Bulma CSS framework.<br>
HTMX allows the webapp to perform like a SPA.

## Prerequisites

- Python 3.6 or higher

## Installation

1. Clone the repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Run `python manage.py makemigrations`
4. Run `python manage.py migrate`
5. Run the server using `python manage.py runserver`.

## Features

- Users can upload and like photos.
- Progress bar is shown while uploading.
- Users can search and view photos.
- Uses the Bulma CSS framework and Masonry.js for styling.
- Has infinity scrolling.
- Behaves like a Single page application.
- Can edit own profile.

## Usage

1. Open your browser and navigate to `http://localhost:8000`.
2. Add photos to the site.
3. Browse through the available photos.
4. Browse the photos or search for photos with tags.
5. Like a photo.
6. Browse others profiles.
