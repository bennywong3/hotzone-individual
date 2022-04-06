# HotZone Release 1 Sprint 1
Contributors:

- Wong Ka Ngai (UID 3035568881)

Django project root hz, readme.pdf and README.md is included.

## Project description
Please read HotZone_ProjectDescription.pdf for more details of this project. 

In short, this individual project is a practice of Agile development. The individual part ends at sprint 1, which makes the project web-enabled and allows users to search for the geodata of the input location.

**You can access this project online**. 

https://glacial-forest-18359.herokuapp.com/locations/find

<h3>This project is put into production by switching to use gunicorn and a production-level DBMS, PostgreSQL, and then deploying to a cloud-based hosting platform, Heroku. </h3>

You can aslo install this django project locally, see instuctions below.



## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requests for Python 3 before running the source code.

```bash
pip3 install requests
```

## Function
**http://localhost:8000/locations/find**

There is only one input field. Input the location name and click the Go button. If HTTP response is successful, name, address, x-coordinate and y-coordinate of the location will be saved into the database. 

A message under the input field will be shown to tell the user that data are saved to the database.

**Example Message**
```bash
HTTP response is successful, connected to Geodata Location Search API.
Location The University of Hong Kong Chong Yuet Ming Physics Building
with address THE UNIVERSITY OF HONG KONG
at X-coordindate: 832459 ,Y-coordindate 816024
is found and imported to database.
```

## Admin panel
**http://localhost:8000/admin**
```bash
username: admin
password: admin
```
Data are stored in model **Geodata** with attributes name, address, Xcoor, Ycoor.
```
name = models.CharField(max_length=200)
address = models.TextField()
Xcoor = models.DecimalField(max_digits=20, decimal_places=10)
Ycoor = models.DecimalField(max_digits=20, decimal_places=10)
```
## Assumptions and limitations
>Assume that there is only one GeoData location that satisfies the search criteria. 

>Assume that every location input is not already known to HotZone.

If there are multiple GeoData locations that satisfy the search criteria, it selects the first one.

If user input the same location twice, the database will have two identical records.

Also, as this is just a "Tracer Bullet", the design is not beautiful, but it serves the purpose.
