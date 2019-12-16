#gallery

#### This is my personal gallery website where you can see photos that I have uploaded.

## As users you can :
* View different photos that interest me.
* View different categories of photos.
*search photos by category
* Copy a link to the photo to share with my friends.
***

### Usage example

1. Open the website and browse the images.
2. If you see an image that interests you you can click on it to view it.***


## Development setup

- To access the Code behind this site, you will need to:

1. Clone this repo:
  ```bash
  git clone https://github.com/njoroge33/gallery
  ```
2. Move to the folder and install requirements
  ```bash
  cd gallery
  pip install -r requirements.txt
  ```
3. Create database on psql shell
  ```SQL
  psql
  CREATE DATABASE gallery;
  ```
4. Migrate the database and run the application
  ```bash
  python manage.py migrate
  python manage.py runserver
  ```