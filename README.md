# urlShortener
Url shortener based in flask

## Description
This project is a RESTful API developed with Flask and SQLAlchemy that creates short URLs from a destination one. The reference is saved in a Postgres database. 

The app redirects to the destination URL. 

The app provides endpoints to enable/disable the url redirection and to change the destination url

## Requirements
- Python 3.x
- Flask
- SQLAlchemy
- PostgreSQL

## Instalation

1. Clone the repository:
``` bash 
git clone https://github.com/edebonis/urlShortener.git
```
2. Create a virtualenv:
``` bash 
python3 -m venv env
```
3. Install dependencies:
``` bash 
pip install -r requirements.txt
```
4. Create a `.env`file in the root folder with following variables:
``` bash 
echo DATABASE_URL=postgresql://username:password@localhost/db_name > .env
```
5. Run the `run.py`file
``` bash 
python3 run.py
```

# Endpoints
## 1. __Shorten URL__
* __URL:__ `/api/shorten`
* __Method:__ `POST`
* __Description:__ Shortens a URL and saves it to the database
* __Request Body:__
```json
{
  "destination_url": "https://example.com"
}
```
* __Response:__
```json
{
  "short_url": "abc123"
}
```

## 2. __Shorten URL__
* __URL:__ `/<short_url>`
* __Method:__ `GET`
* __Description:__ Redirects to the destination URL based on the shortened URL.
* __Response:__ Redirects to the original URL

## 3. __Update URL__
* __URL:__ `/api/update/<short_url>`
* __Method:__ `POST`
* __Description:__ Update the destination URL associated with the short URL. Saves it to the database.
* __Request Body:__
```json
{
  "destination_url": "https://newexample.com"
}
```
* __Response:__
```json
{
  "short_url": "abc123",
  "destination_url": "https://newexample.com"
}
```
## 4. __Disable URL__
* __URL:__ `/api/disable/<short_url>`
* __Method:__ `POST`
* __Description:__ Disables a shortened URL, making it inaccessible. Updates the flag in database.
* __Response:__
```json
{
  "short_url": "abc123",
  "destination_url": "https://example.com"
}
```
## 5. __Enable URL__
* __URL:__ `/api/enable/<short_url>`
* __Method:__ `POST`
* __Description:__ Enables a shortened URL. Updates the flag in database.
* __Response:__
```json
{
  "short_url": "abc123",
  "destination_url": "https://example.com"
}
```